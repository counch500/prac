N = int(input())
i = N
while i <= N + 2:
    j = N
    while j <= N + 2:
        col = i * j
        r = 0
        tmp_col = col
        while tmp_col > 0:
            r += tmp_col % 10
            tmp_col //= 10

        if r == 6:
            result = ":=)"
        else:
            result = str(col)

        print(f"{i} * {j} = {result:<5}", end=' ')
        j += 1
    print()
    i += 1
