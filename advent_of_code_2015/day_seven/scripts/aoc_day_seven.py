from collections import defaultdict
from enum import StrEnum
import numpy as np

with open("advent_of_code_2015/day_seven/data/aoc_day_seven.txt", "r") as aoc_day_seven_file:
    aoc_day_seven_data = aoc_day_seven_file.readlines()

class GateType(StrEnum):
    AND = "AND"
    LSHIFT = "LSHIFT"
    NOT = "NOT"
    OR = "OR"
    RSHIFT = "RSHIFT"
    
class LogicGate:
    def __init__(self):
        self.value_dictionary = {}

    def logic_gate_type(self, instruction):
        if (GateType.AND in instruction) or (GateType.OR in instruction):
            self.and_or_gate(instruction)
        elif (GateType.RSHIFT in instruction) or (GateType.LSHIFT in instruction):
            self.shift_gate(instruction)
        elif GateType.NOT in instruction:
            self.not_gate(instruction)
        else:
            self.pass_signal(instruction)

    def pass_signal(self, instruction):
        from_value, _, to_value = instruction.split(" ")
        try:
            if from_value.isnumeric():
                self.value_dictionary[to_value.strip()] = np.array([int(from_value)], dtype="uint16")[0]
            else:
                self.value_dictionary[to_value.strip()] = self.value_dictionary[from_value]
        except KeyError:
            return None
    
    def and_or_gate(self, instruction):
        from_value_a, _, from_value_b, _, to_value = instruction.split(" ")
        try:
            if (from_value_a.strip().isnumeric()):
                from_value_a = int(from_value_a.strip())
                from_value_b = self.value_dictionary[from_value_b.strip()]
            else:
                from_value_a = self.value_dictionary[from_value_a.strip()]
                from_value_b = self.value_dictionary[from_value_b.strip()]
            if GateType.AND in instruction:
                to_value_number = from_value_a & from_value_b
            else:
                to_value_number = from_value_a | from_value_b
            self.value_dictionary[to_value.strip()] = np.array([to_value_number], dtype="uint16")[0]
        except KeyError:
            return KeyError
    
    def shift_gate(self, instruction):
        from_value, _, shift_value, _, to_value = instruction.split(" ")
        try:
            from_value = self.value_dictionary[from_value.strip()]
            if GateType.RSHIFT in instruction:
                to_value_number = from_value >> int(shift_value)
            else:
                to_value_number = from_value << int(shift_value)
            self.value_dictionary[to_value.strip()] = np.array([to_value_number], dtype="uint16")[0]
        except KeyError:
            return None

    def not_gate(self, instruction):
        _, from_value, _, to_value = instruction.split(" ")
        try:
            from_value = self.value_dictionary[from_value.strip()]
            to_value_number = ~int(from_value)
            self.value_dictionary[to_value.strip()] = np.array([to_value_number], dtype="uint16")[0]
        except KeyError:

            return None

logic_gate = LogicGate()

while True:
    for _, instruction in enumerate(sorted(aoc_day_seven_data)):
        logic_gate.logic_gate_type(instruction)
    if logic_gate.value_dictionary.get("a") is not None:
        break

logic_gate.value_dictionary.get("a")  # Part One Answer

logic_gate_parttwo = LogicGate()

while True:
    for _, instruction in enumerate(sorted(aoc_day_seven_data)):
        _, assignment = instruction.split("->")
        if assignment.strip() == "b":
            instruction = f"{logic_gate.value_dictionary.get('a')} -> b"
        logic_gate_parttwo.logic_gate_type(instruction)
    if logic_gate_parttwo.value_dictionary.get("a") is not None:
        break

logic_gate_parttwo.value_dictionary.get("a")  # Part Two Answer
