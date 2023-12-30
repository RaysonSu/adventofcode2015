OUTPUT_TYPE = int


def main_part_1(inp: list[str], target: int = 150) -> int:
    counts: list[int] = list(map(int, inp))

    ret: int = 0
    for i in range(2 ** len(counts)):
        total: int = 0
        count: int = 0
        while i:
            digit: int
            i, digit = divmod(i, 2)
            if digit:
                total += counts[count]
            count += 1

        if total == target:
            ret += 1

    return ret


def main_part_2(inp: list[str], target: int = 150) -> int:
    counts: list[int] = list(map(int, inp))

    lowest: int = len(inp)
    ret: int = 0
    for i in range(2 ** len(counts)):
        total: int = 0
        count: int = 0
        used: int = 0
        while i:
            digit: int
            i, digit = divmod(i, 2)
            if digit:
                total += counts[count]
                used += 1
            count += 1

        if total == target:
            if used == lowest:
                ret += 1
            elif used < lowest:
                lowest = used
                ret = 1

    return ret


def main() -> None:
    test_input: str = """20
15
10
5
5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4
    test_output_part_2_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2015/Day 17/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 25)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed, 25)

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
