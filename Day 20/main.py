OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> int:
    return int(inp[0])


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    num: int = parse_inp(inp)
    counts: list[int] = [0 for _ in range(num // 10)]

    elf: int = 1
    while True:
        for i in range(elf - 1, num // 10, elf):
            counts[i] += elf * 10

        if counts[elf - 1] > num:
            return elf

        elf += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    num: int = parse_inp(inp)
    counts: list[int] = [0 for _ in range(num // 11)]

    elf: int = 1
    while True:
        for i, _ in zip(range(elf - 1, num // 11, elf), range(50)):
            counts[i] += elf * 11

        if counts[elf - 1] > num:
            return elf

        elf += 1


def main() -> None:
    test_input: str = """100"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 6
    test_output_part_2_expected: OUTPUT_TYPE = 6

    file_location: str = "python/Advent of Code/2015/Day 20/input.txt"
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
