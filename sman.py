import datetime
import simplejson as json
from azure.storage.table import TableService, Entity # had to install
from azure.servicebus import ServiceBusService, Message, Queue # haad to install
import azure #had to install

bus_service = ServiceBusService(
    service_namespace='cloudassignment34ed0', 
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')
    
table_service = TableService(account_name='cloudassignment34ed0', account_key='U1NMHbxFuE8vFnUFKKTsR/DY0FYZGVuiUDqWKYfM0YCQfh7nMa3jMgeVyur52fyqq0L4hageFuZu9hatbAUQ5w==')
bus_service.create_queue('taskqueue')
table_service.create_table('failstore')

class StorageManager(object):
    
    def getqsize(self,qname):
        return bus_service.get_queue(qname).message_count
    
    def enqueue(self,qname,msg):
       bus_service.send_queue_message(qname, msg)
    
    def dequeue(self,qname):
        return bus_service.receive_queue_message(qname, peek_lock=True).delete()
        
    def peek(self,qname):
        return bus_service.receive_queue_message(qname, peek_lock=True)
    
    def delete_all_messages(self,qname):
        # bus_service.clear_messages('taskqueue')
        # for i in range(0,self.getqsize(qname)):
        self.dequeue(qname)
    def add_dummy_data(self):
        # data = json.dumps(request.get_json())
        # d = json.loads(data)
        d={}
        for i in range(0,10):
            d['TransactionID']=str(i)
            d['UserId']="A"+str(i)
            d['SellerID']="S"+str(i)
            d['Product_Name']="Financial Trap"+str(i)
            d['Transaction_Date']=str(datetime.datetime.utcnow())
            d['PartitionKey']=d['UserId']
            d['RowKey']=d['Transaction_Date']
            transaction = d
            msg = Message(str(d))
            bus_service.send_queue_message('taskqueue', msg)
            # table_service.insert_entity('failstore', transaction)
        return json.dumps(d)
        

test = StorageManager()
# test.add_dummy_data()
print (test.getqsize('taskqueue'))
# print (test.peek('taskqueue').body)
# test.delete_all_messages('taskqueue')
# print ("apple1")
# bus_service.receive_queue_message('taskqueue', peek_lock=True).delete()
# print ("apple2")
# print (test.getqsize('taskqueue'))


# https://github.com/facebook/prophet/issues/140
# https://github.com/ansible/ansible/issues/31741
# sudo pip install --upgrade setuptools
# sudo apt-get install libffi-dev libssl-dev