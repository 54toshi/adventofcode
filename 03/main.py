import re


def part_one():
    with open("input.txt", "r") as file:
        nums = re.findall("(?<=mul\()\d{1,3},\d{1,3}(?=\))", file.read())
        sum_nums_multiplied = 0
        for i in nums:
            sum_nums_multiplied += int(i.split(",")[0]) * int(i.split(",")[1])
        return sum_nums_multiplied


def part_two():
    with open("input.txt", "r") as file:
        instructions = re.findall(
            "(?<=mul\()\d{1,3},\d{1,3}(?=\))|do\(\)|don't\(\)", file.read()
        )
        sum_nums_multiplied = 0
        enabled = True
        for i in instructions:
            if "do()" in i:
                enabled = True
            elif "don't()" in i:
                enabled = False
            elif enabled:
                sum_nums_multiplied += int(i.split(",")[0]) * int(i.split(",")[1])
        return sum_nums_multiplied


print("part one: ", part_one())
print("part two: ", part_two())
