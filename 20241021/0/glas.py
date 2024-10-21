from string import ascii_lowercase

glas = set()
soglas = set()
glas1 = set("aeiyou")
soglas2 = set("wrtnbvczsfdqghjklpm")
while True:
	k = set(input())
	if k == "":
		break
	k.ascii_lowercase
	k.split()
	for char in k:
		if char in glas1:
			glas.add(char)
		elif char in soglas1:
			soglas.add(char)
gl = frozenset(glas)
sg = frozenset(soglas)
print(len(gl), len(sg))
