c = 0
while a:= input():
	if int(a) <= 0:
		print(a)
		break
	c += int(a)
	if int(c) > 21:
		print(c)
		break
