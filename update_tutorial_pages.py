#!/usr/bin/env python3
"""Update all tutorial pages (depth-2 index.html files):
- Add h2 'Your Digital Marketing Instructor' before instructor-strip
"""
import os, re

BASE = '/home/user/xyzlab'

PILLAR_DIRS = [
    'bing-webmaster-tools', 'chatgpt', 'claude', 'data-studio',
    'go-high-level', 'godaddy', 'google-ads', 'google-ads-editor',
    'google-analytics', 'google-search-console', 'google-tag-manager',
    'linkedin', 'linkedin-ads', 'meta-ads', 'microsoft-ads',
    'pinterest-ads', 'reddit-ads', 'shopify', 'tiktok-ads', 'wix'
]

heading = '<h2 class="instructor-section-title">Your Digital Marketing Instructor</h2>\n      '

updated = []
total = 0

for pillar in PILLAR_DIRS:
    pillar_path = os.path.join(BASE, pillar)
    if not os.path.isdir(pillar_path):
        continue
    for sub in os.listdir(pillar_path):
        sub_path = os.path.join(pillar_path, sub)
        if not os.path.isdir(sub_path):
            continue
        page = os.path.join(sub_path, 'index.html')
        if not os.path.exists(page):
            continue
        total += 1
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html

        # Add instructor heading before instructor-strip
        if 'instructor-section-title' not in html and '<div class="instructor-strip">' in html:
            html = html.replace(
                '<div class="instructor-strip">',
                heading + '<div class="instructor-strip">'
            )

        if html != original:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(html)
            updated.append(f'{pillar}/{sub}')

print(f'Updated {len(updated)}/{total} tutorial pages.')
