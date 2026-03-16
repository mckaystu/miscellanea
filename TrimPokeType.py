# Get the current list of types from the poketype field
#By using the set() function in Python, I don't care how many times the word is found; I only want to store the unique values."
types_list = document.get_meta_data_value("poketype")

if types_list:
    # 1. We use set() to remove all duplicate strings
    # 2. We convert it back to a list
    unique_types = list(set(types_list))
    
    # 3. Update the metadata field with the clean, unique list
    document.add_metadata({"poketype": unique_types})
