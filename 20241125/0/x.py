class C:
	def __get__(self, obj, cls):
		print("GET", obj)
		return obj._value
	def __set__(self, obj, val):
		print("SET", obj, val)
		obj._value = val
	def __delete__(self, obj):
		print("DELETE", obj)
