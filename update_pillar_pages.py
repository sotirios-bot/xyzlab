#!/usr/bin/env python3
"""Update all 20 pillar index pages:
- 'Book a Coaching Session' → 'Book Training' in coaching-cta button
- Move coaching-section (form+instructor) to right after playlist-section
- Remove SVG course-icon links from courses-grid, add emojis to titles
- Add h2 'Your Digital Marketing Instructor' before instructor-strip
"""
import os, re

PILLAR_DIRS = [
    'bing-webmaster-tools', 'chatgpt', 'claude', 'data-studio',
    'go-high-level', 'godaddy', 'google-ads', 'google-ads-editor',
    'google-analytics', 'google-search-console', 'google-tag-manager',
    'linkedin', 'linkedin-ads', 'meta-ads', 'microsoft-ads',
    'pinterest-ads', 'reddit-ads', 'shopify', 'tiktok-ads', 'wix'
]

EMOJI_MAP = {
    'Google Ads': '🚀',
    'Google Ads Editor': '✏️',
    'Meta Ads': '📱',
    'TikTok Ads': '🎵',
    'Microsoft Ads': '🪟',
    'Pinterest Ads': '📌',
    'Reddit Ads': '🗣️',
    'LinkedIn Ads': '💼',
    'Google Analytics': '📊',
    'Google Tag Manager': '🏷️',
    'Data Studio': '📈',
    'Claude AI': '🤖',
    'ChatGPT': '💬',
    'Google Search Console': '🔍',
    'Bing Webmaster Tools': '🌐',
    'Shopify': '🛍️',
    'Wix': '🎨',
    'Go High Level': '⚡',
    'GoDaddy': '🌍',
    'LinkedIn': '🔗',
}

def add_emoji_to_h3(card):
    """Add emoji to the h3 link text inside a course card."""
    def replace_h3(m):
        content = m.group(1)
        for platform, emoji in EMOJI_MAP.items():
            if platform in content and emoji not in content:
                content = content.replace(platform, platform + ' ' + emoji)
        return '<h3>' + content + '</h3>'
    return re.sub(r'<h3>(.*?)</h3>', replace_h3, card, flags=re.DOTALL)

def remove_course_icon(card):
    """Remove the <a ... class="course-icon" ...>...</a> block."""
    # Match <a with class="course-icon" anywhere in the tag
    return re.sub(
        r'\s*<a\b[^>]*\bclass="course-icon"[^>]*>.*?</a>',
        '',
        card,
        flags=re.DOTALL
    )

def update_course_cards(html):
    """Update all course cards: remove SVG icon, add emoji to title."""
    def process_card(m):
        card = m.group(0)
        card = remove_course_icon(card)
        card = add_emoji_to_h3(card)
        return card
    return re.sub(
        r'<article class="course-card">.*?</article>',
        process_card,
        html,
        flags=re.DOTALL
    )

def add_instructor_heading(html):
    """Add h2 'Your Digital Marketing Instructor' before instructor-strip."""
    if 'instructor-section-title' in html:
        return html
    heading = '<h2 class="instructor-section-title">Your Digital Marketing Instructor</h2>\n      '
    return html.replace('<div class="instructor-strip">', heading + '<div class="instructor-strip">')

BASE = '/home/user/xyzlab'
updated = []

for pillar in PILLAR_DIRS:
    path = os.path.join(BASE, pillar, 'index.html')
    if not os.path.exists(path):
        print(f'SKIP (not found): {path}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. "Book a Coaching Session" → "Book Training" in coaching-cta button
    html = html.replace('>Book a Coaching Session<', '>Book Training<')

    # 2. Move coaching-section to right after playlist-section
    coaching_match = re.search(
        r'(\s*<!-- COACHING / TALLY -->.*?</section>)',
        html, re.DOTALL
    )
    if coaching_match:
        coaching_block = coaching_match.group(1)
        html_without = html[:coaching_match.start()] + html[coaching_match.end():]
        # Find end of playlist-section
        playlist_end = re.search(
            r'(</section>)(\s*\n\s*(?:<!-- COACHING|<!-- MORE))',
            html_without
        )
        if playlist_end:
            pos = playlist_end.start() + len(playlist_end.group(1))
            html = html_without[:pos] + '\n' + coaching_block + html_without[pos:]

    # 3. Update course cards
    html = update_course_cards(html)

    # 4. Add instructor heading
    html = add_instructor_heading(html)

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        updated.append(pillar)
        print(f'Updated: {pillar}')
    else:
        print(f'No change: {pillar}')

print(f'\nDone. Updated {len(updated)}/{len(PILLAR_DIRS)} pillar pages.')
