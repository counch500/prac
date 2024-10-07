def rbin(n, lst, b):
	if n > 0:
		rbin(n - 1, lst + [b], 0)
		rbin(n - 1, lst + [b], 1)
	elif b == 1:
		print(*lst, sep="")
