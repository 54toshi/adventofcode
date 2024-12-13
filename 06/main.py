# Algorithms used:
# FSM Finite State Machine
# Cycle Detection
# BFS Breadth First Search

# TODO: part 2

from pprint import pprint
from copy import deepcopy


def get_position_guard(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "^":
                return i, j


# returns mapped matrix
# returns False if looping
def map_matrix(matrix):

    i, j = get_position_guard(matrix)
    states = {f"x{i}y{j}d^": 1}

    # while in bounds of matrix
    while i != 0 and i != len(matrix) - 1 and j != 0 and j != len(matrix) - 1:

        direction = matrix[i][j]
        matrix[i][j] = "X"

        match direction:
            case "^":
                if matrix[i - 1][j] in [".", "X"]:
                    matrix[i - 1][j] = "^"
                    i -= 1
                else:  # turn right
                    matrix[i][j + 1] = ">"
                    j += 1
            case ">":
                if matrix[i][j + 1] in [".", "X"]:
                    matrix[i][j + 1] = ">"
                    j += 1
                else:  # turn right
                    matrix[i + 1][j] = "v"
                    i += 1
            case "v":
                if matrix[i + 1][j] in [".", "X"]:
                    matrix[i + 1][j] = "v"
                    i += 1
                else:  # turn right
                    matrix[i][j - 1] = "<"
                    j -= 1
            case "<":
                if matrix[i][j - 1] in [".", "X"]:
                    matrix[i][j - 1] = "<"
                    j -= 1
                else:  # turn right
                    matrix[i - 1][j] = "^"
                    i -= 1
            case _:
                raise Exception

        # check if looping by remembering how often a field got visited
        if f"x{i}y{j}d{direction}" in states:
            states[f"x{i}y{j}d{direction}"] = states.get(f"x{i}y{j}d{direction}") + 1
        else:
            states[f"x{i}y{j}d{direction}"] = 1
        if (
            states.get(f"x{i}y{j}d{direction}") > 15
        ):  # max 9 visits for nonlooping matrices
            # pprint("\n".join(["".join(row) for row in matrix]))
            return False

        # pprint("\n".join(["".join(row) for row in matrix]))
    matrix[i][j] = "X"  # replace last direction with X
    return matrix


def part_one():
    with open("input.txt", "r") as file:
        matrix = [list(line.rstrip("\n")) for line in file]
        return sum(row.count("X") for row in map_matrix(matrix))


def part_two():
    with open("input.txt", "r") as file:
        matrix = [list(line.rstrip("\n")) for line in file]

        mapped_matrix = map_matrix(deepcopy(matrix))

        count_cycle_matrices = 0
        count_nocycle_matrices = 0
        x, y = get_position_guard(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if mapped_matrix[i][j] == "X" and [i, j] != [x, y]:
                    matrix_with_obstacle = deepcopy(matrix)
                    matrix_with_obstacle[i][j] = "O"
                    if not map_matrix(matrix_with_obstacle):
                        count_cycle_matrices += 1
                        print(count_cycle_matrices)
                    else:
                        count_nocycle_matrices += 1

        print(f"no cycle matrices: {count_nocycle_matrices}")
        print(f"sum: {count_cycle_matrices+count_nocycle_matrices}")
        return count_cycle_matrices


if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
