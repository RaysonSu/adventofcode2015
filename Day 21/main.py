from itertools import permutations
OUTPUT_TYPE = int


def main_part_1(inp: list[str], self_hp: int = 100) -> OUTPUT_TYPE:
    boss_hp: int = int(inp[0][12:])
    boss_attack: int = int(inp[1][8:])
    boss_defence: int = int(inp[2][7:])

    weapons: list[tuple[int, int, int]] = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]
    armor: list[tuple[int, int, int]] = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]
    rings: list[tuple[int, int, int]] = [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]

    weapon_choices: range = range(len(weapons))
    armor_choices: range = range(len(armor))
    ring_choices: list[tuple[int, int]]
    ring_choices = list(permutations(range(len(rings)), 2))

    choices: list[tuple[int, int, tuple[int, int]]]
    choices = []
    for weapon in weapon_choices:
        for arm in armor_choices:
            for ring in ring_choices:
                choices.append((weapon, arm, ring))

    min_cost: int = 1000000000
    for weapon, arm, ring in choices:
        cost: int = weapons[weapon][0] \
            + armor[arm][0] \
            + rings[ring[0]][0] \
            + rings[ring[1]][0]

        attack: int = weapons[weapon][1] \
            + armor[arm][1] \
            + rings[ring[0]][1] \
            + rings[ring[1]][1]

        defence: int = weapons[weapon][2] \
            + armor[arm][2] \
            + rings[ring[0]][2] \
            + rings[ring[1]][2]

        if defence == 5 and attack == 5:
            pass

        if attack <= boss_defence:
            continue

        if boss_attack <= defence:
            min_cost = min(min_cost, cost)
            continue

        if boss_hp // max(0, attack - boss_defence) <= self_hp // max(0, boss_attack - defence):
            min_cost = min(min_cost, cost)

    return min_cost


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    boss_hp: int = int(inp[0][12:])
    boss_attack: int = int(inp[1][8:])
    boss_defence: int = int(inp[2][7:])

    weapons: list[tuple[int, int, int]] = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]
    armor: list[tuple[int, int, int]] = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]
    rings: list[tuple[int, int, int]] = [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]

    weapon_choices: range = range(len(weapons))
    armor_choices: range = range(len(armor))
    ring_choices: list[tuple[int, int]]
    ring_choices = list(permutations(range(len(rings)), 2))

    choices: list[tuple[int, int, tuple[int, int]]]
    choices = []
    for weapon in weapon_choices:
        for arm in armor_choices:
            for ring in ring_choices:
                choices.append((weapon, arm, ring))

    max_cost: int = 0
    for weapon, arm, ring in choices:
        cost: int = weapons[weapon][0] \
            + armor[arm][0] \
            + rings[ring[0]][0] \
            + rings[ring[1]][0]

        attack: int = weapons[weapon][1] \
            + armor[arm][1] \
            + rings[ring[0]][1] \
            + rings[ring[1]][1]

        defence: int = weapons[weapon][2] \
            + armor[arm][2] \
            + rings[ring[0]][2] \
            + rings[ring[1]][2]

        if defence == 5 and attack == 5:
            pass

        if attack <= boss_defence:
            max_cost = max(max_cost, cost)
            continue

        if boss_attack <= defence:
            continue

        if boss_hp // max(0, attack - boss_defence) > 100 // max(0, boss_attack - defence):
            max_cost = max(max_cost, cost)

    return max_cost


def main() -> None:
    test_input: str = """Hit Points: 12
Damage: 7
Armor: 2"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 90
    test_output_part_2_expected: OUTPUT_TYPE = 0

    file_location: str = "python/Advent of Code/2015/Day 21/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 8)
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
