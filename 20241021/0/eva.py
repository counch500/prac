expr = input()
a, b = eval(input())
print(eval(expr, None, {"x": a, "y": b}))
print(eval(expr, None, {"x": b, "y": a}))

