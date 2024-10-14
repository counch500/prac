from math import sin
A, B = -4, 4
def scale(a, b, A, B, x):
	coef = (B - A)/(b - a)
	X = coef*(x - a) + A
	return(X)
def sinc():
	for i in range(20):
        	x = scale(0, 19, A, B, i)
        	y = sin(x)
        	spc = round(scale(-1, 1, 0, 20, y))
        	print(spc * " " , "*")

sinc()
