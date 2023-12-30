from collections import defaultdict
from itertools import permutations
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[set[str], defaultdict[str, int]]:
    people: set[str] = set()
    scores: defaultdict[str, int] = defaultdict(lambda: 0)
    for row in inp:
        row = row.replace("gain ", "").replace("lose ", "-").strip()
        data: list[str] = row.split(" ")
        scores[data[0][0] + data[-1][0]] += int(data[2])
        scores[data[-1][0] + data[0][0]] += int(data[2])
        people.add(data[0][0])

    return people, scores


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    people: set[str]
    scores: defaultdict[str, int]
    people, scores = parse_inp(inp)

    best: int = 0
    for permute in permutations(people):
        score: int = 0
        order: str = "".join(permute) + permute[0]
        for first, second in zip(order, order[1:]):
            score += scores[first + second]
        best = max(best, score)

    return best


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    people: set[str]
    scores: defaultdict[str, int]
    people, scores = parse_inp(inp)

    best: int = 0
    for permute in permutations(people):
        score: int = 0
        order: str = "".join(permute)
        for first, second in zip(order, order[1:]):
            score += scores[first + second]
        best = max(best, score)

    return best


def main() -> None:
    test_input: str = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 330
    test_output_part_2_expected: OUTPUT_TYPE = 286

    file_location: str = "python/Advent of Code/2015/Day 13/input.txt"
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
