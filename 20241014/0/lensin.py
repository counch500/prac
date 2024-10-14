from math import sin
a, b = -4, 4
for i in range(20):
	x = a + (b - a)*i/19
	y = sin(x)
	spc = round((1 + y)/2*40)
	print(spc * " " , "*")
