#!/usr/bin/env python3
"""
Insert programme info block before Cal.com booking widget in coaching sections,
and add 'How it works' nav link before 'Book Training' button on all HTML pages.
"""
import os, re

BASE = '/home/user/xyzlab'

PROGRAMME_HTML = '''      <div class="programme-info">
        <div class="programme-meta">
          <div class="programme-meta-item">
            <span class="pm-icon">&#128197;</span>
            <div>
              <strong>1 Session &times; 2 Hours</strong>
              <span>Deep-dive working session</span>
            </div>
          </div>
          <div class="programme-meta-item">
            <span class="pm-icon">&#128181;</span>
            <div>
              <strong>$150</strong>
              <span>Paid online</span>
            </div>
          </div>
          <div class="programme-meta-item pm-guarantee">
            <span class="pm-icon">&#9989;</span>
            <div>
              <strong>Performance Guarantee</strong>
              <span>No improvement within 2 weeks of applying all changes? Get a free follow-up account review.</span>
            </div>
          </div>
        </div>
        <div class="programme-session">
          <div class="programme-session-header">
            <span class="session-badge">Session 1</span>
            <h3>Performance Marketing Campaigns Audit</h3>
          </div>
          <div class="programme-session-body">
            <div class="programme-agenda">
              <h4>What we cover</h4>
              <ol class="agenda-list">
                <li>
                  <strong>Define what success means for the business</strong>
                  <ul>
                    <li>North Star Metric</li>
                    <li>Business objective: 3, 6 &amp; 12 month roadmap</li>
                    <li>Ideal Customer Profile and communication angle</li>
                  </ul>
                </li>
                <li>
                  <strong>Map &amp; Track your Purchase Funnel</strong>
                  <ul>
                    <li>Funnel communication in each step of the journey</li>
                    <li>Soft KPIs and Key Actions per funnel stage</li>
                    <li>Easy-to-use weekly performance tracker</li>
                  </ul>
                </li>
                <li>
                  <strong>Identify the right channels to use</strong>
                  <ul>
                    <li>Paid vs Organic Media</li>
                    <li>Paid and Organic media tactics</li>
                  </ul>
                </li>
              </ol>
            </div>
            <div class="programme-outcome">
              <h4>Outcome</h4>
              <p>A complete Digital Marketing Plan including:</p>
              <ul class="outcome-list">
                <li>Communication approach across every funnel stage</li>
                <li>Recommended Channels &amp; Tactics</li>
                <li>Campaign restructuring (keep / pause / update / create)</li>
                <li>Creative and ad copy angles document</li>
                <li>Bid Strategy and dimensions optimisation</li>
                <li>Implementation roadmap</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
'''

HOW_IT_WORKS_ITEM = '<li><a href="#coaching">How it works</a></li>\n        '
BOOK_TRAINING_ITEM = '<li><a href="#coaching" class="btn btn-primary btn-sm">Book Training</a></li>'

updated_programme = 0
updated_nav = 0
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

        # 1. Insert programme info before Cal.com booking widget (if not already present)
        if 'programme-info' not in html and '<div id="cal-booking"' in html:
            html = html.replace('<div id="cal-booking"', PROGRAMME_HTML + '      <div id="cal-booking"', 1)
            updated_programme += 1

        # 2. Add 'How it works' nav link before Book Training button (if not already present)
        if 'How it works' not in html and BOOK_TRAINING_ITEM in html:
            html = html.replace(BOOK_TRAINING_ITEM, HOW_IT_WORKS_ITEM + BOOK_TRAINING_ITEM, 1)
            updated_nav += 1

        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)

print(f'Programme block inserted in: {updated_programme} files')
print(f'How it works nav added in: {updated_nav} files')
print(f'Total files scanned: {total}')
