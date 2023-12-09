import numpy as np

with open("advent_of_code_2023/day_nine/data_input.txt") as data_input:
    sensor_sequence_raw = data_input.readlines()
    sensor_sequence = [
        [int(value) for value in sequence.strip().split(" ")]
        for sequence in sensor_sequence_raw
        ]
    
sensor_sequence = np.array(sensor_sequence)

# Part One Answer

extrapolated_values = 0

for sequence_array in sensor_sequence:
    array_not_zero = True
    value_differences = sequence_array.copy()
    last_value_array = []

    while array_not_zero:
        last_value_array.append(value_differences[-1])
        value_differences = np.diff(value_differences)
        if len(value_differences) == 0:
            array_not_zero = False

    last_value_array.reverse()
    final_history_values = np.cumsum(last_value_array)

    extrapolated_value = sequence_array[-1] + final_history_values[-2]
    
    extrapolated_values += extrapolated_value

extrapolated_values

# Part Two Answer

extrapolated_values = 0

for sequence_array in sensor_sequence:
    array_not_zero = True
    sequence_array = np.flip(sequence_array)
    value_differences = sequence_array.copy()
    last_value_array = []

    while array_not_zero:
        last_value_array.append(value_differences[-1])
        value_differences = np.diff(value_differences)
        if len(value_differences) == 0:
            array_not_zero = False

    last_value_array.reverse()
    final_history_values = np.cumsum(last_value_array)

    extrapolated_value = sequence_array[-1] + final_history_values[-2]
    
    extrapolated_values += extrapolated_value

extrapolated_values
