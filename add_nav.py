import glob
import re

files = glob.glob('*.html')

header_insert = '\n<li><a class="nav-link" href="medical-billing/index.html">Medical Billing</a></li>'
footer_insert = '\n<li><a href="medical-billing/index.html">Medical Billing</a></li>'

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Find where to insert in header
    # Let's insert after Partnerships
    content = re.sub(r'(<li><a class="nav-link(?: active)?" data-i18n="t_5" href="partnerships.html">Our Partnerships</a></li>)', r'\1' + header_insert, content)
    
    # Find where to insert in footer
    content = re.sub(r'(<li><a data-i18n="t_5" href="partnerships.html">Our Partnerships</a></li>)', r'\1' + footer_insert, content)

    with open(file, 'w') as f:
        f.write(content)

print("Updated nav in all HTML files.")
