#!/usr/bin/env python3
"""Generate Email Marketing benchmark pages: pillar + 35 country pages."""
import os

BASE_DIR    = '/home/user/xyzlab'
PILLAR      = os.path.join(BASE_DIR, 'email-marketing/benchmarks')
CHANNEL     = 'Email Marketing'
CHANNEL_DESC = 'Email Campaigns &amp; Newsletters'
DATA_FILE   = 'email-marketing-data.js'
STORAGE_KEY = 'bm_email_unlocked'
STRIPE_URL  = 'https://buy.stripe.com/4gMcN6cdz5IG2GH0Kk3Je0d'
# Metrics: Open Rate, Click Rate, Unsubscribe Rate, Bounce Rate (all % — no currency)
PERKS_METRICS = 'Open Rate, Click Rate, Unsubscribe Rate &amp; Bounce Rate'

# (slug, bm_country, display, curr_str, curr_code, flag, open_approx, market_type, region)
# open_approx = BASE_OPEN(21.50) * openm — used for FAQ context
# curr_str / curr_code unused for display (all metrics %) but kept for template compat
COUNTRIES = [
    ('argentina',     'Argentina',    'Argentina',      'percentages', 'n/a', '🇦🇷', '17.6%',  'emerging', 'Latin America'),
    ('australia',     'Australia',    'Australia',      'percentages', 'n/a', '🇦🇺', '21.9%',  'high',     'the Asia Pacific'),
    ('bahrain',       'Bahrain',      'Bahrain',        'percentages', 'n/a', '🇧🇭', '17.2%',  'mid',      'the Middle East'),
    ('brazil',        'Brazil',       'Brazil',         'percentages', 'n/a', '🇧🇷', '17.6%',  'emerging', 'Latin America'),
    ('canada',        'Canada',       'Canada',         'percentages', 'n/a', '🇨🇦', '21.5%',  'high',     'North America'),
    ('denmark',       'Denmark',      'Denmark',        'percentages', 'n/a', '🇩🇰', '23.2%',  'high',     'Europe'),
    ('france',        'France',       'France',         'percentages', 'n/a', '🇫🇷', '21.1%',  'high',     'Europe'),
    ('germany',       'Germany',      'Germany',        'percentages', 'n/a', '🇩🇪', '23.7%',  'high',     'Europe'),
    ('hong-kong',     'Hong Kong',    'Hong Kong',      'percentages', 'n/a', '🇭🇰', '18.9%',  'mid',      'Asia Pacific'),
    ('india',         'India',        'India',          'percentages', 'n/a', '🇮🇳', '16.8%',  'emerging', 'Asia Pacific'),
    ('indonesia',     'Indonesia',    'Indonesia',      'percentages', 'n/a', '🇮🇩', '15.5%',  'emerging', 'Asia Pacific'),
    ('ireland',       'Ireland',      'Ireland',        'percentages', 'n/a', '🇮🇪', '22.6%',  'high',     'Europe'),
    ('italy',         'Italy',        'Italy',          'percentages', 'n/a', '🇮🇹', '19.8%',  'mid',      'Europe'),
    ('japan',         'Japan',        'Japan',          'percentages', 'n/a', '🇯🇵', '24.1%',  'high',     'Asia Pacific'),
    ('malaysia',      'Malaysia',     'Malaysia',       'percentages', 'n/a', '🇲🇾', '17.2%',  'emerging', 'Asia Pacific'),
    ('mexico',        'Mexico',       'Mexico',         'percentages', 'n/a', '🇲🇽', '17.6%',  'emerging', 'Latin America'),
    ('netherlands',   'Netherlands',  'Netherlands',    'percentages', 'n/a', '🇳🇱', '22.6%',  'high',     'Europe'),
    ('new-zealand',   'New Zealand',  'New Zealand',    'percentages', 'n/a', '🇳🇿', '21.9%',  'high',     'the Asia Pacific'),
    ('norway',        'Norway',       'Norway',         'percentages', 'n/a', '🇳🇴', '23.2%',  'high',     'Europe'),
    ('philippines',   'Philippines',  'Philippines',    'percentages', 'n/a', '🇵🇭', '16.1%',  'emerging', 'Asia Pacific'),
    ('poland',        'Poland',       'Poland',         'percentages', 'n/a', '🇵🇱', '18.9%',  'mid',      'Europe'),
    ('qatar',         'Qatar',        'Qatar',          'percentages', 'n/a', '🇶🇦', '17.6%',  'mid',      'the Middle East'),
    ('saudi-arabia',  'Saudi Arabia', 'Saudi Arabia',   'percentages', 'n/a', '🇸🇦', '17.6%',  'mid',      'the Middle East'),
    ('singapore',     'Singapore',    'Singapore',      'percentages', 'n/a', '🇸🇬', '19.8%',  'mid',      'Asia Pacific'),
    ('south-africa',  'South Africa', 'South Africa',   'percentages', 'n/a', '🇿🇦', '17.2%',  'emerging', 'Africa'),
    ('south-korea',   'South Korea',  'South Korea',    'percentages', 'n/a', '🇰🇷', '18.3%',  'mid',      'Asia Pacific'),
    ('spain',         'Spain',        'Spain',          'percentages', 'n/a', '🇪🇸', '19.8%',  'mid',      'Europe'),
    ('sweden',        'Sweden',       'Sweden',         'percentages', 'n/a', '🇸🇪', '23.2%',  'high',     'Europe'),
    ('switzerland',   'Switzerland',  'Switzerland',    'percentages', 'n/a', '🇨🇭', '23.2%',  'high',     'Europe'),
    ('thailand',      'Thailand',     'Thailand',       'percentages', 'n/a', '🇹🇭', '15.5%',  'emerging', 'Asia Pacific'),
    ('turkiye',       'Turkiye',      'Türkiye',        'percentages', 'n/a', '🇹🇷', '17.2%',  'emerging', 'Europe & the Middle East'),
    ('uae',           'UAE',          'UAE',            'percentages', 'n/a', '🇦🇪', '18.3%',  'mid',      'the Middle East'),
    ('united-kingdom','UK',           'United Kingdom', 'percentages', 'n/a', '🇬🇧', '22.6%',  'high',     'Europe'),
    ('united-states', 'USA',          'United States',  'percentages', 'n/a', '🇺🇸', '21.5%',  'high',     'North America'),
    ('vietnam',       'Vietnam',      'Vietnam',        'percentages', 'n/a', '🇻🇳', '15.1%',  'emerging', 'Asia Pacific'),
]

COUNTRY_CARDS = [
    ('australia',      '🇦🇺', 'Australia',     'AU, NZ, ZA, UK, US, CA, IE'),
    ('canada',         '🇨🇦', 'Canada',         ''),
    ('ireland',        '🇮🇪', 'Ireland',        ''),
    ('new-zealand',    '🇳🇿', 'New Zealand',    ''),
    ('south-africa',   '🇿🇦', 'South Africa',   ''),
    ('united-kingdom', '🇬🇧', 'United Kingdom', ''),
    ('united-states',  '🇺🇸', 'United States',  ''),
    ('denmark',        '🇩🇰', 'Denmark',        ''),
    ('france',         '🇫🇷', 'France',         ''),
    ('germany',        '🇩🇪', 'Germany',        ''),
    ('italy',          '🇮🇹', 'Italy',          ''),
    ('netherlands',    '🇳🇱', 'Netherlands',    ''),
    ('norway',         '🇳🇴', 'Norway',         ''),
    ('poland',         '🇵🇱', 'Poland',         ''),
    ('spain',          '🇪🇸', 'Spain',          ''),
    ('sweden',         '🇸🇪', 'Sweden',         ''),
    ('switzerland',    '🇨🇭', 'Switzerland',    ''),
    ('turkiye',        '🇹🇷', 'Türkiye',        ''),
    ('hong-kong',      '🇭🇰', 'Hong Kong',      ''),
    ('india',          '🇮🇳', 'India',          ''),
    ('indonesia',      '🇮🇩', 'Indonesia',      ''),
    ('japan',          '🇯🇵', 'Japan',          ''),
    ('malaysia',       '🇲🇾', 'Malaysia',       ''),
    ('philippines',    '🇵🇭', 'Philippines',    ''),
    ('singapore',      '🇸🇬', 'Singapore',      ''),
    ('south-korea',    '🇰🇷', 'South Korea',    ''),
    ('thailand',       '🇹🇭', 'Thailand',       ''),
    ('vietnam',        '🇻🇳', 'Vietnam',        ''),
    ('argentina',      '🇦🇷', 'Argentina',      ''),
    ('brazil',         '🇧🇷', 'Brazil',         ''),
    ('mexico',         '🇲🇽', 'Mexico',         ''),
    ('bahrain',        '🇧🇭', 'Bahrain',        ''),
    ('qatar',          '🇶🇦', 'Qatar',          ''),
    ('saudi-arabia',   '🇸🇦', 'Saudi Arabia',   ''),
    ('uae',            '🇦🇪', 'UAE',            ''),
]

# Email has no currency — override card display to show open rate context
COUNTRY_CARDS_DISPLAY = [
    ('australia',      '🇦🇺', 'Australia',     'Open ~21.9%'),
    ('canada',         '🇨🇦', 'Canada',         'Open ~21.5%'),
    ('ireland',        '🇮🇪', 'Ireland',        'Open ~22.6%'),
    ('new-zealand',    '🇳🇿', 'New Zealand',    'Open ~21.9%'),
    ('south-africa',   '🇿🇦', 'South Africa',   'Open ~17.2%'),
    ('united-kingdom', '🇬🇧', 'United Kingdom', 'Open ~22.6%'),
    ('united-states',  '🇺🇸', 'United States',  'Open ~21.5%'),
    ('denmark',        '🇩🇰', 'Denmark',        'Open ~23.2%'),
    ('france',         '🇫🇷', 'France',         'Open ~21.1%'),
    ('germany',        '🇩🇪', 'Germany',        'Open ~23.7%'),
    ('italy',          '🇮🇹', 'Italy',          'Open ~19.8%'),
    ('netherlands',    '🇳🇱', 'Netherlands',    'Open ~22.6%'),
    ('norway',         '🇳🇴', 'Norway',         'Open ~23.2%'),
    ('poland',         '🇵🇱', 'Poland',         'Open ~18.9%'),
    ('spain',          '🇪🇸', 'Spain',          'Open ~19.8%'),
    ('sweden',         '🇸🇪', 'Sweden',         'Open ~23.2%'),
    ('switzerland',    '🇨🇭', 'Switzerland',    'Open ~23.2%'),
    ('turkiye',        '🇹🇷', 'Türkiye',        'Open ~17.2%'),
    ('hong-kong',      '🇭🇰', 'Hong Kong',      'Open ~18.9%'),
    ('india',          '🇮🇳', 'India',          'Open ~16.8%'),
    ('indonesia',      '🇮🇩', 'Indonesia',      'Open ~15.5%'),
    ('japan',          '🇯🇵', 'Japan',          'Open ~24.1%'),
    ('malaysia',       '🇲🇾', 'Malaysia',       'Open ~17.2%'),
    ('philippines',    '🇵🇭', 'Philippines',    'Open ~16.1%'),
    ('singapore',      '🇸🇬', 'Singapore',      'Open ~19.8%'),
    ('south-korea',    '🇰🇷', 'South Korea',    'Open ~18.3%'),
    ('thailand',       '🇹🇭', 'Thailand',       'Open ~15.5%'),
    ('vietnam',        '🇻🇳', 'Vietnam',        'Open ~15.1%'),
    ('argentina',      '🇦🇷', 'Argentina',      'Open ~17.6%'),
    ('brazil',         '🇧🇷', 'Brazil',         'Open ~17.6%'),
    ('mexico',         '🇲🇽', 'Mexico',         'Open ~17.6%'),
    ('bahrain',        '🇧🇭', 'Bahrain',        'Open ~17.2%'),
    ('qatar',          '🇶🇦', 'Qatar',          'Open ~17.6%'),
    ('saudi-arabia',   '🇸🇦', 'Saudi Arabia',   'Open ~17.6%'),
    ('uae',            '🇦🇪', 'UAE',            'Open ~18.3%'),
]

FAQS = {
    'high': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email open rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email open rate in {display} is around {open_approx} across all industries. {display} has a mature email marketing culture with high inbox engagement. Healthcare, Education, Non-Profit, and Finance consistently see above-average open rates. Dating and Crypto see lower open rates due to subscriber fatigue. Note that open rates are inflated by Apple\'s Mail Privacy Protection (MPP) — click rate is a more reliable engagement signal.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email click rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email click rate (clicks ÷ delivered emails) in {display} is around 2.6–3.0%. Food &amp; Beverage, Travel, Flights, Restaurants, and Retail consistently see the highest click rates because their content is deal-driven and visual. Click-to-open rate (CTOR) is often more meaningful — divide your click rate by your open rate to see what share of openers actually click. A CTOR below 10% usually signals weak call-to-action placement or irrelevant content for the audience.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good unsubscribe rate for email in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email unsubscribe rate in {display} is around 0.16–0.20% per send. Anything above 0.5% is a strong signal that you are either sending too frequently, your content is not relevant, or your list health is poor. In {display}, subscribers have high expectations for email relevance — segment your list and send targeted content rather than batch-and-blast campaigns. An unsubscribe spike after a specific campaign is a useful diagnostic: it usually points to the offer, tone, or audience mismatch.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email bounce rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email bounce rate in {display} is around 0.50–0.65% (hard + soft combined). A hard bounce rate above 2% is a serious list health problem and will damage your sender reputation. In {display}, maintain a clean list by removing hard bounces immediately and running regular list hygiene checks. Use double opt-in for new subscribers to reduce bounce rates — it typically cuts hard bounces by 50–70% versus single opt-in.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How do email benchmarks in {display} compare to other markets in {region}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>{display} sits at the higher end of email engagement in {region} — open rates and click rates tend to be above regional averages. The high email adoption rate reflects a mature digital marketing environment with strong permission-based email cultures. Unsubscribe and bounce rates are lower than regional averages, reflecting better list management practices and subscriber quality among {display} marketers.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} email marketing benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on email platform, list quality, send frequency, content relevance, and subject line quality.</p>\n'
         '          </div>\n'
         '        </details>'),
    ],
    'mid': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email open rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email open rate in {display} is around {open_approx} across all industries. {display} has a moderate email engagement environment — open rates are competitive with global averages. Healthcare, Education, Finance, and Non-Profit industries see the highest open rates. Note that Apple\'s Mail Privacy Protection (MPP) inflates open rate figures — click rate is the more reliable engagement metric for {display} campaigns.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email click rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email click rate in {display} is around 2.3–2.8% (clicks ÷ delivered). Travel, Food &amp; Beverage, Flights, and Retail categories see the strongest click rates with deal-driven, visual content. Improve click rates by placing your CTA above the fold, using a single primary CTA per email, and personalising the content to subscriber behaviour. Click-to-open rate (CTOR) above 15% indicates strong email-content alignment for your {display} audience.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good unsubscribe rate for email in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email unsubscribe rate in {display} is around 0.19–0.22% per send. An unsubscribe rate above 0.5% per campaign is a warning sign. Common causes in {display} are excessive send frequency, irrelevant content, or purchased lists. Segment your audience and send targeted campaigns rather than sending the same email to your entire list — segmented sends typically reduce unsubscribes by 30–50% while improving open and click rates.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good bounce rate for email campaigns in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email bounce rate in {display} is around 0.60–0.72% (hard + soft combined). Anything above 2% hard bounce rate is a significant sender reputation risk. Remove all hard bounces immediately after each send. For {display} campaigns, list hygiene matters — re-engagement campaigns for inactive subscribers and double opt-in for new sign-ups will keep your bounce rate well below benchmark thresholds.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Which email platform is best for {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The main email platforms used in {display} are Klaviyo (eCommerce), Mailchimp (small business), HubSpot (B2B/CRM), ActiveCampaign (automation), and Campaign Monitor. For eCommerce merchants in {display}, Klaviyo integrates directly with Shopify and delivers the most sophisticated segmentation. B2B businesses typically benefit most from HubSpot or ActiveCampaign for CRM-integrated email workflows. All platforms support local currency and {display} timezone scheduling for optimal send-time optimisation.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} email benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on email platform, list quality, send frequency, content relevance, and subject line quality.</p>\n'
         '          </div>\n'
         '        </details>'),
    ],
    'emerging': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good email open rate in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email open rate in {display} is around {open_approx} across all industries — lower than mature markets like the USA or Germany. This reflects a combination of less established permission-based email culture, higher spam filtering rates, and lower Apple device penetration (which inflates open rates via Mail Privacy Protection). Click rate is a more reliable engagement metric in {region} because it is not affected by MPP inflation.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Why are email open rates lower in {display} than in the USA or UK?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Email open rates in {display} are lower for several reasons: higher spam filter aggressiveness in local ISPs, lower Apple Mail usage (so less MPP inflation), busier inboxes due to less permission-based email culture, and less email marketing sophistication in local senders meaning recipients receive more irrelevant emails. Improve {display} open rates with localised subject lines, sending at {region} peak engagement times, and building a double-opted-in list rather than purchasing contacts.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good click rate for email in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email click rate in {display} is around 2.0–2.4% (clicks ÷ delivered). Given that open rates in {region} can be unreliable due to lower Apple device penetration, click rate is the most actionable metric to track — it is not affected by Mail Privacy Protection inflation. A click rate above 3% is a strong result for {display} campaigns. Mobile optimisation is critical — the majority of email opens in {region} occur on mobile devices.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good unsubscribe rate for email in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average email unsubscribe rate in {display} is around 0.22–0.28% per send — slightly above mature market averages. This often reflects less established list permission practices in {region}. High unsubscribes in {display} are typically a sign of purchased or scraped lists, irrelevant content, or sending to contacts who did not actively opt in. Using double opt-in and cleaning inactive subscribers every 6 months will bring unsubscribe rates down significantly.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Which email platform is best for {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>For eCommerce businesses in {display}, Klaviyo is the strongest option for Shopify integration and revenue-based segmentation. Mailchimp and Brevo (formerly Sendinblue) offer good value for small-to-medium businesses in {region}. For B2B, HubSpot and ActiveCampaign provide CRM-integrated email workflows. Ensure your chosen platform supports {region} timezone optimisation and has good deliverability in {display} — some platforms have stronger local ISP relationships than others.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} email benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on email platform, list quality, send frequency, content relevance, and subject line quality.</p>\n'
         '          </div>\n'
         '        </details>'),
    ],
}

# ── Shared HTML blocks ────────────────────────────────────────────────────────

def nav(prefix):
    return f'''  <header class="nav-wrapper">
    <nav class="nav container">
      <a href="{prefix}" class="logo">
        <img src="{prefix}XYZLab.gif" alt="XYZ Lab" class="logo-img" />
      </a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links">
        <li class="nav-has-dropdown">
          <a href="{prefix}#courses">Courses <span class="nav-caret" aria-hidden="true"></span></a>
          <ul class="nav-dropdown">
            <li><a href="{prefix}google-ads-course/">AI for Google Ads</a></li>
            <li><a href="{prefix}meta-ads-course/">AI for Meta Ads</a></li>
            <li><a href="{prefix}seo-aio-course/">AI for SEO</a></li>
            <li><a href="{prefix}ai-marketing-analytics-course/">AI for Marketing Analytics</a></li>
            <li><a href="{prefix}ai-content-creation-course/">AI Content Creation</a></li>
            <li><a href="{prefix}vibe-coding-course/">Vibe Coding with AI</a></li>
          </ul>
        </li>
        <li class="nav-has-dropdown">
          <a href="{prefix}#topics">Tutorials <span class="nav-caret" aria-hidden="true"></span></a>
          <div class="nav-dropdown nav-mega">
            <div class="mega-col"><span class="mega-label">PPC</span><ul>
                <li><a href="{prefix}google-ads/">Google Ads</a></li>
                <li><a href="{prefix}google-ads-editor/">Google Ads Editor</a></li>
                <li><a href="{prefix}meta-ads/">Meta Ads</a></li>
                <li><a href="{prefix}tiktok-ads/">TikTok Ads</a></li>
                <li><a href="{prefix}microsoft-ads/">Microsoft Ads</a></li>
                <li><a href="{prefix}pinterest-ads/">Pinterest Ads</a></li>
                <li><a href="{prefix}reddit-ads/">Reddit Ads</a></li>
                <li><a href="{prefix}linkedin-ads/">LinkedIn Ads</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">Analytics</span><ul>
                <li><a href="{prefix}google-analytics/">Google Analytics</a></li>
                <li><a href="{prefix}google-tag-manager/">Google Tag Manager</a></li>
                <li><a href="{prefix}data-studio/">Data Studio</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">SEO</span><ul>
                <li><a href="{prefix}google-search-console/">Google Search Console</a></li>
                <li><a href="{prefix}bing-webmaster-tools/">Bing Webmaster Tools</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">AI Tools</span><ul>
                <li><a href="{prefix}claude/">Claude AI</a></li>
                <li><a href="{prefix}chatgpt/">ChatGPT</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">eCommerce</span><ul>
                <li><a href="{prefix}shopify/">Shopify</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">Web Builders</span><ul>
                <li><a href="{prefix}wix/">Wix</a></li><li><a href="{prefix}go-high-level/">Go High Level</a></li><li><a href="{prefix}godaddy/">GoDaddy</a></li>
            </ul></div>
            <div class="mega-col"><span class="mega-label">Social Media</span><ul>
                <li><a href="{prefix}linkedin/">LinkedIn</a></li>
                <li><a href="{prefix}youtube/">YouTube</a></li>
            </ul></div>
          </div>
        </li>        <li><a href="{prefix}#contact">Contact</a></li>
        <li class="nav-has-dropdown">
          <a href="#">Benchmarks <span class="nav-caret" aria-hidden="true"></span></a>
          <ul class="nav-dropdown">
            <li><a href="/meta-ads/benchmarks/">Meta Ads Benchmarks</a></li>
            <li><a href="/google-ads/benchmarks/">Google Ads Benchmarks</a></li>
            <li><a href="/seo/benchmarks/">SEO Benchmarks</a></li>
            <li><a href="/tiktok-ads/benchmarks/">TikTok Ads Benchmarks</a></li>
            <li><a href="/linkedin-ads/benchmarks/">LinkedIn Ads Benchmarks</a></li>
            <li><a href="/reddit-ads/benchmarks/">Reddit Ads Benchmarks</a></li>
            <li><a href="/shopify/benchmarks/">Shopify Benchmarks</a></li>
          <li><a href="/email-marketing/benchmarks/">Email Marketing Benchmarks</a></li>
          </ul>
        </li>
        <li><a href="#coaching" class="btn btn-primary btn-sm">Book Coaching</a></li>
      </ul>
    </nav>
  </header>'''

def footer(prefix):
    return f'''  <footer class="footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <p>Hands-On, AI-First Digital Marketing Training. Work Smarter with AI.</p>
        <div class="footer-socials">
          <a href="https://www.linkedin.com/in/seridis/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          </a>
          <a href="https://www.youtube.com/@xyzl" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58 2.78 2.78 0 0 0 1.95 1.96C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.96-1.96A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white"/></svg>
          </a>
        </div>
      </div>
      <div class="footer-links">
        <div class="footer-col"><h4>Courses</h4><ul>
            <li><a href="{prefix}google-ads-course/">AI for Google Ads</a></li>
            <li><a href="{prefix}meta-ads-course/">AI for Meta Ads</a></li>
            <li><a href="{prefix}seo-aio-course/">AI for SEO</a></li>
            <li><a href="{prefix}ai-marketing-analytics-course/">Analytics</a></li>
            <li><a href="{prefix}ai-content-creation-course/">AI Content Creation</a></li>
            <li><a href="{prefix}vibe-coding-course/">Vibe Coding</a></li>
        </ul></div>
        <div class="footer-col"><h4>PPC</h4><ul>
            <li><a href="{prefix}google-ads/">Google Ads</a></li>
            <li><a href="{prefix}google-ads-editor/">Google Ads Editor</a></li>
            <li><a href="{prefix}meta-ads/">Meta Ads</a></li>
            <li><a href="{prefix}tiktok-ads/">TikTok Ads</a></li>
            <li><a href="{prefix}microsoft-ads/">Microsoft Ads</a></li>
            <li><a href="{prefix}pinterest-ads/">Pinterest Ads</a></li>
            <li><a href="{prefix}reddit-ads/">Reddit Ads</a></li>
            <li><a href="{prefix}linkedin-ads/">LinkedIn Ads</a></li>
        </ul></div>
        <div class="footer-col"><h4>Analytics</h4><ul>
            <li><a href="{prefix}google-analytics/">Google Analytics</a></li>
            <li><a href="{prefix}google-tag-manager/">Google Tag Manager</a></li>
            <li><a href="{prefix}data-studio/">Data Studio</a></li>
        </ul></div>
        <div class="footer-col"><h4>AI Tools</h4><ul>
            <li><a href="{prefix}claude/">Claude AI</a></li>
            <li><a href="{prefix}chatgpt/">ChatGPT</a></li>
        </ul></div>
        <div class="footer-col"><h4>SEO</h4><ul>
            <li><a href="{prefix}google-search-console/">Google Search Console</a></li>
            <li><a href="{prefix}bing-webmaster-tools/">Bing Webmaster Tools</a></li>
        </ul></div>
        <div class="footer-col"><h4>Benchmarks</h4><ul>
            <li><a href="/meta-ads/benchmarks/">Meta Ads</a></li>
            <li><a href="/google-ads/benchmarks/">Google Ads</a></li>
            <li><a href="/seo/benchmarks/">SEO</a></li>
            <li><a href="/tiktok-ads/benchmarks/">TikTok Ads</a></li>
            <li><a href="/linkedin-ads/benchmarks/">LinkedIn Ads</a></li>
            <li><a href="/reddit-ads/benchmarks/">Reddit Ads</a></li>
            <li><a href="/shopify/benchmarks/">Shopify</a></li>
          <li><a href="/email-marketing/benchmarks/">Email Marketing</a></li>
        </ul></div>
        <div class="footer-col"><h4>eCommerce</h4><ul>
            <li><a href="{prefix}shopify/">Shopify</a></li>
        </ul></div>
        <div class="footer-col"><h4>Web Builders</h4><ul>
            <li><a href="{prefix}wix/">Wix</a></li><li><a href="{prefix}go-high-level/">Go High Level</a></li><li><a href="{prefix}godaddy/">GoDaddy</a></li>
        </ul></div>
        <div class="footer-col"><h4>Social Media</h4><ul>
            <li><a href="{prefix}linkedin/">LinkedIn</a></li>
            <li><a href="{prefix}youtube/">YouTube</a></li>
        </ul></div>
        <div class="footer-col"><h4>Company</h4><ul>
            <li><a href="{prefix}#contact">Contact</a></li>
            <li><a href="mailto:hello@xyzlab.com">hello@xyzlab.com</a></li>
            <li><a href="https://wa.me/6594260742">+65 9426 0742</a></li>
        </ul></div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <p>&copy; <span id="year"></span> XYZ Lab. All rights reserved.</p>
      </div>
    </div>
  </footer>'''

GTM_HEAD = '''  <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WXGTNNN');</script>
<!-- End Google Tag Manager -->'''

GTM_BODY = '''  <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WXGTNNN"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->'''

TALLY = '''      <iframe data-tally-src="https://tally.so/embed/RGVaXv?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1" loading="lazy" width="100%" height="1" frameborder="0" marginheight="0" marginwidth="0" title="Book a 90-Minute Digital Marketing Coaching Session"></iframe>
      <script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){e.src=e.dataset.tallySrc}))};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}</script>'''

BM_STYLES = '''.bm-filters { display:flex; flex-wrap:wrap; gap:1rem; align-items:center; margin-bottom:1.5rem; }
.bm-filters select { padding:.6rem 1rem; border:1.5px solid #e2e8f0; border-radius:8px; font-family:inherit; font-size:.95rem; font-weight:500; background:#fff; color:#1a202c; cursor:pointer; min-width:180px; }
.bm-filters select:focus { outline:none; border-color:var(--primary); box-shadow:0 0 0 3px rgba(8,191,173,.12); }
#bm-country-wrap { display:none; }
.bm-actions { display:flex; flex-wrap:wrap; gap:.75rem; margin-bottom:1.5rem; }
.bm-actions button { padding:.55rem 1.1rem; border:1.5px solid var(--primary); border-radius:8px; font-family:inherit; font-size:.875rem; font-weight:600; cursor:pointer; transition:all .18s; }
.btn-copy { background:#fff; color:var(--primary); }
.btn-copy:hover { background:var(--primary); color:#fff; }
.btn-dl { background:var(--primary); color:#fff; }
.btn-dl:hover { background:#07a99a; }
.bm-wrap { overflow-x:auto; border:1px solid #e2e8f0; border-radius:12px; }
.bm-table { width:100%; border-collapse:collapse; font-size:.875rem; white-space:nowrap; }
.bm-table thead th { position:sticky; top:0; background:#f8fafc; padding:.75rem 1rem; text-align:left; font-size:.78rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em; color:#64748b; border-bottom:2px solid #e2e8f0; }
.bm-table thead th:not(.col-ind) { text-align:right; }
.bm-table td { padding:.65rem 1rem; border-bottom:1px solid #f1f5f9; color:#374151; }
.bm-table td:not(.col-ind) { text-align:right; font-variant-numeric:tabular-nums; }
.bm-table tbody tr:last-child td { border-bottom:none; }
.bm-table tbody tr:hover { background:#f8fafc; }
.bm-table tbody tr.bm-hi { background:#f0fdfb !important; }
.bm-table tbody tr.bm-hi td:first-child { font-weight:700; color:var(--primary); border-left:3px solid var(--primary); }
.col-ind { min-width:220px; white-space:normal; }
.col-curr { font-size:.7rem; font-weight:500; color:#94a3b8; display:block; }
.bm-meta { font-size:.8rem; color:#94a3b8; margin-bottom:1rem; }
.bm-note { margin-top:1.5rem; padding:1rem 1.25rem; background:#f8fafc; border-left:3px solid var(--primary); border-radius:0 8px 8px 0; font-size:.85rem; color:#64748b; }
@media(max-width:640px){.bm-filters select{min-width:140px;} .col-ind{min-width:160px;}}
.bm-blurred td { filter:blur(5px); user-select:none; pointer-events:none; }
.bm-gate-wrap { position:relative; }
.bm-paywall { display:none; flex-direction:column; align-items:center; margin-top:1.25rem; background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:12px; padding:2.25rem 1.5rem; text-align:center; }
.bm-paywall-box { text-align:center; max-width:460px; }
.bm-paywall-box h3 { font-size:1.25rem; font-weight:800; color:#1a202c; margin:0 0 .5rem; }
.bm-paywall-box p  { font-size:.9rem; color:#64748b; margin:0 0 1rem; }
.bm-perks { list-style:none; padding:0; margin:0 0 1.25rem; text-align:left; display:inline-block; }
.bm-perks li { font-size:.875rem; color:#374151; padding:.2rem 0; }
.bm-perks li::before { content:'\\2713 '; color:var(--primary); font-weight:700; }
.bm-unlock-btn { display:inline-block; padding:.75rem 2rem; font-size:1rem; font-weight:700; border-radius:8px; background:var(--primary); color:#fff !important; text-decoration:none; transition:background .18s; }
.bm-unlock-btn:hover { background:#07a99a; }
.bm-already-paid { margin-top:.85rem; font-size:.8rem; color:#94a3b8; }
.bm-already-paid a { color:var(--primary); text-decoration:underline; }
#bm-copy:disabled, #bm-download:disabled { opacity:.4; cursor:not-allowed; }
.bm-btn-tip-wrap { position:relative; display:inline-block; }
.bm-btn-tip { visibility:hidden; opacity:0; position:absolute; bottom:calc(100% + 8px); left:50%; transform:translateX(-50%); background:#1e293b; color:#fff; padding:.45rem .9rem; border-radius:6px; white-space:nowrap; font-size:.8rem; font-weight:500; transition:opacity .15s; z-index:200; pointer-events:none; }
.bm-btn-tip::before { content:''; position:absolute; bottom:-8px; left:-10px; right:-10px; height:8px; }
.bm-btn-tip::after { content:''; position:absolute; top:100%; left:50%; transform:translateX(-50%); border:5px solid transparent; border-top-color:#1e293b; }
.bm-btn-tip-wrap:hover .bm-btn-tip { visibility:visible; opacity:1; pointer-events:auto; }
.bm-btn-tip a { color:var(--secondary); font-weight:700; text-decoration:none; }
.bm-btn-tip a:hover { text-decoration:underline; }
.bm-success { display:none; align-items:center; gap:1rem; background:#f0fdfb; border:1.5px solid var(--primary); border-radius:10px; padding:1rem 1.25rem; margin-bottom:1.5rem; transition:opacity .7s ease; }
.bm-success-icon { flex-shrink:0; width:36px; height:36px; background:var(--primary); border-radius:50%; display:flex; align-items:center; justify-content:center; }
.bm-success-icon svg { display:block; }
.bm-success strong { display:block; color:#0f766e; font-size:.95rem; margin-bottom:.2rem; }
.bm-success p { margin:0; font-size:.82rem; color:#64748b; }'''

# ── PILLAR PAGE ───────────────────────────────────────────────────────────────

def make_card(slug, flag, name, sub):
    return (f'            <a href="{slug}/" class="bm-country-card">\n'
            f'              <span class="bm-country-flag">{flag}</span>\n'
            f'              <span class="bm-country-info"><span class="bm-country-name">{name}</span>'
            f'<span class="bm-country-curr">{sub}</span></span>\n'
            f'            </a>')

def region_block(label, cards):
    return (f'        <div>\n'
            f'          <p class="bm-region-label">{label}</p>\n'
            f'          <div class="bm-country-grid">\n'
            + '\n'.join(make_card(*c) for c in cards) +
            f'\n          </div>\n        </div>')

regions = [
    ('English-Speaking Markets', COUNTRY_CARDS_DISPLAY[0:7]),
    ('Europe',                   COUNTRY_CARDS_DISPLAY[7:18]),
    ('Asia Pacific',             COUNTRY_CARDS_DISPLAY[18:28]),
    ('Americas',                 COUNTRY_CARDS_DISPLAY[28:31]),
    ('Middle East',              COUNTRY_CARDS_DISPLAY[31:35]),
]
country_grid = '\n\n'.join(region_block(lbl, cards) for lbl, cards in regions)

pillar = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="google-adsense-account" content="ca-pub-5220550180754289">
{GTM_HEAD}
  <link rel="icon" type="image/png" href="../../favicon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Email marketing benchmarks by country and industry — open rate, click rate, unsubscribe rate and bounce rate for 35 countries. Select your country to view localised benchmark data." />
  <link rel="canonical" href="https://xyzlab.com/email-marketing/benchmarks/" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://xyzlab.com/email-marketing/benchmarks/" />
  <meta property="og:title" content="Email Marketing Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab" />
  <meta property="og:description" content="Email marketing benchmarks by country and industry — open rate, click rate, unsubscribe rate and bounce rate for 35 countries." />
  <meta property="og:image" content="https://xyzlab.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Email Marketing Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab" />
  <meta name="twitter:description" content="Email marketing benchmarks by country and industry — open rate, click rate, unsubscribe rate and bounce rate for 35 countries." />
  <meta name="twitter:image" content="https://xyzlab.com/og-image.jpg" />
  <title>Email Marketing Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../style.css" />
  <link rel="stylesheet" href="../../course.css" />
  <style>
.bm-pillar-intro {{ max-width:720px; margin:0 auto 3rem; text-align:center; }}
.bm-regions {{ display:flex; flex-direction:column; gap:2.5rem; }}
.bm-region-label {{ font-size:.75rem; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:#94a3b8; margin:0 0 1rem; }}
.bm-country-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr)); gap:.75rem; }}
.bm-country-card {{ display:flex; align-items:center; gap:.75rem; padding:.85rem 1rem; background:#fff; border:1.5px solid #e2e8f0; border-radius:10px; text-decoration:none; transition:border-color .18s,box-shadow .18s; }}
.bm-country-card:hover {{ border-color:var(--primary); box-shadow:0 4px 16px rgba(8,191,173,.1); }}
.bm-country-flag {{ font-size:1.5rem; line-height:1; flex-shrink:0; }}
.bm-country-info {{ display:flex; flex-direction:column; gap:.1rem; }}
.bm-country-name {{ font-size:.9rem; font-weight:700; color:#1a202c; }}
.bm-country-curr {{ font-size:.75rem; color:#94a3b8; font-weight:500; }}
.bm-what {{ background:#f8fafc; border-radius:16px; padding:2.5rem; margin-top:3rem; }}
.bm-what h3 {{ font-size:1.2rem; font-weight:800; color:#1a202c; margin:0 0 .75rem; }}
.bm-what p {{ font-size:.92rem; color:#64748b; line-height:1.7; margin:0 0 .75rem; }}
.bm-what p:last-child {{ margin:0; }}
.bm-metrics {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:1rem; margin-top:2rem; }}
.bm-metric {{ background:#fff; border:1.5px solid #e2e8f0; border-radius:10px; padding:1rem 1.25rem; }}
.bm-metric-label {{ font-size:.7rem; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:#94a3b8; margin:0 0 .3rem; }}
.bm-metric-name {{ font-size:.9rem; font-weight:700; color:#1a202c; }}
.bm-metric-desc {{ font-size:.78rem; color:#64748b; margin:.2rem 0 0; line-height:1.5; }}
@media(max-width:640px){{ .bm-country-grid{{grid-template-columns:1fr 1fr;}} .bm-metrics{{grid-template-columns:1fr 1fr;}} }}
  </style>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "Email Marketing Benchmarks by Country and Industry (Q2 2026)",
    "description": "Email marketing open rate, click rate, unsubscribe rate and bounce rate benchmarks for 35 countries and 38 industries. Q2 2026 industry aggregates.",
    "publisher": {{ "@type": "Organization", "name": "XYZ Lab", "url": "https://xyzlab.com" }},
    "url": "https://xyzlab.com/email-marketing/benchmarks/",
    "keywords": ["email marketing benchmarks", "email open rate benchmarks", "email click rate benchmarks", "email unsubscribe rate benchmarks"]
  }}
  </script>
</head>
<body>
{GTM_BODY}

{nav("../../")}

  <section class="video-tutorial-hero">
    <div class="container tutorial-hero-inner">
      <nav class="breadcrumb">
        <a href="../../">Home</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <span class="breadcrumb-current">Email Marketing Benchmarks</span>
      </nav>
      <h1>Email Marketing <span class="highlight">Benchmarks</span> by Country &amp; Industry</h1>
      <p class="hero-sub">Average email marketing open rate, click rate, unsubscribe rate and bounce rate across 38 industries for 35 countries. Select your country below.</p>
      <div style="margin-top:1.75rem;">
        <a href="#countries" class="btn btn-primary">Select Your Country</a>
        <a href="#coaching" class="btn btn-outline">Book Coaching</a>
      </div>
    </div>
  </section>

  <section class="outcomes" id="countries">
    <div class="container">
      <div class="section-header">
        <div class="badge badge-secondary">Q2 2026</div>
        <h2>Select Your <span class="highlight">Country</span></h2>
        <p>38 industries &bull; Open Rate &bull; Click Rate &bull; Unsubscribe Rate &bull; Bounce Rate</p>
      </div>
      <div class="bm-regions">
{country_grid}
      </div>
      <div class="bm-what">
        <h3>What are email marketing benchmarks?</h3>
        <p>Email marketing benchmarks are industry median performance figures — open rate, click rate, unsubscribe rate and bounce rate — aggregated across email campaigns and newsletters. They give you a reference point to evaluate whether your email programme is performing above, at, or below industry norms in your market.</p>
        <p>All benchmarks are country-adjusted for local email adoption, inbox culture and platform mix. Open rates are measured by pixel and click-inferred opens — note that Apple's Mail Privacy Protection (MPP) artificially inflates open rates. Click rate is the more reliable engagement signal as it is unaffected by MPP.</p>
        <div class="bm-metrics">
          <div class="bm-metric"><p class="bm-metric-label">Open Rate</p><p class="bm-metric-name">Email Open Rate</p><p class="bm-metric-desc">Opens ÷ delivered. Inflated by Apple MPP — use click rate for accuracy.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">Click Rate</p><p class="bm-metric-name">Email Click Rate</p><p class="bm-metric-desc">Clicks ÷ delivered. The most reliable engagement metric for email.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">Unsub Rate</p><p class="bm-metric-name">Unsubscribe Rate</p><p class="bm-metric-desc">Unsubscribes ÷ delivered. Below 0.2% per send is healthy.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">Bounce Rate</p><p class="bm-metric-name">Bounce Rate</p><p class="bm-metric-desc">Hard + soft bounces ÷ sent. Keep hard bounces below 2%.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="coaching-cta">
    <div class="container">
      <div class="coaching-cta-inner">
        <div class="coaching-cta-text">
          <h3>Need 1-on-1 help with Email Marketing?</h3>
          <p>Book a 90-minute coaching session and we'll review your email programme and benchmarks together!</p>
        </div>
        <a href="#coaching" class="btn btn-primary">Book a Coaching Session</a>
      </div>
    </div>
  </section>

  <section class="faq" id="faq">
    <div class="container">
      <div class="section-header">
        <div class="badge">FAQ</div>
        <h2>Frequently Asked Questions</h2>
        <p>Common questions about email marketing benchmarks.</p>
      </div>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question"><span>Why are email open rates different by country?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>Email open rates vary by country due to differences in email culture, device mix, and Apple Mail adoption. Countries with high Apple iPhone penetration (USA, Australia, UK) see artificially inflated open rates due to Mail Privacy Protection (MPP), which pre-loads email pixels regardless of whether the email was actually read. Emerging markets with lower Apple device penetration show more accurate but lower open rates. Click rate is universally the most reliable engagement metric because it is unaffected by MPP.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>What is Apple Mail Privacy Protection and how does it affect benchmarks?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>Apple's Mail Privacy Protection (MPP), launched with iOS 15 in 2021, pre-downloads email content including tracking pixels when an email arrives — regardless of whether the subscriber opens it. This means any email sent to an Apple Mail user on iPhone or Mac will register as "opened" even if it was never read. In markets with high Apple device penetration (USA, UK, Australia, Canada), open rates can be 5–15 percentage points higher than actual engagement. Use click rate and revenue-per-email as your primary performance signals.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>How do email benchmarks differ by country?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>Email engagement varies significantly by country due to Apple device penetration (affects open rates), email culture maturity (affects list permission quality), local spam filtering standards, and typical send volumes. Northern European markets (Germany, Denmark, Norway, Sweden) have high open rates and low unsubscribes — they have strong permission-based email cultures. Emerging markets (Indonesia, Vietnam, Philippines) show lower open rates but are less affected by MPP inflation, making their click rates a more accurate signal.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>How often are these email marketing benchmarks updated?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on email platform, list quality, send frequency, content relevance, and subject line quality.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="coaching-section" id="coaching">
    <div class="container coaching-inner">
      <div class="section-header">
        <div class="badge badge-secondary">Get Personal Help</div>
        <h2>Book a <span class="highlight">1-on-1 Coaching Session</span></h2>
        <p>Need a hands-on walkthrough tailored to your account? Book a 90-minute coaching session and we'll set it up together.</p>
      </div>
{TALLY}
    </div>
  </section>

{footer("../../")}

  <script src="../../main.js"></script>
</body>
</html>'''

os.makedirs(PILLAR, exist_ok=True)
with open(os.path.join(PILLAR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(pillar)
print('  wrote email-marketing/benchmarks/index.html')

# ── COUNTRY PAGES ─────────────────────────────────────────────────────────────

COUNTRY_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="google-adsense-account" content="ca-pub-5220550180754289">
  <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-WXGTNNN');</script>
<!-- End Google Tag Manager -->
  <link rel="icon" type="image/png" href="../../../favicon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Email marketing benchmarks for {display} — average open rate, click rate, unsubscribe rate and bounce rate across 38 industries. Q2 2026 data." />
  <link rel="canonical" href="https://xyzlab.com/email-marketing/benchmarks/{slug}/" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://xyzlab.com/email-marketing/benchmarks/{slug}/" />
  <meta property="og:title" content="Email Marketing Benchmarks {display} (Q2 2026) — Open Rate, Click Rate by Industry | XYZ Lab" />
  <meta property="og:description" content="Email marketing benchmarks for {display} — average open rate, click rate, unsubscribe rate and bounce rate across 38 industries. Q2 2026 data." />
  <meta property="og:image" content="https://xyzlab.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Email Marketing Benchmarks {display} (Q2 2026) — Open Rate, Click Rate by Industry | XYZ Lab" />
  <meta name="twitter:description" content="Email marketing benchmarks for {display} — average open rate, click rate, unsubscribe rate and bounce rate across 38 industries. Q2 2026 data." />
  <meta name="twitter:image" content="https://xyzlab.com/og-image.jpg" />
  <title>Email Marketing Benchmarks {display} (Q2 2026) — Open Rate, Click Rate by Industry | XYZ Lab</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../../style.css" />
  <link rel="stylesheet" href="../../../course.css" />
  <style>
{styles}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
  <script>
    window.BENCHMARK_COUNTRY    = '{bm_country}';
    window.BENCHMARK_STATIC_URL = true;
    window.BENCHMARK_STATIC_H1  = true;
    window.BENCHMARK_GATE = {{
      storageKey:   'bm_email_unlocked',
      stripeUrl:    'https://buy.stripe.com/4gMcN6cdz5IG2GH0Kk3Je0d',
      price:        '$9.99',
      supportEmail: 'hello@xyzlab.com'
    }};
  </script>
  <script src="../../../benchmarks/email-marketing-data.js"></script>
  <script src="../../../benchmarks/benchmarks.js"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "Email Marketing Benchmarks — {display} (Q2 2026)",
    "description": "Email marketing open rate, click rate, unsubscribe rate and bounce rate for 38 industries in {display}. Q2 2026 industry aggregates.",
    "publisher": {{ "@type": "Organization", "name": "XYZ Lab", "url": "https://xyzlab.com" }},
    "url": "https://xyzlab.com/email-marketing/benchmarks/{slug}/",
    "keywords": ["email marketing benchmarks {display}", "email open rate {display}", "email click rate {display}", "email unsubscribe rate {display}"]
  }}
  </script>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WXGTNNN"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

{nav_html}

  <section class="video-tutorial-hero">
    <div class="container tutorial-hero-inner">
      <nav class="breadcrumb">
        <a href="../../../">Home</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <a href="../">Email Marketing Benchmarks</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <span class="breadcrumb-current">{display}</span>
      </nav>
      <h1 id="bm-h1">Email Marketing Benchmarks in <span class="highlight">{display}</span></h1>
      <p class="hero-sub" id="bm-sub">Average email marketing performance in {display} across all industries. Open rate, click rate, unsubscribe rate and bounce rate.</p>
      <div style="margin-top:1.75rem;">
        <a href="#benchmarks" class="btn btn-primary">View Benchmarks</a>
        <a href="#coaching" class="btn btn-outline">Book Coaching</a>
      </div>
    </div>
  </section>

  <section class="outcomes" id="benchmarks">
    <div class="container">
      <div class="section-header">
        <div class="badge badge-secondary">{flag} {display} — Q2 2026</div>
        <h2>Email Marketing Benchmarks — <span class="highlight">{display}</span></h2>
        <p>Select an industry to highlight it in the table. All metrics are percentages.</p>
      </div>
      <div class="bm-filters">
        <div id="bm-country-wrap">
          <label for="bm-country" style="display:block;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#64748b;margin-bottom:.35rem;">Country</label>
          <select id="bm-country"></select>
        </div>
        <div>
          <label for="bm-industry" style="display:block;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#64748b;margin-bottom:.35rem;">Industry</label>
          <select id="bm-industry"></select>
        </div>
      </div>
      <div id="bm-success" class="bm-success">
        <div class="bm-success-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div><strong>Payment confirmed — your download is starting now</strong><p>A ZIP file with all 35 countries is downloading. The full table is now unlocked below.</p></div>
      </div>
      <div class="bm-actions">
        <button id="bm-copy" class="btn-copy">Copy Table</button>
        <button id="bm-download" class="btn-dl">&#8595; Download All Countries (ZIP)</button>
      </div>
      <p class="bm-meta"><span id="bm-count"></span> industries shown &nbsp;&bull;&nbsp; Source: XYZ Lab industry aggregates &nbsp;&bull;&nbsp; <span id="bm-updated">Q2 2026</span></p>
      <div class="bm-gate-wrap">
        <div class="bm-wrap">
          <table class="bm-table"><thead id="bm-thead"></thead><tbody id="bm-tbody"></tbody></table>
        </div>
      </div>
      <div id="bm-paywall" class="bm-paywall">
        <div class="bm-paywall-box">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="none" style="margin:0 auto .75rem;display:block;"><rect x="3" y="11" width="18" height="11" rx="2" stroke="#08bfad" stroke-width="1.8"/><path d="M7 11V7a5 5 0 0 1 10 0v4" stroke="#08bfad" stroke-width="1.8" stroke-linecap="round"/></svg>
          <h3>Unlock All 38 Industries</h3>
          <p>8 of 38 industries shown above. Unlock the full table + instant ZIP download for all 35 countries.</p>
          <ul class="bm-perks">
            <li>All 38 industries — full table unlocked</li>
            <li>35 countries in one ZIP download</li>
            <li>Open Rate, Click Rate, Unsubscribe Rate &amp; Bounce Rate</li>
            <li>Instant ZIP download — all countries in one file</li>
            <li>Copy table to paste into Google Sheets or Excel</li>
          </ul>
          <a href="https://buy.stripe.com/4gMcN6cdz5IG2GH0Kk3Je0d" class="bm-unlock-btn">Unlock for $9.99 &rarr;</a>
          <p class="bm-already-paid">Already paid but lost access? <a href="mailto:hello@xyzlab.com?subject=Email%20Marketing%20Benchmarks%20%E2%80%94%20Restore%20Access">Email us to restore</a></p>
        </div>
      </div>
      <div class="bm-note">
        <strong>Methodology:</strong> Benchmarks are industry aggregates compiled from anonymised campaign data and published industry reports (Q2 2026). Figures represent medians across promotional, newsletter and transactional email campaigns. Open rates are measured by pixel and click-inferred opens — Apple Mail Privacy Protection (MPP) inflates open rates in markets with high Apple device penetration. Click rate is the more reliable engagement signal for {display} campaigns. Unsubscribe and bounce rates represent per-send averages.
      </div>
    </div>
  </section>

  <section class="coaching-cta">
    <div class="container">
      <div class="coaching-cta-inner">
        <div class="coaching-cta-text">
          <h3>Need 1-on-1 help with Email Marketing in {display}?</h3>
          <p>Book a 90-minute coaching session and we\'ll review your email programme and {display} benchmarks together!</p>
        </div>
        <a href="#coaching" class="btn btn-primary">Book a Coaching Session</a>
      </div>
    </div>
  </section>

  <section class="faq" id="faq">
    <div class="container">
      <div class="section-header">
        <div class="badge">FAQ</div>
        <h2>Email Marketing Benchmarks — {display} FAQ</h2>
        <p>Common questions about email marketing performance in {display}.</p>
      </div>
      <div class="faq-list">
        {faq_block}
      </div>
    </div>
  </section>

  <section class="outcomes" style="background:var(--white);">
    <div class="container">
      <div class="section-header">
        <div class="badge badge-secondary">Keep Learning</div>
        <h2>Related <span class="highlight">Benchmarks</span></h2>
        <p>Compare email performance against other marketing channels in {display}.</p>
      </div>
      <div class="courses-grid">
        <article class="course-card">
          <a href="/email-marketing/benchmarks/" class="course-icon" tabindex="-1" style="background:#e8faf9;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#e8faf9"/><rect x="8" y="18" width="3" height="6" rx="1" fill="#08bfad"/><rect x="13" y="13" width="3" height="11" rx="1" fill="#08bfad" opacity=".7"/><rect x="18" y="9" width="3" height="15" rx="1" fill="#08bfad" opacity=".4"/><rect x="23" y="14" width="3" height="10" rx="1" fill="#08bfad"/></svg>
          </a>
          <h3><a href="/email-marketing/benchmarks/">Email Marketing Benchmarks by Country</a></h3>
          <ul class="course-bullets">
            <li>Compare benchmarks across 35 countries</li>
            <li>Open rate, click rate, unsubscribe &amp; bounce</li>
            <li>38 industries — select your vertical</li>
          </ul>
          <a href="/email-marketing/benchmarks/" class="course-link">View All Countries &#8594;</a>
        </article>
        <article class="course-card">
          <a href="/meta-ads/benchmarks/" class="course-icon" tabindex="-1" style="background:#fff3e0;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#fff3e0"/><rect x="7" y="18" width="4" height="7" rx="1" fill="#fec55c"/><rect x="14" y="12" width="4" height="13" rx="1" fill="#fec55c" opacity=".7"/><rect x="21" y="7" width="4" height="18" rx="1" fill="#fec55c" opacity=".4"/></svg>
          </a>
          <h3><a href="/meta-ads/benchmarks/">Meta Ads Benchmarks</a></h3>
          <ul class="course-bullets">
            <li>CPM, CPC and ROAS by industry</li>
            <li>35 countries in local currency</li>
            <li>Compare paid social vs email ROI</li>
          </ul>
          <a href="/meta-ads/benchmarks/" class="course-link">View Benchmarks &#8594;</a>
        </article>
        <article class="course-card">
          <a href="/google-ads/benchmarks/" class="course-icon" tabindex="-1" style="background:#e8faf9;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#e8faf9"/><circle cx="14" cy="14" r="6" stroke="#08bfad" stroke-width="1.8"/><path d="M19 19l4 4" stroke="#08bfad" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
          <h3><a href="/google-ads/benchmarks/">Google Ads Benchmarks</a></h3>
          <ul class="course-bullets">
            <li>CPC, CTR and ROAS by industry</li>
            <li>35 countries in local currency</li>
            <li>Compare search intent vs email engagement</li>
          </ul>
          <a href="/google-ads/benchmarks/" class="course-link">View Benchmarks &#8594;</a>
        </article>
      </div>
    </div>
  </section>

  <section class="coaching-section" id="coaching">
    <div class="container coaching-inner">
      <div class="section-header">
        <div class="badge badge-secondary">Get Personal Help</div>
        <h2>Book a <span class="highlight">1-on-1 Coaching Session</span></h2>
        <p>Need a hands-on walkthrough tailored to your account? Book a 90-minute coaching session and we\'ll set it up together.</p>
      </div>
      <iframe data-tally-src="https://tally.so/embed/RGVaXv?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1" loading="lazy" width="100%" height="1" frameborder="0" marginheight="0" marginwidth="0" title="Book a 90-Minute Digital Marketing Coaching Session"></iframe>
      <script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){{"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){{e.src=e.dataset.tallySrc}}))}};if("undefined"!=typeof Tally)v();else if(d.querySelector(\'script[src="\'+w+\'"]\')===null){{var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}}</script>
    </div>
  </section>

{footer_html}

  <script src="../../../main.js"></script>
</body>
</html>'''

nav_c    = nav('../../../')
footer_c = footer('../../../')

for (slug, bm_country, display, curr_str, curr_code, flag, open_approx, market_type, region) in COUNTRIES:
    faq_items = FAQS[market_type]
    faq_block = '\n\n        '.join(
        item.replace('{display}', display).replace('{open_approx}', open_approx)
            .replace('{code}', curr_code).replace('{region}', region)
        for item in faq_items
    )
    html = COUNTRY_PAGE.format(
        slug=slug, bm_country=bm_country, display=display,
        curr_str=curr_str, code=curr_code, flag=flag,
        faq_block=faq_block, styles=BM_STYLES,
        nav_html=nav_c, footer_html=footer_c,
    )
    out_dir = os.path.join(PILLAR, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  wrote email-marketing/benchmarks/{slug}/')

print(f'\nDone — 35 country pages + 1 pillar page')
