import re

with open("advent_of_code_2023/day_one/data_input.txt") as data_input:
    calibration_values = data_input.readlines()
    calibration_values = [
        value.strip()
        for value in calibration_values
    ]

def extract_calibration_values(calibration_value_sequence):
                               
    calibration_digits = re.findall("(\d)", calibration_value_sequence)
    first_digit = calibration_digits[0]
    last_digit = calibration_digits[-1]
    two_digit_number = int(f"{first_digit}{last_digit}")
    
    return two_digit_number



def replace_letters_with_digits(calibration_value_sequence):

    character_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    calibration_digits = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", calibration_value_sequence)
    first_digit = calibration_digits[0]
    last_digit = calibration_digits[-1]

    if first_digit in character_mapping.keys():
        first_digit = character_mapping.get(first_digit)

    if last_digit in character_mapping.keys():
        last_digit = character_mapping.get(last_digit) 

    two_digit_number = int(f"{first_digit}{last_digit}")

    return two_digit_number



# Part One Answer

sum((  
    extract_calibration_values(value) 
    for value in calibration_values
))

# Part Two Answer

sum((
    replace_letters_with_digits(value)
    for value in calibration_values
))
