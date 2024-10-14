from fractions import Fraction
from decimal import Decimal

def multiplier(x, y, Type):
	a = Type(x)
	b = Type(y)
	return a*b
print(multiplier("1/6", "2/3", Fraction))
print(multiplier("1.2", "1.4", Decimal))
print(multiplier("1.3", "2.3", float))
