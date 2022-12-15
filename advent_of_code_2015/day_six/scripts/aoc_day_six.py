from enum import StrEnum
import numpy as np 
import re 

with open("advent_of_code_2015/day_six/data/aoc_day_six.txt", "r") as aoc_day_six_file:
    aoc_day_six_data = aoc_day_six_file.readlines()

class LightInstruction(StrEnum):
    ON = "turn on"
    OFF = "turn off"
    TOGGLE = "toggle"

def extract_light_positions(instruction):
    light_positions = re.findall("[0-9]+", instruction)
    light_positions = [int(position) for position in light_positions]
    return light_positions

def toggle_light(light):
    return np.where(light == 0, 1, 0)

def light_instruction(instruction, light_matrix):
    row_start, column_start, row_end, column_end = extract_light_positions(instruction)
    if LightInstruction.ON in instruction:
        light_matrix[row_start:row_end+1, column_start:column_end+1] = 1
    elif LightInstruction.OFF in instruction:
        light_matrix[row_start:row_end+1, column_start:column_end+1] = 0
    elif LightInstruction.TOGGLE in instruction:
        light_matrix[row_start:row_end+1, column_start:column_end+1] = np.apply_along_axis(
            toggle_light,
            1,
            light_matrix[row_start:row_end+1, column_start:column_end+1]
        )

def light_brightness_instruction(instruction, light_matrix):
    row_start, column_start, row_end, column_end = extract_light_positions(instruction)
    if LightInstruction.ON in instruction:
        light_matrix[row_start:row_end+1, column_start:column_end+1] += 1
    elif LightInstruction.OFF in instruction:
        with np.nditer(light_matrix[row_start:row_end+1, column_start:column_end+1], op_flags=['readwrite']) as light_values:
            for light_value in light_values:
                if light_value != 0:
                    light_value[...] -= 1
    elif LightInstruction.TOGGLE in instruction:
        light_matrix[row_start:row_end+1, column_start:column_end+1] += 2



initial_matrix = np.zeros((1000,1000))

for i in aoc_day_six_data:
    print(np.sum(initial_matrix))
    light_instruction(i, initial_matrix)

np.sum(initial_matrix)  # Part One Answer

initial_matrix_parttwo = np.zeros((1000,1000))

for i in aoc_day_six_data:
    light_brightness_instruction(i, initial_matrix_parttwo)

np.sum(initial_matrix_parttwo)  # Part Two Answer