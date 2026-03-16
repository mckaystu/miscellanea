# Get the current value of the poketype metadata
# We use .get() to avoid errors if the field is missing
poketype_raw = document.get_meta_data_value("poketype")

if poketype_raw:
    # 1. Take the first item if it's a list, or just the string
    # 2. Split by commas (if multiple types are merged)
    # 3. Strip whitespace and take the first unique instance
    # Note: Coveo metadata values can be returned as a list or a single string
    
    if isinstance(poketype_raw, list):
        # If it's a list, just take the first unique element
        trimmed_type = poketype_raw[0].strip()
    else:
        # If it's a string like "Fire, Fire", split it and take the first
        trimmed_type = poketype_raw.split(',')[0].strip()

    # CORRECT WAY to set metadata:
    # Use document.add_meta_data({'key': 'value'}) 
    # OR document.set_meta_data_value("key", "value")
    document.add_meta_data({"poketype": trimmed_type})
