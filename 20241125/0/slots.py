class C:
	__slots__ = "a", "b", "c"
	ro = "Readonly"
	def __init__(self):
		for s in self.__slots__:
			setattr(self, s, f"<{s}>")
c = C()
print(c.a)
print(c.b)
