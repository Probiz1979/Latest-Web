import json
with open('en_strings.json', 'r', encoding='utf-8') as f:
    en_map = json.load(f)

# we need to extract from translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    txt = f.read()

prefix = 'const translations = '
suffix = ';\n'
if txt.startswith(prefix):
    json_txt = txt[len(prefix):]
    if json_txt.endswith(suffix):
        json_txt = json_txt[:-len(suffix)]
    elif json_txt.endswith(';'):
        json_txt = json_txt[:-1]
    
data = json.loads(json_txt)

reverse_en = { ' '.join(v.split()).strip() : k for k, v in en_map.items() }

new_data = {}
for lang, tr in data.items():
    new_data[lang] = {}
    for eng_k, val in tr.items():
        c_eng = ' '.join(eng_k.split()).strip()
        if c_eng in reverse_en:
            t_key = reverse_en[c_eng]
            new_data[lang][t_key] = val
        else:
            # specifically handle hero
            if "We engineered Probiz" in c_eng:
                new_data[lang]["hero_desc"] = val
            else:
                new_data[lang][c_eng] = val
                
with open('translations_i18n.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(new_data, ensure_ascii=False, indent=4) + ';\n')
print("Wrote translations_i18n.js!")
