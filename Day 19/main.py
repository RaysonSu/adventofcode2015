OUTPUT_TYPE = int


def replace(string: str, repalcer: str, replaced: str) -> set[str]:
    ret: set[str] = set()

    index: int = 0
    while index <= len(string):
        if repalcer not in string[index:]:
            break

        ret.add(string[:index] + string[index:].replace(repalcer, replaced, 1))
        index += 1

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    seen: str = inp[-1]
    inp = inp[:-2]

    ret: set[str] = set()
    for task in inp:
        task = task.strip()
        ret = ret.union(replace(seen, task.split(
            " => ")[0], task.split(" => ")[1]))

    return len(ret)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    seen: set[str] = {inp[-1]}
    inp = inp[:-2]

    reps: int = 0
    while "e" not in seen:
        ret: set[str] = set()
        for chem in seen:
            for task in inp:
                task = task.strip()
                ret = ret.union(replace(chem, task.split(
                    " => ")[1], task.split(" => ")[0]))

        parsed: list[str] = [
            chem
            for chem in ret
            if "e" not in chem or chem == "e"]
        parsed.sort(key=len)
        seen = {parsed.pop(0)}
        reps += 1

    return reps


def main() -> None:
    test_input: str = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4
    test_output_part_2_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2015/Day 19/input.txt"
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
