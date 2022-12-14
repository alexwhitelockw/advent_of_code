from collections import Counter
import re

class NaughtyNiceCheck:
    def __init__(self):
        self.vowel_number = 0
        self.three_vowels = False
        self.repeated_characters = False
        self.disallowed_substring = False 
        self.character_pair_nonrepeat = False
        self.nice_decision = False
    def vowel_count(self, input_character):
        if input_character in ("a", "e", "i", "o", "u"):
            self.vowel_number += 1
    def vowel_check(self):
        if self.vowel_number >= 3:
            self.three_vowels = True    
    def repeated_character_check(self, input_character, comparison_character):
        if input_character == comparison_character:
            self.repeated_characters = True
    def disallowed_substring_check(self, input_character, comparison_character):
        collapsed_string = "".join([input_character, comparison_character])
        if collapsed_string in ("ab", "cd", "pq", "xy"):
            self.disallowed_substring = True
    def non_overlap_repeat_check(self, input_string):
        character_pair = [f"{input_string[i]}{input_string[i+1]}" 
            for i, _ in enumerate(input_string) 
            if i+1 < len(input_string)]
        character_pair_counts = Counter(character_pair)
        character_pair_repeats = [key for key, value in character_pair_counts.items() if value > 1]
        try:
            for characters in character_pair_repeats:
                find_char_pairs = re.finditer(characters, input_string)
                index_set = [set(list(range(char_pairs.start(), char_pairs.end()))) for char_pairs in find_char_pairs]
                if not index_set[0].intersection(index_set[1]):
                    self.character_pair_nonrepeat = True
        except IndexError:
            return None
        #character_pairs = re.findall(pattern=r"[a-z]{2}", string=input_string)
        #character_pair_counts = [(pair, character_pairs.count(pair)) for pair in character_pairs]
        #for pair in character_pair_counts:
        #    _, count = pair
        #    if count > 1:
        #        self.character_pair_nonrepeat = True
    def naughty_or_nice_partone(self):
        if (self.three_vowels == True) and (self.repeated_characters == True) and (self.disallowed_substring == False):
            self.nice_decision = True
    def naught_or_nice_parttwo(self):
        if all([self.repeated_characters, self.character_pair_nonrepeat]):
            self.nice_decision = True


with open("advent_of_code_2015/day_five/data/aoc_day_five.txt", "r") as aoc_day_five_file:
    aoc_day_five_data = aoc_day_five_file.readlines()
    aoc_day_five_data = [character_string.strip("\n") for character_string in aoc_day_five_data]

naughty_nice_check = [NaughtyNiceCheck() for _ in range(len(aoc_day_five_data))]

nice_instances = 0

for i, string in enumerate(aoc_day_five_data):
    [naughty_nice_check[i].vowel_count(character) for character in string]
    naughty_nice_check[i].vowel_check()
    [naughty_nice_check[i].repeated_character_check(string[index], string[index+1]) 
        for index, _ in enumerate(string) 
        if index+1 < len(string)]
    [naughty_nice_check[i].disallowed_substring_check(string[index], string[index+1]) 
        for index, _ in enumerate(string) 
        if index+1 < len(string)]
    naughty_nice_check[i].naughty_or_nice_partone()
    if naughty_nice_check[i].nice_decision:
        nice_instances += 1
    
print(f"There are {nice_instances} instances of nice strings")  # Part One Answer

naughty_nice_check_parttwo = [NaughtyNiceCheck() for _ in range(len(aoc_day_five_data))]

nice_instances_parttwo = 0

for i, string in enumerate(aoc_day_five_data):
    [naughty_nice_check_parttwo[i].repeated_character_check(string[index], string[index+2]) 
            for index, _ in enumerate(string) 
            if index+2 < len(string)]
    naughty_nice_check_parttwo[i].non_overlap_repeat_check(string)
    naughty_nice_check_parttwo[i].naught_or_nice_parttwo()
    if naughty_nice_check_parttwo[i].nice_decision:
        nice_instances_parttwo += 1

print(f"There are {nice_instances_parttwo} instances of nice strings")  # Part Two Answer
