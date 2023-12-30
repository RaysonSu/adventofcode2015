OUTPUT_TYPE = str

ALPHABET: str = "abcdefghjkmnpqrstuvwxyz"


def conv_to_num(string: str) -> int:
    ret: int = 0
    for char in string:
        ret *= len(ALPHABET)
        ret += ALPHABET.index(char)
    return ret


def conv_to_str(num: int) -> str:
    ret: str = ""
    while num:
        digit: int
        num, digit = divmod(num, len(ALPHABET))
        ret += ALPHABET[digit]

    return ret[::-1]


def is_valid(password: str) -> bool:
    if "i" in password or "o" in password or "l" in password:
        return False

    laps: set[str] = set()
    for left, right in zip(password, password[1:]):
        if left == right:
            laps.add(left)

    if len(laps) < 2:
        return False

    for left, middle, right in zip(password, password[1:], password[2:]):
        if ord(left) + 1 == ord(middle) and ord(middle) + 1 == ord(right):
            return True

    return False


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    guess: int = conv_to_num(inp[0].strip()) + 1
    while not is_valid(conv_to_str(guess)):
        guess += 1

    return conv_to_str(guess)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1([main_part_1(inp)])


def main() -> None:
    test_input: str = """ghjaaaaa"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "ghjaabcc"
    test_output_part_2_expected: OUTPUT_TYPE = "ghjbbcdd"

    file_location: str = "python/Advent of Code/2015/Day 11/input.txt"
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
