def fun(n):
	sum = 0
	n = 1
	while True:
		sum += 1/(n**2)
		yield sum
		n += 1

