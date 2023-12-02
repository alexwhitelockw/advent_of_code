import pandas as pd

if __name__ == "__main__":
    with open("advent_of_code_2015/day_nine/data/aoc_day_nine.txt", "r") as aoc_day_nine_file:
        aoc_day_nine_data = aoc_day_nine_file.readlines()

    travel_distances = []

    for distance in aoc_day_nine_data:
        from_location, _, to_location, _, distance = distance.split()
        travel_distances.append((from_location, to_location, int(distance)))
    
    travel_distance_df = pd.DataFrame(
        travel_distances, 
        columns=["From", "To", "Distance"])
    
    travel_distance_df = travel_distance_df.pivot(
        index="From",
        columns="To",
        values="Distance"
    )

    travel_distance_df.iloc[2]
    travel_distance_df.iloc[0]
    
    sum(axis=1, skipna=True)