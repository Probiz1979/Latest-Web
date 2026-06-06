import json
import re
from bs4 import BeautifulSoup
import glob

# Identify text nodes to translate
html_files = glob.glob('*.html')
translations = {"en": {}}
idx = 1

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Exclude script, style, and comments
    for script in soup(["script", "style"]):
        script.extract()
        
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if parent.name in ['script', 'style', 'head', 'title', 'meta', 'link', 'html', 'body']:
            continue
            
        t = text_node.strip()
        # ignore very short strings like punctuation or empty spaces
        if len(t) > 1 and not re.match(r'^[\W_]+$', t):
            # check if it contains actual words
            if re.search(r'[A-Za-z]', t):
                # Clean up newlines and extra spaces
                t = re.sub(r'\s+', ' ', t).strip()
                # Check if it's already recorded
                if t not in translations["en"].values():
                    translations["en"][f"t_{idx}"] = t
                    parent['data-i18n'] = f"t_{idx}"
                    idx += 1
                else:
                    # Find existing key
                    for k, v in translations["en"].items():
                        if v == t:
                            parent['data-i18n'] = k
                            break

    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

with open('en_strings.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, indent=4, ensure_ascii=False)

print(f"Extracted {idx} strings.")
