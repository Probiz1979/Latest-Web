import os
import re

base_dir = "/Users/muhammadumerali/Desktop/probiz_website/medical-billing"

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

contact_regex = re.compile(
    r'<div class="footer-col">\s*<h4[^>]*>Contact</h4>.*?</ul>\s*</div>',
    re.DOTALL | re.IGNORECASE
)

new_contact_block = """<div class="footer-col">
  <h4>Contact</h4>
  <ul>
    <li><a href="mailto:info@probizsms.com"><i class="fa-solid fa-envelope" style="width:20px;margin-right:8px"></i>info@probizsms.com</a></li>
    <li><a href="tel:044181222"><i class="fa-solid fa-phone" style="width:20px;margin-right:8px"></i>044181222</a></li>
    <li><a href="https://wa.me/971544433410" target="_blank"><i class="fa-brands fa-whatsapp" style="width:20px;margin-right:8px"></i>+971 54 443 3410</a></li>
    <li><a href="../contact.html"><i class="fa-solid fa-location-dot" style="width:20px;margin-right:8px"></i>Office 1904, Al Zarooni Building 3, Al Mamzar, Dubai, UAE</a></li>
  </ul>
</div>"""

updated_count = 0

for filename in sorted(html_files):
    # Skip campaign.html as it is a landing page with a custom structure and doesn't use the standard footer
    if filename == "campaign.html":
        continue
        
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = contact_regex.search(content)
    if match:
        print(f"File {filename}: Found contact block to replace.")
        new_content = contact_regex.sub(new_contact_block, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
    else:
        print(f"File {filename}: WARNING - Contact block NOT found!")

print(f"\nSuccessfully updated {updated_count} files.")
