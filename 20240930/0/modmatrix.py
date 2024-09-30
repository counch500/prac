l, s = eval(input())
res = [i for i in range (l//2 + 1, s + 1, 2) if '3' not in str(i)]
print(res)

