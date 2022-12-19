from enum import StrEnum
import re

if __name__ == "__main__":
    
    class CharacteristicVariable(StrEnum):
        CHILDREN = "children"
        CATS = "cats"
        SAMOYEDS = "samoyeds"
        POMERANIANS = "pomeranians"
        AKITAS = "akitas"
        VIZSLAS = "vizslas"
        GOLDFISH = "goldfish"
        TREES = "trees"
        CARS = "cars"
        PERFUMES = "perfumes"

    class SueType:
        def __init__(self):
            self.sue_number = None
            self.children_count = None 
            self.cat_count = None
            self.samoyeds_count = None
            self.pomeranians_count = None
            self.akitas_count = None
            self.vizslas_count = None
            self.goldfish_count = None 
            self.tree_count = None
            self.car_count = None
            self.perfume_count = None
        def extract_sue_number(self, sue_data):
            sue_id = re.match("Sue [0-9]+", sue_data.strip()).group()
            sue_id = re.sub("Sue ", "", sue_id)
            self.sue_number = int(sue_id)
        def extract_variable_count(self, sue_data):
            item_list = re.sub("^Sue [0-9]+: ", "", sue_data)
            item_list = re.split(",", item_list)
            for item in item_list:
                if CharacteristicVariable.CHILDREN in item:
                    self.children_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.CATS in item:
                    self.cat_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.SAMOYEDS in item:
                    self.samoyeds_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.POMERANIANS in item:
                    self.pomeranians_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.AKITAS in item:
                    self.akitas_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.VIZSLAS in item:
                    self.vizslas_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.GOLDFISH in item:
                    self.goldfish_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.TREES in item:
                    self.tree_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.CARS in item:
                    self.car_count = int(re.search("[0-9]+", item.strip()).group())
                elif CharacteristicVariable.PERFUMES in item:
                    self.perfume_count = int(re.search("[0-9]+", item.strip()).group())

    with open("advent_of_code_2015/day_sixteen/data/aoc_day_sixteen.txt", "r") as aoc_day_sixteen_file:
        aoc_day_sixteen_data = aoc_day_sixteen_file.readlines()
        sue_list = []
        for sue_data in aoc_day_sixteen_data:
            sue_instance = SueType()
            sue_instance.extract_sue_number(sue_data)
            sue_instance.extract_variable_count(sue_data)
            sue_list.append(sue_instance)
    
    child_criteria = {sue.sue_number for sue in sue_list if sue.children_count is None or sue.children_count == 3}
    cat_criteria = {sue.sue_number for sue in sue_list if sue.cat_count is None or sue.cat_count == 7}
    samoyed_criteria = {sue.sue_number for sue in sue_list if sue.samoyeds_count is None or sue.samoyeds_count == 2}
    pomeranian_criteria = {sue.sue_number for sue in sue_list if sue.pomeranians_count is None or sue.pomeranians_count == 3}
    akita_criteria = {sue.sue_number for sue in sue_list if sue.akitas_count is None or sue.akitas_count == 0}
    vizslas_criteria = {sue.sue_number for sue in sue_list if sue.vizslas_count is None or sue.vizslas_count == 0}
    goldfish_criteria = {sue.sue_number for sue in sue_list if sue.goldfish_count is None or sue.goldfish_count == 5}
    tree_criteria = {sue.sue_number for sue in sue_list if sue.tree_count is None or sue.tree_count == 3}
    car_criteria = {sue.sue_number for sue in sue_list if sue.car_count is None or sue.car_count == 2}
    perfume_criteria = {sue.sue_number for sue in sue_list if sue.perfume_count is None or sue.perfume_count == 1}

    child_criteria.intersection(cat_criteria,  # Part One Answer
        samoyed_criteria, 
        pomeranian_criteria, 
        akita_criteria, 
        vizslas_criteria,
        goldfish_criteria,
        tree_criteria,
        car_criteria,
        perfume_criteria)

    child_criteria = {sue.sue_number for sue in sue_list if sue.children_count is None or sue.children_count == 3}
    cat_criteria = {sue.sue_number for sue in sue_list if sue.cat_count is None or sue.cat_count > 7}
    samoyed_criteria = {sue.sue_number for sue in sue_list if sue.samoyeds_count is None or sue.samoyeds_count == 2}
    pomeranian_criteria = {sue.sue_number for sue in sue_list if sue.pomeranians_count is None or sue.pomeranians_count < 3}
    akita_criteria = {sue.sue_number for sue in sue_list if sue.akitas_count is None or sue.akitas_count == 0}
    vizslas_criteria = {sue.sue_number for sue in sue_list if sue.vizslas_count is None or sue.vizslas_count == 0}
    goldfish_criteria = {sue.sue_number for sue in sue_list if sue.goldfish_count is None or sue.goldfish_count < 5}
    tree_criteria = {sue.sue_number for sue in sue_list if sue.tree_count is None or sue.tree_count > 3}
    car_criteria = {sue.sue_number for sue in sue_list if sue.car_count is None or sue.car_count == 2}
    perfume_criteria = {sue.sue_number for sue in sue_list if sue.perfume_count is None or sue.perfume_count == 1}

    child_criteria.intersection(cat_criteria,  # Part Two Answer
        samoyed_criteria, 
        pomeranian_criteria, 
        akita_criteria, 
        vizslas_criteria,
        goldfish_criteria,
        tree_criteria,
        car_criteria,
        perfume_criteria)