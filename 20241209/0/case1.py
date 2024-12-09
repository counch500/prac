res = eval(input())
match res:
	case 1, 2:
		print("Excact 1, 2")
	case a, 3:
		print(a, "with 3")
	case (3 | 4), *tail:
		print(a, "with", tail)
	case 2, *tail:
		print("2 with", tail)
	case _:
		print("Any", res)
