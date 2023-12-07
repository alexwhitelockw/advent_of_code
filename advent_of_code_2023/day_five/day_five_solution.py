
mapping_dictionary = {}

with open("advent_of_code_2023/day_five/data_input.txt") as data_input:
    for line in data_input:
        line = line.strip()
        
        if "seeds:" in line:
            line = line.replace("seeds: ", "")
            line = [int(seed_value) for seed_value in line.split(" ")]
            seed_information = line
            continue

        if "map:" in line:
            map_name = line.replace(":", "")
            map_dictionary = {
                map_name: []
            }
            continue

        if line != "":
            map_details = [int(map_value) for map_value in line.split(" ")]
            map_dictionary[map_name].append(map_details)
        
        if line == "":
            continue

        mapping_dictionary.update(map_dictionary)

# Part One Answer

def find_location_mapping(mapping_dictionary, seed_information):

    location_mappings = []
    mapping_dictionary_keys = [key for key in mapping_dictionary.keys()]
    
    for seed in seed_information:
        mapping_dictionary_keys_copy = mapping_dictionary_keys.copy()

        while mapping_dictionary_keys_copy:
            mapping_key = mapping_dictionary_keys_copy.pop(0)
            source_to_destination = mapping_dictionary.get(mapping_key)

            for source_mapping in source_to_destination:
                destination_mapping_start, source_mapping_start, mapping_length = source_mapping
                        
                if source_mapping_start <= seed < source_mapping_start + mapping_length:
                    distance_from_source_start = seed - source_mapping_start
                    seed = destination_mapping_start + distance_from_source_start
                    break
        
        location_mappings.append(seed)

    return location_mappings


location_maps = find_location_mapping(
    mapping_dictionary=mapping_dictionary,
    seed_information=seed_information)

min(location_maps)

# Part Two Answer

def seed_information_range(seed_information):
    while seed_information:
        seed_start_range = seed_information.pop(0)
        seed_range_length = seed_information.pop(0)
        for seed_placement in range(seed_start_range, seed_start_range + seed_range_length):
            location_map = find_location_mapping(
                mapping_dictionary=mapping_dictionary,
                seed_information=[seed_placement])

            yield location_map


seed_range_location_maps = seed_information_range(
    seed_information=seed_information)

min(seed_range_location_maps)
