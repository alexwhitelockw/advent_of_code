import functools
import operator
import re

with open ("advent_of_code_2023/day_six/data_input.txt") as data_input:
    race_data = [line.strip() for line in data_input]

race_duration_numeric = []

for race_information in race_data:
    numeric_details = re.findall(r"([0-9]{2,4})", race_information)
    numeric_details = [int(detail) for detail in numeric_details]
    race_duration_numeric.append(numeric_details)

race_time, race_distance = race_duration_numeric

race_distances_met = []

for i, time in enumerate(race_time):
    boat_speed = 0
    distance_met = 0
    
    while boat_speed <= time:
        distance = race_distance[i]
        time_to_race = time - boat_speed
        distance_travelled = boat_speed * time_to_race

        if distance_travelled >= distance:
            distance_met += 1

        boat_speed += 1
    
    race_distances_met.append(distance_met)

part_one_answer = functools.reduce(operator.mul, race_distances_met, 1)

print(f"The boat can win a total of {part_one_answer} ways across the races.")

actual_race_details = []

for race_information in race_data:
    numeric_details = re.findall(r"([0-9]{2,4})", race_information)
    numeric_details = int("".join(numeric_details))
    actual_race_details.append(numeric_details)

actual_race_time, actual_race_distance = actual_race_details

boat_speed = 0
distance_met = 0

while boat_speed <= actual_race_time:
    time_to_race = actual_race_time - boat_speed
    distance_travelled = boat_speed * time_to_race

    if distance_travelled >= actual_race_distance:
        distance_met += 1

    boat_speed += 1
