import re

if __name__ == "__main__":
    with open("advent_of_code_2015/day_eight/data/aoc_day_eight.txt", "r") as aoc_day_eight_file:
        aoc_day_eight_data = aoc_day_eight_file.readlines()

    string_code = 0
    new_string_len = 0
    string_values = 0

    for string in aoc_day_eight_data:
        string = string.strip()
        string_code += len(string)
        new_string = string
        new_string = new_string.replace("\\", "\\\\")
        new_string = new_string.replace('"', '\\"')
        new_string_len += len(new_string) + 2
        string_escaped = string.encode().decode('unicode-escape')
        string_escaped = re.sub("(^\")|(\"$)", "", string_escaped)
        string_values += len(string_escaped)
    
    print(f"Part One Answer: {string_code - string_values}")  # Part One Answer
    print(f"Part Two Answer: {new_string_len - string_code}")  # Part Two Answer
