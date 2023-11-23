import re

text = input()
word = input()

pattern = fr"\b({word.lower()})\b"
match = re.findall(pattern, text.lower())

result = len(match)

print(result)
