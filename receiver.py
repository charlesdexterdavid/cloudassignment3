#!/usr/bin/env python3
import random
import asyncio
from aiohttp import ClientSession
from datetime import datetime
from gentoken import _sign_string
# https://gist.github.com/sedouard/8412cb51629ef9614fd4
service_namespace='cloudassignment34ed0'
shared_access_key_name='RootManageSharedAccessKey'
shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0='
queue_name='taskqueue'
# headers ={'Authorization':_sign_string("https://cloudassignment34ed0.servicebus.windows.net/taskqueue",shared_access_key_value,shared_access_key_name),'Content-Type': 'application/json'}
headers={}
headers['Authorization']=_sign_string("https://cloudassignment34ed0.servicebus.windows.net/taskqueue",shared_access_key_value,shared_access_key_name)
headers['Content-Type']='application/json'
api_get='https://{}.servicebus.windows.net/{}/messages/head'.format(service_namespace,queue_name)
# print (requests.post(api_get,headers=headers).content )

async def fetch(url):
    async with ClientSession() as session:
        async with session.delete(url,headers=headers) as response:
            async for _ in response.content:
                print(_)
            return await response.read()


async def bound_fetch(sem, url):
    # getter function with semaphore
    async with sem:
        await fetch(url)


async def run(loop,  r):
    global api_get
    url = api_get#"http://localhost:8080/{}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)
    for i in range(r):
        # pass Semaphore to every GET request
        task = asyncio.ensure_future(bound_fetch(sem, url))
        tasks.append(task)
        await asyncio.sleep(0)

    responses = asyncio.gather(*tasks)
    await responses

number = 1000#70000#10#00000
loop = asyncio.get_event_loop()
print(datetime.now().strftime('Start:%Y-%m-%d %H:%M:%S'))
future = asyncio.ensure_future(run(loop, number))
loop.run_until_complete(future)
print(datetime.now().strftime('End:%Y-%m-%d %H:%M:%S'))



# #!/usr/bin/env python3

# import random
# import asyncio
# from aiohttp import ClientSession

# async def fetch(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             print(url)
#             return await response.read()


# async def bound_fetch(sem, url):
#     # getter function with semaphore
#     async with sem:
#         await fetch(url)


# async def run(loop,  r):
#     url = "http://localhost:8080/{}"
#     tasks = []
#     # create instance of Semaphore
#     sem = asyncio.Semaphore(10)
#     for i in range(r):
#         # pass Semaphore to every GET request
#         task = asyncio.ensure_future(bound_fetch(sem, api_get))
#         tasks.append(task)
#         await asyncio.sleep(0)

#     responses = asyncio.gather(*tasks)
#     await responses

# # number = 40000
# # loop = asyncio.get_event_loop()

# # future = asyncio.ensure_future(run(loop, number))
# # loop.run_until_complete(future)

# number = 1000#70000#10#00000
# loop = asyncio.get_event_loop()
# print(datetime.now().strftime('Start:%Y-%m-%d %H:%M:%S'))
# future = asyncio.ensure_future(run(loop, number))
# loop.run_until_complete(future)
# print(datetime.now().strftime('End:%Y-%m-%d %H:%M:%S'))

