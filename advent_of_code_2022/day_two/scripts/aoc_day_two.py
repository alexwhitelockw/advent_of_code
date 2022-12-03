from advent_of_code_2022.day_two.scripts.game_score_calculation import calculate_game_score_partone
from advent_of_code_2022.day_two.scripts.game_score_calculation import calculate_game_score_parttwo

with open("advent_of_code_2022/day_two/data/aoc_day_two.txt", "r") as aoc_day_two_file:
    aoc_day_two_data = aoc_day_two_file.readlines()
    aoc_day_two_data = [result.split() for result in aoc_day_two_data]

sum([calculate_game_score_partone(game) for game in aoc_day_two_data])  # Part One Answer

sum([calculate_game_score_parttwo(game) for game in aoc_day_two_data])  # Part Two Answer
