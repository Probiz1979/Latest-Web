import json
from bs4 import BeautifulSoup

# Open index.html
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

with open('translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

json_str = js_content.split('const translations = ')[1].split(';')[0].strip()
translations = json.loads(json_str)
ar_dict = translations['ar']

matched = 0
total = 0

for tag in soup.find_all(attrs={"data-i18n": True}):
    text = list(tag.stripped_strings)
    if not text: continue
    for t in text:
        key = ' '.join(t.split())
        total += 1
        if key in ar_dict:
            matched += 1

print(f"Matched {matched} out of {total} text nodes.")
