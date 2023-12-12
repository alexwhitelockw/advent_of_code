from collections import Counter
import numpy as np

with open("advent_of_code_2016/day_six/data_input.txt") as data_input:
    message_received = [
        [value for value in line.strip()]
        for line in data_input
    ]

message_received_array = np.array(message_received)

_, number_columns = message_received_array.shape

common_character_list = []

for column_index in range(number_columns):
    column_characters = message_received_array[:,column_index]
    for common_character in Counter(column_characters).most_common(1):
        character, _ = common_character
        common_character_list.append(character)

"".join(common_character_list)

least_common_character_list = []

for column_index in range(number_columns):
    column_characters = message_received_array[:,column_index]
    for least_common_character in Counter(column_characters).most_common()[:-1-1:-1]:
        character, _ = least_common_character
        least_common_character_list.append(character)

"".join(least_common_character_list)