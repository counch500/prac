class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput("Invalid input")

    for coord in (x1, y1, x2, y2, x3, y3):
        if not isinstance(coord, (int, float)):
            raise InvalidInput("Invalid input")

    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    if a + b <= c or a + c <= b or b + c <= a:
        raise BadTriangle("Not a triangle")

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area

while inStr := input():
    try:
        area = triangleSquare(inStr)
        print(f"{round(area, 2):.2f}")
        break
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')

