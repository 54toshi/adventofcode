# disk map - puzzle input
# each second number represents free disk space or file blocks
# checksum - add up the result of multiplying each of these blocks' position with the file ID number it contain
# If a block contains free space, skip it

from copy import deepcopy


def checksum(disk: list) -> int:
    checksum = 0
    for position, block_id in enumerate(disk):
        if block_id != ".":
            checksum += position * int(block_id)
            # print(f"{position}*{block_id}")  # print status
    return checksum


def get_disk_map() -> list:
    with open("input.txt", "r") as file:
        disk_layout = list()
        block_index = 0
        for i, num in enumerate(str(file.readline().strip())):
            if i % 2 == 0:  # file block
                for _ in range(int(num)):
                    disk_layout.append(block_index)
            else:  # free space
                for _ in range(int(num)):
                    disk_layout.append(".")
                block_index += 1
        return disk_layout


def part_one() -> int:
    disk_layout = get_disk_map()

    dot_count = disk_layout.count(".") - 1
    new_disk_layout = deepcopy(disk_layout)
    disk_layout.reverse()
    for k, num_reverse in enumerate(disk_layout):
        # print(f"{k}/{dot_count}") # print status

        new_disk_layout[new_disk_layout.index(".")] = num_reverse
        new_disk_layout[len(new_disk_layout) - k - 1] = "."
        if k >= dot_count:
            break

    return checksum(new_disk_layout)


def part_two() -> int:
    disk_layout = get_disk_map()

    new_disk_layout = deepcopy(disk_layout)
    disk_layout.reverse()
    filesize = 1
    for k, num_reverse in enumerate(disk_layout):
        # print(f"{k}/{len(disk_layout)}")  # print status

        try:
            if disk_layout[k + 1] == num_reverse and num_reverse != ".":
                filesize += 1
                continue
            elif disk_layout[k] != ".":
                file = disk_layout[k - filesize + 1 : k + 1]

                for m in range(len(new_disk_layout) - k):
                    if all(
                        item == "." for item in new_disk_layout[m : m + filesize]
                    ):  # find first empty space large enough to fit file

                        # pop file and replace with empty space if copied
                        for item_i, item in enumerate(new_disk_layout):
                            if item == num_reverse:
                                new_disk_layout[item_i] = "."
                        new_disk_layout[m : m + filesize] = file
                        break

                filesize = 1
        except IndexError:
            break

    return checksum(new_disk_layout)


if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
