res = []
while arr:= input():
        res.append(eval(arr))
if any([len(num) != len(res) for num in res]):
	print("Neqadrat")
	exit(1)

for i in range(len(res)):
        for j in range(i + 1,len(res)):
                res[i][j], res[j][i] = res[j][i], res[i][j]
for num in res:
        print(num)

