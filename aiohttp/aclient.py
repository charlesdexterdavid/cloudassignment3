#!/usr/bin/env python3
# http://skipperkongen.dk/2016/09/09/easy-parallel-http-requests-with-python-and-asyncio/
import random
import asyncio
from aiohttp import ClientSession
from datetime import datetime
from azure.servicebus import ServiceBusService, Message, Queue
from flask import Flask,request

app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='cloudassignment34ed0', 
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')

bus_service.create_queue('taskqueue2')


@app.route('/add',methods=['GET'])
async def add_to_storage():
    # name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    msg = Message( "Test at "+str(datetime.now().strftime('Start:%Y-%m-%d %H:%M:%S')))
    bus_service.send_queue_message('taskqueue2', msg)
    return web.Response(body=text.encode('utf-8'))
    # if request.method == 'POST':
    #      data = json.dumps(request.get_json())
    #      d = json.loads(data)
    #      d['transtime']=str(datetime.datetime.utcnow())
    #     d['PartitionKey']=d['user']
    #     d['RowKey']=d['transtime']
        # transaction = d
        # table_service.insert_entity('evenstore', transaction)
#         return json.dumps(d)
# {"TransactionID":"1","UserId":"A1","SellerID":"S1","Product Name":"Financial Trap","Sale Price":1000000,"Transaction Date":" "}

#         result=jnd.createTransaction(request)
#         jnd.updateView(request)# update the materialized view stored in an azure table called materializedview
#         return result

@app.route('/start',methods=['GET'])
def startclient():
    number = 100#9000
    loop = asyncio.get_event_loop()
    print(datetime.now().strftime('Start:%Y-%m-%d %H:%M:%S'))
    future = asyncio.ensure_future(run(loop, number))
    loop.run_until_complete(future)
    print(datetime.now().strftime('End:%Y-%m-%d %H:%M:%S'))
    return ""

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print(url)

          

            return await response.read()



async def bound_fetch(sem, url):
    # getter function with semaphore
    async with sem:
        await fetch(url)


async def run(loop,  r):
    url = "http://localhost:8082/{}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(100)
    for i in range(r):
        # pass Semaphore to every GET request
        # {"TransactionID":"1","UserId":"A1","SellerID":"S1","Product Name":"Financial Trap","Sale Price":1000000,"Transaction Date":" "}"
        task = asyncio.ensure_future(bound_fetch(sem, url.format("add")))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    await responses





if __name__ == '__main__':
    app.run(port=8082,host="0.0.0.0")