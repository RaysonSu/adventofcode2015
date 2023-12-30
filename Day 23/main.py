OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regs: dict[str, int] = {"a": 0, "b": 0}
    instruction: int = 0

    while True:
        if instruction >= len(inp):
            return regs["b"]

        jumped: bool = False

        ins: str = inp[instruction].strip()
        chars: list[str] = ins.replace(",", "").split(" ")
        print(regs, instruction, ins, len(inp))

        if chars[0] == "hlf":
            regs[chars[1]] >>= 1
        elif chars[0] == "tpl":
            regs[chars[1]] *= 3
        elif chars[0] == "inc":
            regs[chars[1]] += 1
        elif chars[0] == "jmp":
            jumped = True
            instruction += int(chars[1])
        elif chars[0] == "jie":
            if regs[chars[1]] % 2 == 0:
                jumped = True
                instruction += int(chars[2])
        elif chars[0] == "jio":
            if regs[chars[1]] == 1:
                jumped = True
                instruction += int(chars[2])

        if not jumped:
            instruction += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    regs: dict[str, int] = {"a": 1, "b": 0}
    instruction: int = 0

    while True:
        if instruction >= len(inp):
            return regs["b"]

        jumped: bool = False

        ins: str = inp[instruction].strip()
        chars: list[str] = ins.replace(",", "").split(" ")
        print(regs, instruction, ins, len(inp))

        if chars[0] == "hlf":
            regs[chars[1]] >>= 1
        elif chars[0] == "tpl":
            regs[chars[1]] *= 3
        elif chars[0] == "inc":
            regs[chars[1]] += 1
        elif chars[0] == "jmp":
            jumped = True
            instruction += int(chars[1])
        elif chars[0] == "jie":
            if regs[chars[1]] % 2 == 0:
                jumped = True
                instruction += int(chars[2])
        elif chars[0] == "jio":
            if regs[chars[1]] == 1:
                jumped = True
                instruction += int(chars[2])

        if not jumped:
            instruction += 1


def main() -> None:
    test_input: str = """inc a
jio a, +2
tpl a
inc a
inc b
tpl b"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2015/Day 23/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed.copy())

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file.copy())}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    print(f"Part 2: {main_part_2(input_file.copy())}")


if __name__ == "__main__":
    main()
