def div_ab(a, b):

	if b < 0.001:

		raise ValueError("No")

	return a/b

def new(fun, a, b):

	try:
		return fun(a, b)
	except:
		return "OO"
