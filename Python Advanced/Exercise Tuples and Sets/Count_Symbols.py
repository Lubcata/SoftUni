text = input()
symbols = {}

for el in text:
    symbols[el] = text.count(el)


for symbol, times in sorted(symbols.items()):
    print(f"{symbol}: {times} time/s")