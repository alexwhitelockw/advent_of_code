import hashlib
import re

eight_character_password = []
index = 0

while len(eight_character_password) != 8:
    door_id = "".join(["reyedfim", str(index)])
    door_id_hash = hashlib.md5(door_id.encode()).hexdigest()

    if re.match(r"(^[0]{5})", door_id_hash):
        eight_character_password.append(door_id_hash[5])
    
    index += 1

print("".join(eight_character_password))

new_password = []
index = 0

while len(new_password) != 8:
    door_id = "".join(["reyedfim", str(index)])
    door_id_hash = hashlib.md5(door_id.encode()).hexdigest()

    if re.match(r"(^[0]{5})", door_id_hash):
        try:
            position = int(door_id_hash[5])
            if 0 <= position < 8 and position not in [char[0] for char in new_password]:
                new_password.append((position, door_id_hash[6]))
        except ValueError:
            pass

    index += 1


sorted_password = sorted(new_password, key=lambda x: x[0])

print("".join(char[1] for char in sorted_password))
