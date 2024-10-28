def fun(a):
	for i in range(a):
		print(">>")
		yeild f"<{i}>"
		print("<<")
res = fun(4)
n = next(res)
print(n)
