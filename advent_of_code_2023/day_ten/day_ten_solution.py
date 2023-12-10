from enum import StrEnum
import numpy as np
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class Pipes(StrEnum):
    VERTICAL = "|"
    HORIZONTAL = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    GROUND = "."
    ANIMAL = "S"


with open("advent_of_code_2023/day_ten/data_input.txt") as data_input:
    pipe_map = [
        [value for value in line.strip()]
        for line in data_input.readlines()
    ]
    pipe_map = np.array(pipe_map)

# Part One Answer

def find_start_position(pipe_map_matrix):
    starting_position = np.where(pipe_map_matrix == "S")
    return starting_position

def create_empty_map(pipe_map_matrix):
    pipe_map_shape = pipe_map_matrix.shape
    empty_map = np.zeros(pipe_map_shape)
    return empty_map

def update_empty_map(empty_matrix_map, current_position):
    empty_matrix_map[current_position] = 1
    return empty_matrix_map

def check_surrounding_values(current_map_position, pipe_map_matrix):
    axis_zero_position, axis_one_position = current_map_position
    max_row, max_col = pipe_map_matrix.shape

    def is_valid_position(row, col):
        return 0 <= row < max_row and 0 <= col < max_col

    north_value = pipe_map_matrix[axis_zero_position - 1, axis_one_position] if is_valid_position(axis_zero_position - 1, axis_one_position) else None
    east_value = pipe_map_matrix[axis_zero_position, axis_one_position + 1] if is_valid_position(axis_zero_position, axis_one_position + 1) else None
    south_value = pipe_map_matrix[axis_zero_position + 1, axis_one_position] if is_valid_position(axis_zero_position + 1, axis_one_position) else None
    west_value = pipe_map_matrix[axis_zero_position, axis_one_position - 1] if is_valid_position(axis_zero_position, axis_one_position - 1) else None

    surrounding_values = (
        north_value,
        east_value,
        south_value,
        west_value
    )

    return surrounding_values

def select_possible_move(current_map_position, pipe_matrix, coordinate_history):
    
    if isinstance(current_map_position, list):
        current_map_position = current_map_position[0]

    axis_zero_position, axis_one_position = current_map_position
    coordinate_values = []

    def is_valid_move(new_coordinate):
        return new_coordinate not in coordinate_history 

    north_value, east_value, south_value, west_value = check_surrounding_values(current_map_position, pipe_matrix)
    current_value = pipe_matrix[current_map_position]

    if north_value in (Pipes.VERTICAL, Pipes.SOUTH_WEST, Pipes.SOUTH_EAST) and current_value in (Pipes.ANIMAL, Pipes.VERTICAL, Pipes.NORTH_EAST, Pipes.NORTH_WEST):
        north_coordinate = (axis_zero_position - 1, axis_one_position)
        if is_valid_move(north_coordinate):
            coordinate_values.append(north_coordinate)
    
    if east_value in (Pipes.HORIZONTAL, Pipes.NORTH_WEST, Pipes.SOUTH_WEST) and current_value in (Pipes.ANIMAL, Pipes.HORIZONTAL, Pipes.NORTH_EAST, Pipes.SOUTH_EAST):
        east_coordinate = (axis_zero_position, axis_one_position + 1)
        if is_valid_move(east_coordinate):
            coordinate_values.append(east_coordinate)
    
    if south_value in (Pipes.VERTICAL, Pipes.NORTH_WEST, Pipes.NORTH_EAST) and current_value in (Pipes.ANIMAL, Pipes.VERTICAL, Pipes.SOUTH_WEST, Pipes.SOUTH_EAST):
        south_coordinate = (axis_zero_position + 1, axis_one_position)
        if is_valid_move(south_coordinate):
            coordinate_values.append(south_coordinate)
    
    if west_value in (Pipes.HORIZONTAL, Pipes.NORTH_EAST, Pipes.SOUTH_EAST) and current_value in (Pipes.ANIMAL, Pipes.HORIZONTAL, Pipes.NORTH_WEST, Pipes.SOUTH_WEST):
        west_coordinate = (axis_zero_position, axis_one_position - 1)
        if is_valid_move(west_coordinate):
            coordinate_values.append(west_coordinate)

    if len(coordinate_values) > 1:
        return random.choice(coordinate_values)
    elif coordinate_values:
        return coordinate_values[0]
    #return coordinate_values



current_position = find_start_position(pipe_map)
coordinate_record = []
empty_pipe_map = create_empty_map(pipe_map)
previous_position = np.empty((0,0))

while True:
    coordinate_record.append(current_position)
    next_position = select_possible_move(current_position, pipe_map, coordinate_record)
    empty_pipe_map = update_empty_map(empty_pipe_map, current_position)
    current_position = next_position

    if next_position is None:
        break

np.savetxt("test_empty_map.txt", empty_pipe_map, fmt="%d")

print(f"The further point along the loop is {len(coordinate_record)/2} steps")

# Part Two Answer

empty_pipe_map_iteration = np.nditer(empty_pipe_map, flags=["multi_index"])  # Iterate over the pipleine map
# The multi-index allows us to retain the coordinates

loop_polygon = Polygon(coordinate_record)  # Create a polygon based on the visited coordinates

inner_area_tile_count = 0

for index in empty_pipe_map_iteration:  # For each value in the pipeline iteration, check that index isn't
    if empty_pipe_map_iteration.multi_index not in coordinate_record:  # in the coordinate record (not a part of the loop)
        if loop_polygon.contains(Point(empty_pipe_map_iteration.multi_index)):  # Check if the coordinates are in
            inner_area_tile_count += 1  # the polygon shape, if so then update count by 1 -- space within the loop


print(f"The number of tiles within the loop equals {inner_area_tile_count}")