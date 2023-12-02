import os
import sys
from functools import reduce


def solve():
    total = 0
    here = os.path.dirname(os.path.abspath(__file__))
    filpath = os.path.join(here, "q2.txt")

    with open(filpath, "r") as f:
        lines = f.readlines()

    for line in lines:
        s = line.strip().split(":")
        game_set = s[1].strip().split(";")
        at_least_count_map = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for game in game_set:
            cubes = game.split(",")
            for cube in cubes:
                count, color = cube.strip().split(" ")
                at_least_count_map[color] = max(int(count), at_least_count_map[color])

        total += reduce(lambda acc, cur: acc * cur, at_least_count_map.values(), 1)

    return total


if __name__ == "__main__":
    print(solve())
