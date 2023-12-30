from itertools import chain, combinations
OUTPUT_TYPE = int


def split(amount: list[int], cap: int, count: int = 100000000000) -> list[tuple[list[int], list[int]]]:
    amount = amount.copy()
    amount.sort()

    ret: list[tuple[list[int], list[int]]] = []
    stack: list[int] = [0]
    while stack and len(ret) < count:
        if stack[-1] == len(amount):
            stack.pop()
            if stack:
                stack[-1] += 1
            continue

        total: int = sum([amount[index] for index in stack])
        if total < cap:
            stack.append(stack[-1] + 1)
        elif total == cap:
            ret.append((
                [amount[index] for index in stack],
                [amount[index] for index in range(len(amount))
                 if index not in stack]
            ))
            stack[-1] += 1
        elif total > cap:
            stack.pop()
            stack[-1] += 1

    return ret


def key(data: list[int]) -> int:
    qe: int = 1
    for i in data:
        qe *= i

    return (len(data) << 64) + qe


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    weights: list[int] = list(map(int, inp))
    weight_third: int = sum(weights) // 3

    splits: list[list[int]] = []
    c = split(weights, weight_third)
    for i, d in enumerate(c):
        first, other = d
        if split(other, weight_third, 1):
            splits.append(first)

    splits.sort(key=key)

    ret: int = 1
    for i in splits[0]:
        ret *= i

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    weights: list[int] = list(map(int, inp))
    weight_third: int = sum(weights) // 4

    splits: list[list[int]] = []
    c = split(weights, weight_third)
    for i, d in enumerate(c):
        first, other = d
        yes: bool = False
        other = split(other, weight_third)
        q: int = 0
        while q < len(other) and not yes:
            _, x = other[q]
            if split(x, weight_third, 1):
                yes = True
            q += 1

        if yes:
            splits.append(first)
        print("\r", i, len(c), end="")

    splits.sort(key=key)

    ret: int = 1
    for i in splits[0]:
        ret *= i

    return ret


def main() -> None:
    test_input: str = """11
9 
10
8
2
7
5
4
3
1"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 99
    test_output_part_2_expected: OUTPUT_TYPE = 44

    file_location: str = "python/Advent of Code/2015/Day 24/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
