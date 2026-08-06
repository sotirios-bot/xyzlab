#!/usr/bin/env python3
"""Replace all XYZLab.gif logo img src with /xyz-lab-logo.png across all HTML files."""
import os, re

BASE = '/home/user/xyzlab'
updated = 0
total = 0

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    for fn in files:
        if not fn.endswith('.html'):
            continue
        path = os.path.join(root, fn)
        total += 1
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html
        # Replace any relative path to XYZLab.gif with absolute /xyz-lab-logo.png
        html = re.sub(
            r'src="(?:\.\./)*XYZLab\.gif"',
            'src="/xyz-lab-logo.png"',
            html
        )
        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            updated += 1

print(f'Updated {updated}/{total} files.')
