
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[tuple[int, ...]]:
    ret: list[tuple[int, ...]] = []
    for row in inp:
        data: list[int] = [
            int(number)
            for number
            in "".join(
                char.replace(",", " ")
                for char
                in row
                if char.isnumeric() or char in "-, "
            ).split(" ")
            if number != ""
        ]

        ret.append(tuple(data))

    return ret


def valid(amounts: list[int], maxmium: int = 100):
    return sum(amounts) <= maxmium


def next_list(amounts: list[int], maxmium: int = 100):
    for i in range(len(amounts) - 1, -1, -1):
        attempt: list[int] = amounts.copy()
        attempt[i] += 1

        for j in range(len(amounts) - 1, i, -1):
            attempt[j] = 0

        if valid(attempt, maxmium):
            return attempt

    return amounts


def score(recipes: list[tuple[int, ...]], amounts: list[int]) -> int:
    scores: list[int] = [0 for _ in recipes[0]]
    for index, ingredient in enumerate(recipes):
        for other_index, score in enumerate(ingredient):
            scores[other_index] += score * amounts[index]

    ret: int = 1
    for score in scores:
        ret *= max(0, score)

    return ret


def calorie(cals: list[int], amounts: list[int]) -> int:
    return sum([x * y for x, y in zip(cals, amounts)])


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: list[tuple[int, ...]] = parse_inp(inp)
    data = [row[:-1] for row in data]

    current: list[int] = [0 for _ in range(len(inp) - 1)]
    prev: list[int] = []
    best: int = 0
    while current != prev:
        prev = current.copy()
        amounts: list[int] = current + [100 - sum(current)]
        best = max(best, score(data, amounts))
        current = next_list(current)

    return best


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: list[tuple[int, ...]] = parse_inp(inp)
    cals = [row[-1] for row in data]
    data = [row[:-1] for row in data]

    current: list[int] = [0 for _ in range(len(inp) - 1)]
    prev: list[int] = []
    best: int = 0
    while current != prev:
        prev = current.copy()
        amounts: list[int] = current + [100 - sum(current)]

        if calorie(cals, amounts) == 500:
            best = max(best, score(data, amounts))
        current = next_list(current)

    return best


def main() -> None:
    test_input: str = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 62842880
    test_output_part_2_expected: OUTPUT_TYPE = 57600000

    file_location: str = "python/Advent of Code/2015/Day 15/input.txt"
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
