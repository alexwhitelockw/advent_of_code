import numpy as np

with open("advent_of_code_2016/day_three/data_input.txt") as data_input:
    triangle_data = [
        [int(value) for value in line.strip().split("  ") if value != ""]
        for line in data_input
    ]

def is_possible_triangle(triangle_measures):
    side_one, side_two, side_three = sorted(triangle_measures)
    sum_two_sides = side_one + side_two
    if sum_two_sides > side_three:
        return True
    else:
        return False


sum((is_possible_triangle(triangle_dimensions) for triangle_dimensions in triangle_data))

triangle_dimension_array = np.array(triangle_data)
number_of_splits = len(triangle_dimension_array) // 3
_, number_columns = triangle_dimension_array.shape

column_triangle_dimensions = []

for index in range(number_columns):
    column_chunks = np.array_split(triangle_dimension_array[:, index], number_of_splits)
    for chunk in column_chunks:
        chunk_dimension_possible = is_possible_triangle(chunk)
        column_triangle_dimensions.append(chunk_dimension_possible)

sum(column_triangle_dimensions)