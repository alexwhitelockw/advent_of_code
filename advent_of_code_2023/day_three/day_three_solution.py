import numpy as np
import re

with open("advent_of_code_2023/day_three/data_input.txt") as data_input:
    engine_data = data_input.readlines()
    engine_data = [
        [symbol for symbol in value.strip()]
        for value in engine_data
    ]

engine_data_array = np.array(engine_data)

def get_neighbor_value(array, i, j):
    # Function to get the value at indices (i, j) if they are within bounds
    if 0 <= i < array.shape[0] and 0 <= j < array.shape[1]:
        return array[i, j]
    else:
        # Return a sentinel value or handle out-of-bounds as needed
        return "." 

# Part One Answer

part_number_locations = []

for index, value in np.ndenumerate(engine_data_array):
    index_i_value, index_j_value = index

    value_back = get_neighbor_value(engine_data_array, index_i_value, index_j_value - 1)
    value_ahead = get_neighbor_value(engine_data_array, index_i_value, index_j_value + 1)
    value_up = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value)
    value_down = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value)
    value_upper_left = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value - 1)
    value_upper_right = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value + 1)
    value_lower_left = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value - 1)
    value_lower_right = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value + 1)

    neighbourhood_values = (
        value_back, value_ahead, value_up, value_down, 
        value_upper_left, value_upper_right, value_lower_left, value_lower_right)

    for neighbourhood_value in neighbourhood_values:
        if not re.match(r"[\d\\.]", neighbourhood_value) and re.match(r"[\d]", value):
            part_number_locations.append(index)

number_coordinates = set()

while part_number_locations:
    for index_values in part_number_locations:
        index_i_value, index_j_value = index_values

        number_coordinates.add(index_values)
        part_number_locations.remove(index_values)

        value_back = get_neighbor_value(engine_data_array, index_i_value, index_j_value - 1)
        value_back_coordinates = (index_i_value, index_j_value - 1)

        value_ahead = get_neighbor_value(engine_data_array, index_i_value, index_j_value + 1)
        value_ahead_coordinates = (index_i_value, index_j_value + 1)


        if re.match(r"[\d]", value_back) and value_back_coordinates not in number_coordinates:
            part_number_locations.append(value_back_coordinates)
        if re.match(r"[\d]", value_ahead) and value_ahead_coordinates not in number_coordinates:
            part_number_locations.append(value_ahead_coordinates)

sorted_number_coordinates = [
    coordinates
    for coordinates in sorted(number_coordinates)]

part_number_list = []

values_remaining = True

while values_remaining:
    
    current_coordinate = sorted_number_coordinates.pop(0)
    index_i_value, index_j_value = current_coordinate

    part_number = f"{engine_data_array[index_i_value, index_j_value]}"

    for next_coordinate in sorted_number_coordinates:
        next_index_i_value, next_index_j_value = next_coordinate

        if int(next_index_j_value) - int(index_j_value) == 1 and next_index_i_value == index_i_value:
            part_number += f"{engine_data_array[next_index_i_value, next_index_j_value]}"
            index_i_value, index_j_value = next_coordinate
        else:
            part_number_list.append(int(part_number))
            part_number = f"{engine_data_array[next_index_i_value, next_index_j_value]}"
            index_i_value, index_j_value = next_coordinate
        
    part_number_list.append(int(part_number))
    values_remaining = False

sum(part_number_list)

# Part Two Answer

gear_part_locations = []

for index, value in np.ndenumerate(engine_data_array):
    index_i_value, index_j_value = index

    value_back = get_neighbor_value(engine_data_array, index_i_value, index_j_value - 1)
    value_ahead = get_neighbor_value(engine_data_array, index_i_value, index_j_value + 1)
    value_up = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value)
    value_down = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value)
    value_upper_left = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value - 1)
    value_upper_right = get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value + 1)
    value_lower_left = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value - 1)
    value_lower_right = get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value + 1)

    neighbourhood_values = (
        value_back, value_ahead, value_up, value_down, 
        value_upper_left, value_upper_right, value_lower_left, value_lower_right)

    for neighbourhood_value in neighbourhood_values:
        if re.match(r"[\d]", neighbourhood_value) and re.match(r"[\*]", value) and index not in gear_part_locations:
            gear_part_locations.append(index)

gear_ratio_values = []

for gear_location in gear_part_locations:
    index_i_value, index_j_value = gear_location

    gear_number_locations = []

    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value, index_j_value - 1)):
        gear_number_locations.append((index_i_value, index_j_value - 1))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value, index_j_value + 1)):
        gear_number_locations.append((index_i_value, index_j_value + 1))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value)):
        gear_number_locations.append((index_i_value - 1, index_j_value))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value)):
        gear_number_locations.append((index_i_value + 1, index_j_value))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value - 1)):
        gear_number_locations.append((index_i_value - 1, index_j_value - 1))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value - 1, index_j_value + 1)):
        gear_number_locations.append((index_i_value - 1, index_j_value + 1))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value - 1)):
        gear_number_locations.append((index_i_value + 1, index_j_value - 1))
    if re.match(r"[\d]", get_neighbor_value(engine_data_array, index_i_value + 1, index_j_value + 1)):
        gear_number_locations.append((index_i_value + 1, index_j_value + 1))
    
    number_coordinates = set()

    while gear_number_locations:
        for index_values in gear_number_locations:
            index_i_value, index_j_value = index_values

            number_coordinates.add(index_values)
            gear_number_locations.remove(index_values)

            value_back = get_neighbor_value(engine_data_array, index_i_value, index_j_value - 1)
            value_back_coordinates = (index_i_value, index_j_value - 1)

            value_ahead = get_neighbor_value(engine_data_array, index_i_value, index_j_value + 1)
            value_ahead_coordinates = (index_i_value, index_j_value + 1)

            if re.match(r"[\d]", value_back) and value_back_coordinates not in number_coordinates:
                gear_number_locations.append(value_back_coordinates)
            if re.match(r"[\d]", value_ahead) and value_ahead_coordinates not in number_coordinates:
                gear_number_locations.append(value_ahead_coordinates)
    
    sorted_number_coordinates = [
        coordinates
        for coordinates in sorted(number_coordinates)]

    part_number_list = []

    values_remaining = True

    while values_remaining:
        
        current_coordinate = sorted_number_coordinates.pop(0)
        index_i_value, index_j_value = current_coordinate

        part_number = f"{engine_data_array[index_i_value, index_j_value]}"

        for next_coordinate in sorted_number_coordinates:
            next_index_i_value, next_index_j_value = next_coordinate

            if int(next_index_j_value) - int(index_j_value) == 1 and next_index_i_value == index_i_value:
                part_number += f"{engine_data_array[next_index_i_value, next_index_j_value]}"
                index_i_value, index_j_value = next_coordinate
            else:
                part_number_list.append(int(part_number))
                part_number = f"{engine_data_array[next_index_i_value, next_index_j_value]}"
                index_i_value, index_j_value = next_coordinate
            
        part_number_list.append(int(part_number))
        values_remaining = False

    if len(part_number_list) == 2:
        gear_ratio_values.append(part_number_list[0] * part_number_list[1])

sum(gear_ratio_values)
    
