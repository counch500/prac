def MINF(*f):
	def fun(x):
		return min([i(x) for i in f])
	return fun
