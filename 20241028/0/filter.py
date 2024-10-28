from itertools import filterfalse

def fifa(n, seq):
	yield from filterfalse(lambda x: x % n, seq)
