import json

# 1. Load the English mapping (t_X -> "English string")
with open('en_strings.json', 'r', encoding='utf-8') as f:
    en_map = json.load(f)

# Create a reverse map: "English string" -> "t_X"
# We strip and clean spaces to match the keys in translations.js just in case
reverse_en_map = {}
for k, v in en_map.items():
    clean_v = ' '.join(v.split()).strip()
    reverse_en_map[clean_v] = k

# 2. Read the current translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Parse the JSON out of translations.js
json_str = js_content.split('const translations = ')[1].strip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

data = json.loads(json_str)

# 3. Create a new data dictionary where keys are t_X instead of English strings
new_data = {}
for lang, dictionary in data.items():
    new_data[lang] = {}
    for eng_key, translated_val in dictionary.items():
        clean_eng_key = ' '.join(eng_key.split()).strip()
        
        if clean_eng_key in reverse_en_map:
            t_key = reverse_en_map[clean_eng_key]
            new_data[lang][t_key] = translated_val
        else:
            # If we don't have a t_X for it (like the new hero text), we will just keep the English key
            # But wait! I added data-i18n="hero_desc" for the new hero text!
            # So let's map it manually:
            if "We engineered Probiz" in clean_eng_key:
                new_data[lang]["hero_desc"] = translated_val
            else:
                new_data[lang][eng_key] = translated_val

# 4. Save the new translations.js
with open('translations.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(new_data, ensure_ascii=False, indent=4) + ';\n')

print("Translations fixed with t_X keys!")
