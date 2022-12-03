
with open("advent_of_code_2022/day_two/data/aoc_day_two.txt", "r") as aoc_day_two_file:
    aoc_day_two_data = aoc_day_two_file.readlines()
    aoc_day_two_data = [result.split() for result in aoc_day_two_data]

def calculate_game_score(game_results) -> int:
    match game_results:
        case ["A", "X"]:
            return 4
        case ["A", "Y"]:
            return 8
        case ["A", "Z"]:
            return 3
        case ["B", "X"]:
            return 1
        case ["B", "Y"]:
            return 5
        case ["B", "Z"]:
            return 9
        case ["C", "X"]:
            return 7
        case ["C", "Y"]:
            return 2
        case ["C", "Z"]:
            return 6

sum([calculate_game_score(game) for game in aoc_day_two_data])  # Part One Answer