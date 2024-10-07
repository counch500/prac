n = int(input())
matrix1 = [list(map(int, input().split(","))) for _ in range(n)]
matrix2 = [list(map(int, input().split(","))) for _ in range(n)]

result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    for k in range(n):
      result[i][j] += matrix1[i][k] * matrix2[k][j]

for i in range(n):
  print(*result[i], sep=",")
