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
    
    def getqsize(self,name):
        bus_service.get_queue(name).message_count
    
    def enqueue(self,qname,msg):
       bus_service.send_queue_message(qname, msg)
    
    def dequeue(self,qname):
        return bus_service.receive_queue_message(qname, peek_lock=False)
        
    def peek(self,qname):
        return bus_service.receive_queue_message(qname, peek_lock=True)
    
    def add_dummy_data(self):
        # data = json.dumps(request.get_json())
        # d = json.loads(data)
        d={}
        d['TransactionID']="1"
        d['UserId']="A1"
        d['SellerID']="S1"
        d['Product_Name']="Financial Trap"
        d['Transaction_Date']=str(datetime.datetime.utcnow())
        d['PartitionKey']=d['UserId']
        d['RowKey']=d['Transaction_Date']
        transaction = d
        table_service.insert_entity('failstore', transaction)
        return json.dumps(d)
        

test = StorageManager()
test.add_dummy_data()

# https://github.com/facebook/prophet/issues/140
# https://github.com/ansible/ansible/issues/31741
# sudo pip install --upgrade setuptools
# sudo apt-get install libffi-dev libssl-dev