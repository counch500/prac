from decimal import Decimal

def esum(N, one):
	sum = 0
	n = 0
	frac = 1
	while n <= N:
		sum += one/frac
		n += 1
		frac *= n
	return sum

print(esum(7, float(1)))
