from collections import deque

collection = deque()

while True:
    data = input()
    if data == "End":
        print(f"{len(collection)} people remaining.")
        break
    elif data == "Paid":
        while collection:
            print(collection.popleft())
    else:
        collection.append(data)
