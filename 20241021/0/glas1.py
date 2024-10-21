from string import ascii_lowercase

wovels = set("aouie")
consonants = set(ascii_lowercase) - wovels
letters = set(input("Vvedite:"))
print(len(letters & wovels), len(letters & consonants))

