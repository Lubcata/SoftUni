from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

worms_count = len(worms)
matches = 0

while worms and holes:
    curr_hole = holes[0]
    curr_worm = worms[-1]

    if curr_worm == curr_hole:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")

if not worms and matches == worms_count:
    print("Every worm found a suitable hole!")
elif not worms and matches < worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(el) for el in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(el) for el in holes)}")

