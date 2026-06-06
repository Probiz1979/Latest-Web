import os

base_dir = "/Users/muhammadumerali/Desktop/probiz_website/medical-billing"

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

updated_files = 0
total_replacements = 0

for filename in sorted(html_files):
    if filename == "campaign.html":
        continue
        
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="contact.html" with href="../contact.html#contact-form"
    # Replace href='contact.html' with href='../contact.html#contact-form'
    original_content = content
    
    content = content.replace('href="contact.html"', 'href="../contact.html#contact-form"')
    content = content.replace("href='contact.html'", "href='../contact.html#contact-form'")
    
    if content != original_content:
        # Count how many replacements occurred
        count1 = original_content.count('href="contact.html"')
        count2 = original_content.count("href='contact.html'")
        count = count1 + count2
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"File {filename}: Replaced {count} instances of contact.html link.")
        updated_files += 1
        total_replacements += count

print(f"\nCompleted! Replaced {total_replacements} contact links across {updated_files} files.")
