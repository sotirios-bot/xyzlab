(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  // Email marketing averages (cross-industry, USA baseline)
  // Figures represent blended performance across all email types (promotional,
  // transactional, newsletter). Open Rate is measured by pixel/click-inferred opens.
  var BASE_OPEN   = 21.50;  // %
  var BASE_CLICK  = 2.80;   // %
  var BASE_UNSUB  = 0.20;   // %
  var BASE_BOUNCE = 0.65;   // % (combined hard + soft bounce rate)

  // openm   = Open rate multiplier (email adoption, inbox culture)
  // clickm  = Click rate multiplier (engagement depth)
  // unsubm  = Unsubscribe rate multiplier (>1 = more unsubscribes)
  // bouncem = Bounce rate multiplier (>1 = more bounces / poorer list quality)
  var countries = {
    'Argentina':    { openm: 0.82, clickm: 0.80, unsubm: 1.15, bouncem: 1.30 },
    'Australia':    { openm: 1.02, clickm: 1.00, unsubm: 0.92, bouncem: 0.88 },
    'Austria':  { openm: 0.95, clickm: 0.92, unsubm: 0.99, bouncem: 1.02 },
    'Bahrain':      { openm: 0.80, clickm: 0.78, unsubm: 1.05, bouncem: 1.15 },
    'Bangladesh':  { openm: 0.76, clickm: 0.72, unsubm: 1.26, bouncem: 1.45 },
    'Belgium':  { openm: 0.96, clickm: 0.94, unsubm: 0.98, bouncem: 1.02 },
    'Brazil':       { openm: 0.82, clickm: 0.85, unsubm: 1.12, bouncem: 1.22 },
    'Bulgaria':  { openm: 0.85, clickm: 0.82, unsubm: 1.1, bouncem: 1.12 },
    'Canada':       { openm: 1.00, clickm: 1.00, unsubm: 0.90, bouncem: 0.88 },
    'Chile':  { openm: 0.87, clickm: 0.84, unsubm: 1.08, bouncem: 1.12 },
    'Colombia':  { openm: 0.85, clickm: 0.82, unsubm: 1.12, bouncem: 1.18 },
    'Croatia':  { openm: 0.9, clickm: 0.88, unsubm: 1.04, bouncem: 1.06 },
    'Czechia':  { openm: 0.92, clickm: 0.9, unsubm: 1.02, bouncem: 1.04 },
    'Denmark':      { openm: 1.08, clickm: 1.05, unsubm: 0.82, bouncem: 0.78 },
    'Ecuador':  { openm: 0.84, clickm: 0.82, unsubm: 1.12, bouncem: 1.2 },
    'Egypt':  { openm: 0.8, clickm: 0.78, unsubm: 1.18, bouncem: 1.32 },
    'Finland':  { openm: 1.02, clickm: 1.0, unsubm: 0.92, bouncem: 0.95 },
    'France':       { openm: 0.98, clickm: 0.92, unsubm: 0.88, bouncem: 0.85 },
    'Germany':      { openm: 1.10, clickm: 0.95, unsubm: 0.80, bouncem: 0.75 },
    'Greece':  { openm: 0.88, clickm: 0.86, unsubm: 1.08, bouncem: 1.1 },
    'Hong Kong':    { openm: 0.88, clickm: 0.85, unsubm: 0.95, bouncem: 0.95 },
    'Hungary':  { openm: 0.86, clickm: 0.84, unsubm: 1.1, bouncem: 1.12 },
    'India':        { openm: 0.78, clickm: 0.88, unsubm: 1.18, bouncem: 1.38 },
    'Indonesia':    { openm: 0.72, clickm: 0.80, unsubm: 1.22, bouncem: 1.48 },
    'Ireland':      { openm: 1.05, clickm: 1.02, unsubm: 0.85, bouncem: 0.82 },
    'Israel':  { openm: 0.98, clickm: 0.96, unsubm: 0.96, bouncem: 1.0 },
    'Italy':        { openm: 0.92, clickm: 0.88, unsubm: 0.92, bouncem: 0.92 },
    'Japan':        { openm: 1.12, clickm: 0.88, unsubm: 0.70, bouncem: 0.80 },
    'Kenya':  { openm: 0.8, clickm: 0.78, unsubm: 1.18, bouncem: 1.3 },
    'Malaysia':     { openm: 0.80, clickm: 0.82, unsubm: 1.10, bouncem: 1.20 },
    'Mexico':       { openm: 0.82, clickm: 0.85, unsubm: 1.08, bouncem: 1.18 },
    'Morocco':  { openm: 0.82, clickm: 0.8, unsubm: 1.16, bouncem: 1.28 },
    'Netherlands':  { openm: 1.05, clickm: 1.00, unsubm: 0.82, bouncem: 0.80 },
    'New Zealand':  { openm: 1.02, clickm: 1.00, unsubm: 0.92, bouncem: 0.88 },
    'Nigeria':  { openm: 0.78, clickm: 0.76, unsubm: 1.2, bouncem: 1.35 },
    'Norway':       { openm: 1.08, clickm: 1.05, unsubm: 0.82, bouncem: 0.78 },
    'Pakistan':  { openm: 0.78, clickm: 0.74, unsubm: 1.24, bouncem: 1.42 },
    'Paraguay':  { openm: 0.82, clickm: 0.8, unsubm: 1.14, bouncem: 1.22 },
    'Peru':  { openm: 0.83, clickm: 0.81, unsubm: 1.14, bouncem: 1.2 },
    'Philippines':  { openm: 0.75, clickm: 0.80, unsubm: 1.18, bouncem: 1.42 },
    'Poland':       { openm: 0.88, clickm: 0.90, unsubm: 0.95, bouncem: 0.98 },
    'Portugal':  { openm: 0.92, clickm: 0.9, unsubm: 1.02, bouncem: 1.04 },
    'Qatar':        { openm: 0.82, clickm: 0.80, unsubm: 1.05, bouncem: 1.12 },
    'Romania':  { openm: 0.88, clickm: 0.85, unsubm: 1.08, bouncem: 1.1 },
    'Saudi Arabia': { openm: 0.82, clickm: 0.82, unsubm: 1.05, bouncem: 1.12 },
    'Singapore':    { openm: 0.92, clickm: 0.90, unsubm: 0.95, bouncem: 0.92 },
    'South Africa': { openm: 0.80, clickm: 0.82, unsubm: 1.08, bouncem: 1.20 },
    'South Korea':  { openm: 0.85, clickm: 0.85, unsubm: 0.95, bouncem: 0.95 },
    'Spain':        { openm: 0.92, clickm: 0.90, unsubm: 0.92, bouncem: 0.90 },
    'Sweden':       { openm: 1.08, clickm: 1.05, unsubm: 0.82, bouncem: 0.78 },
    'Switzerland':  { openm: 1.08, clickm: 1.02, unsubm: 0.82, bouncem: 0.80 },
    'Taiwan':  { openm: 0.88, clickm: 0.86, unsubm: 1.06, bouncem: 1.08 },
    'Thailand':     { openm: 0.72, clickm: 0.78, unsubm: 1.18, bouncem: 1.40 },
    'Turkiye':      { openm: 0.80, clickm: 0.82, unsubm: 1.10, bouncem: 1.20 },
    'UAE':          { openm: 0.85, clickm: 0.85, unsubm: 1.00, bouncem: 1.05 },
    'UK':           { openm: 1.05, clickm: 1.02, unsubm: 0.88, bouncem: 0.85 },
    'USA':          { openm: 1.00, clickm: 1.00, unsubm: 1.00, bouncem: 1.00 },
    'Ukraine':  { openm: 0.84, clickm: 0.82, unsubm: 1.14, bouncem: 1.2 },
    'Uruguay':  { openm: 0.86, clickm: 0.84, unsubm: 1.08, bouncem: 1.12 },
    'Venezuela':  { openm: 0.78, clickm: 0.76, unsubm: 1.18, bouncem: 1.3 },
    'Vietnam':      { openm: 0.70, clickm: 0.78, unsubm: 1.22, bouncem: 1.52 }
  };

  var countryNames = Object.keys(countries).sort();

  // [name, open_m, click_m, unsub_m, bounce_m]
  // Healthcare, Non-Profit and Finance consistently show above-average open rates.
  // Dating and Crypto show elevated unsubscribe rates due to subscriber fatigue.
  // Food, Travel and Restaurants excel on click rates (visual, deal-driven content).
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.95, 1.22, 1.12, 1.05],
    ['Automotive',                             0.92, 0.88, 0.95, 1.02],
    ['Banking & Finance',                      1.12, 1.08, 0.85, 0.88],
    ['Beauty & Salons',                        1.02, 1.18, 1.08, 1.02],
    ['Crypto & Web3',                          0.88, 0.95, 1.45, 1.28],
    ['Dating',                                 0.85, 1.05, 1.55, 1.35],
    ['Education',                              1.18, 1.12, 0.78, 0.82],
    ['Electronics (E-Commerce)',               0.95, 1.08, 1.05, 1.08],
    ['Entertainment & Media',                  1.05, 1.15, 1.08, 1.02],
    ['Fitness & Gyms',                         1.08, 1.12, 1.02, 0.95],
    ['Flights',                                1.02, 1.28, 0.92, 0.90],
    ['Food & Beverage',                        1.12, 1.35, 0.88, 0.88],
    ['Furniture & Home Décor (E-Commerce)',    0.95, 1.05, 1.02, 1.05],
    ['Gaming',                                 0.92, 1.08, 1.18, 1.10],
    ['Healthcare',                             1.28, 1.05, 0.72, 0.78],
    ['Health & Wellness (E-Commerce)',         1.12, 1.18, 0.92, 0.90],
    ['Home Appliances (E-Commerce)',           0.92, 1.05, 1.02, 1.05],
    ['Home Services',                          1.02, 0.95, 0.95, 0.98],
    ['Hotels',                                 1.05, 1.22, 0.88, 0.88],
    ['Insurance',                              1.08, 0.92, 0.88, 0.88],
    ['Jewelry & Accessories (E-Commerce)',     0.98, 1.12, 1.05, 1.02],
    ['Jobs & Recruitment',                     1.08, 1.18, 1.02, 0.95],
    ['Legal',                                  0.92, 0.82, 1.08, 1.05],
    ['Logistics',                              0.88, 0.85, 0.98, 1.05],
    ['Moving & Cleaning Services',             0.95, 0.95, 0.98, 1.00],
    ['Non-Profit & Charity',                   1.22, 1.05, 0.72, 0.82],
    ['Online Courses & EdTech',                1.15, 1.12, 0.85, 0.85],
    ['Pet Products (E-Commerce)',              1.08, 1.22, 0.95, 0.95],
    ['Property',                               1.02, 1.08, 0.95, 0.92],
    ['Restaurants & Food Delivery',            1.10, 1.32, 0.88, 0.85],
    ['Skincare (E-Commerce)',                  1.02, 1.18, 0.98, 0.95],
    ['Software & SaaS',                        1.05, 1.12, 0.90, 0.88],
    ['Sports & Outdoors (E-Commerce)',         1.02, 1.15, 1.00, 0.98],
    ['Subscription Boxes',                     1.08, 1.22, 0.88, 0.88],
    ['Toys & Baby (E-Commerce)',               1.05, 1.15, 0.95, 0.95],
    ['Travel',                                 1.05, 1.28, 0.88, 0.88],
    ['Wedding & Events',                       1.08, 1.12, 0.95, 0.95]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], open_m = ind[1], click_m = ind[2], unsub_m = ind[3], bounce_m = ind[4];
      var open   = r(BASE_OPEN   * cm.openm   * open_m,   2);
      var click  = r(BASE_CLICK  * cm.clickm  * click_m,  2);
      var unsub  = r(BASE_UNSUB  * cm.unsubm  * unsub_m,  2);
      var bounce = r(BASE_BOUNCE * cm.bouncem * bounce_m, 2);
      data[cname][iname] = { open: open, click: click, unsub: unsub, bounce: bounce };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'Email Marketing',
    channelDesc: 'Email Campaigns & Newsletters',
    channelSlug: 'email-marketing',
    updated:     'Q2 2026',
    countries:   countryNames,
    industries:  industryNames,
    columns: [
      { key: 'open',   head: 'Open Rate',         fmt: 'pct' },
      { key: 'click',  head: 'Click Rate',         fmt: 'pct' },
      { key: 'unsub',  head: 'Unsubscribe Rate',   fmt: 'pct' },
      { key: 'bounce', head: 'Bounce Rate',        fmt: 'pct' }
    ],
    data: data
  };
})();
