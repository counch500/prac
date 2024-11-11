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
	def __getitem__(self, idx):
		return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))[idx]
	def __bool__(self):
		return abs(self) != 0
	def __del__(self):
		self.__class__.rectnct -= 1
		return(self.rectnct)
	def __abs__(self):
		return abs(self.x2 - self.x1)*(self.y2 - self.y1)
	def __lt__(self, other):
		return abs(self) < abs(other)
	def __eq__(self, other):
		return abs(self) == abs(other)
	def __iter__(self):
		return iter(((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)))
	def __mul__(self, num):
		return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)
	__rmul__ = __mul__

r4 = Rectangle( 1, 33, 55, 78)
#print(fun())
#r = Rectangle(1, 1, 1, 1)
#r2 = Rectangle(11, 2, 3, 55)
#r3 = Rectangle(22, 33, 44, 55)
for x, y in Rectangle(1, 2, 5, 6):
	print(x, y)

if r4:
	print(abs(r4))
else:
	print("No.")

#print(r2[2])
#print(r * 8)
#print(9 * r2)
#print(r.rectnct)
#print(r2.rect_2)
#print(r == r3)
#print(r < r2)

