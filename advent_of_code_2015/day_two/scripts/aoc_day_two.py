class SurfaceCalculator:
    def __init__(self, length, width, height):
        self.length = eval(length)
        self.width = eval(width)
        self.height = eval(height)
    def calculate_box_surface_area(self):
        smallest_side = min((self.length * self.width), (self.width * self.height), (self.height * self.length))
        surface_area = (2 * (self.length * self.width)) + (2 * (self.width * self.height)) + (2 * (self.height * self.length)) + smallest_side
        return surface_area
    def calculate_ribbon_length(self):
        shortest_distance = min((2 * (self.length + self.width)), (2 * (self.height + self.length)), (2 * (self.height + self.width)))
        ribbon_feet = shortest_distance + (self.length * self.width * self.height)
        return ribbon_feet

with open("advent_of_code_2015/day_two/data/aoc_day_two.txt", "r") as aoc_day_two_file:
    aoc_day_two_data = aoc_day_two_file.readlines()

aoc_day_two_data = [dimensions.split("x") for dimensions in aoc_day_two_data]

box_surface_areas = []

for _, dimensions in enumerate(aoc_day_two_data):
    box_area = SurfaceCalculator(dimensions[0], dimensions[1], dimensions[2])
    surface_area = box_area.calculate_box_surface_area()
    box_surface_areas.append(surface_area)

print(f"The total surface area of wrapping paper required is {sum(box_surface_areas)}")  # Part One Answer

ribbon_feet_list = []

for _, dimensions in enumerate(aoc_day_two_data):
    ribbon_area = SurfaceCalculator(dimensions[0], dimensions[1], dimensions[2])
    surface_area = ribbon_area.calculate_ribbon_length()
    ribbon_feet_list.append(surface_area)

print(f"The total feet of ribbon required is {sum(ribbon_feet_list)}")  # Part Two Answer

