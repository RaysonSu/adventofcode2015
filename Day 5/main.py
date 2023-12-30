OUTPUT_TYPE = int


def is_nice_p1(string: str) -> bool:
    if sum([string.count(x) for x in "aeiou"]) < 3:
        return False

    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False

    for first, second in zip(string, string[1:]):
        if first == second:
            return True

    return False


def is_nice_p2(string: str) -> bool:
    for first, third in zip(string, string[2:]):
        if first == third:
            break
    else:
        return False

    pairs: list = [""]
    for first, second in zip(string, string[1:]):
        if (first + second) in pairs[:-1]:
            return True
        pairs.append(first + second)

    return False


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row in inp:
        if is_nice_p1(row.strip()):
            ret += 1
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row in inp:
        if is_nice_p2(row.strip()):
            ret += 1
    return ret


def main() -> None:
    test_input: str = """ugknbfddgicrmopn
jchzalrnumimnmhp
qjhvhtzxzqqjkmpb
uurcxstgmygtbstg"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1
    test_output_part_2_expected: OUTPUT_TYPE = 1

    file_location: str = "python/Advent of Code/2015/Day 5/input.txt"
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
