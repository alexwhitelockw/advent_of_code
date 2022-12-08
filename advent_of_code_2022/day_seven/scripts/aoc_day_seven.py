from collections import defaultdict
import re

with open("advent_of_code_2022/day_seven/data/aoc_day_seven.txt", "r") as aoc_day_seven_file:
    aoc_day_seven_data = aoc_day_seven_file.read()
    aoc_day_seven_data = aoc_day_seven_data.split("\n")

file_path = []
directory_file_sizes = defaultdict(list)

def track_directory_movement(command: str, file_path: list, directory_file_size: dict) -> dict:
    """
    Track directory movement based on given command input
    :param command: The specific command line command inputted
    :param file_path: Empty list to append the directory location
    :param directory_file_size: Empty dictionary to append file path locations and file sizes
    :return:
    """
    if re.search("^\$ cd \.\.", command):
        file_path.pop()
    elif re.search("^\$ cd [\/a-zA-Z]+", command):
        directory = re.search("[\/a-zA-Z]+$", command).group()
        directory = "".join([directory, "/"])
        file_path.append(directory)
    elif re.search("(^\$ ls)|(^dir)", command):
        next
    else:
        file_size = eval(re.search("^[0-9]+", command).group())
        file_path_copy = file_path.copy()
        while len(file_path_copy) > 1:
            directory_file_path = ''.join(file_path_copy)
            directory_file_size[directory_file_path].append(file_size)
            file_path_copy.pop()
        return directory_file_size

[track_directory_movement(command=command, file_path=file_path, directory_file_size=directory_file_sizes) 
    for command in aoc_day_seven_data]

file_sizes = [value for _, value in directory_file_sizes.items()]

directory_sizes = [sum(file_size) for file_size in file_sizes]

sum([directory_size for directory_size in directory_sizes if directory_size <= 100000])  # Part One Answer

top_level_directories = [
    item 
    for item, _ in directory_file_sizes.items() 
    if len(re.split("/", item)) < 5]

top_level_filesizes = [
    directory_file_sizes.get(dir) 
    for dir in top_level_directories]

space_required = sum([sum(file_sizes) for file_sizes in top_level_filesizes]) + 30000000 - 70000000

min([directory_size for directory_size in directory_sizes if directory_size >= space_required])  # Part One Answer
