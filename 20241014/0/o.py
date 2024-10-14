from math import sin
A, B = -4, 4
W = 60
H = 20
screen = [['.']*W for i in range(H)]
def scale(a, b, A, B, x):
        coef = (B - A)/(b - a)
        X = coef*(x - a) + A
        return(X)

for i in range(W):
        x = scale(0, W - 1, A, B, i)
        y = sin(x)
        spc = round(scale(-1, 1, 0, H - 1, y))
        screen[spc][i] = "@"
print("\n".join(["".join(s) for s in screen]))
