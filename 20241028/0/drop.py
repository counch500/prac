from itertools import islice, dropwhile
def sue():
	sum = 0
	n = 1
	while True:
		sum += 1/(n*n)
		yield sum
		n += 1

for e in islice(dropwhile(lambda x: x <= 1.6, sue()), 10):
	print(e)

