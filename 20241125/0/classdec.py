class Dumper:
	def __init__(self, func):
		self.func = func
	def __call__(self, *args, **kwargs):
		print(args, kwargs, end = " -> ")
		res = self.func(*args, **kwargs)
		print(res)
		return res
