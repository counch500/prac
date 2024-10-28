from itertools import product
print([f"{a}{n}" for a, n in product("abcdefgh", range(1,9))])
