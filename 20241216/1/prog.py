import asyncio
from asyncio import Queue

async def writer(queue, delay, stop_event):
    counter = 0
    await asyncio.sleep(delay)
    while not stop_event.is_set():
        await queue.put(f"{counter}_{delay}")
        counter += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set():
        stack.insert(0, await queue.get())

async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)
    for _ in range(count):
        while not stack:
            await asyncio.sleep(0.01)
        print(stack.pop())
        await asyncio.sleep(delay)
    stop_event.set()

async def main(delay1, delay2, delay3, count):
    queue = Queue()
    stack = []
    stop_event = asyncio.Event()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(writer(queue, delay1, stop_event))
        tg.create_task(writer(queue, delay2, stop_event))
        tg.create_task(stacker(queue, stack, stop_event))
        tg.create_task(reader(stack, count, delay3, stop_event))

asyncio.run(main(*map(int, input().strip().split(","))))
