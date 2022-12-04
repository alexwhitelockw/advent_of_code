import string

ascii_characters = ''.join([
    string.ascii_lowercase, 
    string.ascii_uppercase])

ascii_character_map = dict([
    (character, value + 1)
    for value, character in enumerate(ascii_characters)])

with open("advent_of_code_2022/day_three/data/aoc_day_three.txt", "r") as aoc_day_three_file:
    aoc_day_three_data = aoc_day_three_file.readlines()

def extract_common_character(character_list):
    list_length = int(len(character_list) / 2)
    list_first_part = set(character_list[:list_length])
    list_second_part = set(character_list[list_length:])
    common_character = list_first_part.intersection(list_second_part)
    return common_character

common_characters = [
    extract_common_character(character_list) 
    for character_list in aoc_day_three_data]

sum([  # Part One Answer
    ascii_character_map.get(character) 
    for item in common_characters 
    for character in item])


character_list_groups = [
    aoc_day_three_data[i:i+3] 
    for i in range(0, len(aoc_day_three_data), 3)]

def find_group_commonality(character_list):
    set_one, set_two, set_three = character_list
    set_one = set(set_one.replace('\n', ''))
    set_two = set(set_two.replace('\n', ''))
    set_three = set(set_three.replace('\n', ''))
    common_character = set_one.intersection(set_two, set_three)
    return common_character

group_common_characters = [
    find_group_commonality(group) 
    for group in character_list_groups]

sum([  # Part Two Answer
    ascii_character_map.get(character) 
    for item in group_common_characters 
    for character in item])