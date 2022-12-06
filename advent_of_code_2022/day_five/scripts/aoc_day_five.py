import pandas as pd
import re

with open("advent_of_code_2022/day_five/data/aoc_day_five.txt", "r") as aoc_day_five_file:
    aoc_day_five_data = aoc_day_five_file.readlines()
    aoc_day_five_data = [
        re.findall('[0-9]+', instruction)
        for instruction in aoc_day_five_data]

initial_crate_positions = pd.read_fwf(
    "advent_of_code_2022/day_five/data/aoc_day_five_crates.txt", 
    header=None)
initial_crate_positions.drop(8, inplace=True)

def crate_mover(model=["9000", "9001"], initial_crate_positions=None, instruction_list=None):
    crate_positions = [values.dropna().to_list()[::-1] for _, values in initial_crate_positions.items()]
    for instruction in instruction_list:
        instruction = [eval(item) for item in instruction]
        quantity, index_from, index_to = instruction
        if model == "9000":
            crates_to_move = reversed(crate_positions[index_from-1][-quantity:])
        else:
            crates_to_move = crate_positions[index_from-1][-quantity:]
        crate_positions[index_to-1].extend(crates_to_move)
        del crate_positions[index_from-1][-quantity:]
    return crate_positions

part_one_answer = crate_mover( 
    model="9000", 
    initial_crate_positions=initial_crate_positions, 
    instruction_list=aoc_day_five_data)

[crate_position[-1] for crate_position in part_one_answer]  # Part One Answer

part_two_answer = crate_mover(
    model="9001", 
    initial_crate_positions=initial_crate_positions, 
    instruction_list=aoc_day_five_data)

[crate_position[-1] for crate_position in part_two_answer]  # Part Two Answer
