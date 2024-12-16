import asyncio

q1, q2 = asyncio.Queue(), asyncio.Queue()

async def prod():
	for i in range(5):
		value = f"value_{i}"
		await q1.put(value)
		await asyncio.sleep(1)
		print(f"prod: put {value} to q1")
async def mid():
	while True:
		value = await q1.get()
		await q2.put(value)
		print(f"mid: get {value} from q1")
		print(f"mid: put {value} to q2")

async def cons():
	while True:
		value = await q2.get()
		print(f"cons: get {value} from q2")

async def main():
	tp, tm, tc = [asyncio.create_task(coro()) for coro in(prod, mid, cons)]
	await tp
	tp.cancel()
	tc.cancel()
