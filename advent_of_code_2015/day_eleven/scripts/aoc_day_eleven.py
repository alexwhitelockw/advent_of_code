import re
import string

character_mapping = {}

for value, char in enumerate(string.ascii_lowercase):
    character_mapping[char] = value

class PassWordManager:
    def __init__(self, charater_map):
        self.current_password = "cqjxjnds"
        self.character_map = charater_map
        self.integer_password = None
    def map_character_to_int(self):
        password_characters = re.split("", self.current_password)
        self.integer_password = [character_mapping[char] 
        for char in password_characters 
        if char != ""]
    def increment_end_value(self):
        if self.integer_password[-1] != 25:
            self.integer_password[-1] += 1
        else:
            self.integer_password[-1] = 0
    def check_integer_values(self):
        if self.integer_password[-1] == 0:
            self.integer_password

password_manager = PassWordManager(character_mapping)
password_manager.map_character_to_int()

password_manager.increment_password(-1)
password_manager.integer_password
