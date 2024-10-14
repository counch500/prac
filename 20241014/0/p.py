W = 60
H = 20
screen = [['.']*W for i in range(H)]
for i in range(7):
	screen[i][i+10] = "&"
print("\n".join(["".join(s) for s in screen]))
