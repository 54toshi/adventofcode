import os
import time


def part_one():
    with open("input.txt", "r") as file:
        matrix = [list(line.rstrip("\n")) for line in file]

        # os.system("clear")
        # print("\n".join(["".join(row) for row in matrix]))

        while True:
            found = False
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    char = matrix[i][j]

                    if char == "^":
                        matrix[i][j] = "X"
                        if i == 0:
                            return sum(row.count("X") for row in matrix)
                        elif matrix[i - 1][j] == "." or matrix[i - 1][j] == "X":
                            matrix[i - 1][j] = "^"
                        elif matrix[i - 1][j] == "#":
                            if matrix[i][j + 1] == "#":
                                matrix[i - 1][j] = "v"
                            else:
                                matrix[i][j + 1] = ">"
                        found = True
                        break

                    elif char == ">":
                        matrix[i][j] = "X"
                        if j == len(matrix):
                            return sum(row.count("X") for row in matrix)
                        elif matrix[i][j + 1] == "." or matrix[i][j + 1] == "X":
                            matrix[i][j + 1] = ">"
                        elif matrix[i][j + 1] == "#":
                            if matrix[i + 1][j] == "#":
                                matrix[i][j - 1] = "<"
                            else:
                                matrix[i + 1][j] = "v"
                        found = True
                        break

                    elif char == "<":
                        matrix[i][j] = "X"
                        if j == 0:
                            return sum(row.count("X") for row in matrix)
                        elif matrix[i][j - 1] == "." or matrix[i][j - 1] == "X":
                            matrix[i][j - 1] = "<"
                        elif matrix[i][j - 1] == "#":
                            if matrix[i - 1][j] == "#":
                                matrix[i][j + 1] = ">"
                            else:
                                matrix[i - 1][j] = "^"
                        found = True
                        break

                    elif char == "v":
                        matrix[i][j] = "X"
                        if i == len(matrix) - 1:
                            return sum(row.count("X") for row in matrix)
                        elif matrix[i + 1][j] == "." or matrix[i + 1][j] == "X":
                            matrix[i + 1][j] = "v"
                        elif matrix[i + 1][j] == "#":
                            if matrix[i][j - 1] == "#":
                                matrix[i - 1][j] = "^"
                            else:
                                matrix[i][j - 1] = "<"
                        found = True
                        break
                if found:
                    break

            # os.system("clear")
            # print("\n".join(["".join(row) for row in matrix]))
            # time.sleep(0.05)


def part_two():
    with open("input.txt", "r") as file:
        return 0


print("part one: ", part_one())
print("part two: ", part_two())
