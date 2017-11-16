#!/usr/bin/env python3

import random
import asyncio
from aiohttp import ClientSession
from datetime import datetime
async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # print(url)
            return await response.read()


async def bound_fetch(sem, url):
    # getter function with semaphore
    async with sem:
        await fetch(url)


async def run(loop,  r):
    url = "http://localhost:8080/{}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(100)
    for i in range(r):
        # pass Semaphore to every GET request
        task = asyncio.ensure_future(bound_fetch(sem, url.format(i)))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    await responses

number = 1000000
loop = asyncio.get_event_loop()
print(datetime.now().strftime('Start:%Y-%m-%d %H:%M:%S'))
future = asyncio.ensure_future(run(loop, number))
loop.run_until_complete(future)
print(datetime.now().strftime('End:%Y-%m-%d %H:%M:%S'))