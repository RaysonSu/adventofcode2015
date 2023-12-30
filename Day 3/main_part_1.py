F = open("python/Advent of Code/2015/Day 3/input.txt", "r").readline()

directions = {">": 40000, "<": -40000, "^": 1, "v": -1}

seen = {0}
location = 0
for i in F:
    location += directions[i]
    seen.add(location)

print(len(seen))
