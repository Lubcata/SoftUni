import re

line = input()
pattern = r"(w{3}\.[a-zA-Z0-9\-]+\.[a-z\.?]+)"

while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    line = input()

