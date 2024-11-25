def isins(f):
	def newfun(*args):
		if not all(isinstance(a, int) for a in args):
			raise TypeError("Not all parametrs are int", args)
		return f(*args)
	return newfun

