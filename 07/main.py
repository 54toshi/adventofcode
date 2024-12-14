from itertools import product


def check_equation(sum_given, values, symbols):
    for operations in product(symbols, repeat=len(values) - 1):
        sum_new = values[0]
        for i, operation in enumerate(operations):
            if operation == "+":
                sum_new += values[i + 1]
            elif operation == "*":
                sum_new *= values[i + 1]
            elif operation == "|":
                sum_new = int(str(sum_new) + str(values[i + 1]))
            if sum_new > sum_given:
                break
        if sum_new == sum_given:
            return True
    return False


def part_one():
    with open("input.txt", "r") as file:
        final_sum = 0
        for equation in file:
            sum_given = int(equation.split(":")[0])
            values = list(map(int, equation.split(": ")[1].strip().split(" ")))
            if check_equation(sum_given, values, "+*"):
                final_sum += sum_given
        return final_sum


def part_two():
    final_sum = 0
    with open("input.txt", "r") as file:
        for i, equation in enumerate(file.readlines()):
            print(f"{i+1}/850 => {equation.strip()}")
            sum_given = int(equation.split(":")[0])
            values = list(map(int, equation.split(": ")[1].strip().split(" ")))
            if check_equation(sum_given, values, "+*|"):
                final_sum += sum_given
        return final_sum


if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
