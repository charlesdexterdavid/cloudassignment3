from flask import Flask,request, jsonify, make_response
import requests
from gentoken import _sign_string
# https://gist.github.com/sedouard/8412cb51629ef9614fd4
service_namespace='cloudassignment34ed0'
shared_access_key_name='RootManageSharedAccessKey'
shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0='
queue_name='taskqueue'

#post reads the message and locks it.. analogus to peek lock
# delete reads the message and leaves it 

headers ={'Authorization':_sign_string("https://cloudassignment34ed0.servicebus.windows.net/taskqueue",shared_access_key_value,shared_access_key_name),'Content-Type': 'application/json'}

api_get='https://{}.servicebus.windows.net/{}/messages/head'.format(service_namespace,queue_name)
print (requests.post(api_get,headers=headers).content )

# print (headers)