import math


def example_composable():
    # process whole file without reading more than 1 line in memory
    with open("nums.txt") as file:
        nums = (row.partition("#")[0] for row in file)
        nums = (row for row in nums if row)
        nums = (float(row) for row in nums)
        nums = (x for x in nums if math.isinfinite(x))
        nums = (max(0.0, x) for x in nums)
        s = sum(nums)
        print(f"the sum is {s}")
