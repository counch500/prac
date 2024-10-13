from math import *

def Calc(s,t,u):
	l1 = lambda x: eval(s)
	l2 = lambda x: eval(t)
	l3 = lambda x, y: eval(u)
	return lambda x: l3(l1(x), l2(x))

a, b, c = eval(input())
fun = Calc(a, b, c)
print(fun(eval(input())))
