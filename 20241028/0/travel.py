def travel(n):
	for i in range(n):
		yield "po kochkam"
	return "i v yamu"

def travelwrap(n):
	res = yield from travel(n)
	yield res
