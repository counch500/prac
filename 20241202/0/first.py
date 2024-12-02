import sys
with open(sys.argv[1], "rb") as f:
	res = f.read()
with open(sys.argv[1], "wb") as f:
	f.write(res[len(res) // 2:])
	f.write(res[:len(res) // 2])
