import pandas as pd

aoc_data_one_data = pd.read_csv(
    "advent_of_code_2022/day_one/data/aoc_day_one.txt", 
    names=["Calories"], 
    skip_blank_lines=False,)

aoc_data_one_data.loc[:, "elf"] = aoc_data_one_data.loc[:, "Calories"].isna()

aoc_data_one_data.loc[:, "elf"] = aoc_data_one_data.loc[:, "elf"].cumsum()

aoc_data_one_summary = aoc_data_one_data.groupby(["elf"]).aggregate(
    sum_calories=pd.NamedAgg("Calories", "sum")
)

aoc_data_one_summary.max()