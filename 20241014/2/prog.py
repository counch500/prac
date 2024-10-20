from math import *

def view():
    print("\n".join("".join(line) for line in matrix))

def normalize(x, minIn, maxIn, minOut, maxOut):
    return (x - minIn) * (maxOut - minOut) / (maxIn - minIn) + minOut

def drawLine(ix0, iy0, iy1):
    ix1 = ix0 + 1
    if iy0 > iy1:
        iy0, iy1 = iy1, iy0
        ix0, ix1 = ix1, ix0
    for iy in range(iy0, iy1):
        if H - 1 - iy >= 0:
            matrix[H - 1 - iy][ix0] = '*'
    if iy1 < H:
        matrix[H - 1 - iy1][ix1] = '*'

W, H, A, B, fun = input().split()
W, H, A, B = int(W), int(H), float(A), float(B)
fun = lambda x, fun=fun: eval(fun)
matrix = [[' '] * W for _ in range(H)]

miny = fun(normalize(0, 0, W - 1, A, B))
maxy = miny

for ix in range(W):
    y = fun(normalize(ix, 0, W - 1, A, B))
    miny = min(miny, y)
    maxy = max(maxy, y)
iy0 = round(normalize(fun(normalize(0, 0, W, A, B)), miny, maxy, 0, H - 1))
for ix in range(W - 1):
    iy1 = round(normalize(fun(normalize(ix + 1, 0, W - 1, A, B)), miny, maxy, 0, H - 1))
    drawLine(ix, iy0, iy1)
    iy0 = iy1
view()

