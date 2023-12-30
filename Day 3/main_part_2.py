F = open("python/Advent of Code/2015/Day 3/input.txt", "r").readline() + " "

santa = F[0::2] + "  "
robo = F[1::2] + "  "

directions = {">": 40000, "<": -40000, "^": 1, "v": -1, " ": 0}

seen = {0}
location_santa = 0
location_robo = 0
for san, rob in zip(santa, robo):
    location_santa += directions[san]
    location_robo += directions[rob]
    seen.add(location_santa)
    seen.add(location_robo)

print(len(seen))
