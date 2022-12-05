import numpy as np
import re

with open("advent_of_code_2022/day_four/data/aoc_day_four.txt", "r") as aoc_day_four_file:
    aoc_day_four_data = aoc_day_four_file.readlines()

def tidy_assignment_range(assignment_range, part_one=True):
    assignment_range = re.split(",|-", assignment_range)
    assignment_range = np.array(assignment_range, dtype="int")
    if part_one:
        return ((assignment_range[0] >= assignment_range[2]) & (assignment_range[1] <= assignment_range[3])) | ((assignment_range[2] >= assignment_range[0]) & (assignment_range[3] <= assignment_range[1]))
    set_one_range = set(
        np.arange(assignment_range[0], assignment_range[1]+1)
    )
    set_two_range = set(
        np.arange(assignment_range[2], assignment_range[3]+1)
    )
    if set_one_range.intersection(set_two_range):
        return True
    else:
        return False

sum([tidy_assignment_range(line, part_one=True) for line in aoc_day_four_data])  # Part One Answer

sum([tidy_assignment_range(line, part_one=False) for line in aoc_day_four_data])  # Part Two Answer

