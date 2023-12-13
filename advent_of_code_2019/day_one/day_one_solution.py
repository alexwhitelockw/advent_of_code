with open("advent_of_code_2019/day_one/data_input.txt") as data_input:
    fuel_data = [
        int(fuel.strip())
        for fuel in data_input
    ]

sum(((fuel // 3) - 2 for fuel in fuel_data))

def fuel_calculation(fuel):
    fuel_values = []

    while (fuel // 3) - 2 > 0:
        fuel = (fuel // 3) - 2
        fuel_values.append(fuel)
    
    fuel_values = sum(fuel_values)

    return fuel_values

sum((fuel_calculation(fuel) for fuel in fuel_data))
