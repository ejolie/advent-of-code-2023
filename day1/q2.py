import re

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def to_int(char):
    if char.isdigit():
        return int(char)
    return NUMBER_MAP[char]


def solve():
    total = 0
    # '(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))' - correct (54203)
    # '([0-9]|one|two|three|four|five|six|seven|eight|nine)' - incorrect (54185)
    pattern = re.compile(r"(?=([0-9]|{0}))".format("|".join(NUMBER_MAP)))

    with open("q2.txt", "r") as file:
        for line in file:
            matches = re.findall(pattern, line.strip())
            if matches:
                first_digit = matches[0]
                last_digit = matches[-1]

                total += to_int(first_digit) * 10 + to_int(last_digit)

    return total


if __name__ == "__main__":
    print(solve())  # 54203
