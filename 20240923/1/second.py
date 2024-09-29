check = 0
while a:= int(input()):
	if a <= 0:
		print(a)
		break
	check += a
	if check > 21:
		print(check)
		break
