from enum import StrEnum

class HouseMovement(StrEnum):
    NORTH = "^"
    SOUTH = "v" 
    EAST = ">"
    WEST = "<"

class SantaTracker:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.houses_visited = [(0,0)]
    def santa_movement(self, movement):
        match movement:
            case HouseMovement.NORTH:
                self.y_coord += 1
                self.houses_visited.append((self.x_coord, self.y_coord))
            case HouseMovement.SOUTH:
                self.y_coord -= 1
                self.houses_visited.append((self.x_coord, self.y_coord))
            case HouseMovement.EAST:
                self.x_coord += 1
                self.houses_visited.append((self.x_coord, self.y_coord))
            case HouseMovement.WEST:
                self.x_coord -= 1
                self.houses_visited.append((self.x_coord, self.y_coord))

santa_tracker = SantaTracker()

with open("advent_of_code_2015/day_three/data/aoc_day_three.txt", "r") as aoc_day_three_file:
    aoc_day_three_data = aoc_day_three_file.read()

[santa_tracker.santa_movement(direction) for direction in aoc_day_three_data]

print(f"Santa visited {len(set(santa_tracker.houses_visited))} at least once")  # Part One Answer

original_santa = SantaTracker()
robo_santa = SantaTracker()

[robo_santa.santa_movement(direction) 
    for index, direction in enumerate(aoc_day_three_data) 
    if index%2 == 0]

[original_santa.santa_movement(direction)
    for index, direction in enumerate(aoc_day_three_data)
    if index%2 != 0]  

robo_santa_set = set(robo_santa.houses_visited)
original_santa_set = set(original_santa.houses_visited)

print(f"Robo Santa and Santa visited {len(robo_santa_set.symmetric_difference(original_santa_set)) + len(robo_santa_set.intersection(original_santa_set))} at least once")  # Part Two Answer