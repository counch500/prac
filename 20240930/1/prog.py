a, b = eval(input())
print([i for i in range(a, b) if not any(i % j == 0 for j in range(2, int(i ** 0.5) + 1)) and i != 1])
