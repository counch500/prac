class Sole(type):
	def __new__(metacls, name, parents, namespace):
			if len(parents) > 1:
				raise TypeError("Cannot have more than one parent")
			return super().__new__(metacls, name, parents, namespace)
class C(metaclass = Sole): pass
class D(C): pass
class C(D, int): pass
