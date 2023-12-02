def solve():
    total = 0

    with open("q1.txt", "r") as file:
        for line in file:
            nums = []
            for char in line.strip():
                if char.isdigit():
                    nums.append(int(char))
            if len(nums) >= 1:
                total += nums[0] * 10 + nums[-1]

    return total


if __name__ == "__main__":
    print(solve())  # 54667
