import re

# List of fields to clean
fields_to_clean = ['evolution_chain', 'pokemon_stats', 'title']

for field in fields_to_clean:
    raw_value = str(document.get_meta_data_value(field))
    if raw_value:
        # Regex to strip all HTML tags
        clean_value = re.sub('<[^<]+?>', '', raw_value)
        document.add_meta_data({field: clean_value})
