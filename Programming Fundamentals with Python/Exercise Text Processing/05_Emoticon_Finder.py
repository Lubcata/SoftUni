text = input()
for index, symbol in enumerate(text):
    if symbol == ":":
        if index + 1 < len(text):
            next_symbol = text[index + 1]
            if next_symbol != " ":
                result = symbol+next_symbol
                print(result)
