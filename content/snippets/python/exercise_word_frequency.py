from collections import Counter
import re

text = "This is a test. This test is simple."
words = re.findall(r"[a-zA-Z]+", text.lower())
counts = Counter(words)

for word, count in sorted(counts.items(), key=lambda p: (-p[1], p[0])):
    print(f"{word}: {count}")
