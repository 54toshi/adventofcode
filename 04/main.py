import numpy as np


def part_one():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    matrix = np.array([list(line.rstrip("\n")) for line in lines])
    xmas_cnt = int()

    # horizontal
    for i in range(0, len(matrix[0])):
        row = "".join(matrix[i])
        if "XMAS" in row:
            xmas_cnt += row.count("XMAS")
        if "SAMX" in row:
            xmas_cnt += row.count("SAMX")

    # vertical
    for i in range(0, len(matrix[0])):
        if "XMAS" in "".join(matrix[:, i]):
            xmas_cnt += "".join(matrix[:, i]).count("XMAS")
        if "SAMX" in "".join(matrix[:, i]):
            xmas_cnt += "".join(matrix[:, i]).count("SAMX")

    # principal diagonal
    for i in range(int(-len(matrix[0]) + 4), int(len(matrix[0]) - 3)):
        diagonal = matrix.diagonal(i)
        if "XMAS" in "".join(diagonal):
            xmas_cnt += "".join(diagonal).count("XMAS")
        if "SAMX" in "".join(diagonal):
            xmas_cnt += "".join(diagonal).count("SAMX")

    # anti-diagonal
    for i in range(int(-len(matrix[0]) + 4), int(len(matrix[0]) - 3)):
        diagonal = np.fliplr(matrix).diagonal(i)  # horizontal flip
        if "XMAS" in "".join(diagonal):
            xmas_cnt += "".join(diagonal).count("XMAS")
        if "SAMX" in "".join(diagonal):
            xmas_cnt += "".join(diagonal).count("SAMX")
    return xmas_cnt


def part_two():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    matrix = np.array([list(line.rstrip("\n")) for line in lines])

    x_cnt = 0
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            if (
                i < len(matrix[0]) - 2
                and j < len(matrix[0]) - 2
                and matrix[i + 1][j + 1] == "A"
                and (
                    (matrix[i][j] == "M" and matrix[i + 2][j + 2] == "S")
                    or (matrix[i][j] == "S" and matrix[i + 2][j + 2] == "M")
                )
                and (
                    (matrix[i][j + 2] == "M" and matrix[i + 2][j] == "S")
                    or (matrix[i][j + 2] == "S" and matrix[i + 2][j] == "M")
                )
            ):
                x_cnt += 1
    return x_cnt


print("part one: ", part_one())
print("part two: ", part_two())
