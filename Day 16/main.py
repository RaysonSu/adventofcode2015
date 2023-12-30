OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[set[tuple[str, int]]]:
    ret: list[set[tuple[str, int]]] = []
    for row in inp:
        row = row.strip().split(": ", 1)[1]
        items: set[tuple[str, int]] = set()
        for know in row.split(", "):
            items.add((
                know.split(": ")[0],
                int(know.split(": ")[1])
            ))

        ret.append(items)
    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    base_data: set[tuple[str, int]] = {
        ("children", 3),
        ("cats", 7),
        ("samoyeds", 2),
        ("pomeranians", 3),
        ("akitas", 0),
        ("vizslas", 0),
        ("goldfish", 5),
        ("trees", 3),
        ("cars", 2),
        ("perfumes", 1),
    }

    sues: list[set[tuple[str, int]]] = parse_inp(inp)
    for sue, objects in enumerate(sues, 1):
        if objects.issubset(base_data):
            return sue

    return 0


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    base_data: dict[str, int] = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    sues: list[set[tuple[str, int]]] = parse_inp(inp)
    for sue, objects in enumerate(sues, 1):
        for key, value in objects:
            if key in ["cats", "trees"]:
                if value <= base_data[key]:
                    break
            elif key in ["pomeranians", "goldfish"]:
                if value >= base_data[key]:
                    break
            else:
                if value != base_data[key]:
                    break
        else:
            return sue

    return 0


def main() -> None:
    test_input: str = """Sue 1: goldfish: 3, cars: 2, samoyeds: 2
Sue 2: perfumes: 1, trees: 3, goldfish: 5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 2
    test_output_part_2_expected: OUTPUT_TYPE = 1

    file_location: str = "python/Advent of Code/2015/Day 16/input.txt"
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
