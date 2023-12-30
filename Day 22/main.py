from __future__ import annotations
import heapq
OUTPUT_TYPE = int


class State:
    def __init__(self,
                 hp: int,
                 mana: int,
                 mana_used: int = 0,
                 damage_dealt: int = 0,
                 boss_damage: int = 8,
                 boss_hp: int = 14,
                 effects: dict[str, int] = {},
                 logs: str = "",
                 extra_dmg: int = 0) -> None:

        self.hp: int = hp
        self.mana: int = mana
        self.mana_used: int = mana_used
        self.damage_dealt: int = damage_dealt
        self.boss_damage: int = boss_damage
        self.boss_hp: int = boss_hp
        self.effects: dict[str, int] = effects
        self.logs: str = logs
        self.extra_dmg: int = extra_dmg

    def generate_neighbours(self) -> list[State]:
        ret: list[State] = []
        costs: dict[str, int] = {
            "miss": 53,
            "drai": 73,
            "shie": 113,
            "pois": 173,
            "rech": 229
        }
        for spell in ["miss", "drai", "shie", "pois", "rech"]:
            # player turn
            armor: int = 0
            tmp_hp: int = self.hp
            tmp_damage_dealt: int = self.damage_dealt
            tmp_mana: int = self.mana
            tmp_mana_used: int = self.mana_used
            tmp_effects: dict[str, int] = self.effects.copy()
            tmp_logs: str = self.logs

            tmp_logs += "\n-- Player turn --\n"
            tmp_logs += f"- Player has {tmp_hp} hit points, {armor} armor, {tmp_mana} mana\n"
            tmp_logs += f"- Boss has {self.boss_hp - tmp_damage_dealt} hit points\n"
            tmp_hp -= self.extra_dmg
            if self.extra_dmg > 0:
                tmp_logs += f"Player takes {self.extra_dmg} extra damage.\n"
            if tmp_hp <= 0:
                continue

            for effect, timer in tmp_effects.items():
                if timer <= 0:
                    continue

                if effect == "shie":
                    armor = 7
                    tmp_logs += f"Shield's timer is now {timer - 1}.\n"
                elif effect == "pois":
                    tmp_damage_dealt += 3
                    tmp_logs += f"Poison deals 3 damage; it's timer is now {timer - 1}.\n"
                    if tmp_damage_dealt >= self.boss_hp:
                        tmp_logs = tmp_logs[:-1]
                        tmp_logs += " This kills the boss, and the player wins.\n"
                elif effect == "rech":
                    tmp_mana += 101
                    tmp_logs += f"Recharge provides 101 mana; timer is now {timer - 1}.\n"

                tmp_effects[effect] -= 1
                if tmp_effects[effect] == 0:
                    if effect == "shie":
                        tmp_logs += "Shield's wears off, decreasing armor by 7.\n"
                    elif effect == "pois":
                        tmp_logs += "Poison wears off.\n"
                    elif effect == "rech":
                        tmp_logs += "Recharge wears off.\n"

            tmp_mana -= costs[spell]
            tmp_mana_used += costs[spell]

            if tmp_mana < 0:
                continue

            if spell == "miss":
                tmp_damage_dealt += 4
                tmp_logs += "Player casts Magic Missile, dealing 4 damage.\n"
            elif spell == "drai":
                tmp_hp += 2
                tmp_logs += "Player casts Drain, dealing 4 damage, and healing 2 hit points.\n"
                tmp_damage_dealt += 2
            elif spell == "shie":
                if "shie" in tmp_effects.keys() and tmp_effects["shie"] > 0:
                    continue
                tmp_logs += "Player casts Shield, increasing armor by 7.\n"
                tmp_effects["shie"] = 6
            elif spell == "pois":
                if "pois" in tmp_effects.keys() and tmp_effects["pois"] > 0:
                    continue
                tmp_logs += "Player casts Poision.\n"
                tmp_effects["pois"] = 6
            elif spell == "rech":
                if "rech" in tmp_effects.keys() and tmp_effects["rech"] > 0:
                    continue
                tmp_logs += "Player casts Recharge.\n"

                tmp_effects["rech"] = 5

            if tmp_damage_dealt >= self.boss_hp:
                tmp_logs = tmp_logs[:-1]
                tmp_logs += f" This kills the boss, and the player wins.\n"

#            tmp_logs += f"{spell} {tmp_hp} {tmp_damage_dealt} {tmp_mana_used} {tmp_mana} {tmp_effects}\n"

            # boss turn
            tmp_logs += "\n-- Boss turn --\n"
            tmp_logs += f"- Player has {tmp_hp} hit points, {armor} armor, {tmp_mana} mana\n"
            tmp_logs += f"- Boss has {self.boss_hp - tmp_damage_dealt} hit points\n"

            if tmp_hp <= 0:
                continue

            armor = 0
            for effect, timer in tmp_effects.items():
                if timer <= 0:
                    continue

                if effect == "shie":
                    armor = 7
                    tmp_logs += f"Shield's timer is now {timer - 1}.\n"
                elif effect == "pois":
                    tmp_damage_dealt += 3
                    tmp_logs += f"Poison deals 3 damage; it's timer is now {timer - 1}.\n"
                    if tmp_damage_dealt >= self.boss_hp:
                        tmp_logs = tmp_logs[:-1]
                        tmp_logs += " This kills the boss, and the player wins.\n"
                elif effect == "rech":
                    tmp_mana += 101
                    tmp_logs += f"Recharge provides 101 mana; timer is now {timer - 1}.\n"

                tmp_effects[effect] -= 1
                if tmp_effects[effect] == 0:
                    if effect == "shie":
                        tmp_logs += "Shield's wears off, decreasing armor by 7.\n"
                    elif effect == "pois":
                        tmp_logs += "Poison wears off.\n"
                    elif effect == "rech":
                        tmp_logs += "Recharge wears off.\n"

            if tmp_damage_dealt < self.boss_hp:
                if armor == 0:
                    tmp_logs += f"Boss attacks for {self.boss_damage} damage!\n"
                else:
                    tmp_logs += f"Boss attacks for {self.boss_damage} - {armor} = {max(1, self.boss_damage - armor)} damage!\n"

                tmp_hp -= max(1, self.boss_damage - armor)

            if tmp_hp <= 0:
                continue

#            tmp_logs += f"-/- {tmp_hp} {tmp_damage_dealt} {tmp_mana_used} {tmp_mana} {tmp_effects}\n"

            ret.append(State(
                tmp_hp,
                tmp_mana,
                tmp_mana_used,
                tmp_damage_dealt,
                self.boss_damage,
                self.boss_hp,
                tmp_effects,
                tmp_logs,
                self.extra_dmg
            ))

        return ret

    def __lt__(self, other) -> bool:
        return self.mana_used < other.mana_used


def main_part_1(inp: list[str], data: tuple[int, int] = (50, 500)) -> OUTPUT_TYPE:
    boss_hp: int = int(inp[0][12:])
    boss_att: int = int(inp[1][8:])

    initial_state: State = State(data[0], data[1], 0, 0, boss_att, boss_hp)
    states: list[State] = [initial_state]

    while states:
        current_state: State
        current_state = heapq.heappop(states)

        if current_state.damage_dealt >= boss_hp:
            #            print(current_state.logs)
            return current_state.mana_used

        for new_state in current_state.generate_neighbours():
            heapq.heappush(states, new_state)

    return -1


def main_part_2(inp: list[str], data: tuple[int, int] = (50, 500)) -> OUTPUT_TYPE:
    boss_hp: int = int(inp[0][12:])
    boss_att: int = int(inp[1][8:])

    initial_state: State = State(
        data[0], data[1], 0, 0, boss_att, boss_hp, {}, "", 1)
    states: list[State] = [initial_state]

    while states:
        current_state: State
        current_state = heapq.heappop(states)

        if current_state.damage_dealt >= boss_hp:
            #            print(current_state.logs)
            return current_state.mana_used

        for new_state in current_state.generate_neighbours():
            heapq.heappush(states, new_state)

    return -1


def main() -> None:
    test_input: str = """Hit Points: 14
Damage: 8"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 641
    test_output_part_2_expected: OUTPUT_TYPE = -1

    file_location: str = "python/Advent of Code/2015/Day 22/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, (10, 250))
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed, (10, 250))

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
