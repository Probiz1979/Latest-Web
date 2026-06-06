import os

base_dir = "/Users/muhammadumerali/Desktop/probiz_website/medical-billing"

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

updated_files = 0

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_img = "../assets/rcm_workflow_diagram_1777765088139.png"
    new_img = "../assets/rcm_workflow_diagram.png"
    
    if old_img in content:
        content = content.replace(old_img, new_img)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated image reference in {filename}")
        updated_files += 1

print(f"Completed! Fixed image references in {updated_files} files.")
