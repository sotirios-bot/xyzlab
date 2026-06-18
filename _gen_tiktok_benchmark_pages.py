#!/usr/bin/env python3
"""Generate TikTok Ads benchmark pages: pillar + 35 country pages."""
import os

BASE_DIR    = '/home/user/xyzlab'
PILLAR      = os.path.join(BASE_DIR, 'tiktok-ads/benchmarks')
CHANNEL     = 'TikTok Ads'
CHANNEL_DESC = 'In-Feed Video &amp; TopView'
DATA_FILE   = 'tiktok-ads-data.js'
STORAGE_KEY = 'bm_tiktok_unlocked'
STRIPE_URL  = 'https://buy.stripe.com/7sY5kEcdz0oma998cM3Je09'
# Metrics: CTR, CPC, CPM, CPV, Conv. Rate, CPA (no ROAS)
PERKS_METRICS = 'CTR, CPC, CPM, CPV, Conversion Rate &amp; CPA'

# (slug, bm_country, display, curr_str, curr_code, flag, cpc_approx, market_type, region)
# CPC approx = BASE_CPC(1.18) * cpcm
COUNTRIES = [
    ('argentina',     'Argentina',    'Argentina',      'ARS (AR$)',  'ARS', '🇦🇷', 'AR$486',   'emerging', 'Latin America'),
    ('australia',     'Australia',    'Australia',      'AUD (AU$)',  'AUD', '🇦🇺', 'AU$1.46',  'high',     'the Asia Pacific'),
    ('bahrain',       'Bahrain',      'Bahrain',        'BHD',        'BHD', '🇧🇭', 'BHD 0.20', 'mid',      'the Middle East'),
    ('brazil',        'Brazil',       'Brazil',         'BRL (R$)',   'BRL', '🇧🇷', 'R$1.83',   'emerging', 'Latin America'),
    ('canada',        'Canada',       'Canada',         'CAD (CA$)',  'CAD', '🇨🇦', 'CA$1.39',  'high',     'North America'),
    ('denmark',       'Denmark',      'Denmark',        'DKK',        'DKK', '🇩🇰', 'DKK 13.38','high',     'Europe'),
    ('france',        'France',       'France',         'EUR (€)',    'EUR', '🇫🇷', '€0.60',    'mid',      'Europe'),
    ('germany',       'Germany',      'Germany',        'EUR (€)',    'EUR', '🇩🇪', '€0.73',    'high',     'Europe'),
    ('hong-kong',     'Hong Kong',    'Hong Kong',      'HKD (HK$)', 'HKD', '🇭🇰', 'HK$5.08',  'mid',      'Asia Pacific'),
    ('india',         'India',        'India',          'INR (₹)',   'INR', '🇮🇳', '₹9.74',    'emerging', 'Asia Pacific'),
    ('indonesia',     'Indonesia',    'Indonesia',      'IDR (Rp)',  'IDR', '🇮🇩', 'Rp1,217',  'emerging', 'Asia Pacific'),
    ('ireland',       'Ireland',      'Ireland',        'EUR (€)',    'EUR', '🇮🇪', '€0.91',    'high',     'Europe'),
    ('italy',         'Italy',        'Italy',          'EUR (€)',    'EUR', '🇮🇹', '€0.46',    'mid',      'Europe'),
    ('japan',         'Japan',        'Japan',          'JPY (¥)',   'JPY', '🇯🇵', '¥84.96',   'mid',      'Asia Pacific'),
    ('malaysia',      'Malaysia',     'Malaysia',       'MYR (RM)', 'MYR', '🇲🇾', 'RM 2.43',  'emerging', 'Asia Pacific'),
    ('mexico',        'Mexico',       'Mexico',         'MXN (MX$)', 'MXN', '🇲🇽', 'MX$12.17', 'emerging', 'Latin America'),
    ('netherlands',   'Netherlands',  'Netherlands',    'EUR (€)',    'EUR', '🇳🇱', '€0.65',    'high',     'Europe'),
    ('new-zealand',   'New Zealand',  'New Zealand',    'NZD (NZ$)', 'NZD', '🇳🇿', 'NZ$1.32',  'high',     'the Asia Pacific'),
    ('norway',        'Norway',       'Norway',         'NOK',        'NOK', '🇳🇴', 'NOK 21.90','high',     'Europe'),
    ('philippines',   'Philippines',  'Philippines',    'PHP (₱)',   'PHP', '🇵🇭', '₱7.30',    'emerging', 'Asia Pacific'),
    ('poland',        'Poland',       'Poland',         'PLN (zł)',  'PLN', '🇵🇱', 'zł1.34',   'emerging', 'Europe'),
    ('qatar',         'Qatar',        'Qatar',          'QAR',        'QAR', '🇶🇦', 'QAR 2.49', 'mid',      'the Middle East'),
    ('saudi-arabia',  'Saudi Arabia', 'Saudi Arabia',   'SAR',        'SAR', '🇸🇦', 'SAR 2.30', 'mid',      'the Middle East'),
    ('singapore',     'Singapore',    'Singapore',      'SGD (S$)',  'SGD', '🇸🇬', 'S$0.99',   'high',     'Asia Pacific'),
    ('south-africa',  'South Africa', 'South Africa',   'ZAR (R)',   'ZAR', '🇿🇦', 'R6.08',    'emerging', 'Africa'),
    ('south-korea',   'South Korea',  'South Korea',    'KRW (₩)',   'KRW', '🇰🇷', '₩669',     'mid',      'Asia Pacific'),
    ('spain',         'Spain',        'Spain',          'EUR (€)',    'EUR', '🇪🇸', '€0.43',    'mid',      'Europe'),
    ('sweden',        'Sweden',       'Sweden',         'SEK',        'SEK', '🇸🇪', 'SEK 17.03','high',     'Europe'),
    ('switzerland',   'Switzerland',  'Switzerland',    'CHF',        'CHF', '🇨🇭', 'CHF 2.43', 'high',     'Europe'),
    ('thailand',      'Thailand',     'Thailand',       'THB (฿)',   'THB', '🇹🇭', '฿9.09',    'emerging', 'Asia Pacific'),
    ('turkiye',       'Turkiye',      'Türkiye',        'TRY (₺)',   'TRY', '🇹🇷', '₺6.80',    'emerging', 'Europe & the Middle East'),
    ('uae',           'UAE',          'UAE',            'AED',        'AED', '🇦🇪', 'AED 3.68', 'mid',      'the Middle East'),
    ('united-kingdom','UK',           'United Kingdom', 'GBP (£)',   'GBP', '🇬🇧', '£0.72',    'high',     'Europe'),
    ('united-states', 'USA',          'United States',  'USD ($)',   'USD', '🇺🇸', '$1.18',    'high',     'North America'),
    ('vietnam',       'Vietnam',      'Vietnam',        'VND (₫)',   'VND', '🇻🇳', '₫9,731',   'emerging', 'Asia Pacific'),
]

COUNTRY_CARDS = [
    ('australia',      '🇦🇺', 'Australia',     'AUD (AU$)'),
    ('canada',         '🇨🇦', 'Canada',         'CAD (CA$)'),
    ('ireland',        '🇮🇪', 'Ireland',        'EUR (€)'),
    ('new-zealand',    '🇳🇿', 'New Zealand',    'NZD (NZ$)'),
    ('south-africa',   '🇿🇦', 'South Africa',   'ZAR (R)'),
    ('united-kingdom', '🇬🇧', 'United Kingdom', 'GBP (£)'),
    ('united-states',  '🇺🇸', 'United States',  'USD ($)'),
    ('denmark',        '🇩🇰', 'Denmark',        'DKK'),
    ('france',         '🇫🇷', 'France',         'EUR (€)'),
    ('germany',        '🇩🇪', 'Germany',        'EUR (€)'),
    ('italy',          '🇮🇹', 'Italy',          'EUR (€)'),
    ('netherlands',    '🇳🇱', 'Netherlands',    'EUR (€)'),
    ('norway',         '🇳🇴', 'Norway',         'NOK'),
    ('poland',         '🇵🇱', 'Poland',         'PLN (zł)'),
    ('spain',          '🇪🇸', 'Spain',          'EUR (€)'),
    ('sweden',         '🇸🇪', 'Sweden',         'SEK'),
    ('switzerland',    '🇨🇭', 'Switzerland',    'CHF'),
    ('turkiye',        '🇹🇷', 'Türkiye',        'TRY (₺)'),
    ('hong-kong',      '🇭🇰', 'Hong Kong',      'HKD (HK$)'),
    ('india',          '🇮🇳', 'India',          'INR (₹)'),
    ('indonesia',      '🇮🇩', 'Indonesia',      'IDR (Rp)'),
    ('japan',          '🇯🇵', 'Japan',          'JPY (¥)'),
    ('malaysia',       '🇲🇾', 'Malaysia',       'MYR (RM)'),
    ('philippines',    '🇵🇭', 'Philippines',    'PHP (₱)'),
    ('singapore',      '🇸🇬', 'Singapore',      'SGD (S$)'),
    ('south-korea',    '🇰🇷', 'South Korea',    'KRW (₩)'),
    ('thailand',       '🇹🇭', 'Thailand',       'THB (฿)'),
    ('vietnam',        '🇻🇳', 'Vietnam',        'VND (₫)'),
    ('argentina',      '🇦🇷', 'Argentina',      'ARS (AR$)'),
    ('brazil',         '🇧🇷', 'Brazil',         'BRL (R$)'),
    ('mexico',         '🇲🇽', 'Mexico',         'MXN (MX$)'),
    ('bahrain',        '🇧🇭', 'Bahrain',        'BHD'),
    ('qatar',          '🇶🇦', 'Qatar',          'QAR'),
    ('saudi-arabia',   '🇸🇦', 'Saudi Arabia',   'SAR'),
    ('uae',            '🇦🇪', 'UAE',            'AED'),
]

FAQS = {
    'high': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPC for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average CPC for TikTok Ads in {display} is around {cpc} across all industries. {display} is a mature, competitive market — advertiser demand is high and consumer value per click drives up auction costs. Entertainment, beauty and gaming tend to see lower CPCs; legal, finance and insurance see the highest. TikTok CPCs are generally lower than Google Search but higher than Meta Ads in most markets.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPM for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>TikTok Ads CPMs in {display} sit at the higher end globally, reflecting strong advertiser competition. In-Feed ads on the For You Page command a premium CPM; TopView and Branded Hashtag Challenge placements are significantly more expensive but offer mass reach. CPMs spike during Q4 and major shopping events like Black Friday. Always optimise for the lowest CPA rather than targeting the lowest CPM placement.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CTR for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>A good CTR for TikTok In-Feed Ads in {display} is typically 0.8–1.5%, with a cross-industry average around 0.76–0.84%. TikTok CTR is lower than Google Search because users are in an entertainment mindset. The first 1–3 seconds of your video are the most critical — a strong hook that stops the scroll is the single biggest driver of CTR on TikTok.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good conversion rate for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average TikTok Ads conversion rate in {display} is approximately 1.6–1.8% across all industries. TikTok conversion rates are lower than Google Search because traffic is interest-based rather than intent-based. Landing page speed is critical — {display} users expect fast mobile experiences. TikTok Shop and native checkout options significantly improve conversion rates versus redirecting to external sites.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How do {display} TikTok Ads benchmarks compare to other markets in {region}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>{display} sits at the higher end of TikTok Ads costs in {region}. Higher CPCs and CPMs reflect strong advertiser demand and high consumer value per click. TikTok\'s algorithm performs well in {display} — the platform has strong penetration across younger demographics and conversion rates trend above global averages when creative is well-optimised for the local market.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} TikTok Ads benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on creative quality, audience targeting, bid strategy and TikTok algorithm changes.</p>\n'
         '          </div>\n'
         '        </details>'),
    ],
    'mid': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPC for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average CPC for TikTok Ads in {display} is around {cpc} across all industries. {display} sits in the mid-range globally for TikTok costs — more competitive than emerging markets but below the highest-cost English-speaking markets. Beauty, entertainment and gaming typically see the lowest CPCs; legal, finance and insurance the highest.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPM for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>TikTok CPMs in {display} are moderate compared to global averages. In-Feed (For You Page) ads are the most common placement and offer a good balance of reach and cost. TopView placements carry a significant CPM premium but deliver guaranteed first-impression exposure. Monitor your blended CPM across placements and prioritise the ones delivering the lowest CPA for your campaign objective.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CTR for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>A good CTR for TikTok In-Feed Ads in {display} is typically 0.7–1.3%, with a cross-industry average around 0.69–0.76%. TikTok CTR is primarily driven by the video hook in the first 1–3 seconds. Text overlays, on-screen CTAs and a clear value proposition in the opening frame make the biggest impact on CTR performance.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good conversion rate for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average TikTok Ads conversion rate in {display} is approximately 1.5–1.7% across all industries. Conversion rates are lower than Google Search because TikTok traffic is interest-based rather than intent-based. Fast mobile landing pages and native checkout options significantly improve conversion rates. Consider TikTok\'s Lead Generation campaign type for B2B and service businesses as an alternative to website conversions.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Should I use {code} or USD figures for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Always plan and report in local currency ({code}) when advertising in {display}. TikTok Ads Manager bills in the currency set for your ad account — if set to {code}, all costs will be in {code}. USD benchmarks create misleading comparisons because local auction dynamics, purchasing power and TikTok\'s CPM pricing differ from the US market.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} TikTok Ads benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on creative quality, audience targeting, bid strategy and TikTok algorithm changes.</p>\n'
         '          </div>\n'
         '        </details>'),
    ],
    'emerging': [
        ('<details class="faq-item" open>\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPC for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average CPC for TikTok Ads in {display} is around {cpc} across all industries. {display} has lower CPCs than mature markets, reflecting lower advertiser competition and average order values. TikTok has strong organic traction in {region} — paid amplification of well-performing organic content is often the most cost-effective strategy. CPCs are rising year-over-year as TikTok Ads adoption grows.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good CPM for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>{display} has some of the lowest TikTok CPMs globally, making it highly cost-effective for reach and awareness. The lower CPMs mean your budget goes further in terms of video views and impressions. TikTok\'s algorithm is particularly strong in {region} — the For You Page reaches highly relevant audiences even with modest budgets. Use Spark Ads to boost organic content for the most cost-efficient results.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Why are TikTok Ads costs lower in {display} than in the USA or UK?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>TikTok Ads CPCs and CPMs in {display} are lower because advertiser competition is lower and consumer average order values are smaller than in mature markets. Fewer high-budget international brands compete for the same audiences, keeping auction costs low. Mobile is dominant in {region}, and TikTok\'s mobile-native format performs exceptionally well — short-form video content resonates strongly with local audiences.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>What is a good conversion rate for TikTok Ads in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>The average TikTok Ads conversion rate in {display} is approximately 1.2–1.4% across all industries. Conversion rates in {region} can be lower than mature markets due to less developed mobile payment infrastructure and longer trust-building cycles. TikTok Shop and in-app checkout remove friction and can significantly improve conversion rates compared to redirecting users to external websites.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>Should I use {code} or USD for TikTok Ads budgets in {display}?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Always plan and report in local currency ({code}). TikTok Ads Manager bills in your ad account\'s set currency — if it\'s {code}, all costs will be in {code}. USD benchmarks for {display} create misleading comparisons because local auction dynamics, purchasing power and TikTok\'s pricing structures differ substantially from the US market. Use these {code} benchmarks to set realistic CPA targets for {display} campaigns.</p>\n'
         '          </div>\n'
         '        </details>'),
        ('<details class="faq-item">\n'
         '          <summary class="faq-question">\n'
         '            <span>How often are these {display} TikTok Ads benchmarks updated?</span>\n'
         '            <span class="faq-chevron" aria-hidden="true">&#8964;</span>\n'
         '          </summary>\n'
         '          <div class="faq-answer">\n'
         '            <p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on creative quality, audience targeting, bid strategy and TikTok algorithm changes.</p>\n'
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

def make_card(slug, flag, name, curr):
    return (f'            <a href="{slug}/" class="bm-country-card">\n'
            f'              <span class="bm-country-flag">{flag}</span>\n'
            f'              <span class="bm-country-info"><span class="bm-country-name">{name}</span>'
            f'<span class="bm-country-curr">{curr}</span></span>\n'
            f'            </a>')

def region_block(label, cards):
    return (f'        <div>\n'
            f'          <p class="bm-region-label">{label}</p>\n'
            f'          <div class="bm-country-grid">\n'
            + '\n'.join(make_card(*c) for c in cards) +
            f'\n          </div>\n        </div>')

regions = [
    ('English-Speaking Markets', COUNTRY_CARDS[0:7]),
    ('Europe',                   COUNTRY_CARDS[7:18]),
    ('Asia Pacific',             COUNTRY_CARDS[18:28]),
    ('Americas',                 COUNTRY_CARDS[28:31]),
    ('Middle East',              COUNTRY_CARDS[31:35]),
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
  <meta name="description" content="TikTok Ads benchmarks by country and industry — CTR, CPC, CPM, CPV and conversion rate for 35 countries in local currency. Select your country to view localised benchmark data." />
  <link rel="canonical" href="https://xyzlab.com/tiktok-ads/benchmarks/" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://xyzlab.com/tiktok-ads/benchmarks/" />
  <meta property="og:title" content="TikTok Ads Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab" />
  <meta property="og:description" content="TikTok Ads benchmarks by country and industry — CTR, CPC, CPM, CPV and conversion rate for 35 countries in local currency." />
  <meta property="og:image" content="https://xyzlab.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="TikTok Ads Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab" />
  <meta name="twitter:description" content="TikTok Ads benchmarks by country and industry — CTR, CPC, CPM, CPV and conversion rate for 35 countries in local currency." />
  <meta name="twitter:image" content="https://xyzlab.com/og-image.jpg" />
  <title>TikTok Ads Benchmarks by Country &amp; Industry (Q2 2026) | XYZ Lab</title>
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
    "name": "TikTok Ads Benchmarks by Country and Industry (Q2 2026)",
    "description": "TikTok Ads average CTR, CPC, CPM, CPV and conversion rate benchmarks for 35 countries and 38 industries. Q2 2026 industry aggregates in local currency.",
    "publisher": {{ "@type": "Organization", "name": "XYZ Lab", "url": "https://xyzlab.com" }},
    "url": "https://xyzlab.com/tiktok-ads/benchmarks/",
    "keywords": ["TikTok Ads benchmarks", "TikTok CPC benchmarks", "TikTok CPM benchmarks", "TikTok CPV benchmarks", "TikTok conversion rate benchmarks"]
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
        <a href="../">TikTok Ads Tutorials</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <span class="breadcrumb-current">Benchmarks</span>
      </nav>
      <h1>TikTok Ads <span class="highlight">Benchmarks</span> by Country &amp; Industry</h1>
      <p class="hero-sub">Average TikTok Ads (In-Feed Video &amp; TopView) CTR, CPC, CPM, CPV and conversion rate across 38 industries for 35 countries — all figures in local currency. Select your country below.</p>
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
        <p>38 industries &bull; CTR &bull; CPC &bull; CPM &bull; CPV &bull; Conversion Rate &bull; CPA &bull; Local currency</p>
      </div>
      <div class="bm-regions">
{country_grid}
      </div>
      <div class="bm-what">
        <h3>What are TikTok Ads benchmarks?</h3>
        <p>TikTok Ads benchmarks are industry median performance figures — CTR, CPC, CPM, CPV and conversion rate — aggregated across thousands of TikTok campaigns. They give you a reference point to evaluate whether your own campaigns are performing above, at, or below industry norms in your market.</p>
        <p>All figures are shown in local currency and adjusted for country-level auction competition. TikTok benchmarks differ significantly from Google or Meta because the platform is video-first, scroll-driven and skewed toward younger demographics — making direct comparisons misleading.</p>
        <div class="bm-metrics">
          <div class="bm-metric"><p class="bm-metric-label">CTR</p><p class="bm-metric-name">Click-Through Rate</p><p class="bm-metric-desc">Clicks ÷ impressions. Driven almost entirely by video hook quality.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">CPC</p><p class="bm-metric-name">Cost Per Click</p><p class="bm-metric-desc">Average cost per link click. Lower than Google Search in most markets.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">CPM</p><p class="bm-metric-name">Cost Per 1,000 Impressions</p><p class="bm-metric-desc">Auction cost to reach 1,000 users. Key metric for awareness objectives.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">CPV</p><p class="bm-metric-name">Cost Per View</p><p class="bm-metric-desc">Cost per 6-second video view. TikTok-specific metric for video performance.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">Conv. Rate</p><p class="bm-metric-name">Conversion Rate</p><p class="bm-metric-desc">Conversions ÷ clicks. Lower than search because traffic is interest-based.</p></div>
          <div class="bm-metric"><p class="bm-metric-label">CPA</p><p class="bm-metric-name">Cost Per Acquisition</p><p class="bm-metric-desc">CPC ÷ conversion rate. The cost to acquire one customer or lead.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="coaching-cta">
    <div class="container">
      <div class="coaching-cta-inner">
        <div class="coaching-cta-text">
          <h3>Need 1-on-1 help with TikTok Ads?</h3>
          <p>Book a 90-minute coaching session and we'll review your TikTok Ads account and benchmarks together!</p>
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
        <p>Common questions about TikTok Ads benchmarks.</p>
      </div>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question"><span>Why are TikTok Ads CTRs lower than Google Ads?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>TikTok users are in an entertainment and discovery mindset — they're not actively searching for products or services. This produces lower click-through rates (typically 0.7–1.5%) compared to Google Search (3–5%). A low CTR on TikTok doesn't necessarily mean poor creative performance; high view rates, engagement and brand recall are equally important signals on a video-first platform.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>What is CPV and why does it matter for TikTok Ads?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>CPV (Cost Per View) measures what you pay for a 6-second video view. It's a TikTok-specific metric that reflects how efficiently your video creative captures attention. A low CPV means your content hooks users quickly and the algorithm rewards it with cheaper distribution. CPV is particularly important for awareness and consideration campaigns where the goal is video consumption rather than click-through.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>How do TikTok Ads benchmarks differ by country?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>TikTok Ads costs are shaped by advertiser competition, audience size and local purchasing power. The USA has the highest CPMs globally. English-speaking markets (UK, Australia, Canada) are the next tier. Asian markets like Indonesia, Philippines and Vietnam have very low CPMs but also lower conversion rates. Always compare your campaigns to benchmarks for your specific country and currency to get meaningful signals.</p></div>
        </details>
        <details class="faq-item">
          <summary class="faq-question"><span>How often are these TikTok Ads benchmarks updated?</span><span class="faq-chevron" aria-hidden="true">&#8964;</span></summary>
          <div class="faq-answer"><p>Benchmarks are reviewed and updated quarterly. The current data reflects Q2 2026 industry aggregates compiled from anonymised campaign data and published industry reports. Individual results will vary based on creative quality, audience targeting, bid strategy and TikTok algorithm changes.</p></div>
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
print('  wrote tiktok-ads/benchmarks/index.html')

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
  <meta name="description" content="TikTok Ads benchmarks for {display} — average CTR, CPC, CPM, CPV and conversion rate across 38 industries in {code}. Q2 2026 data for advertisers in {display}." />
  <link rel="canonical" href="https://xyzlab.com/tiktok-ads/benchmarks/{slug}/" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://xyzlab.com/tiktok-ads/benchmarks/{slug}/" />
  <meta property="og:title" content="TikTok Ads Benchmarks {display} (Q2 2026) — CTR, CPC, CPA by Industry | XYZ Lab" />
  <meta property="og:description" content="TikTok Ads benchmarks for {display} — average CTR, CPC, CPM, CPV and conversion rate across 38 industries in {code}. Q2 2026 data." />
  <meta property="og:image" content="https://xyzlab.com/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="TikTok Ads Benchmarks {display} (Q2 2026) — CTR, CPC, CPA by Industry | XYZ Lab" />
  <meta name="twitter:description" content="TikTok Ads benchmarks for {display} — average CTR, CPC, CPM, CPV and conversion rate across 38 industries in {code}." />
  <meta name="twitter:image" content="https://xyzlab.com/og-image.jpg" />
  <title>TikTok Ads Benchmarks {display} (Q2 2026) — CTR, CPC, CPA by Industry | XYZ Lab</title>
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
      storageKey:   'bm_tiktok_unlocked',
      stripeUrl:    'https://buy.stripe.com/7sY5kEcdz0oma998cM3Je09',
      price:        '$9.99',
      supportEmail: 'hello@xyzlab.com'
    }};
  </script>
  <script src="../../../benchmarks/tiktok-ads-data.js"></script>
  <script src="../../../benchmarks/benchmarks.js"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "TikTok Ads Benchmarks — {display} (Q2 2026)",
    "description": "TikTok Ads average CTR, CPC, CPM, CPV and conversion rate for 38 industries in {display}. All figures in {code}. Q2 2026 industry aggregates.",
    "publisher": {{ "@type": "Organization", "name": "XYZ Lab", "url": "https://xyzlab.com" }},
    "url": "https://xyzlab.com/tiktok-ads/benchmarks/{slug}/",
    "keywords": ["TikTok Ads benchmarks {display}", "TikTok CPC {display}", "TikTok CPM {display}", "TikTok CPV {display}", "TikTok conversion rate {display}"]
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
        <a href="../../">TikTok Ads Tutorials</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <a href="../">Benchmarks</a>
        <span class="breadcrumb-sep">&#8250;</span>
        <span class="breadcrumb-current">{display}</span>
      </nav>
      <h1 id="bm-h1">TikTok Ads Benchmarks in <span class="highlight">{display}</span></h1>
      <p class="hero-sub" id="bm-sub">Average TikTok Ads performance in {display} across all industries. Figures in {curr_str}.</p>
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
        <h2>TikTok Ads Benchmarks — <span class="highlight">{display}</span></h2>
        <p>Select an industry to highlight it in the table. All figures in {curr_str}.</p>
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
            <li>35 countries in local currency</li>
            <li>CTR, CPC, CPM, CPV, Conversion Rate &amp; CPA</li>
            <li>Instant ZIP download — all countries in one file</li>
            <li>Copy table to paste into Google Sheets or Excel</li>
          </ul>
          <a href="https://buy.stripe.com/7sY5kEcdz0oma998cM3Je09" class="bm-unlock-btn">Unlock for $9.99 &rarr;</a>
          <p class="bm-already-paid">Already paid but lost access? <a href="mailto:hello@xyzlab.com?subject=TikTok%20Ads%20Benchmarks%20%E2%80%94%20Restore%20Access">Email us to restore</a></p>
        </div>
      </div>
      <div class="bm-note">
        <strong>Methodology:</strong> Benchmarks are industry aggregates compiled from anonymised campaign data and published industry reports (Q2 2026). Figures represent medians across multiple advertisers and campaign types. All values are in {code} and adjusted for {display} market auction dynamics. Individual results will vary based on creative quality, audience targeting, bid strategy and TikTok algorithm changes.
      </div>
    </div>
  </section>

  <section class="coaching-cta">
    <div class="container">
      <div class="coaching-cta-inner">
        <div class="coaching-cta-text">
          <h3>Need 1-on-1 help with TikTok Ads in {display}?</h3>
          <p>Book a 90-minute coaching session and we\'ll review your TikTok Ads account and {display} benchmarks together!</p>
        </div>
        <a href="#coaching" class="btn btn-primary">Book a Coaching Session</a>
      </div>
    </div>
  </section>

  <section class="faq" id="faq">
    <div class="container">
      <div class="section-header">
        <div class="badge">FAQ</div>
        <h2>TikTok Ads Benchmarks — {display} FAQ</h2>
        <p>Common questions about TikTok Ads performance in {display}.</p>
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
        <h2>Related <span class="highlight">TikTok Ads Tutorials</span></h2>
        <p>More step-by-step guides to get better results from your TikTok Ads campaigns.</p>
      </div>
      <div class="courses-grid">
        <article class="course-card">
          <a href="/tiktok-ads/benchmarks/" class="course-icon" tabindex="-1" style="background:#e8faf9;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#e8faf9"/><rect x="8" y="18" width="3" height="6" rx="1" fill="#08bfad"/><rect x="13" y="13" width="3" height="11" rx="1" fill="#08bfad" opacity=".7"/><rect x="18" y="9" width="3" height="15" rx="1" fill="#08bfad" opacity=".4"/><rect x="23" y="14" width="3" height="10" rx="1" fill="#08bfad"/></svg>
          </a>
          <h3><a href="/tiktok-ads/benchmarks/">TikTok Ads Benchmarks by Country</a></h3>
          <ul class="course-bullets">
            <li>Compare benchmarks across 35 countries</li>
            <li>Select your market for local-currency data</li>
            <li>CTR, CPC, CPM, CPV, conversion rate &amp; CPA</li>
          </ul>
          <a href="/tiktok-ads/benchmarks/" class="course-link">View All Countries &#8594;</a>
        </article>
        <article class="course-card">
          <a href="../../setup-event-tracking/" class="course-icon" tabindex="-1" style="background:#fff3e0;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#fff3e0"/><path d="M10 16l4-4 4 4 4-4" stroke="#fec55c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <h3><a href="../../setup-event-tracking/">Set Up TikTok Ads Event Tracking</a></h3>
          <ul class="course-bullets">
            <li>Install the TikTok Pixel correctly</li>
            <li>Track purchases, leads and page views</li>
            <li>Verify events with the TikTok Events Manager</li>
          </ul>
          <a href="../../setup-event-tracking/" class="course-link">Watch Tutorial &#8594;</a>
        </article>
        <article class="course-card">
          <a href="../../customer-lists/" class="course-icon" tabindex="-1" style="background:#e8faf9;">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#e8faf9"/><circle cx="12" cy="13" r="4" stroke="#08bfad" stroke-width="2"/><path d="M4 24c0-4 3.6-7 8-7s8 3 8 7" stroke="#08bfad" stroke-width="2" stroke-linecap="round"/><path d="M22 11v6M25 14h-6" stroke="#08bfad" stroke-width="2" stroke-linecap="round"/></svg>
          </a>
          <h3><a href="../../customer-lists/">Upload Customer Lists to TikTok Ads</a></h3>
          <ul class="course-bullets">
            <li>Create custom audiences from your CRM</li>
            <li>Build lookalike audiences from customers</li>
            <li>Exclude existing customers from campaigns</li>
          </ul>
          <a href="../../customer-lists/" class="course-link">Watch Tutorial &#8594;</a>
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

for (slug, bm_country, display, curr_str, curr_code, flag, cpc_approx, market_type, region) in COUNTRIES:
    faq_items = FAQS[market_type]
    faq_block = '\n\n        '.join(
        item.replace('{display}', display).replace('{cpc}', cpc_approx)
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
    print(f'  wrote tiktok-ads/benchmarks/{slug}/')

print(f'\nDone — 35 country pages + 1 pillar page')
