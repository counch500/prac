class istype:
	def __init__(self, typ):
		self.typ = typ
	def __call__(self, fun):
		def newfun(*args):
			if not all(isinstance(a, self.typ) for a in args):
				raise TypeError(f"not all items are {self.typ}", args)
			return fun(*args)
		return newfun
@istype(int)
def ssum(a, b, c):
	return a + b*c

print(ssum(1,2,3))
