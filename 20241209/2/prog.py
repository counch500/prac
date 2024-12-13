import math
import sys
import re

line_pattern = re.compile(r'^\s*(?:(\S+):)?\s*(\w+)\s*(.*)$')
variables, commands, labels = {}, [], {}

program = sys.stdin.read()
for i, line in enumerate(program.splitlines()):
    line = line.strip()
    if line:
        m = line_pattern.match(line)
        label, op, operands_str = m.groups()
        if label:
            labels[label] = len(commands)
        operands = operands_str.split() if operands_str else []
        commands.append((op, operands))

for op, operands in commands:
    if op.startswith("if") and len(operands) == 3:
        if operands[2] not in labels:
            sys.exit(0)

get_val = lambda t: float(t) if t.replace('.', '', 1).isdigit() else variables.get(t, 0)
pointer = 0
while pointer < len(commands):
    op, operands = commands[pointer]
    if op == "stop":
        break
    elif op == "store" and len(operands) == 2:
        variables[operands[1]] = get_val(operands[0])
    elif op in ["add", "sub", "mul", "div"] and len(operands) == 3:
        a, b = get_val(operands[0]), get_val(operands[1])
        variables[operands[2]] = {'add': a+b, 'sub': a-b, 'mul': a*b, 'div': a/b if b else math.inf}[op]
    elif op.startswith("if") and len(operands) == 3:
        a, b = get_val(operands[0]), get_val(operands[1])
        if (op == "ifeq" and a == b) or \
           (op == "ifne" and a != b) or \
           (op == "ifgt" and a > b) or \
           (op == "ifge" and a >= b) or \
           (op == "iflt" and a < b) or \
           (op == "ifle" and a <= b):
            pointer = labels[operands[2]]
            continue
    elif op == "out" and len(operands) == 1:
        print(get_val(operands[0]))
    pointer += 1


