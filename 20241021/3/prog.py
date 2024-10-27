import re
from collections import Counter

W = int(input().strip())

lines = []
while line := input():
    lines.append(line)

text = " ".join(lines)
cleaned_text = re.sub(r'[^a-zA-Z\s]', ' ', text).lower()

words = cleaned_text.split()
filtered_words = [word for word in words if len(word) == W]

word_count = Counter(filtered_words)

if word_count:
    max_frequency = max(word_count.values())
    most_popular_words = [word for word, count in word_count.items() if count == max_frequency]
    print(" ".join(sorted(most_popular_words)))

