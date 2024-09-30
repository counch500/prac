res = []
while arr:= input():
	res.append(eval(arr))
for i in range(len(res)):
	for j in range(i + 1,len(res)):
		res[i][j], res[j][i] = res[j][i], res[i][j]
for num in res:
	print(num)
