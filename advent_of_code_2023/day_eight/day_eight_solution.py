import math
import re

with open("advent_of_code_2023/day_eight/data_input.txt") as data_input:
    direction_instructions = data_input.readline().strip()
    element_list = data_input.readlines()

    element_lookup = {}

    for element in element_list:
        element = element.strip()
        elements_extracted = re.findall(r"[A-Z]{3}", element)

        if len(elements_extracted) != 0:
            element_key, *element_direction = elements_extracted

            element_lookup.update({
                element_key: element_direction
            })

def parse_direction(current_element_selected, direction_instruction, element_lookup_map):
    new_element_location = element_lookup_map.get(current_element_selected)

    if direction_instruction == "L":
        next_element_selected = new_element_location[0]
    elif direction_instruction == "R":
        next_element_selected = new_element_location[1]
    
    return next_element_selected

def monitor_direction_index(current_direction_index, direction_instruction_list):
    if 0 <= current_direction_index < len(direction_instruction_list):
        return current_direction_index
    else:
        current_direction_index = 0
        return current_direction_index

# Part One Answer

current_element = "AAA"
last_element = "ZZZ"
number_of_steps = 0
direction_index = 0

while current_element != last_element:

    direction_index = monitor_direction_index(direction_index, direction_instructions)
    direction_selected = direction_instructions[direction_index]

    current_element = parse_direction(current_element, direction_selected, element_lookup)

    number_of_steps += 1
    direction_index += 1


print(f"The number of steps taken was {number_of_steps}.")

# Part Two Answer

current_elements = [key for key in element_lookup.keys() if re.search(r"([A-Z]{2}A)", key)]

loop_lengths = []

for starting_element in current_elements:
    all_end_with_z = False
    number_of_steps = 1
    direction_index = 0

    current_element = starting_element

    while all_end_with_z == False:

        direction_index = monitor_direction_index(direction_index, direction_instructions)
        direction_selected = direction_instructions[direction_index]

        current_element = parse_direction(current_element, direction_selected, element_lookup)

        if current_element.endswith("Z"):
            loop_lengths.append(number_of_steps)
            all_end_with_z = True

        number_of_steps += 1
        direction_index += 1

   

print(f"The number of steps taken was {math.lcm(*loop_lengths)}.")

