a, b, c = eval(input())
if max(a, b, c) < (a + b + c) - max(a, b, c) and min(a, b, c) > 0:
	print("triangle")
else:
	print("wtf?")

