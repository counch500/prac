from string import ascii_lowercase
from timeit import Timer

wovels = set("aoiue")
consonants = set(ascii_lowercase) - wovels

letters = input("Vvedite:")

def func():
	return len(set(letters) & wovels), len(set(letters) & consonants)
T = Timer(func)
print(T.autorange())
