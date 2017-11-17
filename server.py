from azure.servicebus import ServiceBusService, Message, Queue
bus_service = ServiceBusService(
    service_namespace='cloudassignment34ed0', 
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')

# bus_service.create_queue('taskqueue')
# msg = Message(b'Test Message David 2')
# bus_service.send_queue_message('taskqueue', msg)

# bus_service_r = ServiceBusService(
#     service_namespace='cloudassignment34ed0', 
#     shared_access_key_name='RootManageSharedAccessKey',
#     shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')

for i in range(0,bus_service.get_queue('taskqueue').message_count-1):
    # val=bus_service.get_queue('taskqueue').message_count #number of messages on the quque
    # print (val)
    print (i)
    msg = bus_service.receive_queue_message('taskqueue', peek_lock=True)
    print(msg.body)
# queue_service.delete_queue('taskqueue')