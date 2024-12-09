def fun(a, val):
	a.var = val
C = type('C', (), {'var': 100500, '__init__':fun})
print(C.var)
c = C(123)
print(c.var)
