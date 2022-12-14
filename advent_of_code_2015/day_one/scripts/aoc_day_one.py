from enum import StrEnum

class FloorMovement(StrEnum):
    UP = "("
    DOWN = ")"

class SantaMovement:
    def __init__(self):
        self.floor_position = 0
    def move_santa(self, direction):
        match direction:
            case FloorMovement.UP:
                self.floor_position += 1
            case FloorMovement.DOWN:
                self.floor_position -= 1

with open("advent_of_code_2015/day_one/data/aoc_day_one.txt", "r") as aoc_day_one_file:
    aoc_day_one_data = aoc_day_one_file.read()

santa_movement_tracker_partone = SantaMovement()

[santa_movement_tracker_partone.move_santa(direction=direction) for direction in aoc_day_one_data]

print(f"Santa ends up on floor {santa_movement_tracker_partone.floor_position}")  # Part One Answer

santa_movement_tracker_parttwo = SantaMovement()

for index, direction in enumerate(aoc_day_one_data):  # Part Two Answer
    santa_movement_tracker_parttwo.move_santa(direction)
    print(santa_movement_tracker_parttwo.floor_position)
    if santa_movement_tracker_parttwo.floor_position == -1:
        print(f"Santa enters the basement at character position {index+1}")
        break