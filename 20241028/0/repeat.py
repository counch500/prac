from itertools import repeat

def repeater(seq, n):
	for el in seq:
		yield from repeat(el, n)
