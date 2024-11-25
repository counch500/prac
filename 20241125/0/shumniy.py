def dumper(fun):
	def newfun(*args, **kwargs):
		print(">", *args, **kwargs)
		res = fun(*args, **kwargs)
		print("<", res)
		return res
	return newfun

@dumper
def fun(a, b, c):
	e = a + b*c
	return e
print(fun(2,3,4))
