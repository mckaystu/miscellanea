# Get the current value from the metadata
# Ensure the key matches source metadata name
raw_species = document.get_meta_data_value("pokemonspecies")

if raw_species:
    # We take the first element if it's a list (common in Coveo)
    species_text = raw_species[0] if isinstance(raw_species, list) else raw_species
    
    # Trim " Pokémon" (case-insensitive or specific)
    # Using .replace() is safer than slicing
    clean_species = species_text.replace(" Pokémon", "").replace(" pokemon", "").strip()
    
    # Update the metadata directly
    # In V2, we just assign the value back to the document
    document.add_meta_data({"pokemonspecies": clean_species})
