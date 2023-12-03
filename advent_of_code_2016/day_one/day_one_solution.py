import re

with open("advent_of_code_2016/day_one/data_input.txt") as data_input:
    instructions = data_input.readline().split(",")
    instructions = [
        instruction.strip()
        for instruction in instructions
    ]

class userDirection:
    def __init__(self) -> None:
        self.rotation = 0
        self.x_position = 0
        self.y_position = 0
        self.history = []
    def adjust_rotation(self, instruction):
        if re.match(r"[R]", instruction):
            self.rotation += 90
            if abs(self.rotation) == 360:
                self.rotation = 0
        if re.match(r"[L]", instruction):
            self.rotation -= 90
            if abs(self.rotation) == 360:
                self.rotation = 0
    def adjustment_position(self, instruction):
        number_moves = int(re.search(r"([0-9]+)", instruction).group(0))
        for _ in range(number_moves):
            if self.rotation == 0:
                self.y_position += 1
            elif self.rotation == 90 or self.rotation == -270:
                self.x_position += 1
            elif abs(self.rotation) == 180:
                self.y_position -= 1
            elif self.rotation == -90 or self.rotation == 270:
                self.x_position -= 1
            self.history.append((self.x_position, self.y_position))
            

user_direction = userDirection()

for instruction in instructions:
    user_direction.adjust_rotation(instruction)
    user_direction.adjustment_position(instruction)
    print(f"Instruction: {instruction}, Rotation: {user_direction.rotation}, X: {user_direction.x_position}, Y: {user_direction.y_position}")

print(f"The Manhattan Distance is {abs(user_direction.x_position - 0) + abs(user_direction.y_position - 0)}")

for coordinate in user_direction.history:
    if user_direction.history.count(coordinate) == 2:
        x_position, y_position = coordinate
        break

print(f"The Manhattan Distance is {abs(x_position - 0) + abs(y_position - 0)}")
