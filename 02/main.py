def is_valid_report(levels):
    is_valid_report = True

    for i, value in enumerate(levels):
        if levels == sorted(levels) or levels == sorted(levels, reverse=True):
            if (
                i != 0
                and i <= len(levels)
                and (
                    levels[i - 1] > (value + 3)
                    or levels[i - 1] < (value - 3)
                    or levels[i - 1] == value
                )
            ):
                is_valid_report = False
                break
        else:
            is_valid_report = False

    return is_valid_report


def part_one():
    with open("input.txt", "r") as file:
        count_safe_levels = 0
        for report in file:
            levels = list(map(int, report.strip().split()))

            if is_valid_report(levels):
                count_safe_levels += 1

        return count_safe_levels


def part_two():
    with open("input.txt", "r") as file:
        count_safe_levels = 0
        for report in file:
            levels = list(map(int, report.strip().split()))

            if is_valid_report(levels):
                count_safe_levels += 1
                continue

            for i in range(len(levels)):
                dampened_levels = levels[:i] + levels[i + 1 :]
                if is_valid_report(dampened_levels):
                    count_safe_levels += 1
                    break
        return count_safe_levels


print("part one: ", part_one())
print("part two: ", part_two())
