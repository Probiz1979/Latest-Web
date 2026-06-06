#!/usr/bin/env python3
"""
Fix nav order (Medical Billing moves to 3rd position) and 
restore hero image visibility across all pages.
"""

import os, re, glob

ROOT = "/Users/muhammadumerali/Desktop/probiz_website"

# ---------- 1. Fix CSS hero image opacity ----------
css_path = os.path.join(ROOT, "styles.css")
with open(css_path) as f:
    css = f.read()

# Restore image to be visible (0.28 opacity) while keeping text readable overlay
css = css.replace(
    "    opacity: 0.18;\n}\n.subpage-hero::after {\n    content: ''; position: absolute; inset: 0; z-index: 1;\n    background: linear-gradient(160deg, rgba(6,11,30,0.75) 0%, rgba(6,11,30,0.92) 60%, rgba(15,29,74,0.98) 100%);",
    "    opacity: 0.30;\n}\n.subpage-hero::after {\n    content: ''; position: absolute; inset: 0; z-index: 1;\n    background: linear-gradient(160deg, rgba(6,11,30,0.60) 0%, rgba(6,11,30,0.82) 55%, rgba(15,29,74,0.92) 100%);"
)
with open(css_path, "w") as f:
    f.write(css)
print("CSS hero image visibility fixed")

# ---------- 2. Nav order for ROOT pages ----------
# Current order: Home | Industries & Services | Our Partnerships | Medical Billing | Career | About | Contact
# Target order:  Home | Industries & Services | Medical Billing | Our Partnerships | Career | About | Contact

ROOT_OLD_NAV = """<li><a class="nav-link" href="services.html">Industries &amp; Services</a></li>
<li><a class="nav-link" href="partnerships.html">Our Partnerships</a></li>
<li class="nav-item-dropdown">
<a class="nav-link" href="medical-billing/index.html">Medical Billing"""

ROOT_NEW_NAV = """<li><a class="nav-link" href="services.html">Industries &amp; Services</a></li>
<li class="nav-item-dropdown">
<a class="nav-link" href="medical-billing/index.html">Medical Billing"""

# We also need to move partnerships after the MB dropdown closing tag
# Better approach: rewrite the whole nav block for root pages

def reorder_root_nav(html, current_page=""):
    """Reorder nav: Home, Industries, Medical Billing (dropdown), Partnerships, Career, About, Contact"""
    # Pattern to find the nav menu ul content
    old_order_pattern = r'(<li><a class="nav-link[^"]*" href="services\.html"[^<]*>Industries[^<]*</a></li>)\s*(<li><a class="nav-link[^"]*" href="partnerships\.html"[^<]*>Our Partnerships[^<]*</a></li>)\s*(<li class="nav-item-dropdown">.*?</li>)\s*(<li><a class="nav-link[^"]*" href="career\.html"[^<]*>Career[^<]*</a></li>)'
    
    match = re.search(old_order_pattern, html, re.DOTALL)
    if match:
        services_li = match.group(1)
        partnerships_li = match.group(2)
        mb_dropdown_li = match.group(3)
        career_li = match.group(4)
        
        new_order = services_li + "\n" + mb_dropdown_li + "\n" + partnerships_li + "\n" + career_li
        html = html[:match.start()] + new_order + html[match.end():]
        print(f"  Reordered nav in root page")
    else:
        print(f"  WARNING: could not find nav pattern in root page")
    return html

# Root HTML files
root_files = glob.glob(os.path.join(ROOT, "*.html"))
root_files = [f for f in root_files if "test_" not in f]

for fpath in root_files:
    with open(fpath) as f:
        html = f.read()
    fname = os.path.basename(fpath)
    new_html = reorder_root_nav(html, fname)
    if new_html != html:
        with open(fpath, "w") as f:
            f.write(new_html)
        print(f"Updated nav order: {fname}")

# ---------- 3. Nav order for SUBPAGES ----------
# Current: Home | Industries | Partnerships | MB | Career | About | Contact
# Target:  Home | Industries | MB | Partnerships | Career | About | Contact

def reorder_sub_nav(html):
    old_pattern = r'(<li><a class="nav-link[^"]*" href="\.\./services\.html"[^<]*>Industries[^<]*</a></li>)\s*(<li><a class="nav-link[^"]*" href="\.\./partnerships\.html"[^<]*>Our Partnerships[^<]*</a></li>)\s*(<li class="nav-item-dropdown">.*?</li>)\s*(<li><a class="nav-link[^"]*" href="\.\./career\.html"[^<]*>Career[^<]*</a></li>)'
    match = re.search(old_pattern, html, re.DOTALL)
    if match:
        services_li = match.group(1)
        partnerships_li = match.group(2)
        mb_dropdown_li = match.group(3)
        career_li = match.group(4)
        new_order = services_li + "\n" + mb_dropdown_li + "\n" + partnerships_li + "\n" + career_li
        return html[:match.start()] + new_order + html[match.end():]
    return html

sub_files = glob.glob(os.path.join(ROOT, "medical-billing", "*.html"))
for fpath in sub_files:
    with open(fpath) as f:
        html = f.read()
    new_html = reorder_sub_nav(html)
    if new_html != html:
        with open(fpath, "w") as f:
            f.write(new_html)
        print(f"Updated sub nav order: {os.path.basename(fpath)}")
    else:
        print(f"  Sub nav already correct: {os.path.basename(fpath)}")

print("\nAll done!")
