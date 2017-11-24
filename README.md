# Messsage Generator and Receive 0.0.1

## Quick Access Link:

* [folder containing the java files](https://github.com/charlesdexterdavid/cloudassignment3/tree/master/Code%20For%20MsgGenRecv/src/main/java/com/ptasdevz)



## Synopsis: The application works in two parts: 

  1. **A message genrator**: the message generator will allow you to generate any amount of messages at a rate specified to be pushed to a specified queue on Azure Service Bus. limitations are due to the machine specifications.
  
  2. **A message receiver**: The receive will allow the retrieval and storages of messages from an Azure Service Bus queue at a rate specifed. Limitations are due to the machine specifications 

## USING THE JAR FILE:

### Usage Syntax format for generating messages (using the MsgGenRecv.jar file): 

``` java -jar MsgGenRecv.jar send_messages <queue_name> <message_count> <message_send_rate> [<verbose_switch>]```
 
***Example***: ```java -jar MsgGenRecv.jar send_messages taskqueue 1000000 1000```

* <span style="color:orange;">queue_name</span> :  The name of the service bus queue. Please note that the queue will be created if it doesnt exist. e.g.: ```taskqueue```

* <span style="color:orange;">message_count</span> : A number which represents the amount of messages you will like to push to the queue. e.g.: ```1000000```

* <span style="color:orange;">message_send_rate</span> : A number of concurrent request sent by the generator. e.g.:```1000```

* <span style="color:orange;">-v</span> : An OPTONAL switch to enable the generator to be verbose when sending messages.

### Usage Syntax format for receiving messages (using the MsgGenRecv.jar file): 

##### Note: below configuaration in the example is what is being used when the jar file is deployed due to the settings in the arm template (azuredeploy.json)

```java -jar MsgGenRecv.jar receive_messages <queue_name> <message_recv_rate> [<verbose_switch>]```

***Example***: ```java -jar MsgGenRecv.jar receive_messages taskqueue 400```

* <span style="color:	#ADFF2F;">queue_name</span> : The name of the service bus queue.

* <span style="color:	#ADFF2F;">message_recv_rate</span> : A number which represents the amount of messages that should be pulled concurrently from the queue. e.g: ```400```

* <span style="color:	#ADFF2F"> -v</span> : An OPTONAL switch to enable the generator to be verbose when sending messages i.e. pints each incoming message read from queue.

