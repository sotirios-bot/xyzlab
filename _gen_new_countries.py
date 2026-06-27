#!/usr/bin/env python3
"""
Generate 14 new country pages across 8 benchmark channels.
112 HTML pages + 8 JS data updates + 8 index HTML updates + sitemap.xml update
"""

import os
import re
import json

BASE = '/home/user/xyzlab'

# ─── Country data ────────────────────────────────────────────────────────────
COUNTRIES = [
    {
        'name': 'Colombia', 'slug': 'colombia', 'flag': '🇨🇴',
        'sym': 'COP ', 'sym_display': 'COP', 'code': 'COP',
        'noDecimal': True, 'ctm': 0.90, 'cpcm': 609.0, 'convm': 0.73, 'roasm': 0.78,
        'region': 'Americas', 'curr_label': 'COP',
        'adj': 'Colombian',
        # Shopify
        'carm': 1.14, 'marginm': 0.82,
        # Email
        'openm': 0.85, 'clickm': 0.82, 'unsubm': 1.12, 'bouncem': 1.18,
        # SEO
        'trafficm': 0.22, 'ctrm': 0.88, 'compm': 0.68,
    },
    {
        'name': 'Chile', 'slug': 'chile', 'flag': '🇨🇱',
        'sym': 'CLP ', 'sym_display': 'CLP', 'code': 'CLP',
        'noDecimal': True, 'ctm': 0.88, 'cpcm': 176.0, 'convm': 0.75, 'roasm': 0.80,
        'region': 'Americas', 'curr_label': 'CLP',
        'adj': 'Chilean',
        'carm': 1.08, 'marginm': 0.86,
        'openm': 0.87, 'clickm': 0.84, 'unsubm': 1.08, 'bouncem': 1.12,
        'trafficm': 0.12, 'ctrm': 0.88, 'compm': 0.68,
    },
    {
        'name': 'Peru', 'slug': 'peru', 'flag': '🇵🇪',
        'sym': 'S/', 'sym_display': 'S/', 'code': 'PEN',
        'noDecimal': False, 'ctm': 0.89, 'cpcm': 0.627, 'convm': 0.74, 'roasm': 0.79,
        'region': 'Americas', 'curr_label': 'PEN (S/)',
        'adj': 'Peruvian',
        'carm': 1.15, 'marginm': 0.81,
        'openm': 0.83, 'clickm': 0.81, 'unsubm': 1.14, 'bouncem': 1.20,
        'trafficm': 0.18, 'ctrm': 0.86, 'compm': 0.65,
    },
    {
        'name': 'Nigeria', 'slug': 'nigeria', 'flag': '🇳🇬',
        'sym': '₦', 'sym_display': '₦', 'code': 'NGN',
        'noDecimal': True, 'ctm': 0.86, 'cpcm': 181.0, 'convm': 0.68, 'roasm': 0.72,
        'region': 'Africa', 'curr_label': 'NGN (₦)',
        'adj': 'Nigerian',
        'carm': 1.22, 'marginm': 0.75,
        'openm': 0.78, 'clickm': 0.76, 'unsubm': 1.20, 'bouncem': 1.35,
        'trafficm': 0.20, 'ctrm': 0.82, 'compm': 0.55,
    },
    {
        'name': 'Kenya', 'slug': 'kenya', 'flag': '🇰🇪',
        'sym': 'KSh ', 'sym_display': 'KSh', 'code': 'KES',
        'noDecimal': False, 'ctm': 0.87, 'cpcm': 13.5, 'convm': 0.70, 'roasm': 0.74,
        'region': 'Africa', 'curr_label': 'KES (KSh)',
        'adj': 'Kenyan',
        'carm': 1.20, 'marginm': 0.76,
        'openm': 0.80, 'clickm': 0.78, 'unsubm': 1.18, 'bouncem': 1.30,
        'trafficm': 0.08, 'ctrm': 0.82, 'compm': 0.52,
    },
    {
        'name': 'Portugal', 'slug': 'portugal', 'flag': '🇵🇹',
        'sym': '€', 'sym_display': '€', 'code': 'EUR',
        'noDecimal': False, 'ctm': 0.89, 'cpcm': 0.325, 'convm': 0.86, 'roasm': 0.84,
        'region': 'Europe', 'curr_label': 'EUR (€)',
        'adj': 'Portuguese',
        'carm': 1.05, 'marginm': 0.90,
        'openm': 0.92, 'clickm': 0.90, 'unsubm': 1.02, 'bouncem': 1.04,
        'trafficm': 0.12, 'ctrm': 0.92, 'compm': 0.75,
    },
    {
        'name': 'Belgium', 'slug': 'belgium', 'flag': '🇧🇪',
        'sym': '€', 'sym_display': '€', 'code': 'EUR',
        'noDecimal': False, 'ctm': 0.91, 'cpcm': 0.359, 'convm': 0.90, 'roasm': 0.88,
        'region': 'Europe', 'curr_label': 'EUR (€)',
        'adj': 'Belgian',
        'carm': 1.03, 'marginm': 0.93,
        'openm': 0.96, 'clickm': 0.94, 'unsubm': 0.98, 'bouncem': 1.02,
        'trafficm': 0.14, 'ctrm': 0.94, 'compm': 0.80,
    },
    {
        'name': 'Austria', 'slug': 'austria', 'flag': '🇦🇹',
        'sym': '€', 'sym_display': '€', 'code': 'EUR',
        'noDecimal': False, 'ctm': 0.90, 'cpcm': 0.342, 'convm': 0.91, 'roasm': 0.89,
        'region': 'Europe', 'curr_label': 'EUR (€)',
        'adj': 'Austrian',
        'carm': 1.04, 'marginm': 0.92,
        'openm': 0.95, 'clickm': 0.92, 'unsubm': 0.99, 'bouncem': 1.02,
        'trafficm': 0.12, 'ctrm': 0.93, 'compm': 0.78,
    },
    {
        'name': 'Finland', 'slug': 'finland', 'flag': '🇫🇮',
        'sym': '€', 'sym_display': '€', 'code': 'EUR',
        'noDecimal': False, 'ctm': 0.92, 'cpcm': 0.376, 'convm': 0.92, 'roasm': 0.90,
        'region': 'Europe', 'curr_label': 'EUR (€)',
        'adj': 'Finnish',
        'carm': 1.02, 'marginm': 0.94,
        'openm': 1.02, 'clickm': 1.00, 'unsubm': 0.92, 'bouncem': 0.95,
        'trafficm': 0.08, 'ctrm': 0.95, 'compm': 0.82,
    },
    {
        'name': 'Romania', 'slug': 'romania', 'flag': '🇷🇴',
        'sym': 'lei ', 'sym_display': 'lei', 'code': 'RON',
        'noDecimal': False, 'ctm': 0.83, 'cpcm': 0.940, 'convm': 0.78, 'roasm': 0.80,
        'region': 'Europe', 'curr_label': 'RON (lei)',
        'adj': 'Romanian',
        'carm': 1.12, 'marginm': 0.82,
        'openm': 0.88, 'clickm': 0.85, 'unsubm': 1.08, 'bouncem': 1.10,
        'trafficm': 0.18, 'ctrm': 0.88, 'compm': 0.68,
    },
    {
        'name': 'Bulgaria', 'slug': 'bulgaria', 'flag': '🇧🇬',
        'sym': 'лв ', 'sym_display': 'лв', 'code': 'BGN',
        'noDecimal': False, 'ctm': 0.82, 'cpcm': 0.331, 'convm': 0.76, 'roasm': 0.78,
        'region': 'Europe', 'curr_label': 'BGN (лв)',
        'adj': 'Bulgarian',
        'carm': 1.14, 'marginm': 0.80,
        'openm': 0.85, 'clickm': 0.82, 'unsubm': 1.10, 'bouncem': 1.12,
        'trafficm': 0.10, 'ctrm': 0.86, 'compm': 0.62,
    },
    {
        'name': 'Croatia', 'slug': 'croatia', 'flag': '🇭🇷',
        'sym': '€', 'sym_display': '€', 'code': 'EUR',
        'noDecimal': False, 'ctm': 0.84, 'cpcm': 0.274, 'convm': 0.80, 'roasm': 0.82,
        'region': 'Europe', 'curr_label': 'EUR (€)',
        'adj': 'Croatian',
        'carm': 1.06, 'marginm': 0.84,
        'openm': 0.90, 'clickm': 0.88, 'unsubm': 1.04, 'bouncem': 1.06,
        'trafficm': 0.05, 'ctrm': 0.88, 'compm': 0.65,
    },
    {
        'name': 'Czechia', 'slug': 'czechia', 'flag': '🇨🇿',
        'sym': 'Kč ', 'sym_display': 'Kč', 'code': 'CZK',
        'noDecimal': False, 'ctm': 0.85, 'cpcm': 5.13, 'convm': 0.84, 'roasm': 0.86,
        'region': 'Europe', 'curr_label': 'CZK (Kč)',
        'adj': 'Czech',
        'carm': 1.05, 'marginm': 0.88,
        'openm': 0.92, 'clickm': 0.90, 'unsubm': 1.02, 'bouncem': 1.04,
        'trafficm': 0.14, 'ctrm': 0.90, 'compm': 0.78,
    },
    {
        'name': 'Taiwan', 'slug': 'taiwan', 'flag': '🇹🇼',
        'sym': 'NT$', 'sym_display': 'NT$', 'code': 'TWD',
        'noDecimal': False, 'ctm': 0.85, 'cpcm': 5.85, 'convm': 0.86, 'roasm': 0.88,
        'region': 'Asia Pacific', 'curr_label': 'TWD (NT$)',
        'adj': 'Taiwanese',
        'carm': 1.06, 'marginm': 0.90,
        'openm': 0.88, 'clickm': 0.86, 'unsubm': 1.06, 'bouncem': 1.08,
        'trafficm': 0.28, 'ctrm': 0.87, 'compm': 0.80,
    },
]

# ─── Channel data ─────────────────────────────────────────────────────────────
CHANNELS = [
    {
        'path': 'google-ads', 'name': 'Google Ads',
        'storageKey': 'bm_google_unlocked',
        'stripeCode': '7sY9AUfpL5IG1CD8cM3Je07',
        'dataFile': 'google-ads-data.js',
        'base_cpc': 2.69, 'base_ctr': 3.51,
        'type': 'ppc_roas',
        'dataScript': '../../../benchmarks/google-ads-data.js',
        'channel_short': 'Google Ads',
    },
    {
        'path': 'meta-ads', 'name': 'Meta Ads',
        'storageKey': 'bm_meta_unlocked',
        'stripeCode': '6oU8wQ1yVc744OP3Ww3Je06',
        'dataFile': 'meta-ads-data.js',
        'base_cpc': 0.97, 'base_ctr': 1.11,
        'type': 'ppc_roas',
        'dataScript': '../../../benchmarks/meta-ads-data.js',
        'channel_short': 'Meta Ads',
    },
    {
        'path': 'tiktok-ads', 'name': 'TikTok Ads',
        'storageKey': 'bm_tiktok_unlocked',
        'stripeCode': '7sY5kEcdz0oma998cM3Je09',
        'dataFile': 'tiktok-ads-data.js',
        'base_cpc': 1.18, 'base_ctr': 0.84,
        'type': 'ppc_no_roas',
        'dataScript': '../../../benchmarks/tiktok-ads-data.js',
        'channel_short': 'TikTok Ads',
    },
    {
        'path': 'linkedin-ads', 'name': 'LinkedIn Ads',
        'storageKey': 'bm_linkedin_unlocked',
        'stripeCode': '6oU9AUdhD7QOftt3Ww3Je0a',
        'dataFile': 'linkedin-ads-data.js',
        'base_cpc': 5.26, 'base_ctr': 0.65,
        'type': 'ppc_no_roas',
        'dataScript': '../../../benchmarks/linkedin-ads-data.js',
        'channel_short': 'LinkedIn Ads',
    },
    {
        'path': 'reddit-ads', 'name': 'Reddit Ads',
        'storageKey': 'bm_reddit_unlocked',
        'stripeCode': '4gMdRafpL1sqa99boY3Je0b',
        'dataFile': 'reddit-ads-data.js',
        'base_cpc': 0.75, 'base_ctr': 0.40,
        'type': 'ppc_no_roas',
        'dataScript': '../../../benchmarks/reddit-ads-data.js',
        'channel_short': 'Reddit Ads',
    },
    {
        'path': 'shopify', 'name': 'Shopify',
        'storageKey': 'bm_shopify_unlocked',
        'stripeCode': 'aFafZicdz5IG3KLfFe3Je0c',
        'dataFile': 'shopify-data.js',
        'base_cpc': 0, 'base_ctr': 0,
        'type': 'shopify',
        'dataScript': '../../../benchmarks/shopify-data.js',
        'channel_short': 'Shopify',
    },
    {
        'path': 'email-marketing', 'name': 'Email Marketing',
        'storageKey': 'bm_email_unlocked',
        'stripeCode': '4gMcN6cdz5IG2GH0Kk3Je0d',
        'dataFile': 'email-marketing-data.js',
        'base_cpc': 0, 'base_ctr': 0,
        'type': 'email',
        'dataScript': '../../../benchmarks/email-marketing-data.js',
        'channel_short': 'Email Marketing',
    },
    {
        'path': 'seo', 'name': 'SEO',
        'storageKey': 'bm_seo_unlocked',
        'stripeCode': 'eVq9AUcdz6MK5STboY3Je08',
        'dataFile': 'seo-data.js',
        'base_cpc': 0, 'base_ctr': 0,
        'type': 'seo',
        'dataScript': '../../../benchmarks/seo-data.js',
        'channel_short': 'SEO',
    },
]

# ─── Helper: format number ─────────────────────────────────────────────────────
def fmt(v):
    """Format a number: round to 2 decimal places, trim trailing zeros."""
    rounded = round(v, 2)
    if rounded == int(rounded):
        return str(int(rounded))
    s = f'{rounded:.2f}'.rstrip('0')
    return s


# ─── FAQ generators ────────────────────────────────────────────────────────────
def faq_ppc(ch, c):
    """6 FAQs for PPC channels (Google, Meta, TikTok, LinkedIn, Reddit)."""
    name = c['name']
    adj = c['adj']
    sym = c['sym_display']
    code = c['code']
    chn = ch['name']
    base_cpc = ch['base_cpc']
    base_ctr = ch['base_ctr']
    cpcm = c['cpcm']
    ctm = c['ctm']
    convm = c['convm']

    local_cpc = round(base_cpc * cpcm, 2 if not c['noDecimal'] else 0)
    local_ctr = round(base_ctr * ctm, 2)
    local_conv = round(4.40 * convm, 1) if ch['path'] == 'google-ads' else round(9.21 * convm, 1) if ch['path'] == 'meta-ads' else round(1.80 * convm, 1) if ch['path'] == 'tiktok-ads' else round(1.60 * convm, 1) if ch['path'] == 'linkedin-ads' else round(1.50 * convm, 1)

    cpc_label = 'CPC' if ch['path'] in ('google-ads', 'linkedin-ads') else 'CPM' if ch['path'] in ('meta-ads', 'tiktok-ads') else 'CPC'
    ctr_label = 'CTR'

    if c['noDecimal']:
        local_cpc_str = f'{sym}{int(local_cpc):,}'
    else:
        local_cpc_str = f'{sym}{local_cpc}'

    # Comparison market
    region = c['region']
    if region == 'Americas':
        comp_market = 'Brazil' if name != 'Brazil' else 'Mexico'
    elif region == 'Africa':
        comp_market = 'South Africa'
    elif region == 'Europe':
        comp_market = 'Germany' if name != 'Germany' else 'France'
    else:
        comp_market = 'Australia'

    # Cost level adjective
    cpc_ratio = cpcm if cpcm <= 1 else 1.0
    cost_level = 'lower' if ctm < 0.90 else 'competitive'

    q1_name = f'What is a good {cpc_label} for {chn} in {name}?'
    q1_ans = (
        f'The average {cpc_label} for {chn} in {name} is around {local_cpc_str} across all industries. '
        f'High-competition verticals like Finance, Insurance and Legal typically see significantly higher costs, '
        f'while lower-competition categories like Food, Entertainment and Non-Profits tend to be more affordable. '
        f'{name}\'s {cpc_label} reflects local market dynamics and advertiser competition in the {adj} market.'
    )

    q2_name = f'What is a good {ctr_label} for {chn} in {name}?'
    q2_ans = (
        f'A good {ctr_label} for {chn} in {name} is approximately {local_ctr:.2f}% across all industries. '
        f'Performance varies significantly by industry — verticals with strong visual or emotional appeal tend to see higher CTRs, '
        f'while B2B and high-consideration categories see lower rates. '
        f'Optimising your creative for the {adj} audience, including local language and cultural references, can significantly improve CTR.'
    )

    q3_name = f'Why are {chn} costs {cost_level} in {name} compared to global averages?'
    q3_ans = (
        f'{name}\'s {chn} market is shaped by local advertiser density, audience purchasing power, and platform penetration. '
        f'Emerging or mid-tier markets like {name} typically have lower advertiser competition than the USA or UK, '
        f'which can result in more cost-effective CPCs — but also lower baseline conversion rates due to trust and payment infrastructure differences. '
        f'Understanding the {adj} consumer journey is key to optimising your return in this market.'
    )

    q4_name = f'What is a good conversion rate for {chn} in {name}?'
    q4_ans = (
        f'The average conversion rate for {chn} in {name} is approximately {local_conv:.1f}% across all industries. '
        f'Service-based industries with clear calls-to-action tend to see higher rates, while eCommerce and travel typically see lower rates due to longer decision cycles. '
        f'Localising your landing pages with {adj} currency, local payment methods, and relevant trust signals can meaningfully lift conversion rates.'
    )

    q5_name = f'How do {name} {chn} benchmarks compare to {comp_market}?'
    q5_ans = (
        f'{name} and {comp_market} share similar regional dynamics but differ in advertiser maturity and audience purchasing power. '
        f'{name} typically offers lower auction competition, which can mean more accessible CPCs for new entrants. '
        f'However, conversion rates and ROAS can vary based on local eCommerce infrastructure, payment method availability, and consumer trust levels. '
        f'Always test creative and landing pages locally rather than assuming one market\'s learnings will transfer directly.'
    )

    q6_name = f'How often are these {name} benchmarks updated?'
    q6_ans = (
        f'Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from '
        f'anonymised campaign data and published industry reports specific to the {name} market. '
        f'Individual results will vary based on keyword competition, creative quality, bid strategy, landing page experience and account structure.'
    )

    return [
        (q1_name, q1_ans),
        (q2_name, q2_ans),
        (q3_name, q3_ans),
        (q4_name, q4_ans),
        (q5_name, q5_ans),
        (q6_name, q6_ans),
    ]


def faq_shopify(ch, c):
    name = c['name']
    adj = c['adj']
    sym = c['sym_display']
    code = c['code']
    convm = c['convm']
    cpcm = c['cpcm']
    roasm = c['roasm']
    carm = c['carm']
    marginm = c['marginm']

    local_cvr = round(2.50 * convm, 1)
    local_cpa = round(42.0 * cpcm, 1 if not c['noDecimal'] else 0)
    local_roas = round(3.20 * roasm, 2)
    local_car = round(70.0 * carm, 1)
    local_margin = round(35.0 * marginm, 1)

    if c['noDecimal']:
        local_cpa_str = f'{sym}{int(local_cpa):,}'
    else:
        local_cpa_str = f'{sym}{local_cpa:.0f}'

    region = c['region']
    if region == 'Americas':
        comp_market = 'Brazil' if name != 'Brazil' else 'Mexico'
    elif region == 'Africa':
        comp_market = 'South Africa'
    elif region == 'Europe':
        comp_market = 'Germany' if name != 'Germany' else 'France'
    else:
        comp_market = 'Australia'

    return [
        (
            f'What is a good Shopify conversion rate in {name}?',
            f'The average Shopify store conversion rate in {name} is approximately {local_cvr:.1f}% across all product categories. '
            f'Fashion, Beauty and Health & Wellness stores tend to see above-average conversion rates in {name}, while high-consideration categories like Electronics and Furniture see lower rates. '
            f'Localising your store with {adj} currency ({sym}), local payment methods, and trust signals like local reviews significantly improves conversion.'
        ),
        (
            f'What is a good CPA for a Shopify store in {name}?',
            f'The average blended CPA (cost per acquisition across all marketing channels) for Shopify stores in {name} is around {local_cpa_str} per customer. '
            f'CPA varies significantly by product category — high-margin products can sustain higher CPAs, while low-margin consumables need tighter cost control. '
            f'Optimising your email and retention marketing is the most effective way to reduce blended CPA in the {name} market.'
        ),
        (
            f'What is a good ROAS for Shopify stores in {name}?',
            f'The average blended ROAS for Shopify stores in {name} is approximately {local_roas:.2f}x. '
            f'This reflects the ratio of revenue to total ad spend across all channels. '
            f'New stores in {name} typically start with lower ROAS as they build audiences and optimise creative — target 2x+ in early stages and work toward 3x+ once you have strong product-market fit.'
        ),
        (
            f'What is the cart abandonment rate for Shopify in {name}?',
            f'The average cart abandonment rate for Shopify stores in {name} is around {local_car:.0f}%. '
            f'Reducing cart abandonment in {name} typically requires offering local payment options, transparent shipping costs, and clear return policies. '
            f'Abandoned cart email sequences and SMS reminders remain the most effective recovery tools — a well-timed series can recover 10–15% of abandoned carts.'
        ),
        (
            f'What is a good profit margin for Shopify stores in {name}?',
            f'The average net profit margin for Shopify stores in {name} is approximately {local_margin:.0f}% after accounting for COGS, shipping, returns and marketing. '
            f'Margins in {name} are affected by local logistics costs, import duties and payment processing fees. '
            f'Focus on increasing average order value through upsells and bundles to improve margins without increasing customer acquisition costs.'
        ),
        (
            f'How often are these {name} Shopify benchmarks updated?',
            f'Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from '
            f'anonymised Shopify store data and published eCommerce reports for the {name} market. '
            f'Individual results will vary based on product category, price point, marketing mix, and logistics complexity.'
        ),
    ]


def faq_email(ch, c):
    name = c['name']
    adj = c['adj']
    openm = c['openm']
    clickm = c['clickm']
    unsubm = c['unsubm']
    bouncem = c['bouncem']

    local_open = round(21.50 * openm, 1)
    local_click = round(2.80 * clickm, 2)
    local_unsub = round(0.20 * unsubm, 3)
    local_bounce = round(0.65 * bouncem, 2)

    region = c['region']
    if region == 'Americas':
        comp_market = 'Brazil' if name != 'Brazil' else 'Mexico'
    elif region == 'Africa':
        comp_market = 'South Africa'
    elif region == 'Europe':
        comp_market = 'Germany' if name != 'Germany' else 'France'
    else:
        comp_market = 'Australia'

    # Best send time varies by region
    if region == 'Americas':
        best_time = 'Tuesday to Thursday, 9–11am local time'
    elif region == 'Africa':
        best_time = 'Tuesday to Thursday, 9–11am local time'
    elif region == 'Europe':
        best_time = 'Tuesday to Thursday, 9–11am local time'
    else:
        best_time = 'Tuesday to Thursday, 10am–12pm local time'

    return [
        (
            f'What is a good email open rate in {name}?',
            f'The average email open rate in {name} is around {local_open:.1f}% across all industries. '
            f'Healthcare, Education and Finance consistently see above-average open rates, while Dating and Crypto see lower rates due to subscriber fatigue. '
            f'Note that open rates are inflated by Apple\'s Mail Privacy Protection (MPP) — click rate is a more reliable engagement signal for the {name} market.'
        ),
        (
            f'What is a good email click rate in {name}?',
            f'The average email click rate (clicks ÷ delivered emails) in {name} is around {local_click:.2f}%. '
            f'Food & Beverage, Travel and Retail consistently see the highest click rates because their content is deal-driven and visual. '
            f'Click-to-open rate (CTOR) is often more meaningful — divide your click rate by your open rate to see how engaged {adj} subscribers really are.'
        ),
        (
            f'What is a good unsubscribe rate for email marketing in {name}?',
            f'The average email unsubscribe rate in {name} is around {local_unsub:.3f}% per send. '
            f'Anything above 0.5% is a strong signal that you are sending too frequently, your content is not relevant, or your list health is poor. '
            f'Segmenting your list and sending targeted content rather than batch-and-blast campaigns significantly reduces unsubscribe rates in the {name} market.'
        ),
        (
            f'What is a good bounce rate for email marketing in {name}?',
            f'The average email bounce rate in {name} is around {local_bounce:.2f}% (hard + soft combined). '
            f'A hard bounce rate above 2% is a serious list health problem and will damage your sender reputation. '
            f'Maintain a clean list by removing hard bounces immediately and using double opt-in for new subscribers to reduce bounce rates.'
        ),
        (
            f'When is the best time to send email campaigns in {name}?',
            f'The optimal send time for email marketing in {name} is typically {best_time}. '
            f'These windows align with when {adj} professionals check their email at the start of the work day or during a mid-morning break. '
            f'Weekend sends typically see 15–25% lower open rates in {name}. Always A/B test send times against your specific audience, as B2C lists may respond differently to B2B lists.'
        ),
        (
            f'How often are these {name} email marketing benchmarks updated?',
            f'Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from '
            f'anonymised campaign data and published industry reports for the {name} market. '
            f'Individual results will vary based on email platform, list quality, send frequency, content relevance and subject line quality.'
        ),
    ]


def faq_seo(ch, c):
    name = c['name']
    adj = c['adj']
    trafficm = c['trafficm']
    ctrm = c['ctrm']
    compm = c['compm']

    local_ctr = round(3.80 * ctrm, 2)
    comp_level = 'moderate' if compm < 0.70 else 'growing' if compm < 0.80 else 'competitive'

    region = c['region']
    if region == 'Americas':
        comp_market = 'Brazil' if name != 'Brazil' else 'Mexico'
    elif region == 'Africa':
        comp_market = 'South Africa'
    elif region == 'Europe':
        comp_market = 'Germany' if name != 'Germany' else 'France'
    else:
        comp_market = 'Australia'

    kd_range = '15–40' if compm < 0.70 else '20–50' if compm < 0.80 else '25–55'

    return [
        (
            f'What is a good organic CTR in {name}?',
            f'The average organic click-through rate (CTR) in {name} is around {local_ctr:.2f}% across all industries. '
            f'{name} is a {comp_level} SEO market where optimising title tags, meta descriptions, and structured data can lift your CTR significantly. '
            f'Industries like Food & Beverage, Entertainment and Local Services see the highest organic CTRs due to visual snippets and high local intent.'
        ),
        (
            f'How competitive is SEO in {name}?',
            (f'{name} has a {comp_level} SEO landscape — keyword difficulty (KD) and domain authority (DA) requirements for page 1 rankings are '
             + ('above' if compm > 0.75 else 'below')
             + f' global averages. '
             f'Finance, Insurance and Legal have the highest competition, while Lifestyle and Local Services are more accessible for newer sites. '
             f'Local SEO (Google Business Profile optimisation) often yields faster results for {adj} service-area businesses.')
        ),
        (
            f'How many backlinks do I need to rank on page 1 in {name}?',
            f'The median number of backlinks needed for a page 1 ranking in {name} varies significantly by industry. '
            f'Competitive niches like Finance and Legal may require 60–100+ referring domains to rank on page 1. '
            f'Lower-competition sectors like Beauty, Pet Products and Local Services often rank with 20–50 backlinks. '
            f'Quality matters more than quantity — links from authoritative {adj} publications carry far more weight than low-authority links.'
        ),
        (
            f'What keyword difficulty (KD) should I target in {name}?',
            f'In {name}, new and medium-authority sites should target keywords with a KD of {kd_range} to see rankings within 3–6 months. '
            f'Keywords with KD above 65 typically require a domain authority of 50+ and an established backlink profile. '
            f'Use KD as a directional filter — always review the actual SERP to understand who ranks before deciding to target a keyword in the {adj} market.'
        ),
        (
            f'How does {name} SEO compare to {comp_market}?',
            (f'{name} and {comp_market} have different SEO dynamics — {comp_market} typically has '
             + ('higher' if compm < 0.78 else 'similar')
             + f' competition and more established authority sites. '
             f'{name} may offer more opportunities in long-tail and local-language keywords for brands that invest in localised content. '
             f'Building topical authority in {name} with {adj}-market focused content is the most sustainable long-term SEO strategy.')
        ),
        (
            f'How often are these {name} SEO benchmarks updated?',
            f'Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from '
            f'published SEO industry reports and anonymised data specific to the {name} market. '
            f'Individual results will vary based on domain authority, content quality, backlink profile, technical SEO health and local competition.'
        ),
    ]


# ─── Build FAQ HTML block ──────────────────────────────────────────────────────
def build_faq_html(faqs):
    items = []
    for i, (q, a) in enumerate(faqs):
        open_attr = ' open' if i == 0 else ''
        items.append(f'''
        <details class="faq-item"{open_attr}>
          <summary class="faq-question">
            <span>{q}</span>
            <span class="faq-chevron" aria-hidden="true">&#8964;</span>
          </summary>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </details>''')
    return '\n'.join(items)


def build_faq_jsonld(faqs):
    entities = []
    for q, a in faqs:
        entities.append({
            '@type': 'Question',
            'name': q,
            'acceptedAnswer': {'@type': 'Answer', 'text': a}
        })
    return json.dumps({
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': entities
    }, ensure_ascii=False, indent=2)


# ─── Dataset JSON-LD by channel type ──────────────────────────────────────────
def build_dataset_jsonld(ch, c):
    name = c['name']
    slug = c['slug']
    code = c['code']
    ch_name = ch['name']
    ch_path = ch['path']

    if ch['type'] in ('ppc_roas', 'ppc_no_roas'):
        if ch_path == 'google-ads':
            desc = f'Google Ads average CTR, CPC, conversion rate, CPA and ROAS for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
            kws = [f'Google Ads benchmarks {name}', f'{name} Google Ads CPC', f'Google Ads CTR {name}', f'CPA benchmarks {name}', f'ROAS benchmarks {name} {code}']
        elif ch_path == 'meta-ads':
            desc = f'Meta Ads average CTR, CPM, CPC, conversion rate and CPA for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
            kws = [f'Meta Ads benchmarks {name}', f'{name} Meta Ads CPM', f'Facebook Ads CPC {name}', f'Meta Ads CTR {name}', f'CPA benchmarks {name} {code}']
        elif ch_path == 'tiktok-ads':
            desc = f'TikTok Ads average CTR, CPC, CPM and conversion rate for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
            kws = [f'TikTok Ads benchmarks {name}', f'{name} TikTok Ads CPC', f'TikTok CTR {name}', f'TikTok Ads CPM {name}']
        elif ch_path == 'linkedin-ads':
            desc = f'LinkedIn Ads average CTR, CPC, CPM and conversion rate for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
            kws = [f'LinkedIn Ads benchmarks {name}', f'{name} LinkedIn Ads CPC', f'LinkedIn CTR {name}', f'LinkedIn Ads CPM {name}']
        else:  # reddit
            desc = f'Reddit Ads average CTR, CPC, CPM and conversion rate for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
            kws = [f'Reddit Ads benchmarks {name}', f'{name} Reddit Ads CPC', f'Reddit CTR {name}', f'Reddit Ads CPM {name}']
    elif ch['type'] == 'shopify':
        desc = f'Shopify average conversion rate, CPA, ROAS, cart abandonment and profit margin for 38 industries in {name}. All figures in {code}. Q2 2026 industry aggregates.'
        kws = [f'Shopify benchmarks {name}', f'Shopify conversion rate {name}', f'Shopify CPA {name}', f'eCommerce benchmarks {name}']
    elif ch['type'] == 'email':
        desc = f'Email marketing open rate, click rate, unsubscribe rate and bounce rate for 38 industries in {name}. Q2 2026 industry aggregates.'
        kws = [f'email marketing benchmarks {name}', f'email open rate {name}', f'email click rate {name}', f'email unsubscribe rate {name}']
    else:  # seo
        desc = f'SEO organic traffic, CTR, backlinks for page 1, keyword difficulty and domain authority for 38 industries in {name}. Q2 2026 industry aggregates.'
        kws = [f'SEO benchmarks {name}', f'organic CTR {name}', f'keyword difficulty {name}', f'backlinks page 1 {name}']

    return json.dumps({
        '@context': 'https://schema.org',
        '@type': 'Dataset',
        'name': f'{ch_name} Benchmarks — {name} (Q2 2026)',
        'description': desc,
        'publisher': {'@type': 'Organization', 'name': 'XYZ Lab', 'url': 'https://xyzlab.com'},
        'url': f'https://xyzlab.com/{ch_path}/benchmarks/{slug}/',
        'keywords': kws,
    }, ensure_ascii=False, indent=2)


# ─── HTML page generation ──────────────────────────────────────────────────────
def gen_html_page(template_html, ch, c):
    """Take australia template and substitute for new country."""
    name = c['name']
    slug = c['slug']
    flag = c['flag']
    adj = c['adj']
    sym_display = c['sym_display']
    code = c['code']
    curr_label = c['curr_label']

    html = template_html

    # 1. BENCHMARK_COUNTRY variable
    html = html.replace(
        "window.BENCHMARK_COUNTRY    = 'Australia';",
        f"window.BENCHMARK_COUNTRY    = '{name}';"
    )

    # 2. canonical and OG URLs: /australia/ -> /{slug}/
    html = html.replace(
        f'/benchmarks/australia/',
        f'/benchmarks/{slug}/'
    )

    # 3. Replace "Australia" text in various places (but NOT in JS paths or data file names)
    # We need to be careful: "Australia" appears in text content and in JS code
    # The JS variable window.BENCHMARK_COUNTRY is already handled
    # The script src paths don't contain "Australia"
    # So a simple replacement of 'Australia' -> name should be safe EXCEPT:
    # - "australian" -> adj (case insensitive)

    # Replace "australian" (case insensitive) before "Australia"
    html = re.sub(r'[Aa]ustralian', lambda m: adj if m.group().istitle() or m.group()[0].isupper() else adj.lower(), html, flags=re.IGNORECASE)

    # Actually let's be more precise:
    html = html.replace('Australian', adj)
    html = html.replace('australian', adj.lower())

    # Replace "Australia" with name
    html = html.replace('Australia', name)

    # 4. Currency replacements
    # "AUD (AU$)" -> curr_label
    html = html.replace('AUD (AU$)', curr_label)
    # "AUD" in text -> code (but not in JS data references like 'AUD' string quotes in JSON-LD keywords)
    # The JSON-LD keywords use "AUD" - we'll replace carefully
    # Actually the dataset JSON-LD is replaced entirely, so let's do broad replace of AUD->code
    # but NOT inside script tags that reference data files
    # The safest approach: replace 'AUD' with code in text content
    # Since we replace the entire JSON-LD blocks anyway, let's do it
    html = html.replace('AUD', code)
    # "AU$" -> sym_display
    html = html.replace('AU$', sym_display)
    # Flag
    html = html.replace('🇦🇺', flag)

    # 5. Replace Dataset JSON-LD block
    dataset_jsonld = build_dataset_jsonld(ch, c)
    # Use string-based replacement to find the Dataset LD+JSON block safely
    DATASET_MARKER = '"@type": "Dataset"'
    SCRIPT_OPEN = '<script type="application/ld+json">'
    SCRIPT_CLOSE = '</script>'
    idx_dataset = html.find(DATASET_MARKER)
    if idx_dataset != -1:
        # Find the opening <script> before this marker
        start = html.rfind(SCRIPT_OPEN, 0, idx_dataset)
        # Find the closing </script> after this marker
        end = html.find(SCRIPT_CLOSE, idx_dataset)
        if start != -1 and end != -1:
            end += len(SCRIPT_CLOSE)
            html = html[:start] + f'<script type="application/ld+json">\n  {dataset_jsonld}\n  </script>' + html[end:]

    # 6. Build FAQs
    if ch['type'] in ('ppc_roas', 'ppc_no_roas'):
        faqs = faq_ppc(ch, c)
    elif ch['type'] == 'shopify':
        faqs = faq_shopify(ch, c)
    elif ch['type'] == 'email':
        faqs = faq_email(ch, c)
    else:
        faqs = faq_seo(ch, c)

    # 7. Replace FAQPage JSON-LD block
    faqpage_jsonld = build_faq_jsonld(faqs)
    FAQPAGE_MARKER = '"@type": "FAQPage"'
    idx_faq = html.find(FAQPAGE_MARKER)
    if idx_faq != -1:
        start = html.rfind(SCRIPT_OPEN, 0, idx_faq)
        end = html.find(SCRIPT_CLOSE, idx_faq)
        if start != -1 and end != -1:
            end += len(SCRIPT_CLOSE)
            html = html[:start] + f'<script type="application/ld+json">\n  {faqpage_jsonld}\n  </script>' + html[end:]

    # 8. Replace HTML FAQ section (between <!-- FAQ --> and <!-- RELATED -->)
    faq_html = build_faq_html(faqs)
    ch_name = ch['name']
    adj_lower = adj.lower()
    ch_name_lower = ch_name.lower()
    new_faq_section = f'''  <!-- FAQ -->
  <section class="faq" id="faq">
    <div class="container">
      <div class="section-header">
        <div class="badge">FAQ</div>
        <h2>{ch_name} Benchmarks — {name} FAQ</h2>
        <p>Common questions about {ch_name_lower} performance in the {adj} market.</p>
      </div>
      <div class="faq-list">
{faq_html}

      </div>
    </div>
  </section>

  <!-- RELATED -->'''

    html = re.sub(
        r'<!-- FAQ -->.*?<!-- RELATED -->',
        new_faq_section,
        html, flags=re.DOTALL
    )

    # Handle shopify template placeholder {styles} if present
    if '{styles}' in html:
        # The shopify template uses placeholders - we need to use a real existing country's rendered HTML
        # This case means the template itself has unfilled placeholders - skip (shouldn't happen with australia)
        pass

    return html


# ─── Data file updates ────────────────────────────────────────────────────────
def get_data_entry(ch_type, c):
    """Return the JS object literal for a country entry."""
    has_no_decimal = c.get('noDecimal', False)
    sym = c['sym']
    code = c['code']

    if ch_type in ('ppc_roas',):
        # google-ads, meta-ads
        parts = [
            f"ctm: {c['ctm']}",
            f"cpcm: {c['cpcm']}",
            f"convm: {c['convm']}",
            f"roasm: {c['roasm']}",
            f"sym: '{sym}'",
            f"code: '{code}'"
        ]
        if has_no_decimal:
            parts.append('noDecimal: true')
        return '{ ' + ', '.join(parts) + ' }'

    elif ch_type in ('ppc_no_roas',):
        # tiktok, linkedin, reddit
        parts = [
            f"ctm: {c['ctm']}",
            f"cpcm: {c['cpcm']}",
            f"convm: {c['convm']}",
            f"sym: '{sym}'",
            f"code: '{code}'"
        ]
        if has_no_decimal:
            parts.append('noDecimal: true')
        return '{ ' + ', '.join(parts) + ' }'

    elif ch_type == 'shopify':
        parts = [
            f"cvrm: {c['convm']}",
            f"cpam: {c['cpcm']}",
            f"roasm: {c['roasm']}",
            f"carm: {c['carm']}",
            f"marginm: {c['marginm']}",
            f"sym: '{sym}'",
            f"code: '{code}'"
        ]
        if has_no_decimal:
            parts.append('noDecimal: true')
        return '{ ' + ', '.join(parts) + ' }'

    elif ch_type == 'email':
        parts = [
            f"openm: {c['openm']}",
            f"clickm: {c['clickm']}",
            f"unsubm: {c['unsubm']}",
            f"bouncem: {c['bouncem']}"
        ]
        return '{ ' + ', '.join(parts) + ' }'

    else:  # seo
        parts = [
            f"trafficm: {c['trafficm']}",
            f"ctrm: {c['ctrm']}",
            f"compm: {c['compm']}"
        ]
        return '{ ' + ', '.join(parts) + ' }'


def update_data_file(data_file_path, ch_type, new_countries):
    """Insert new country entries into a JS data file in alphabetical order."""
    with open(data_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for c in new_countries:
        cname = c['name']
        entry = get_data_entry(ch_type, c)

        # Check if already exists
        if f"'{cname}':" in content:
            print(f"  SKIP (already exists): {cname} in {data_file_path}")
            continue

        # Find insertion point (alphabetical order)
        # Pattern: find all country name entries
        # We'll insert before the next country that comes after cname alphabetically
        # Find the countries object opening
        countries_match = re.search(r'var countries = \{', content)
        if not countries_match:
            print(f"  ERROR: Cannot find countries object in {data_file_path}")
            continue

        # Get all existing country keys
        # Pattern: '    'Name':  { ...'
        existing = re.findall(r"^\s+'([^']+)':\s+\{", content, re.MULTILINE)

        # Find where to insert
        insert_before = None
        for existing_name in existing:
            if existing_name > cname:
                insert_before = existing_name
                break

        new_line = f"    '{cname}':  {entry},"

        if insert_before:
            # Insert before this country
            pattern = re.compile(
                r"(^\s+'" + re.escape(insert_before) + r"':\s+\{)",
                re.MULTILINE
            )
            content = pattern.sub(new_line + '\n' + r'\1', content, count=1)
        else:
            # Insert at the end of the countries object (before closing })
            # Find last entry and insert after it
            # Find the 'USA' entry (often last) or insert before closing brace
            last_entry_pattern = re.compile(r"(^\s+'[^']+':.*?\},?\s*\n)(\s*\};)", re.MULTILINE | re.DOTALL)
            # Actually just insert before the }; that closes countries
            content = re.sub(
                r"(\n\s*\};?\s*\n\s*var countryNames)",
                f"\n{new_line}\n\\1",
                content, count=1
            )

        print(f"  Added: {cname} -> {data_file_path}")

    with open(data_file_path, 'w', encoding='utf-8') as f:
        f.write(content)


# ─── Index page updates ────────────────────────────────────────────────────────
def build_country_card(c):
    return (
        f'            <a href="{c["slug"]}/" class="bm-country-card">\n'
        f'              <span class="bm-country-flag">{c["flag"]}</span>\n'
        f'              <span class="bm-country-info"><span class="bm-country-name">{c["name"]}</span>'
        f'<span class="bm-country-curr">{c["curr_label"]}</span></span>\n'
        f'            </a>'
    )


def update_index_html(index_path, new_countries):
    """Add new country cards to benchmark index page."""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Group new countries by region
    by_region = {}
    for c in new_countries:
        region = c['region']
        by_region.setdefault(region, []).append(c)

    for region, countries in by_region.items():
        # Sort alphabetically
        countries.sort(key=lambda x: x['name'])

        if region == 'Africa':
            # This is a new region - insert after Americas div, before Middle East div
            new_africa_div = '<div>\n          <p class="bm-region-label">Africa</p>\n          <div class="bm-country-grid">\n'
            for c in countries:
                new_africa_div += build_country_card(c) + '\n'
            new_africa_div += '          </div>\n        </div>\n\n        <div>'

            # Find the Middle East div
            middle_east_pattern = re.compile(r'(<div>\s*\n\s*<p class="bm-region-label">Middle East</p>)', re.DOTALL)
            if middle_east_pattern.search(content):
                content = middle_east_pattern.sub(new_africa_div, content, count=1)
                print(f"  Added Africa region to {index_path}")
            else:
                print(f"  WARNING: Could not find Middle East section in {index_path}")
        else:
            # Find the existing region section and add countries
            region_pattern = re.compile(
                r'(<p class="bm-region-label">' + re.escape(region) + r'</p>\s*\n\s*<div class="bm-country-grid">)(.*?)(</div>\s*\n\s*</div>)',
                re.DOTALL
            )
            match = region_pattern.search(content)
            if not match:
                print(f"  WARNING: Could not find region '{region}' in {index_path}")
                continue

            existing_grid = match.group(2)

            # Get existing country names in grid
            existing_links = re.findall(r'href="([^"]+)/"', existing_grid)
            existing_slugs = [l.rstrip('/') for l in existing_links]

            # Build new cards - all cards for this region alphabetically
            # Parse existing cards
            existing_cards = re.findall(r'(<a href="[^"]+/"[^>]*>.*?</a>)', existing_grid, re.DOTALL)

            # Build map of slug -> card
            card_map = {}
            for card in existing_cards:
                href_m = re.search(r'href="([^/]+)/"', card)
                if href_m:
                    card_map[href_m.group(1)] = card.strip()

            # Add new cards
            for c in countries:
                if c['slug'] not in card_map:
                    card_map[c['slug']] = build_country_card(c).strip()

            # Sort all by name
            # Build name->slug map for sorting
            name_slug = {}
            for c in countries:
                name_slug[c['slug']] = c['name']

            # Get existing name mapping
            all_slugs = list(card_map.keys())
            # We need to sort by display name
            # Extract name from card
            def get_card_name(slug):
                card = card_map[slug]
                m = re.search(r'<span class="bm-country-name">([^<]+)</span>', card)
                return m.group(1) if m else slug

            all_slugs_sorted = sorted(all_slugs, key=get_card_name)
            new_grid = '\n' + '\n'.join('            ' + card_map[s] if not card_map[s].startswith('            ') else card_map[s] for s in all_slugs_sorted) + '\n          '

            new_content = match.group(1) + new_grid + match.group(3)
            content = content[:match.start()] + new_content + content[match.end():]
            print(f"  Updated {region} region in {index_path}")

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)


# ─── Sitemap updates ───────────────────────────────────────────────────────────
def update_sitemap(sitemap_path, channels, new_countries):
    """Add new country URLs to sitemap under each channel's section."""
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for ch in channels:
        ch_path = ch['path']
        slugs = sorted([c['slug'] for c in new_countries])

        # Find last URL for this channel's benchmarks
        # Pattern: last occurrence of /{ch_path}/benchmarks/ URL
        last_url_pattern = re.compile(
            r'(<url><loc>https://xyzlab\.com/' + re.escape(ch_path) + r'/benchmarks/[^<]+</loc><changefreq>monthly</changefreq><priority>0\.7</priority></url>)',
        )
        matches = list(last_url_pattern.finditer(content))
        if not matches:
            print(f"  WARNING: No benchmark URLs found for {ch_path} in sitemap")
            continue

        last_match = matches[-1]
        insert_pos = last_match.end()

        new_urls = ''
        for slug in slugs:
            url = f'\n  <url><loc>https://xyzlab.com/{ch_path}/benchmarks/{slug}/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>'
            # Check if already exists
            if f'/{ch_path}/benchmarks/{slug}/' not in content:
                new_urls += url

        if new_urls:
            content = content[:insert_pos] + new_urls + content[insert_pos:]
            print(f"  Added {ch_path} URLs to sitemap")

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)


# ─── Main ──────────────────────────────────────────────────────────────────────
def main():
    pages_created = 0
    pages_skipped = 0

    # 1. Generate HTML pages
    print('\n=== Generating HTML pages ===')
    for ch in CHANNELS:
        ch_path = ch['path']
        template_path = os.path.join(BASE, ch_path, 'benchmarks', 'australia', 'index.html')

        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        for c in COUNTRIES:
            slug = c['slug']
            out_dir = os.path.join(BASE, ch_path, 'benchmarks', slug)
            out_path = os.path.join(out_dir, 'index.html')

            if os.path.exists(out_path):
                print(f'  SKIP (exists): {ch_path}/{slug}')
                pages_skipped += 1
                continue

            os.makedirs(out_dir, exist_ok=True)
            html = gen_html_page(template, ch, c)

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f'  Created: {ch_path}/benchmarks/{slug}/index.html')
            pages_created += 1

    print(f'\nHTML pages: {pages_created} created, {pages_skipped} skipped')

    # 2. Update data JS files
    print('\n=== Updating data files ===')
    for ch in CHANNELS:
        data_path = os.path.join(BASE, 'benchmarks', ch['dataFile'])
        print(f'\n  {ch["dataFile"]}:')
        update_data_file(data_path, ch['type'], COUNTRIES)

    # 3. Update benchmark index pages
    print('\n=== Updating benchmark index pages ===')
    for ch in CHANNELS:
        index_path = os.path.join(BASE, ch['path'], 'benchmarks', 'index.html')
        print(f'\n  {ch["path"]}/benchmarks/index.html:')
        update_index_html(index_path, COUNTRIES)

    # 4. Update sitemap
    print('\n=== Updating sitemap.xml ===')
    sitemap_path = os.path.join(BASE, 'sitemap.xml')
    update_sitemap(sitemap_path, CHANNELS, COUNTRIES)

    # 5. Sanity check
    print('\n=== Sanity Check ===')
    total_expected = len(CHANNELS) * len(COUNTRIES)
    total_found = 0
    for ch in CHANNELS:
        for c in COUNTRIES:
            p = os.path.join(BASE, ch['path'], 'benchmarks', c['slug'], 'index.html')
            if os.path.exists(p):
                total_found += 1
            else:
                print(f'  MISSING: {ch["path"]}/benchmarks/{c["slug"]}/index.html')

    print(f'\nExpected pages: {total_expected}')
    print(f'Found pages:    {total_found}')
    print(f'Status: {"OK" if total_found == total_expected else "INCOMPLETE"}')


if __name__ == '__main__':
    main()
