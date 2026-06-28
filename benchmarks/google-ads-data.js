(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  // Google Ads Search averages (cross-industry baseline)
  var BASE_CTR = 3.51, BASE_CPC = 2.69, BASE_CONV = 4.40, BASE_ROAS = 4.10;

  var countries = {
    'Argentina':    { ctm: 0.90, cpcm: 412.0,  convm: 0.72, roasm: 0.78, sym: 'AR$',  code: 'ARS' },
    'Australia':    { ctm: 0.95, cpcm: 1.24,   convm: 0.94, roasm: 0.92, sym: 'AU$',  code: 'AUD' },
    'Austria':  { ctm: 0.9, cpcm: 0.342, convm: 0.91, roasm: 0.89, sym: '€', code: 'EUR' },
    'Bahrain':      { ctm: 0.80, cpcm: 0.169,  convm: 0.84, roasm: 0.83, sym: 'BHD ', code: 'BHD' },
    'Bangladesh':  { ctm: 1.1, cpcm: 4.09, convm: 0.58, roasm: 0.52, sym: '৳', code: 'BDT', noDecimal: true },
    'Belgium':  { ctm: 0.91, cpcm: 0.359, convm: 0.9, roasm: 0.88, sym: '€', code: 'EUR' },
    'Brazil':       { ctm: 0.95, cpcm: 1.55,   convm: 0.82, roasm: 0.85, sym: 'R$',   code: 'BRL' },
    'Bulgaria':  { ctm: 0.82, cpcm: 0.331, convm: 0.76, roasm: 0.78, sym: 'лв ', code: 'BGN' },
    'Canada':       { ctm: 0.97, cpcm: 1.18,   convm: 0.96, roasm: 0.94, sym: 'CA$',  code: 'CAD' },
    'Chile':  { ctm: 0.88, cpcm: 176.0, convm: 0.75, roasm: 0.8, sym: 'CLP ', code: 'CLP', noDecimal: true },
    'Colombia':  { ctm: 0.9, cpcm: 609.0, convm: 0.73, roasm: 0.78, sym: 'COP ', code: 'COP', noDecimal: true },
    'Croatia':  { ctm: 0.84, cpcm: 0.274, convm: 0.8, roasm: 0.82, sym: '€', code: 'EUR' },
    'Czechia':  { ctm: 0.85, cpcm: 5.13, convm: 0.84, roasm: 0.86, sym: 'Kč ', code: 'CZK' },
    'Denmark':      { ctm: 0.91, cpcm: 11.34,  convm: 0.93, roasm: 0.92, sym: 'DKK ', code: 'DKK' },
    'Ecuador':  { ctm: 0.88, cpcm: 0.204, convm: 0.8, roasm: 0.78, sym: '$', code: 'USD' },
    'Egypt':  { ctm: 0.92, cpcm: 7.4, convm: 0.72, roasm: 0.68, sym: 'EGP ', code: 'EGP', noDecimal: true },
    'Finland':  { ctm: 0.92, cpcm: 0.376, convm: 0.92, roasm: 0.9, sym: '€', code: 'EUR' },
    'France':       { ctm: 0.90, cpcm: 0.506,  convm: 0.89, roasm: 0.87, sym: '€',    code: 'EUR' },
    'Germany':      { ctm: 0.88, cpcm: 0.62,   convm: 0.91, roasm: 0.89, sym: '€',    code: 'EUR' },
    'Greece':  { ctm: 0.86, cpcm: 0.496, convm: 0.88, roasm: 0.85, sym: '€', code: 'EUR' },
    'Hong Kong':    { ctm: 0.88, cpcm: 4.301,  convm: 0.91, roasm: 0.90, sym: 'HK$',  code: 'HKD' },
    'Hungary':  { ctm: 0.84, cpcm: 112.6, convm: 0.85, roasm: 0.8, sym: 'Ft ', code: 'HUF', noDecimal: true },
    'India':        { ctm: 0.92, cpcm: 8.25,   convm: 0.75, roasm: 0.82, sym: '₹',    code: 'INR' },
    'Indonesia':    { ctm: 0.88, cpcm: 1031.0, convm: 0.72, roasm: 0.78, sym: 'Rp ',  code: 'IDR', noDecimal: true },
    'Ireland':      { ctm: 0.92, cpcm: 0.77,   convm: 0.94, roasm: 0.91, sym: '€',    code: 'EUR' },
    'Israel':  { ctm: 0.88, cpcm: 2.41, convm: 1.02, roasm: 0.92, sym: '₪', code: 'ILS' },
    'Italy':        { ctm: 0.88, cpcm: 0.386,  convm: 0.86, roasm: 0.85, sym: '€',    code: 'EUR' },
    'Japan':        { ctm: 0.82, cpcm: 72.0,   convm: 0.88, roasm: 0.88, sym: '¥',    code: 'JPY', noDecimal: true },
    'Kenya':  { ctm: 0.87, cpcm: 13.5, convm: 0.7, roasm: 0.74, sym: 'KSh ', code: 'KES' },
    'Malaysia':     { ctm: 0.85, cpcm: 2.06,   convm: 0.82, roasm: 0.84, sym: 'RM ',  code: 'MYR' },
    'Mexico':       { ctm: 0.90, cpcm: 10.31,  convm: 0.83, roasm: 0.84, sym: 'MX$',  code: 'MXN' },
    'Morocco':  { ctm: 0.9, cpcm: 1.78, convm: 0.7, roasm: 0.68, sym: 'MAD ', code: 'MAD' },
    'Netherlands':  { ctm: 0.93, cpcm: 0.552,  convm: 0.92, roasm: 0.90, sym: '€',    code: 'EUR' },
    'New Zealand':  { ctm: 0.94, cpcm: 1.122,  convm: 0.93, roasm: 0.91, sym: 'NZ$',  code: 'NZD' },
    'Nigeria':  { ctm: 0.86, cpcm: 181.0, convm: 0.68, roasm: 0.72, sym: '₦', code: 'NGN', noDecimal: true },
    'Norway':       { ctm: 0.90, cpcm: 18.56,  convm: 0.94, roasm: 0.94, sym: 'NOK ', code: 'NOK' },
    'Pakistan':  { ctm: 1.08, cpcm: 15.6, convm: 0.6, roasm: 0.55, sym: '₨', code: 'PKR', noDecimal: true },
    'Paraguay':  { ctm: 0.9, cpcm: 780.0, convm: 0.75, roasm: 0.72, sym: '₲', code: 'PYG', noDecimal: true },
    'Peru':  { ctm: 0.89, cpcm: 0.627, convm: 0.74, roasm: 0.79, sym: 'S/', code: 'PEN' },
    'Philippines':  { ctm: 0.96, cpcm: 6.19,   convm: 0.76, roasm: 0.78, sym: '₱',    code: 'PHP' },
    'Poland':       { ctm: 0.85, cpcm: 1.134,  convm: 0.84, roasm: 0.88, sym: 'zł',   code: 'PLN' },
    'Portugal':  { ctm: 0.89, cpcm: 0.325, convm: 0.86, roasm: 0.84, sym: '€', code: 'EUR' },
    'Qatar':        { ctm: 0.82, cpcm: 2.111,  convm: 0.86, roasm: 0.85, sym: 'QAR ', code: 'QAR' },
    'Romania':  { ctm: 0.83, cpcm: 0.94, convm: 0.78, roasm: 0.8, sym: 'lei ', code: 'RON' },
    'Saudi Arabia': { ctm: 0.80, cpcm: 1.950,  convm: 0.85, roasm: 0.84, sym: 'SAR ', code: 'SAR' },
    'Singapore':    { ctm: 0.90, cpcm: 0.837,  convm: 0.93, roasm: 0.92, sym: 'S$',   code: 'SGD' },
    'South Africa': { ctm: 0.82, cpcm: 5.15,   convm: 0.78, roasm: 0.80, sym: 'R ',   code: 'ZAR' },
    'South Korea':  { ctm: 0.85, cpcm: 567.0,  convm: 0.90, roasm: 0.89, sym: '₩',    code: 'KRW', noDecimal: true },
    'Spain':        { ctm: 0.92, cpcm: 0.368,  convm: 0.88, roasm: 0.86, sym: '€',    code: 'EUR' },
    'Sweden':       { ctm: 0.92, cpcm: 14.43,  convm: 0.94, roasm: 0.92, sym: 'SEK ', code: 'SEK' },
    'Switzerland':  { ctm: 0.87, cpcm: 2.06,   convm: 0.93, roasm: 0.92, sym: 'CHF ', code: 'CHF' },
    'Taiwan':  { ctm: 0.85, cpcm: 5.85, convm: 0.86, roasm: 0.88, sym: 'NT$', code: 'TWD' },
    'Thailand':     { ctm: 0.78, cpcm: 7.700,  convm: 0.82, roasm: 0.85, sym: '฿',    code: 'THB' },
    'Turkiye':      { ctm: 0.82, cpcm: 5.760,  convm: 0.80, roasm: 0.80, sym: '₺',    code: 'TRY' },
    'UAE':          { ctm: 0.82, cpcm: 3.12,   convm: 0.87, roasm: 0.86, sym: 'AED ', code: 'AED' },
    'UK':           { ctm: 0.95, cpcm: 0.61,   convm: 0.98, roasm: 0.96, sym: '£',    code: 'GBP' },
    'USA':          { ctm: 1.00, cpcm: 1.00,   convm: 1.00, roasm: 1.00, sym: '$',    code: 'USD' },
    'Ukraine':  { ctm: 0.88, cpcm: 4.76, convm: 0.82, roasm: 0.76, sym: '₴', code: 'UAH', noDecimal: true },
    'Uruguay':  { ctm: 0.88, cpcm: 12.3, convm: 0.88, roasm: 0.84, sym: '$U', code: 'UYU', noDecimal: true },
    'Venezuela':  { ctm: 0.95, cpcm: 0.09, convm: 0.65, roasm: 0.62, sym: '$', code: 'USD' },
    'Vietnam':      { ctm: 0.88, cpcm: 8247.0, convm: 0.77, roasm: 0.80, sym: '₫',    code: 'VND', noDecimal: true }
  };

  var countryNames = Object.keys(countries).sort();

  // Array of [name, cpc_mult, ctr_mult, conv_mult, roas_mult]
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.68, 1.28, 1.15, 1.28],
    ['Automotive',                             2.12, 0.68, 0.52, 0.88],
    ['Banking & Finance',                      2.85, 0.58, 0.62, 0.80],
    ['Beauty & Salons',                        0.82, 1.18, 1.08, 1.38],
    ['Crypto & Web3',                          2.15, 0.78, 0.48, 0.70],
    ['Dating',                                 1.08, 1.12, 1.72, 1.20],
    ['Education',                              0.88, 0.92, 1.05, 1.08],
    ['Electronics (E-Commerce)',               1.18, 0.95, 0.82, 0.92],
    ['Entertainment & Media',                  0.62, 1.42, 1.38, 1.12],
    ['Fitness & Gyms',                         0.92, 1.08, 0.88, 1.15],
    ['Flights',                                1.45, 0.85, 0.38, 1.88],
    ['Food & Beverage',                        0.68, 1.22, 1.28, 1.52],
    ['Furniture & Home Décor (E-Commerce)',    1.22, 0.92, 0.68, 0.90],
    ['Gaming',                                 0.72, 1.38, 1.22, 1.30],
    ['Healthcare',                             1.92, 0.72, 0.68, 0.85],
    ['Health & Wellness (E-Commerce)',         0.95, 1.08, 1.02, 1.25],
    ['Home Appliances (E-Commerce)',           1.28, 0.85, 0.75, 0.85],
    ['Home Services',                          1.68, 0.75, 0.62, 0.92],
    ['Hotels',                                 1.35, 0.88, 0.55, 1.92],
    ['Insurance',                              3.12, 0.52, 0.48, 0.75],
    ['Jewelry & Accessories (E-Commerce)',     1.12, 1.10, 0.82, 1.38],
    ['Jobs & Recruitment',                     1.52, 0.85, 1.02, 0.80],
    ['Legal',                                  3.45, 0.48, 0.42, 0.65],
    ['Logistics',                              1.65, 0.70, 0.65, 0.85],
    ['Moving & Cleaning Services',             1.55, 0.78, 0.72, 1.02],
    ['Non-Profit & Charity',                   0.48, 1.28, 1.58, 1.12],
    ['Online Courses & EdTech',                0.85, 1.02, 1.12, 1.18],
    ['Pet Products (E-Commerce)',              0.75, 1.22, 1.18, 1.32],
    ['Property',                               2.08, 0.65, 0.38, 0.72],
    ['Restaurants & Food Delivery',            0.70, 1.28, 1.42, 1.60],
    ['Skincare (E-Commerce)',                  0.92, 1.20, 1.08, 1.32],
    ['Software & SaaS',                        1.88, 0.78, 0.72, 0.90],
    ['Sports & Outdoors (E-Commerce)',         0.85, 1.15, 1.05, 1.22],
    ['Subscription Boxes',                     0.78, 1.18, 1.15, 1.38],
    ['Toys & Baby (E-Commerce)',               0.72, 1.30, 1.22, 1.28],
    ['Travel',                                 1.22, 0.92, 0.45, 1.72],
    ['Wedding & Events',                       1.18, 1.05, 0.58, 1.12]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], cpc_m = ind[1], ctr_m = ind[2], conv_m = ind[3], roas_m = ind[4];
      var ctr  = r(BASE_CTR  * cm.ctm   * ctr_m,  2);
      var cpc  = r(BASE_CPC  * cm.cpcm  * cpc_m,  2);
      var cpm  = r(cpc * ctr * 10,                 2);
      var conv = r(BASE_CONV * cm.convm * conv_m,  2);
      var cpa  = r(cpc / (conv / 100),             2);
      var roas = r(BASE_ROAS * cm.roasm * roas_m,  2);
      data[cname][iname] = { ctr: ctr, cpc: cpc, cpm: cpm, conv_rate: conv, cpa: cpa, roas: roas };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'Google Ads',
    channelDesc: 'Search, Shopping & Display',
    channelSlug: 'google-ads',
    hideCPM:     true,
    updated:     'June 2026',
    countries:   countryNames,
    currencies:  (function () {
      var o = {};
      countryNames.forEach(function (c) {
        o[c] = { sym: countries[c].sym, code: countries[c].code, noDecimal: !!countries[c].noDecimal };
      });
      return o;
    })(),
    industries:  industryNames,
    data:        data
  };
})();
