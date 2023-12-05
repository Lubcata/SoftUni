import re

eggs = input()
pattern = r"[@#]+([a-z]+)[@#]+[\!\@\$\%\^\&\*\/]+(\d+)[\/]+"
match = re.findall(pattern, eggs)

if eggs:
    for egg in match:
        amount = egg[1]
        color = egg[0]
        print(f"You found {amount} {color} eggs!")
