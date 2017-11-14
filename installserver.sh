{
    "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "vmSku": {
            "defaultValue": "Standard_A1",
            "type": "String",
            "metadata": {
                "description": "Size of VMs in the VM Scale Set."
            }
        },
        "vmssName": {
            "maxLength": 9,
            "type": "String",
            "metadata": {
                "description": "String used as a base for naming resources (9 characters or less). A hash is prepended to this string for some resources, and resource-specific information is appended."
            }
        },
        "instanceCount": {
            "maxValue": 100,
            "type": "Int",
            "metadata": {
                "description": "Number of VM instances (100 or less)."
            }
        },
        "adminUsername": {
            "type": "String",
            "metadata": {
                "description": "Admin username on all VMs."
            }
        },
        "adminPassword": {
            "type": "SecureString",
            "metadata": {
                "description": "Admin password on all VMs."
            }
        }
    },
    "variables": {
        "location": "[resourceGroup().location]",
        "addressPrefix": "10.0.0.0/16",
        "subnetPrefix": "10.0.0.0/24",
        "virtualNetworkName": "[concat(parameters('vmssName'), 'vnet')]",
        "publicIPAddressName": "[concat(parameters('vmssName'), 'pip')]",
        "subnetName": "[concat(parameters('vmssName'), 'subnet')]",
        "loadBalancerName": "[concat(parameters('vmssName'), 'lb')]",
        "publicIPAddressID": "[resourceId('Microsoft.Network/publicIPAddresses',variables('publicIPAddressName'))]",
        "lbID": "[resourceId('Microsoft.Network/loadBalancers',variables('loadBalancerName'))]",
        "natPoolName": "[concat(parameters('vmssName'), 'natpool')]",
        "bePoolName": "[concat(parameters('vmssName'), 'bepool')]",
        "natStartPort": 50000,
        "natEndPort": 50120,
        "natBackendPort": 22,
        "nicName": "[concat(parameters('vmssName'), 'nic')]",
        "ipConfigName": "[concat(parameters('vmssName'), 'ipconfig')]",
        "frontEndIPConfigID": "[concat(variables('lbID'),'/frontendIPConfigurations/loadBalancerFrontEnd')]",
        "osType": {
            "publisher": "Canonical",
            "offer": "UbuntuServer",
            "sku": "16.04-LTS",
            "version": "latest"
        },
        "imageReference": "[variables('osType')]",
        "computeApiVersion": "2017-03-30",
        "networkApiVersion": "2017-04-01",
        "insightsApiVersion": "2015-04-01"
    },
    "resources": [
        {
            "type": "Microsoft.Network/virtualNetworks",
            "name": "[variables('virtualNetworkName')]",
            "apiVersion": "2017-04-01",
            "location": "[variables('location')]",
            "properties": {
                "addressSpace": {
                    "addressPrefixes": [
                        "[variables('addressPrefix')]"
                    ]
                },
                "subnets": [
                    {
                        "name": "[variables('subnetName')]",
                        "properties": {
                            "addressPrefix": "[variables('subnetPrefix')]"
                        }
                    }
                ]
            }
        },
        {
            "type": "Microsoft.Network/publicIPAddresses",
            "name": "[variables('publicIPAddressName')]",
            "apiVersion": "2017-04-01",
            "location": "[variables('location')]",
            "properties": {
                "publicIPAllocationMethod": "Dynamic",
                "dnsSettings": {
                    "domainNameLabel": "[parameters('vmssName')]"
                }
            }
        },
        {
            "type": "Microsoft.Network/loadBalancers",
            "name": "[variables('loadBalancerName')]",
            "apiVersion": "2017-04-01",
            "location": "[variables('location')]",
            "properties": {
                "frontendIPConfigurations": [
                    {
                        "name": "LoadBalancerFrontEnd",
                        "properties": {
                            "publicIPAddress": {
                                "id": "[variables('publicIPAddressID')]"
                            }
                        }
                    }
                ],
                "backendAddressPools": [
                    {
                        "name": "[variables('bePoolName')]"
                    }
                ],
                "inboundNatPools": [
                    {
                        "name": "[variables('natPoolName')]",
                        "properties": {
                            "frontendIPConfiguration": {
                                "id": "[variables('frontEndIPConfigID')]"
                            },
                            "protocol": "tcp",
                            "frontendPortRangeStart": "[variables('natStartPort')]",
                            "frontendPortRangeEnd": "[variables('natEndPort')]",
                            "backendPort": "[variables('natBackendPort')]"
                        }
                    },
                    {
                        "name": "natpool2",
                        "properties": {
                            "frontendIPConfiguration": {
                                "id": "[variables('frontEndIPConfigID')]"
                            },
                            "protocol": "tcp",
                            "frontendPortRangeStart": "9000",
                            "frontendPortRangeEnd": "9120",
                            "backendPort": "9000"
                        }
                    }
                ]
            },
            "dependsOn": [
                "[concat('Microsoft.Network/publicIPAddresses/', variables('publicIPAddressName'))]"
            ]
        },
        {
            "type": "Microsoft.Compute/virtualMachineScaleSets",
            "sku": {
                "name": "[parameters('vmSku')]",
                "tier": "Standard",
                "capacity": "[parameters('instanceCount')]"
            },
            "name": "[parameters('vmssName')]",
            "apiVersion": "2017-03-30",
            "location": "[variables('location')]",
            "properties": {
                "overprovision": "false",
                "upgradePolicy": {
                    "mode": "Manual"
                },
                "virtualMachineProfile": {
                    "storageProfile": {
                        "osDisk": {
                            "createOption": "FromImage",
                            "caching": "ReadWrite"
                        },
                        "imageReference": "[variables('imageReference')]"
                    },
                    "osProfile": {
                        "computerNamePrefix": "[parameters('vmssName')]",
                        "adminUsername": "[parameters('adminUsername')]",
                        "adminPassword": "[parameters('adminPassword')]"
                    },
                    "networkProfile": {
                        "networkInterfaceConfigurations": [
                            {
                                "name": "[variables('nicName')]",
                                "properties": {
                                    "primary": "true",
                                    "ipConfigurations": [
                                        {
                                            "name": "[variables('ipConfigName')]",
                                            "properties": {
                                                "subnet": {
                                                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/virtualNetworks/', variables('virtualNetworkName'), '/subnets/', variables('subnetName'))]"
                                                },
                                                "loadBalancerBackendAddressPools": [
                                                    {
                                                        "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('loadBalancerName'), '/backendAddressPools/', variables('bePoolName'))]"
                                                    }
                                                ],
                                                "loadBalancerInboundNatPools": [
                                                    {
                                                        "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('loadBalancerName'), '/inboundNatPools/', variables('natPoolName'))]"
                                                    },
                                                    {
                                                        "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('loadBalancerName'), '/inboundNatPools/natpool2')]"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extensionProfile": {
                        "extensions": [
                            {
                                "name": "lapextension",
                                "properties": {
                                    "publisher": "Microsoft.Azure.Extensions",
                                    "type": "CustomScript",
                                    "typeHandlerVersion": "2.0",
                                    "autoUpgradeMinorVersion": true,
                                    "settings": {
                                        "fileUris": [
                                            "https://raw.githubusercontent.com/charlesdexterdavid/cloudassignment3/master/installserver.sh",
                                            "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-vmss-bottle-autoscale/workserver.py"
                                        ],
                                        "commandToExecute": "bash installserver.sh"
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "dependsOn": [
                "[concat('Microsoft.Network/loadBalancers/', variables('loadBalancerName'))]",
                "[concat('Microsoft.Network/virtualNetworks/', variables('virtualNetworkName'))]"
            ]
        },
        {
            "type": "Microsoft.Insights/autoscaleSettings",
            "name": "autoscalehost",
            "apiVersion": "2015-04-01",
            "location": "[variables('location')]",
            "properties": {
                "name": "autoscalehost",
                "targetResourceUri": "[concat('/subscriptions/',subscription().subscriptionId, '/resourceGroups/',  resourceGroup().name, '/providers/Microsoft.Compute/virtualMachineScaleSets/', parameters('vmSSName'))]",
                "enabled": true,
                "profiles": [
                    {
                        "name": "Profile1",
                        "capacity": {
                            "minimum": "1",
                            "maximum": "10",
                            "default": "1"
                        },
                        "rules": [
                            {
                                "metricTrigger": {
                                    "metricName": "Percentage CPU",
                                    "metricNamespace": "",
                                    "metricResourceUri": "[concat('/subscriptions/',subscription().subscriptionId, '/resourceGroups/',  resourceGroup().name, '/providers/Microsoft.Compute/virtualMachineScaleSets/', parameters('vmSSName'))]",
                                    "timeGrain": "PT1M",
                                    "statistic": "Average",
                                    "timeWindow": "PT5M",
                                    "timeAggregation": "Average",
                                    "operator": "GreaterThan",
                                    "threshold": 60
                                },
                                "scaleAction": {
                                    "direction": "Increase",
                                    "type": "ChangeCount",
                                    "value": "1",
                                    "cooldown": "PT1M"
                                }
                            },
                            {
                                "metricTrigger": {
                                    "metricName": "Percentage CPU",
                                    "metricNamespace": "",
                                    "metricResourceUri": "[concat('/subscriptions/',subscription().subscriptionId, '/resourceGroups/',  resourceGroup().name, '/providers/Microsoft.Compute/virtualMachineScaleSets/', parameters('vmSSName'))]",
                                    "timeGrain": "PT1M",
                                    "statistic": "Average",
                                    "timeWindow": "PT5M",
                                    "timeAggregation": "Average",
                                    "operator": "LessThan",
                                    "threshold": 30
                                },
                                "scaleAction": {
                                    "direction": "Decrease",
                                    "type": "ChangeCount",
                                    "value": "1",
                                    "cooldown": "PT1M"
                                }
                            }
                        ]
                    }
                ]
            },
            "dependsOn": [
                "[concat('Microsoft.Compute/virtualMachineScaleSets/', parameters('vmSSName'))]"
            ]
        }
    ]
}
