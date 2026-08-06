#!/usr/bin/env python3
"""Update footer across all HTML pages:
- Change footer brand text
- Add YouTube button to footer-socials
"""
import os

OLD_TEXT = 'Hands-on AI marketing training. Work smarter, grow faster with AI.'
NEW_TEXT = "Hands-on, practical digital marketing training. We help companies and digital marketing professionals solve real problems and move the needle where it matters the most!"

OLD_SOCIALS = '''        <div class="footer-socials">
          <a href="https://www.linkedin.com/in/seridis/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          </a>
        </div>'''

NEW_SOCIALS = '''        <div class="footer-socials">
          <a href="https://www.linkedin.com/in/seridis/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          </a>
          <a href="https://www.youtube.com/@xyzl" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </a>
        </div>'''

BASE = '/home/user/xyzlab'
updated = 0
total = 0

for root, dirs, files in os.walk(BASE):
    # Skip hidden dirs and __pycache__
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    for fn in files:
        if not fn.endswith('.html'):
            continue
        path = os.path.join(root, fn)
        total += 1
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html
        html = html.replace(OLD_TEXT, NEW_TEXT)
        html = html.replace(OLD_SOCIALS, NEW_SOCIALS)
        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            updated += 1

print(f'Updated {updated}/{total} files.')
