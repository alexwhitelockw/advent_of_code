import re 

with open("advent_of_code_2023/day_two/data_input.txt") as data_input:
    game_data = data_input.readlines()
    game_data = [
        value.strip()
        for value in game_data
    ]

# Part One Answer

def compare_sample_number(cube_colour_list, bag_loading):
    count_possible = True
    for cube_sample in cube_colour_list:
        cube_sample = cube_sample.strip()
        count, cube_colour = cube_sample.split(" ")
        if int(count) > bag_loading.get(cube_colour):
            count_possible = False

    return count_possible


part_one_loading = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_game_count = 0

for game_details in game_data:
    
    game_number = re.search(r"(?<=Game )\d+", game_details).group(0)
    game_set_details = re.sub(r"(^\w+\s\d+:\s)", "", game_details)

    cube_count_possible = []

    for set_detail in game_set_details.split(";"):
        cubes_colour_set_detail = set_detail.strip().split(",")
        count_possibility = compare_sample_number(cubes_colour_set_detail, part_one_loading)
        cube_count_possible.append(count_possibility)

    if all(cube_count_possible):
        possible_game_count += int(game_number)

    
print(possible_game_count)

# Part Two Answer

set_power_data = []

for game_details in game_data:
    
    game_set_details = re.sub(r"(^\w+\s\d+:\s)", "", game_details)

    blue_cube_count = []
    red_cube_count = []
    green_cube_count = []

    for set_detail in game_set_details.split(";"):
        cubes_colour_set_detail = set_detail.strip().split(",")
        for cube_colour in cubes_colour_set_detail:
            count, colour = cube_colour.strip().split(" ")
            if colour == "blue":
                blue_cube_count.append(int(count))
            elif colour == "red":
                red_cube_count.append(int(count))
            elif colour == "green":
                green_cube_count.append(int(count))
            else:
                print(f"{colour} is not accounted for")
    
    set_power = max(blue_cube_count) * max(red_cube_count) * max(green_cube_count)

    set_power_data.append(set_power)

print(sum(set_power_data))