
N = int(input())
for i in range(N, N + 3):
    for j in range(N, N + 3):
        product = i * j
        digit_sum = sum(int(digit) for digit in str(product))

        if digit_sum == 6:
            output = ":=)"
        else:
            output = str(product)

        print(f"{i} * {j} = {output:<5}", end=' ')
    print()

