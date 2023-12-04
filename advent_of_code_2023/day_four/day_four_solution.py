import re 

with open("advent_of_code_2023/day_four/data_input.txt") as data_input:
    scratch_card_data = data_input.readlines()

def convert_to_array(card_number_list):
    card_numbers = card_number_list.strip()
    card_numbers_split = [
        card_number
        for card_number in card_numbers.split(" ")
        if card_number != ""]
    return card_numbers_split

card_values = []

for scratch_card in scratch_card_data:
    
    scratch_card = scratch_card.strip()
    scratch_card_details = re.split(r"([:|])", scratch_card)
    _, _, winning_numbers, _, user_numbers = scratch_card_details
    
    winning_numbers = convert_to_array(winning_numbers)
    user_numbers = convert_to_array(user_numbers)
    
    user_winning_numbers = [
        user_winning_number 
        for user_winning_number in user_numbers
        if user_winning_number in winning_numbers
    ]

    length_user_winning_numbers = len(user_winning_numbers)

    if length_user_winning_numbers == 1:
        card_value = 1
    else:
        card_value = 0
        for i in range(length_user_winning_numbers):
            if i == 1:
                card_value += 1
            card_value *= 2

    card_values.append(card_value)

print(f"Part One Answer: The total value of the cards is {sum(card_values)}")

scratch_card_originals = []

for scratch_card in scratch_card_data:
    
    scratch_card = scratch_card.strip()
    scratch_card_details = re.split(r"([:|])", scratch_card)
    card_number, _, winning_numbers, _, user_numbers = scratch_card_details

    card_number = int(re.search(r"([0-9]+)", card_number).group(0).strip())
    winning_numbers = convert_to_array(winning_numbers)
    user_numbers = convert_to_array(user_numbers)

    user_winning_numbers = [
        user_winning_number 
        for user_winning_number in user_numbers
        if user_winning_number in winning_numbers
    ]

    length_user_winning_numbers = len(user_winning_numbers)

    scratch_card_original = {
        "card_number": card_number,
        "winning_numbers": length_user_winning_numbers,
        "copy_count": 1
    }

    scratch_card_originals.append(scratch_card_original)

updated_scratch_card_instances = []

max_card_number = max([card.get("card_number") for card in scratch_card_originals])

for scratch_card_instance in scratch_card_originals:
    if scratch_card_instance.get("card_number") == 1:
        updated_scratch_card_instances.append(scratch_card_instance)
        continue
    
    winning_numbers = scratch_card_instance.get("winning_numbers")
    current_card_number = scratch_card_instance.get("card_number")
    copy_count = scratch_card_instance.get("copy_count")
    
    if winning_numbers >0 :
        while copy_count > 0:
                for index in range(1, winning_numbers + 1):
                    next_card_selected = current_card_number + index
                    if next_card_selected <= max_card_number:
                        next_card = next((card for card in scratch_card_originals if card.get("card_number") == next_card_selected), None)
                        if next_card:
                            next_card["copy_count"] += 1
                copy_count -= 1

    updated_scratch_card_instances.append(scratch_card_instance)

print(f"Part Two Answer: {sum([card.get('copy_count') for card in updated_scratch_card_instances])}")
