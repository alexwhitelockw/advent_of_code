
with open("advent_of_code_2016/day_two/data_input.txt") as data_input:
    instructions = data_input.readlines()
    instructions = [
        instruction.strip()
        for instruction in instructions
    ]

class KeyPad:
    def __init__(self) -> None:
        self.x_position = 0
        self.y_position = 0
        self.key_pad = None
    def parse_instruction(self, instruction):
        for direction in instruction:
            if direction == "U" and self.y_position != 1:
                self.y_position += 1
            elif direction == "D" and self.y_position != -1:
                self.y_position -= 1
            elif direction == "L" and self.x_position != -1:
                self.x_position -= 1
            elif direction == "R" and self.x_position != 1:
                self.x_position += 1
    def translate_to_keypad(self):
        if self.x_position == -1 and self.y_position == 1:
            self.key_pad = 1
        elif self.x_position == 0 and self.y_position == 1:
            self.key_pad = 2
        elif self.x_position == 1 and self.y_position == 1:
            self.key_pad = 3
        elif self.x_position == -1 and self.y_position == 0:
            self.key_pad = 4
        elif self.x_position == 0 and self.y_position == 0:
            self.key_pad = 5
        elif self.x_position == 1 and self.y_position == 0:
            self.key_pad = 6
        elif self.x_position == -1 and self.y_position == -1:
            self.key_pad = 7
        elif self.x_position == 0 and self.y_position == -1:
            self.key_pad = 8
        elif self.x_position == 1 and self.y_position == -1:
            self.key_pad = 9


key_pad = KeyPad()

key_pad_code = []

for instruction in instructions:
    key_pad.parse_instruction(instruction)
    key_pad.translate_to_keypad()
    key_pad_code.append(key_pad.key_pad)

print(key_pad_code)
