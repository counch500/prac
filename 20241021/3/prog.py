from collections import Counter

w = int(input())
text = ""
while s := input().lower():
    text += (s + " ")
l = len(text)
for i in range(l):
    if text[i] != " " and text[i].isalpha() == False:
        text = text.replace(text[i], " ")

words_freq = Counter(text.split())
words_w_freq = [word for word, cnt in words_freq.items() if cnt == w]
print(*sorted(words_w_freq))

