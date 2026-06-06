import json
import re

# Load the en_strings.json mapping
with open('en_strings.json', 'r', encoding='utf-8') as f:
    en_map = json.load(f)

# Create a reverse map: "Home" -> "t_1"
reverse_en_map = {v.strip(): k for k, v in en_map.items()}
# Let's clean reverse_en_map spaces just to be sure
# Actually, the keys in en_strings are exact from HTML

# Load translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# We can evaluate translations.js since it's just a JS object assignment
# We'll use regex to parse or just write it out via a quick node script!
# Node is NOT INSTALLED! Bash node: command not found :(
