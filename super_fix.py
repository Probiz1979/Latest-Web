import json
import glob
from bs4 import BeautifulSoup

# Step 1: Extract real mapping from all HTML files
t_map = {}
html_files = glob.glob('*.html')
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        for el in soup.find_all(attrs={"data-i18n": True}):
            tid = el['data-i18n']
            if tid not in t_map:
                # get all text, normalize spaces
                text = ' '.join(list(el.stripped_strings))
                if text:
                    t_map[tid] = text

# Add the hero_desc text manually since it's an exception
t_map['hero_desc'] = "We engineered Probiz because exceptional business growth is driven by flawless execution. From closing high-value sales to expertly managing complex back-office administration, we act as a seamless extension of your enterprise. We do not just handle your outsourced operations; we relentlessly optimize them to elevate your brand reputation and accelerate your commercial success globally."

# Step 2: Extract translations.js dictionary
with open('translations.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

json_text = js_text.split('const translations = ')[1]
if json_text.endswith(';\n'): json_text = json_text[:-2]
if json_text.endswith(';'): json_text = json_text[:-1]

data = json.loads(json_text)

# Step 3: Create language dictionary but map t_X
# Reverse map english text to t_X
reverse_t_map = { v: k for k, v in t_map.items() }

i18n_dict = {}
for lang, tr in data.items():
    i18n_dict[lang] = {}
    for eng_key, ts_val in tr.items():
        clean_eng = ' '.join(eng_key.split()).strip()
        # Find matching t_X
        # Note, some eng keys might perfectly match exactly
        if clean_eng in reverse_t_map:
            t_id = reverse_t_map[clean_eng]
            i18n_dict[lang][t_id] = ts_val
        else:
            # Fallback fuzzy matching just in case
            for html_tid, html_en in t_map.items():
                if clean_eng in html_en or html_en in clean_eng:
                    if html_tid not in i18n_dict[lang] or len(clean_eng) > 10:
                        i18n_dict[lang][html_tid] = ts_val

# Step 4: Write it back exactly to translations.js
with open('translations.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(i18n_dict, ensure_ascii=False, indent=2) + ';\n')

print("Translations successfully re-mapped to t_X keys!")
