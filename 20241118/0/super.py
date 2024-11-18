class C:
	def __init__(self, val):
		self.val = val
class D(C):
	def __init__(self,val):
		super().__init__(val)
		print("Init", val)
