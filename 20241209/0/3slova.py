import readline

class C():
	pass

C.a, C.b, C.c = input("words:").split()
while s:= input("> "):
	res = s.split()
	match res:
		case C.a, *_ if "yes" in res:
			print(1)
		case [C.b]:
			print(2)
		case C.c, *_, C.b:
			print(3)
