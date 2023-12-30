F = open("python/Advent of Code/2015/Day 2/input.txt", "r").readlines()

ret = 0
for i in F:
    data = i.split("x")
    data = list(map(int, data))
    ret += 2 * (data[0] * data[1] + data[1] * data[2] + data[0] * data[2])
    ret += (sum(data) - min(data) - max(data)) * min(data)
print(ret)
