
with open("advent_of_code_2022/day_ten/data/aoc_day_ten.txt", "r") as aoc_day_ten_file:
    aoc_day_ten_data = aoc_day_ten_file.readlines()
    aoc_day_ten_data = [signal_strength.replace("\n", "").split(" ") for signal_strength in aoc_day_ten_data]

class RowDrawing():
    def __init__(self):
        self.drawing = ""
    def draw_message(self, counter_position, signal_strength):
        if (counter_position >= signal_strength - 1) and (counter_position <= signal_strength + 1):
            self.drawing += "#"
        else:
            self.drawing += "."

class SignalCounter():
    def __init__(self):
        self.counter = 0
        self.signal_strength = 1
        self.signal_records = {0:1}
    def increment_counter_value(self, received_signal_strength):
        match received_signal_strength:
            case ["noop"]:
                self.counter += 1
                self.signal_records.update({self.counter: self.signal_strength})
            case ["addx", received_signal_strength]:
                cycle_length = 2
                received_signal_strength = eval(received_signal_strength)
                while cycle_length:
                    self.counter += 1
                    self.signal_records.update({self.counter: self.signal_strength})
                    cycle_length -= 1
                self.signal_strength += received_signal_strength
                self.signal_records.update({self.counter: self.signal_strength})


signal_counter = SignalCounter()
[signal_counter.increment_counter_value(i) for i in aoc_day_ten_data]

signal_list = []

for key, value in signal_counter.signal_records.items():
    key += 1
    if key in (20, 60, 100, 140, 180, 220):
        signal = key * value
        signal_list.append(signal)

sum(signal_list)  # Part One Answer

drawing_list = []

for key, value in signal_counter.signal_records.items():
    if key % 40 == 0:
        drawing_list.append(row_drawing.drawing)
        row_drawing = RowDrawing()
    row_drawing.draw_message(counter_position=key%40, signal_strength=value)

for i in range(1, len(drawing_list)):  # Part Two Answer
    print(drawing_list[i])