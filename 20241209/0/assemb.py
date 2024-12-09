import readline

while s := input('> '):
	match s.split():
		case ["mov", r1, r2]:
			res = print(f"moving {r2} to {r1}")
		case ("pop" | "push") as cmd, *regs if len(regs) > 0:
			res = print(f"{cmd}ing {reglist}")
		case cmd, r1:
			print(f"making {cmd} with {r1}")
		case _:
			print("Parse error")
