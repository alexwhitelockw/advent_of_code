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

max_calorie_count = aoc_data_one_summary.max()  # Part One Answer

print(f"The largest calorie count for an Elf is {int(max_calorie_count.values)}")

aoc_data_one_summary["calorie_rank"] = aoc_data_one_summary.rank(
    method="average",
    ascending=False,
)

top_3_calorie_total = (  # Part Two Answer
    aoc_data_one_summary
        .loc[aoc_data_one_summary["calorie_rank"].isin([1,2,3])]
        .aggregate(total_calories=pd.NamedAgg("sum_calories", "sum"))
)

print(f"The total calories across the top 3 Elves (based on calorie counts) is {int(top_3_calorie_total.values)}")