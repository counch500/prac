import asyncio
evsnd, evmid = asyncio.Event(), [asyncio.Event(), asyncio.Event()]
async def send(ev, name, evsnd):
	ev.set()
	print("<{name}> generated {evname}")
async def recv(ev, name, evname):
	await ev.wait()
	print(f"{name}: recieved {evname}")
async def snd():
	await send(evsnd, "snd", "evsnd")

async def mid(n):
	await recv(evsnd, f"mid{n}","evsnd")
	await send(evmid[n], f"mid{n}", f"evmid{n}")
async def rcv():
	await recv(evmid[0], "rcv", f"evmid{0}")
	await recv(evmid[1], "rcv", f"evmid{1}")
async def main():
	await asyncio.gather(rcv(), mid(1), mid(0), snd())
