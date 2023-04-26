import asyncio

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data":1}

async def print_fun():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def run():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_fun())
    value = await task1
    print(value)
    
    await task2


asyncio.run(run())
