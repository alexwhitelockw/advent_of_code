with open("advent_of_code_2023/day_seven/data_input.txt") as data_input:
    camel_card_hand = [
        card_hand.strip().split(" ") 
        for card_hand in data_input]

five_of_a_kind = []
four_of_a_kind = []
full_house =[]
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

# Part One Answer

for index, card_hand in enumerate(camel_card_hand):
    hand_dealt, bid_made = card_hand

    card_hand_set = {
        (card_value, hand_dealt.count(card_value)) 
        for card_value in hand_dealt}
    
    if len(card_hand_set) == 1:  # Only a single unique card value -- Five of a Kind
        five_of_a_kind.append(index)


    if len(card_hand_set) == 2:
        for cards in card_hand_set:
            _, count = cards
            if count == 4:  # Four of a kind accounted for by this logic
                four_of_a_kind.append(index)
                break
            if count == 3:  # Full house accounted for here -- 2 unique cards, 1 count value is 3
                full_house.append(index)
                break
    
    if len(card_hand_set) == 3:
        for cards in card_hand_set:
            _, count = cards
            if count == 3:  # Three of a kind, 3 unique cards, 1 count value is 3
                three_of_a_kind.append(index)
                break
            if count == 2:  # Two Pairs -- 3 Unique cards, 1 count value is 2
                two_pairs.append(index)
                break

    if len(card_hand_set) == 4:  # One Pair -- 4 Unique cards, 1 count value is 2
        for cards in card_hand_set:
            _, count = cards
            if count == 2:
                one_pair.append(index)
                break

    
    if len(card_hand_set) == 5:  # All distinct values -- 5 unique card values
        high_card.append(index)
        

custom_alphabet = "AKQJT98765432"

# Function to return the sort key for a string
def custom_sort_key(s):
    return [custom_alphabet.index(char) for char in s]

def order_cards_dealt(card_grouping_indices, rank_value, ranked_cards_dealt):
    cards_dealt = []

    for index in card_grouping_indices:
        card_hand, _ = camel_card_hand[index]  # Extract card hands based on the associated index value
        cards_dealt.append(card_hand)

    cards_dealt = sorted(  # Sort cards based on custom alphabet
        cards_dealt, 
        key=custom_sort_key, 
        reverse=True)
    
    for index, cards in enumerate(cards_dealt, rank_value):
        ranked_cards_dealt.append((index, cards))
    
    return ranked_cards_dealt


card_outcomes = [
    high_card,
    one_pair,
    two_pairs,
    three_of_a_kind,
    full_house,
    four_of_a_kind,
    five_of_a_kind
]

rank_value = 1
ranked_cards_dealt = []

for outcome in card_outcomes:
    ordered_cards = order_cards_dealt(outcome, rank_value=rank_value, ranked_cards_dealt=ranked_cards_dealt)
    rank_value, _ = max(ordered_cards)
    rank_value += 1
    ordered_cards

total_winnings = []

for card in ordered_cards:
    rank, card_hand = card
    for camel_card_deal in camel_card_hand:
        if card_hand in camel_card_deal:
            _, card_bid = camel_card_deal
            winning = int(rank) * int(card_bid)
            total_winnings.append(winning)

sum(total_winnings)

# Part Two Answer

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

card_alphabet = "AKQT98765432J"

# Function to return the sort key for a string
def sort_cards(s):
    return [card_alphabet.index(char) for char in s]

for index, card_hand in enumerate(camel_card_hand):
    hand_dealt, bid_made = card_hand

    if "J" in hand_dealt:
        try:
            count_dict = {card: hand_dealt.count(card) for card in hand_dealt if card != 'J'}
            max_count = max(count_dict.values())
            possible_replacements = [card for card, count in count_dict.items() if count == max_count]
            possible_replacements = sorted(  # Sort cards based on custom alphabet
                possible_replacements, 
                key=sort_cards, 
                reverse=True)
            card_to_replace_joker = possible_replacements[0]  # Assumes all cards are numeric -- not the case
            hand_dealt = "".join([card_to_replace_joker if c == 'J' else c for c in hand_dealt])
        except ValueError:
            hand_dealt = hand_dealt

    card_hand_set = {
        (card_value, hand_dealt.count(card_value)) 
        for card_value in hand_dealt}
    
    if len(card_hand_set) == 1:  # Only a single unique card value -- Five of a Kind
        five_of_a_kind.append(index)


    if len(card_hand_set) == 2:
        for cards in card_hand_set:
            _, count = cards
            if count == 4:  # Four of a kind accounted for by this logic
                four_of_a_kind.append(index)
                break
            if count == 3:  # Full house accounted for here -- 2 unique cards, 1 count value is 3
                full_house.append(index)
                break
    
    if len(card_hand_set) == 3:
        for cards in card_hand_set:
            _, count = cards
            if count == 3:  # Three of a kind, 3 unique cards, 1 count value is 3
                three_of_a_kind.append(index)
                break
            if count == 2:  # Two Pairs -- 3 Unique cards, 1 count value is 2
                two_pairs.append(index)
                break

    if len(card_hand_set) == 4:  # One Pair -- 4 Unique cards, 1 count value is 2
        for cards in card_hand_set:
            _, count = cards
            if count == 2:
                one_pair.append(index)
                break

    
    if len(card_hand_set) == 5:  # All distinct values -- 5 unique card values
        high_card.append(index)
        

custom_alphabet_joker = "AKQT98765432J"

# Function to return the sort key for a string
def custom_sort_key_joker(s):
    return [custom_alphabet_joker.index(char) for char in s]

def order_cards_dealt_joker(card_grouping_indices, rank_value, ranked_cards_dealt):
    cards_dealt = []

    for index in card_grouping_indices:
        card_hand, _ = camel_card_hand[index]  # Extract card hands based on the associated index value
        cards_dealt.append(card_hand)

    cards_dealt = sorted(  # Sort cards based on custom alphabet
        cards_dealt, 
        key=custom_sort_key_joker, 
        reverse=True)
    
    for index, cards in enumerate(cards_dealt, rank_value):
        ranked_cards_dealt.append((index, cards))
    
    return ranked_cards_dealt


card_outcomes = [
    high_card,
    one_pair,
    two_pairs,
    three_of_a_kind,
    full_house,
    four_of_a_kind,
    five_of_a_kind
]

rank_value = 1
ranked_cards_dealt = []

for outcome in card_outcomes:
    try:
        ordered_cards = order_cards_dealt_joker(outcome, rank_value=rank_value, ranked_cards_dealt=ranked_cards_dealt)
        rank_value, _ = max(ordered_cards)
        rank_value += 1
    except ValueError:
        print("Problem")

total_winnings_jokers = []

for card in ordered_cards:
    rank, card_hand = card
    for camel_card_deal in camel_card_hand:
        if card_hand in camel_card_deal:
            _, card_bid = camel_card_deal
            winning = int(rank) * int(card_bid)
            total_winnings_jokers.append(winning)

sum(total_winnings_jokers)

