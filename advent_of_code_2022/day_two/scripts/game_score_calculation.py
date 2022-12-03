def calculate_game_score_partone(game_results) -> int:
    """
    Calculate the Game Score for Advent of Code Day 2 Part 1
    :param game_results: A list containing the output of the  Rock, Paper, Scissors game.
    :return: A score based on provided logic.
    """
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

def calculate_game_score_parttwo(game_results) -> int:
    """
    Calculate the Game Score for Advent of Code Day 2 Part 2
    :param game_results: A list containing the output of the  Rock, Paper, Scissors game.
    :return: A score based on provided logic.
    """
    match game_results:
        case ["A", "X"]:
            return 3
        case ["A", "Y"]:
            return 4
        case ["A", "Z"]:
            return 8
        case ["B", "X"]:
            return 1
        case ["B", "Y"]:
            return 5
        case ["B", "Z"]:
            return 9
        case ["C", "X"]:
            return 2
        case ["C", "Y"]:
            return 6
        case ["C", "Z"]:
            return 7

