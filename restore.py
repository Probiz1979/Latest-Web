import os, glob, shutil

history_paths = [
    os.path.expanduser('~/Library/Application Support/Code/User/History'),
    os.path.expanduser('~/Library/Application Support/Cursor/User/History')
]

target_files = {
    'index.html': 'Home',
    'about.html': 'About Us',
    'services.html': 'Industries & Services',
    'career.html': 'Career',
    'partnerships.html': 'Our Partnerships',
    'contact.html': 'Executive Directives'
}

for hp in history_paths:
    if os.path.exists(hp):
        print("Found history dir:", hp)
        all_files = []
        for root, _, files in os.walk(hp):
            for f in files:
                if f != 'entries.json':
                    try:
                        p = os.path.join(root, f)
                        all_files.append((p, os.path.getmtime(p)))
                    except: pass
        
        all_files.sort(key=lambda x: x[1], reverse=True)
        
        found = {}
        target_dest = '/Users/muhammadumerali/Desktop/probiz_website'
        
        for p, t in all_files:
            try:
                with open(p, 'r') as fp:
                    content = fp.read()
                
                if '<!DOCTYPE html>' in content and 'Probiz' in content:
                    for name, title_keyword in list(target_files.items()):
                        if name not in found and title_keyword in content and len(content) > 1000:
                            found[name] = p
                            with open(os.path.join(target_dest, name), 'w') as out:
                                out.write(content)
                            print(f"Restored {name} from {p}")
                            
            except Exception as e: pass

        print("Restored files:", list(found.keys()))

