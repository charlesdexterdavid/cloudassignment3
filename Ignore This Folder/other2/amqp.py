# from proton import Messenger, Message
from proton import *
# from urllib import quote_plus
import urllib
import sys, optparse

 
messenger = Messenger()
message = Message()
# message.address = "amqps://{ISSUER}:{KEY}@{servicebus namespace}.servicebus.windows.net/{queuename}"

# message.address = "amqps://{ISSUER}:{KEY}@{servicebus namespace}.servicebus.windows.net/{queuename}"
# message.address = "amqps://[username]:[password]@[namespace].servicebus.windows.net/[entity]"
service_namespace='cloudassignment34ed0', 
shared_access_key_name='RootManageSharedAccessKey',
shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0='
# enc = urllib.parse.quote_plus(shared_access_key_value)
message.address = "amqps://RootManageSharedAccessKey:"+shared_access_key_value+"@cloudassignment34ed0.servicebus.windows.net/taskqueue"
 
message.body = u"This is a text string"
messenger.put(message)
print("***BEGIN SEND***")
messenger.send()
print("***END SEND***")

# address = "amqps://RootManageSharedAccessKey"+shared_access_key_value+"@cloudassignment34ed0.servicebus.windows.net/taskqueue"

# messenger.subscribe(address)

# messenger.start()
# messenger.recv(1)
# message = Message()
# if messenger.incoming:
#      messenger.get(message)
      
# messenger.stop()





