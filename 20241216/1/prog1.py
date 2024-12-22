import asyncio
from asyncio import Queue

async def writer(q, d, e):
    c = 0
    await asyncio.sleep(d)
    while not e.is_set():
        await q.put(f"{c}_{d}")
        c += 1
        await asyncio.sleep(d)

async def stacker(q, s, e):
    while not e.is_set():
        s.insert(0, await q.get())

async def reader(s, n, d, e):
    await asyncio.sleep(d)
    for _ in range(n):
        while not s: await asyncio.sleep(0.01)
        print(s.pop())
        await asyncio.sleep(d)
    e.set()

async def main(d1, d2, d3, n):
    q, s, e = Queue(), [], asyncio.Event()
    tasks = [asyncio.create_task(f) for f in 
             [writer(q, d1, e), writer(q, d2, e), stacker(q, s, e), reader(s, n, d3, e)]]
    await e.wait()
    [t.cancel() for t in tasks]

asyncio.run(main(*map(int, input().split(","))))
