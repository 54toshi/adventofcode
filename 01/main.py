def part_one():
    nums1 = []
    nums2 = []
    with open("input.txt", "r") as file:
        for line in file:
            nums1.append(line.strip().split("   ")[0])
            nums2.append(line.strip().split("   ")[1])
        nums1.sort()
        nums2.sort()
        ranges = []
        for index, value in enumerate(nums1):
            ranges.append(abs(int(value) - int(nums2[index])))
        return sum(ranges)


def part_two():
    nums1 = []
    nums2 = []
    with open("input.txt", "r") as file:
        for line in file:
            nums1.append(line.strip().split("   ")[0])
            nums2.append(line.strip().split("   ")[1])
        nums1.sort()
        nums2.sort()
        similarity_score = 0
        for value in nums1:
            count = nums2.count(value)
            similarity_score += int(value) * count
        return similarity_score


print("part_one: ", part_one())
print("part_two: ", part_two())
