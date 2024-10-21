from collections import Counter
from timeit import Timer
text = input()
def cnt():
	c = {}
	for w in text:
		c[w] = c.get(w, 0) + 1
	return c
def CNT():
	return Counter(text)
T1 = Timer(cnt)
T2 = Timer(CNT)
print(T1.autorange(), T2.autorange())
