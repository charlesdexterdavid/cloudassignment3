from azure import QueueService, AccessPolicy, SharedAccessPolicy, QueueSharedAccessPermissions
queue_service = QueueService(account_name, account_key)
ap = AccessPolicy(
    expiry='2018-10-12',
    permission=QueueSharedAccessPermissions.READ,
)
sas_token = queue_service.generate_shared_access_signature(
    'taskqueue',
    SharedAccessPolicy(ap),
)