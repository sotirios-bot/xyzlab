(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  // TikTok in-feed video averages (cross-industry, USA baseline)
  var BASE_CTR = 0.84;  // %
  var BASE_CPC = 1.18;  // USD — CPM / (CTR * 10)
  var BASE_CPV = 0.026; // USD — cost per 6-second view
  var BASE_CVR = 1.80;  // %

  // ctm  = CTR multiplier (TikTok engagement by market)
  // cpcm = CPC/CPM/CPV cost multiplier (exchange rate + local pricing)
  // convm = CVR multiplier
  var countries = {
    'Argentina':    { ctm: 0.85, cpcm: 412.0,  convm: 0.68, sym: 'AR$',  code: 'ARS' },
    'Australia':    { ctm: 0.90, cpcm: 1.24,   convm: 0.86, sym: 'AU$',  code: 'AUD' },
    'Austria':  { ctm: 0.9, cpcm: 0.342, convm: 0.91, sym: '€', code: 'EUR' },
    'Bahrain':      { ctm: 0.82, cpcm: 0.169,  convm: 0.80, sym: 'BHD ', code: 'BHD' },
    'Bangladesh':  { ctm: 1.1, cpcm: 4.09, convm: 0.58, sym: '৳', code: 'BDT', noDecimal: true },
    'Belgium':  { ctm: 0.91, cpcm: 0.359, convm: 0.9, sym: '€', code: 'EUR' },
    'Brazil':       { ctm: 0.95, cpcm: 1.55,   convm: 0.78, sym: 'R$',   code: 'BRL' },
    'Bulgaria':  { ctm: 0.82, cpcm: 0.331, convm: 0.76, sym: 'лв ', code: 'BGN' },
    'Canada':       { ctm: 0.92, cpcm: 1.18,   convm: 0.90, sym: 'CA$',  code: 'CAD' },
    'Chile':  { ctm: 0.88, cpcm: 176.0, convm: 0.75, sym: 'CLP ', code: 'CLP', noDecimal: true },
    'Colombia':  { ctm: 0.9, cpcm: 609.0, convm: 0.73, sym: 'COP ', code: 'COP', noDecimal: true },
    'Croatia':  { ctm: 0.84, cpcm: 0.274, convm: 0.8, sym: '€', code: 'EUR' },
    'Czechia':  { ctm: 0.85, cpcm: 5.13, convm: 0.84, sym: 'Kč ', code: 'CZK' },
    'Denmark':      { ctm: 0.85, cpcm: 11.34,  convm: 0.85, sym: 'DKK ', code: 'DKK' },
    'Ecuador':  { ctm: 0.88, cpcm: 0.204, convm: 0.8, sym: '$', code: 'USD' },
    'Egypt':  { ctm: 0.92, cpcm: 7.4, convm: 0.72, sym: 'EGP ', code: 'EGP', noDecimal: true },
    'Finland':  { ctm: 0.92, cpcm: 0.376, convm: 0.92, sym: '€', code: 'EUR' },
    'France':       { ctm: 0.88, cpcm: 0.506,  convm: 0.82, sym: '€',    code: 'EUR' },
    'Germany':      { ctm: 0.85, cpcm: 0.62,   convm: 0.84, sym: '€',    code: 'EUR' },
    'Greece':  { ctm: 0.86, cpcm: 0.496, convm: 0.88, sym: '€', code: 'EUR' },
    'Hong Kong':    { ctm: 0.92, cpcm: 4.301,  convm: 0.88, sym: 'HK$',  code: 'HKD' },
    'Hungary':  { ctm: 0.84, cpcm: 112.6, convm: 0.85, sym: 'Ft ', code: 'HUF', noDecimal: true },
    'India':        { ctm: 1.08, cpcm: 8.25,   convm: 0.62, sym: '₹',    code: 'INR' },
    'Indonesia':    { ctm: 1.15, cpcm: 1031.0, convm: 0.68, sym: 'Rp ',  code: 'IDR', noDecimal: true },
    'Ireland':      { ctm: 0.88, cpcm: 0.77,   convm: 0.88, sym: '€',    code: 'EUR' },
    'Israel':  { ctm: 0.88, cpcm: 2.41, convm: 1.02, sym: '₪', code: 'ILS' },
    'Italy':        { ctm: 0.90, cpcm: 0.386,  convm: 0.80, sym: '€',    code: 'EUR' },
    'Japan':        { ctm: 0.80, cpcm: 72.0,   convm: 0.85, sym: '¥',    code: 'JPY', noDecimal: true },
    'Kenya':  { ctm: 0.87, cpcm: 13.5, convm: 0.7, sym: 'KSh ', code: 'KES' },
    'Malaysia':     { ctm: 1.08, cpcm: 2.06,   convm: 0.78, sym: 'RM ',  code: 'MYR' },
    'Mexico':       { ctm: 0.95, cpcm: 10.31,  convm: 0.78, sym: 'MX$',  code: 'MXN' },
    'Morocco':  { ctm: 0.9, cpcm: 1.78, convm: 0.7, sym: 'MAD ', code: 'MAD' },
    'Netherlands':  { ctm: 0.88, cpcm: 0.552,  convm: 0.86, sym: '€',    code: 'EUR' },
    'New Zealand':  { ctm: 0.90, cpcm: 1.122,  convm: 0.88, sym: 'NZ$',  code: 'NZD' },
    'Nigeria':  { ctm: 0.86, cpcm: 181.0, convm: 0.68, sym: '₦', code: 'NGN', noDecimal: true },
    'Norway':       { ctm: 0.85, cpcm: 18.56,  convm: 0.88, sym: 'NOK ', code: 'NOK' },
    'Pakistan':  { ctm: 1.08, cpcm: 15.6, convm: 0.6, sym: '₨', code: 'PKR', noDecimal: true },
    'Paraguay':  { ctm: 0.9, cpcm: 780.0, convm: 0.75, sym: '₲', code: 'PYG', noDecimal: true },
    'Peru':  { ctm: 0.89, cpcm: 0.627, convm: 0.74, sym: 'S/', code: 'PEN' },
    'Philippines':  { ctm: 1.18, cpcm: 6.19,   convm: 0.70, sym: '₱',    code: 'PHP' },
    'Poland':       { ctm: 0.88, cpcm: 1.134,  convm: 0.80, sym: 'zł',   code: 'PLN' },
    'Portugal':  { ctm: 0.89, cpcm: 0.325, convm: 0.86, sym: '€', code: 'EUR' },
    'Qatar':        { ctm: 0.80, cpcm: 2.111,  convm: 0.82, sym: 'QAR ', code: 'QAR' },
    'Romania':  { ctm: 0.83, cpcm: 0.94, convm: 0.78, sym: 'lei ', code: 'RON' },
    'Saudi Arabia': { ctm: 0.85, cpcm: 1.950,  convm: 0.80, sym: 'SAR ', code: 'SAR' },
    'Singapore':    { ctm: 0.95, cpcm: 0.837,  convm: 0.90, sym: 'S$',   code: 'SGD' },
    'South Africa': { ctm: 0.85, cpcm: 5.15,   convm: 0.72, sym: 'R ',   code: 'ZAR' },
    'South Korea':  { ctm: 0.98, cpcm: 567.0,  convm: 0.88, sym: '₩',    code: 'KRW', noDecimal: true },
    'Spain':        { ctm: 0.90, cpcm: 0.368,  convm: 0.80, sym: '€',    code: 'EUR' },
    'Sweden':       { ctm: 0.88, cpcm: 14.43,  convm: 0.86, sym: 'SEK ', code: 'SEK' },
    'Switzerland':  { ctm: 0.85, cpcm: 2.06,   convm: 0.88, sym: 'CHF ', code: 'CHF' },
    'Taiwan':  { ctm: 0.85, cpcm: 5.85, convm: 0.86, sym: 'NT$', code: 'TWD' },
    'Thailand':     { ctm: 1.10, cpcm: 7.700,  convm: 0.74, sym: '฿',    code: 'THB' },
    'Turkiye':      { ctm: 0.92, cpcm: 5.760,  convm: 0.75, sym: '₺',    code: 'TRY' },
    'UAE':          { ctm: 0.88, cpcm: 3.12,   convm: 0.85, sym: 'AED ', code: 'AED' },
    'UK':           { ctm: 0.92, cpcm: 0.61,   convm: 0.92, sym: '£',    code: 'GBP' },
    'USA':          { ctm: 1.00, cpcm: 1.00,   convm: 1.00, sym: '$',    code: 'USD' },
    'Ukraine':  { ctm: 0.88, cpcm: 4.76, convm: 0.82, sym: '₴', code: 'UAH', noDecimal: true },
    'Uruguay':  { ctm: 0.88, cpcm: 12.3, convm: 0.88, sym: '$U', code: 'UYU', noDecimal: true },
    'Venezuela':  { ctm: 0.95, cpcm: 0.09, convm: 0.65, sym: '$', code: 'USD' },
    'Vietnam':      { ctm: 1.12, cpcm: 8247.0, convm: 0.70, sym: '₫',    code: 'VND', noDecimal: true }
  };

  var countryNames = Object.keys(countries).sort();

  // [name, cpc_m, cpv_m, ctr_m, cvr_m]
  // CPM derived: cpc * ctr * 10  |  CPA derived: cpc / (cvr/100)
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.72, 0.82, 1.35, 1.22],
    ['Automotive',                             1.52, 1.28, 0.72, 0.52],
    ['Banking & Finance',                      1.85, 1.55, 0.60, 0.65],
    ['Beauty & Salons',                        0.68, 0.70, 1.48, 1.35],
    ['Crypto & Web3',                          1.68, 1.38, 0.82, 0.55],
    ['Dating',                                 1.02, 0.95, 1.15, 1.85],
    ['Education',                              0.85, 0.90, 0.92, 1.08],
    ['Electronics (E-Commerce)',               1.08, 1.02, 0.98, 0.88],
    ['Entertainment & Media',                  0.55, 0.62, 1.58, 1.42],
    ['Fitness & Gyms',                         0.78, 0.80, 1.22, 0.95],
    ['Flights',                                1.28, 1.18, 0.88, 0.42],
    ['Food & Beverage',                        0.62, 0.65, 1.42, 1.38],
    ['Furniture & Home Décor (E-Commerce)',    1.12, 1.05, 0.95, 0.72],
    ['Gaming',                                 0.65, 0.68, 1.52, 1.28],
    ['Healthcare',                             1.52, 1.35, 0.75, 0.72],
    ['Health & Wellness (E-Commerce)',         0.82, 0.80, 1.18, 1.05],
    ['Home Appliances (E-Commerce)',           1.15, 1.08, 0.88, 0.78],
    ['Home Services',                          1.38, 1.25, 0.78, 0.65],
    ['Hotels',                                 1.18, 1.10, 0.90, 0.58],
    ['Insurance',                              1.95, 1.68, 0.55, 0.50],
    ['Jewelry & Accessories (E-Commerce)',     0.95, 0.88, 1.12, 0.88],
    ['Jobs & Recruitment',                     1.28, 1.18, 0.88, 1.05],
    ['Legal',                                  2.25, 1.95, 0.52, 0.45],
    ['Logistics',                              1.45, 1.32, 0.72, 0.68],
    ['Moving & Cleaning Services',             1.35, 1.22, 0.80, 0.75],
    ['Non-Profit & Charity',                   0.45, 0.52, 1.32, 1.65],
    ['Online Courses & EdTech',                0.78, 0.82, 1.08, 1.15],
    ['Pet Products (E-Commerce)',              0.72, 0.75, 1.28, 1.22],
    ['Property',                               1.72, 1.52, 0.68, 0.40],
    ['Restaurants & Food Delivery',            0.62, 0.65, 1.45, 1.48],
    ['Skincare (E-Commerce)',                  0.72, 0.75, 1.38, 1.15],
    ['Software & SaaS',                        1.65, 1.45, 0.80, 0.75],
    ['Sports & Outdoors (E-Commerce)',         0.80, 0.82, 1.22, 1.08],
    ['Subscription Boxes',                     0.75, 0.78, 1.18, 1.18],
    ['Toys & Baby (E-Commerce)',               0.68, 0.72, 1.32, 1.25],
    ['Travel',                                 1.08, 0.98, 0.95, 0.48],
    ['Wedding & Events',                       1.05, 0.98, 1.08, 0.62]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], cpc_m = ind[1], cpv_m = ind[2], ctr_m = ind[3], cvr_m = ind[4];
      var ctr = r(BASE_CTR * cm.ctm   * ctr_m, 2);
      var cpc = r(BASE_CPC * cm.cpcm  * cpc_m, 2);
      var cpm = r(cpc * ctr * 10,              2);
      var cpv = r(BASE_CPV * cm.cpcm  * cpv_m, 3);
      var cvr = r(BASE_CVR * cm.convm * cvr_m, 2);
      var cpa = r(cpc / (cvr / 100),           2);
      data[cname][iname] = { ctr: ctr, cpc: cpc, cpm: cpm, cpv: cpv, cvr: cvr, cpa: cpa };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'TikTok Ads',
    channelDesc: 'In-Feed Video & TopView',
    channelSlug: 'tiktok-ads',
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
      { key: 'cpv', head: 'CPV',          fmt: 'money' },
      { key: 'cvr', head: 'Conv. Rate',   fmt: 'pct'   },
      { key: 'cpa', head: 'CPA',          fmt: 'money' }
    ],
    data: data
  };
})();
