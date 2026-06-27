(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  // LinkedIn Sponsored Content averages (cross-industry, USA baseline)
  // LinkedIn carries a B2B premium — CPCs and CPMs are significantly higher
  // than Meta or Google, but audience quality for professional intent is unmatched.
  var BASE_CTR = 0.45;  // %
  var BASE_CPC = 6.50;  // USD
  var BASE_CPE = 0.75;  // USD — cost per engagement (like, comment, share, follow)
  var BASE_CVR = 1.60;  // %

  // ctm  = CTR multiplier (LinkedIn professional audience engagement by market)
  // cpcm = CPC/CPM/CPE cost multiplier (exchange rate + local advertiser density)
  // convm = CVR multiplier
  var countries = {
    'Argentina':    { ctm: 0.75, cpcm: 412.0,  convm: 0.65, sym: 'AR$',  code: 'ARS' },
    'Australia':    { ctm: 0.90, cpcm: 1.24,   convm: 0.90, sym: 'AU$',  code: 'AUD' },
    'Austria':  { ctm: 0.9, cpcm: 0.342, convm: 0.91, sym: '€', code: 'EUR' },
    'Bahrain':      { ctm: 0.80, cpcm: 0.169,  convm: 0.78, sym: 'BHD ', code: 'BHD' },
    'Belgium':  { ctm: 0.91, cpcm: 0.359, convm: 0.9, sym: '€', code: 'EUR' },
    'Brazil':       { ctm: 0.82, cpcm: 1.55,   convm: 0.72, sym: 'R$',   code: 'BRL' },
    'Bulgaria':  { ctm: 0.82, cpcm: 0.331, convm: 0.76, sym: 'лв ', code: 'BGN' },
    'Canada':       { ctm: 0.92, cpcm: 1.18,   convm: 0.94, sym: 'CA$',  code: 'CAD' },
    'Chile':  { ctm: 0.88, cpcm: 176.0, convm: 0.75, sym: 'CLP ', code: 'CLP', noDecimal: true },
    'Colombia':  { ctm: 0.9, cpcm: 609.0, convm: 0.73, sym: 'COP ', code: 'COP', noDecimal: true },
    'Croatia':  { ctm: 0.84, cpcm: 0.274, convm: 0.8, sym: '€', code: 'EUR' },
    'Czechia':  { ctm: 0.85, cpcm: 5.13, convm: 0.84, sym: 'Kč ', code: 'CZK' },
    'Denmark':      { ctm: 0.88, cpcm: 11.34,  convm: 0.88, sym: 'DKK ', code: 'DKK' },
    'Finland':  { ctm: 0.92, cpcm: 0.376, convm: 0.92, sym: '€', code: 'EUR' },
    'France':       { ctm: 0.85, cpcm: 0.506,  convm: 0.84, sym: '€',    code: 'EUR' },
    'Germany':      { ctm: 0.88, cpcm: 0.62,   convm: 0.88, sym: '€',    code: 'EUR' },
    'Hong Kong':    { ctm: 0.85, cpcm: 4.301,  convm: 0.85, sym: 'HK$',  code: 'HKD' },
    'India':        { ctm: 0.92, cpcm: 8.25,   convm: 0.70, sym: '₹',    code: 'INR' },
    'Indonesia':    { ctm: 0.75, cpcm: 1031.0, convm: 0.60, sym: 'Rp ',  code: 'IDR', noDecimal: true },
    'Ireland':      { ctm: 0.92, cpcm: 0.77,   convm: 0.92, sym: '€',    code: 'EUR' },
    'Italy':        { ctm: 0.80, cpcm: 0.386,  convm: 0.78, sym: '€',    code: 'EUR' },
    'Japan':        { ctm: 0.72, cpcm: 72.0,   convm: 0.78, sym: '¥',    code: 'JPY', noDecimal: true },
    'Kenya':  { ctm: 0.87, cpcm: 13.5, convm: 0.7, sym: 'KSh ', code: 'KES' },
    'Malaysia':     { ctm: 0.80, cpcm: 2.06,   convm: 0.65, sym: 'RM ',  code: 'MYR' },
    'Mexico':       { ctm: 0.80, cpcm: 10.31,  convm: 0.70, sym: 'MX$',  code: 'MXN' },
    'Netherlands':  { ctm: 0.90, cpcm: 0.552,  convm: 0.88, sym: '€',    code: 'EUR' },
    'New Zealand':  { ctm: 0.85, cpcm: 1.122,  convm: 0.86, sym: 'NZ$',  code: 'NZD' },
    'Nigeria':  { ctm: 0.86, cpcm: 181.0, convm: 0.68, sym: '₦', code: 'NGN', noDecimal: true },
    'Norway':       { ctm: 0.88, cpcm: 18.56,  convm: 0.90, sym: 'NOK ', code: 'NOK' },
    'Peru':  { ctm: 0.89, cpcm: 0.627, convm: 0.74, sym: 'S/', code: 'PEN' },
    'Philippines':  { ctm: 0.78, cpcm: 6.19,   convm: 0.62, sym: '₱',    code: 'PHP' },
    'Poland':       { ctm: 0.78, cpcm: 1.134,  convm: 0.75, sym: 'zł',   code: 'PLN' },
    'Portugal':  { ctm: 0.89, cpcm: 0.325, convm: 0.86, sym: '€', code: 'EUR' },
    'Qatar':        { ctm: 0.82, cpcm: 2.111,  convm: 0.80, sym: 'QAR ', code: 'QAR' },
    'Romania':  { ctm: 0.83, cpcm: 0.94, convm: 0.78, sym: 'lei ', code: 'RON' },
    'Saudi Arabia': { ctm: 0.82, cpcm: 1.950,  convm: 0.80, sym: 'SAR ', code: 'SAR' },
    'Singapore':    { ctm: 0.90, cpcm: 0.837,  convm: 0.88, sym: 'S$',   code: 'SGD' },
    'South Africa': { ctm: 0.72, cpcm: 5.15,   convm: 0.62, sym: 'R ',   code: 'ZAR' },
    'South Korea':  { ctm: 0.78, cpcm: 567.0,  convm: 0.75, sym: '₩',    code: 'KRW', noDecimal: true },
    'Spain':        { ctm: 0.82, cpcm: 0.368,  convm: 0.80, sym: '€',    code: 'EUR' },
    'Sweden':       { ctm: 0.90, cpcm: 14.43,  convm: 0.90, sym: 'SEK ', code: 'SEK' },
    'Switzerland':  { ctm: 0.88, cpcm: 2.06,   convm: 0.90, sym: 'CHF ', code: 'CHF' },
    'Taiwan':  { ctm: 0.85, cpcm: 5.85, convm: 0.86, sym: 'NT$', code: 'TWD' },
    'Thailand':     { ctm: 0.72, cpcm: 7.700,  convm: 0.58, sym: '฿',    code: 'THB' },
    'Turkiye':      { ctm: 0.75, cpcm: 5.760,  convm: 0.70, sym: '₺',    code: 'TRY' },
    'UAE':          { ctm: 0.88, cpcm: 3.12,   convm: 0.85, sym: 'AED ', code: 'AED' },
    'UK':           { ctm: 0.95, cpcm: 0.61,   convm: 0.96, sym: '£',    code: 'GBP' },
    'USA':          { ctm: 1.00, cpcm: 1.00,   convm: 1.00, sym: '$',    code: 'USD' },
    'Vietnam':      { ctm: 0.70, cpcm: 8247.0, convm: 0.55, sym: '₫',    code: 'VND', noDecimal: true }
  };

  var countryNames = Object.keys(countries).sort();

  // [name, cpc_m, cpe_m, ctr_m, cvr_m]
  // CPM derived: cpc * ctr * 10  |  CPA derived: cpc / (cvr/100)
  // LinkedIn skews heavily B2B — B2C industries show lower CTR and CVR
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.72, 0.80, 0.58, 0.42],
    ['Automotive',                             1.28, 1.15, 0.72, 0.62],
    ['Banking & Finance',                      1.65, 1.35, 0.85, 1.28],
    ['Beauty & Salons',                        0.65, 0.75, 0.52, 0.38],
    ['Crypto & Web3',                          1.45, 1.25, 0.78, 0.68],
    ['Dating',                                 0.85, 0.90, 0.62, 0.55],
    ['Education',                              0.88, 0.92, 1.12, 1.35],
    ['Electronics (E-Commerce)',               0.95, 0.95, 0.65, 0.55],
    ['Entertainment & Media',                  0.75, 0.85, 0.75, 0.62],
    ['Fitness & Gyms',                         0.78, 0.85, 0.72, 0.68],
    ['Flights',                                1.12, 1.05, 0.78, 0.48],
    ['Food & Beverage',                        0.68, 0.78, 0.62, 0.52],
    ['Furniture & Home Décor (E-Commerce)',    0.80, 0.85, 0.60, 0.45],
    ['Gaming',                                 0.72, 0.80, 0.65, 0.55],
    ['Healthcare',                             1.42, 1.25, 0.95, 1.18],
    ['Health & Wellness (E-Commerce)',         0.78, 0.85, 0.68, 0.62],
    ['Home Appliances (E-Commerce)',           0.85, 0.88, 0.62, 0.48],
    ['Home Services',                          1.05, 1.00, 0.72, 0.75],
    ['Hotels',                                 1.15, 1.05, 0.82, 0.65],
    ['Insurance',                              1.72, 1.40, 0.75, 1.12],
    ['Jewelry & Accessories (E-Commerce)',     0.85, 0.90, 0.65, 0.52],
    ['Jobs & Recruitment',                     1.45, 1.25, 1.22, 1.65],
    ['Legal',                                  1.85, 1.55, 0.68, 0.88],
    ['Logistics',                              1.35, 1.20, 0.88, 1.08],
    ['Moving & Cleaning Services',             0.92, 0.95, 0.72, 0.72],
    ['Non-Profit & Charity',                   0.55, 0.65, 0.85, 0.88],
    ['Online Courses & EdTech',                0.82, 0.88, 1.08, 1.42],
    ['Pet Products (E-Commerce)',              0.65, 0.72, 0.55, 0.40],
    ['Property',                               1.32, 1.18, 0.82, 0.78],
    ['Restaurants & Food Delivery',            0.62, 0.72, 0.65, 0.55],
    ['Skincare (E-Commerce)',                  0.70, 0.78, 0.62, 0.50],
    ['Software & SaaS',                        1.35, 1.18, 1.28, 1.52],
    ['Sports & Outdoors (E-Commerce)',         0.75, 0.82, 0.62, 0.48],
    ['Subscription Boxes',                     0.72, 0.78, 0.65, 0.55],
    ['Toys & Baby (E-Commerce)',               0.60, 0.70, 0.52, 0.38],
    ['Travel',                                 1.08, 1.00, 0.85, 0.62],
    ['Wedding & Events',                       0.88, 0.92, 0.75, 0.68]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], cpc_m = ind[1], cpe_m = ind[2], ctr_m = ind[3], cvr_m = ind[4];
      var ctr = r(BASE_CTR * cm.ctm   * ctr_m, 2);
      var cpc = r(BASE_CPC * cm.cpcm  * cpc_m, 2);
      var cpm = r(cpc * ctr * 10,              2);
      var cpe = r(BASE_CPE * cm.cpcm  * cpe_m, 2);
      var cvr = r(BASE_CVR * cm.convm * cvr_m, 2);
      var cpa = r(cpc / (cvr / 100),           2);
      data[cname][iname] = { ctr: ctr, cpc: cpc, cpm: cpm, cpe: cpe, cvr: cvr, cpa: cpa };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'LinkedIn Ads',
    channelDesc: 'Sponsored Content & InMail',
    channelSlug: 'linkedin-ads',
    updated:     'Q2 2026',
    countries:   countryNames,
    currencies:  (function () {
      var o = {};
      countryNames.forEach(function (c) {
        o[c] = { sym: countries[c].sym, code: countries[c].code, noDecimal: !!countries[c].noDecimal };
      });
      return o;
    })(),
    industries:  industryNames,
    columns: [
      { key: 'ctr', head: 'CTR',          fmt: 'pct'   },
      { key: 'cpc', head: 'CPC',          fmt: 'money' },
      { key: 'cpm', head: 'CPM',          fmt: 'money' },
      { key: 'cpe', head: 'CPE',          fmt: 'money' },
      { key: 'cvr', head: 'Conv. Rate',   fmt: 'pct'   },
      { key: 'cpa', head: 'CPA',          fmt: 'money' }
    ],
    data: data
  };
})();
