class Rectangle:
	rectnct = 0
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.__class__.rectnct += 1
		setattr(self, f"rect_{self.rectnct}", self.rectnct)
	def __str__(self):
		return f"({self.x1},{self.y1})({self.x1},{self.y2}),({self.x2},{self.y2}),({self.x2},{self.y1}),({self.rectnct})"
r = Rectangle(11, 21, 161, 17)
r2 = Rectangle(11, 2, 3, 55)
print(r.rectnct)
print(r2.rect_2)
