import re

# Use get_meta_data_value - Always returns a list
ids = document.get_meta_data_value("pokemon_id")
urls = document.get_meta_data_value("pokemon_image_url")

log("--- SYNC START ---", "Normal")

poke_identifier = ""

# 1. Try to get the ID
if ids and len(ids) > 0 and ids[0] is not None:
    val = str(ids[0])
    if "http" not in val:
        # Clean #001 -> 1
        poke_identifier = val.replace("#", "").strip().lstrip("0")
        log("ID Found: " + poke_identifier, "Normal")

# 2. If ID failed, extract from URL
if not poke_identifier and urls and len(urls) > 0 and urls[0] is not None:
    url_str = str(urls[0])
    # Look for name between 'artwork/' and '.'
    match = re.search(r'artwork/([^./?]+)', url_str)
    if match:
        poke_identifier = match.group(1).lower()
        log("Name Extracted: " + poke_identifier, "Normal")

# 3. Final Construction
if poke_identifier:
    # Build URL using simple concatenation
    github_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/" + poke_identifier + ".png"
    
    # Force write to both fields
    document.add_meta_data({"pokemon_thumbnail": github_url})
    document.add_meta_data({"pokemon_image_url": github_url})
    
    log("SUCCESS: " + github_url, "Normal")
else:
    log("FAILED: No identifier found", "Warning")

log("--- SYNC END ---", "Normal")
