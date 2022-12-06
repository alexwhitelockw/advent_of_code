
with open("advent_of_code_2022/day_six/data/aoc_day_six.txt", "r") as aoc_day_six_file:
    aoc_day_six_data = aoc_day_six_file.read()

for index, _ in enumerate(aoc_day_six_data):
    if len(aoc_day_six_data[index:index+4]) == len(set(aoc_day_six_data[index:index+4])):
        print(index+4)  # Part One Answer
        break

for index, _ in enumerate(aoc_day_six_data):
    if len(aoc_day_six_data[index:index+14]) == len(set(aoc_day_six_data[index:index+14])):
        print(index+14)  # Part Two Answer
        break