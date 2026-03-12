import re

# Get the sentence from the scraper
raw_sentence = document.get_meta_data_value("raw_generation_string")

if raw_sentence:
    text = raw_sentence[0]
    # Find 'Generation' followed by the number
    match = re.search(r"Generation\s+(\d+)", text)
    
    if match:
        gen_num = match.group(1)
        clean_value = f"Gen {gen_num}"
        
        # Add it to the field you created
        document.add_meta_data({"pokemongeneration": clean_value})
    else:
        # Fallback if the regex fails but we have text
        document.add_meta_data({"pokemongeneration": "Unknown Gen"})
