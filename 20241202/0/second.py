with open("file1", "r") as f:
	res = f.read()
pos = len(res) // 3
while pos < len(res) and res[pos] != "\n":
	pos+=1
print(res[:pos])
