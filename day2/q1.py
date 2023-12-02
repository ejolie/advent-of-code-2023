import os

MAX_CUBE_COUNT_MAP = {"red": 12, "green": 13, "blue": 14}


def solve():
    total = 0
    here = os.path.dirname(os.path.abspath(__file__))
    filpath = os.path.join(here, "q1.txt")

    with open(filpath, "r") as f:
        for line in f:
            s = line.strip().split(":")
            game_id = int(s[0].split(" ")[-1])
            game_set = s[1].strip().split(";")
            is_valid_game = True

            for game in game_set:
                cubes = game.split(",")
                for cube in cubes:
                    count, color = cube.strip().split(" ")
                    if int(count) > MAX_CUBE_COUNT_MAP[color]:
                        is_valid_game = False
                        break
                if not is_valid_game:
                    break

            if is_valid_game:
                total += game_id

    return total


if __name__ == "__main__":
    print(solve())
