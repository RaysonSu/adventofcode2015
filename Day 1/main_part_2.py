F = open("python/Advent of Code/2015/Day 1/input.txt", "r").readline()

cur = 0
for index, value in enumerate(F):
    cur += {"(": 1, ")": -1}[value]
    if cur < 0:
        print(index + 1)
        exit()
