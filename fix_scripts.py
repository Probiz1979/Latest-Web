import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # If scripts are missing, add them right before </body>
    if 'script.js' not in content:
        content = content.replace("</body>", "    <script src=\"translations.js\"></script>\n    <script src=\"script.js\"></script>\n</body>")
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
            
print("Scripts restored.")
