from copy import deepcopy
from itertools import combinations
import math
import numpy as np

with open("advent_of_code_2023/day_eleven/data_input.txt") as data_input:
    galaxy_matrix = [
        [value for value in line.strip()]
        for line in data_input.readlines()
    ]
    galaxy_matrix = np.array(galaxy_matrix)


def identify_empty_columns(galaxy_matrix):
    empty_column_indices = []
    for index in range(len(galaxy_matrix)):
        if np.unique(galaxy_matrix[:,index]).size == 1:
            empty_column_indices.append(index)
    
    return empty_column_indices

def identify_empty_rows(galaxy_matrix):
    empty_row_indices = []
    for index in range(len(galaxy_matrix)):
        if np.unique(galaxy_matrix[index]).size == 1:
            empty_row_indices.append(index)
    
    return empty_row_indices

def insert_new_rows(galaxy_matrix, row_indices):
    increment = 0

    for row_index in row_indices:
        galaxy_matrix = np.insert(galaxy_matrix, row_index + increment, 0, axis=0)
        increment += 1
    
    return galaxy_matrix

def insert_new_columns(galaxy_matrix, column_indices):
    increment = 0

    for column_index in column_indices:
        galaxy_matrix = np.insert(galaxy_matrix, column_index + increment, 0, axis=1)
        increment += 1
    
    return galaxy_matrix

def calculate_number_of_pairs(galaxy_number):
    return galaxy_number*(galaxy_number-1)/math.factorial(2)

def calculate_manhattan_distance(galaxy_pair):

    galaxy_pair_one, galaxy_pair_two = galaxy_pair

    galaxy_pair_one_x, galaxy_pair_one_y = galaxy_pair_one
    galaxy_pair_two_x, galaxy_pair_two_y = galaxy_pair_two

    manhattan_distance = abs(galaxy_pair_one_x - galaxy_pair_two_x) + abs(galaxy_pair_one_y - galaxy_pair_two_y)
    
    return manhattan_distance

# Identify empty rows and columns -- used across parts 1 and 2

empty_columns = identify_empty_columns(galaxy_matrix)
empty_rows = identify_empty_rows(galaxy_matrix)

# Copy galaxy matrix for part 2

part_two_galaxy_matrix = deepcopy(galaxy_matrix)

# Part 1 Answer

galaxy_matrix = insert_new_rows(galaxy_matrix, empty_rows)
galaxy_matrix = insert_new_columns(galaxy_matrix, empty_columns)

galaxy_matrix.shape

# Identify Galaxy Locations

galaxy_number = 1
galaxy_locations = []

it = np.nditer(galaxy_matrix, flags=["multi_index"])
for value in it:
    if value == "#":
        galaxy_number += 1
        galaxy_locations.append(it.multi_index)

galaxy_pairs = combinations(galaxy_locations, 2)

sum((calculate_manhattan_distance(galaxy_pair) for galaxy_pair in galaxy_pairs))

# Identify Galaxy Locations

galaxy_number = 1
galaxy_locations_part_two = []

it = np.nditer(part_two_galaxy_matrix, flags=["multi_index"])
for value in it:
    if value == "#":
        galaxy_number += 1
        galaxy_locations_part_two.append(it.multi_index)

expanded_galaxy_locations = []

for galaxy_location in galaxy_locations_part_two:
    x_location, y_location = galaxy_location
    new_x_location = x_location  # Don't want the logic comparing to the new updated value
    new_y_location = y_location  # just the original value
    for row in empty_rows:
        if x_location > row:
            new_x_location += 999999
    for column in empty_columns:
        if y_location > column:
            new_y_location += 999999
    
    expanded_galaxy_locations.append((new_x_location, new_y_location))

expanded_galaxy_pairs = combinations(expanded_galaxy_locations, 2)

sum((calculate_manhattan_distance(galaxy_pair) for galaxy_pair in expanded_galaxy_pairs))
