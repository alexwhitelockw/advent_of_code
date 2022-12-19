import itertools

if __name__ == "__main__":

    with open("advent_of_code_2015/day_seventeen/data/aoc_day_seventeen.txt", "r") as aoc_day_seventeen_file:
        aoc_day_seventeen_data = aoc_day_seventeen_file.readlines()
        aoc_day_seventeen_data = [int(size.strip()) for size in aoc_day_seventeen_data]

    adds_to_150 = 0

    for i in range(1, len(aoc_day_seventeen_data)):
        container_combinations = list(itertools.combinations(aoc_day_seventeen_data, r=i))
        for combination in container_combinations:
            if sum(combination) == 150:
                adds_to_150 += 1
    
    adds_to_150  # Part One Answer

    container_fills = {}

    for i in range(1, len(aoc_day_seventeen_data)):
        container_combinations = list(itertools.combinations(aoc_day_seventeen_data, r=i))
        adds_to_150 = 0
        for combination in container_combinations:
            if sum(combination) == 150:
                adds_to_150 += 1
        container_fills[i] = adds_to_150
    
    container_fills  # Part Two Answer