import numpy as np
from scipy.spatial import distance

with open("advent_of_code_2022/day_nine/data/aoc_day_nine.txt", "r") as aoc_day_nine_file:
    aoc_day_nine_data = aoc_day_nine_file.readlines()
    aoc_day_nine_data = [direction.split(' ') for direction in aoc_day_nine_data]

class HeadPosition:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.head_history = set()
    def move_head_position(self, direction):
        match direction:
            case "U":
                self.y_coord += 1
            case "D":
                self.y_coord -= 1
            case "R":
                self.x_coord += 1                    
            case "L":
                self.x_coord -= 1
    def update_history(self):
        self.head_history.add((self.x_coord, self.y_coord))

class TailPosition:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.tail_history = set()
    def correct_tail_position(self, direction, knot_position_x, knot_position_y):
        dist = distance.chebyshev((knot_position_x, knot_position_y), (self.x_coord, self.y_coord))
        match direction:
            case "U" if dist >= 2:
                self.y_coord = knot_position_y - 1
                self.x_coord = knot_position_x
            case "D" if dist >= 2:
                self.y_coord = knot_position_y + 1
                self.x_coord = knot_position_x
            case "R" if dist >= 2:
                self.x_coord = knot_position_x - 1
                self.y_coord = knot_position_y
            case "L" if dist >= 2:
                self.x_coord = knot_position_x + 1
                self.y_coord = knot_position_y
    def update_history(self):
        self.tail_history.add((self.x_coord, self.y_coord))


head = HeadPosition()
tail = TailPosition()

for direction, steps in aoc_day_nine_data:
    steps = eval(steps)
    while steps:
        head.move_head_position(direction)
        head.update_history()
        print(f"Head: {(head.x_coord, head.y_coord)}")
        tail.correct_tail_position(direction=direction, knot_position_x=head.x_coord, knot_position_y=head.y_coord)
        tail.update_history()
        print(f"Tail: {(tail.x_coord, tail.y_coord)}")
        steps -= 1

len(tail.tail_history)    

head = HeadPosition()
tails = [TailPosition() for _ in range(9)]

for direction, steps in aoc_day_nine_data:
    steps = eval(steps)
    while steps:
        head.move_head_position(direction)
        head.update_history()
        print(f"Head: {(head.x_coord, head.y_coord)}")
        tails[0].correct_tail_position(direction=direction, knot_position_x=head.x_coord, knot_position_y=head.y_coord)
        tails[0].update_history()
        print(f"Tail: {(tails[0].x_coord, tails[0].y_coord)}")
        for i in range(1, 9):
            tails[i].correct_tail_position(direction=direction, knot_position_x=tails[i-1].x_coord, knot_position_y=tails[i-1].y_coord)
            tails[i].update_history()
        steps -= 1


len(tails[1].tail_history)
