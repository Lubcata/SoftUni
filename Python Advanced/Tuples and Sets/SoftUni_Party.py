n = int(input())

guests = set(input() for x in range(n))

guest = input()
while guest != "END":
    if guest in guests:
        guests.remove(guest)
    guest = input()

print(len(guests))
for guest in sorted(guests):
    print(guest)