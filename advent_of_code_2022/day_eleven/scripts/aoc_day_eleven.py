from enum import Enum
import math

class Monkey(int, Enum):
    MONKEY_ZERO = 0
    MONKEY_ONE = 1
    MONKEY_TWO = 2
    MONKEY_THREE = 3

class MonkeyDetails():
    def __init__(self, monkey_number):
        self.monkey_number = Monkey(monkey_number)
        self.item_list = []
        self.modulus
    def 




        self.inspection_number = 0
    def initial_list(self):
        match self.monkey_number:
            case Monkey.MONKEY_ZERO:
                self.item_list.extend([79, 98])
            case Monkey.MONKEY_ONE:
                self.item_list.extend([54, 65, 75, 74])
            case Monkey.MONKEY_TWO:
                self.item_list.extend([79, 60, 97])
            case Monkey.MONKEY_THREE:
                self.item_list.extend([74])
    def update_inspection_number(self):
        self.inspection_number += 1
    def remove_item_list(self, worry_monkey_number):
        if worry_monkey_number != self.monkey_number:
            self.item_list.pop(0)

class ItemPassing:
    def worry_calculation(self, monkey_number, previous_worry):
        match monkey_number:
            case Monkey.MONKEY_ZERO:
                current_worry = math.floor((previous_worry * 19) / 3)
                if current_worry % 23 == 0:
                    throw_to_monkey = Monkey.MONKEY_TWO
                    return throw_to_monkey
                else:
                    throw_to_monkey = Monkey.MONKEY_THREE
                    return throw_to_monkey
            case Monkey.MONKEY_ONE:
                current_worry = math.floor((previous_worry + 6) / 3)
                if current_worry % 19 == 0:
                    throw_to_monkey = Monkey.MONKEY_TWO
                    return throw_to_monkey
                else:
                    throw_to_monkey = Monkey.MONKEY_ZERO
                    return throw_to_monkey
            case Monkey.MONKEY_TWO:
                current_worry = math.floor((previous_worry**2) / 3)
                if current_worry % 13 == 0:
                    throw_to_monkey = Monkey.MONKEY_ONE
                    return throw_to_monkey
                else:
                    throw_to_monkey = Monkey.MONKEY_THREE
                    return throw_to_monkey
            case Monkey.MONKEY_THREE:
                current_worry = math.floor((previous_worry + 3) / 3)
                if current_worry % 17 == 0:
                    throw_to_monkey = Monkey.MONKEY_ZERO
                    return throw_to_monkey
                else:
                    throw_to_monkey = Monkey.MONKEY_ONE
                    return throw_to_monkey

monkey = [MonkeyDetails(i) for i in range(4)]
[monkey[i].initial_list() for i in range(4)]

item_pass = ItemPassing()

for i in range(4):
    len_items = len(monkey[i].item_list)
    for item in range(len_items):
        returned_monkey = item_pass.worry_calculation(monkey[i].monkey_number, monkey[i].item_list[item])
        print(returned_monkey)
        monkey[i].update_inspection_number()
        monkey[i].remove_item_list(returned_monkey)
        
monkey[1].item_list

t=item_pass.worry_calculation(monkey[0].item_list[0])

item_pass.worry_calculation(monkey[0].monkey_number, monkey[0].item_list[0])








test = ThrowItem()

test.worry_calculation(monkey[0])

worry_calculation(0, 98)