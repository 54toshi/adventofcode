# conditional sorting algorithm needed
# get sum of middle page number of each correctly-ordered update


def is_valid(update, rules):
    for rule in rules:
        num1 = rule.split("|")[0]
        num2 = rule.split("|")[1]
        if (
            num1 in update
            and num2 in update
            and update.index(num1) > update.index(num2)
        ):
            return False
    return True


def part_one():
    with open("input.txt", "r") as file:
        rules = list()
        updates = list()
        for line in file:
            if "|" in line:
                rules.append(line.strip("\n"))
            elif "," in line:
                updates.append(line.strip("\n"))

    sum = 0
    for update in updates:
        if is_valid(update, rules):
            sum += int(update.split(",")[int(len(update.split(",")) / 2)])

    return sum


def part_two():
    with open("input.txt", "r") as file:
        rules = list()
        updates = list()
        for line in file:
            if "|" in line:
                rules.append(line.strip("\n"))
            elif "," in line:
                updates.append(line.strip("\n"))

    sum = 0
    for update in updates:
        valid_update = True
        update = update.split(",")

        while not is_valid(update, rules):
            for rule in rules:
                num1 = rule.split("|")[0]
                num2 = rule.split("|")[1]
                if (
                    num1 in update
                    and num2 in update
                    and update.index(num1) > update.index(num2)
                ):

                    update = (
                        update[0 : update.index(num2)]
                        + [num1, num2]
                        + update[update.index(num2) + 1 : update.index(num1)]
                        + update[update.index(num1) + 1 :]
                    )
                    valid_update = False

        if not valid_update:
            sum += int(update[int(len(update) / 2)])
    return sum


print("part one: ", part_one())
print("part two: ", part_two())
