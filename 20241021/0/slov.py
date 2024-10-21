count = {}
k = input()
k = k.lower()
for word in k.split():
	count[word] = count.get(word, 0) + 1
print(count)

