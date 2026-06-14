(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  var BASE_CTR = 1.11, BASE_CPC = 0.97, BASE_CONV = 9.21, BASE_ROAS = 3.21;

  var countries = {
    'Argentina':    { ctm: 0.90, cpcm: 412.0,  convm: 0.72, roasm: 0.78, sym: 'AR$',  code: 'ARS' },
    'Australia':    { ctm: 0.95, cpcm: 1.24,   convm: 0.94, roasm: 0.92, sym: 'AU$',  code: 'AUD' },
    'Bahrain':      { ctm: 0.80, cpcm: 0.169,  convm: 0.84, roasm: 0.83, sym: 'BHD ', code: 'BHD' },
    'Brazil':       { ctm: 0.95, cpcm: 1.55,   convm: 0.82, roasm: 0.85, sym: 'R$',   code: 'BRL' },
    'Canada':       { ctm: 0.97, cpcm: 1.18,   convm: 0.96, roasm: 0.94, sym: 'CA$',  code: 'CAD' },
    'Denmark':      { ctm: 0.91, cpcm: 11.34,  convm: 0.93, roasm: 0.92, sym: 'DKK ', code: 'DKK' },
    'France':       { ctm: 0.90, cpcm: 0.506,  convm: 0.89, roasm: 0.87, sym: '€',    code: 'EUR' },
    'Germany':      { ctm: 0.88, cpcm: 0.62,   convm: 0.91, roasm: 0.89, sym: '€',    code: 'EUR' },
    'Hong Kong':    { ctm: 0.88, cpcm: 4.301,  convm: 0.91, roasm: 0.90, sym: 'HK$',  code: 'HKD' },
    'India':        { ctm: 0.92, cpcm: 8.25,   convm: 0.75, roasm: 0.82, sym: '₹',    code: 'INR' },
    'Indonesia':    { ctm: 0.88, cpcm: 1031.0, convm: 0.72, roasm: 0.78, sym: 'Rp ',  code: 'IDR', noDecimal: true },
    'Ireland':      { ctm: 0.92, cpcm: 0.77,   convm: 0.94, roasm: 0.91, sym: '€',    code: 'EUR' },
    'Italy':        { ctm: 0.88, cpcm: 0.386,  convm: 0.86, roasm: 0.85, sym: '€',    code: 'EUR' },
    'Japan':        { ctm: 0.82, cpcm: 72.0,   convm: 0.88, roasm: 0.88, sym: '¥',    code: 'JPY', noDecimal: true },
    'Malaysia':     { ctm: 0.85, cpcm: 2.06,   convm: 0.82, roasm: 0.84, sym: 'RM ',  code: 'MYR' },
    'Mexico':       { ctm: 0.90, cpcm: 10.31,  convm: 0.83, roasm: 0.84, sym: 'MX$',  code: 'MXN' },
    'Netherlands':  { ctm: 0.93, cpcm: 0.552,  convm: 0.92, roasm: 0.90, sym: '€',    code: 'EUR' },
    'New Zealand':  { ctm: 0.94, cpcm: 1.122,  convm: 0.93, roasm: 0.91, sym: 'NZ$',  code: 'NZD' },
    'Norway':       { ctm: 0.90, cpcm: 18.56,  convm: 0.94, roasm: 0.94, sym: 'NOK ', code: 'NOK' },
    'Philippines':  { ctm: 0.96, cpcm: 6.19,   convm: 0.76, roasm: 0.78, sym: '₱',    code: 'PHP' },
    'Poland':       { ctm: 0.85, cpcm: 1.134,  convm: 0.84, roasm: 0.88, sym: 'zł',   code: 'PLN' },
    'Qatar':        { ctm: 0.82, cpcm: 2.111,  convm: 0.86, roasm: 0.85, sym: 'QAR ', code: 'QAR' },
    'Saudi Arabia': { ctm: 0.80, cpcm: 1.950,  convm: 0.85, roasm: 0.84, sym: 'SAR ', code: 'SAR' },
    'Singapore':    { ctm: 0.90, cpcm: 0.837,  convm: 0.93, roasm: 0.92, sym: 'S$',   code: 'SGD' },
    'South Africa': { ctm: 0.82, cpcm: 5.15,   convm: 0.78, roasm: 0.80, sym: 'R ',   code: 'ZAR' },
    'South Korea':  { ctm: 0.85, cpcm: 567.0,  convm: 0.90, roasm: 0.89, sym: '₩',    code: 'KRW', noDecimal: true },
    'Spain':        { ctm: 0.92, cpcm: 0.368,  convm: 0.88, roasm: 0.86, sym: '€',    code: 'EUR' },
    'Sweden':       { ctm: 0.92, cpcm: 14.43,  convm: 0.94, roasm: 0.92, sym: 'SEK ', code: 'SEK' },
    'Switzerland':  { ctm: 0.87, cpcm: 2.06,   convm: 0.93, roasm: 0.92, sym: 'CHF ', code: 'CHF' },
    'Thailand':     { ctm: 0.78, cpcm: 7.700,  convm: 0.82, roasm: 0.85, sym: '฿',    code: 'THB' },
    'Turkiye':      { ctm: 0.82, cpcm: 5.760,  convm: 0.80, roasm: 0.80, sym: '₺',    code: 'TRY' },
    'UAE':          { ctm: 0.82, cpcm: 3.12,   convm: 0.87, roasm: 0.86, sym: 'AED ', code: 'AED' },
    'UK':           { ctm: 0.95, cpcm: 0.61,   convm: 0.98, roasm: 0.96, sym: '£',    code: 'GBP' },
    'USA':          { ctm: 1.00, cpcm: 1.00,   convm: 1.00, roasm: 1.00, sym: '$',    code: 'USD' },
    'Vietnam':      { ctm: 0.88, cpcm: 8247.0, convm: 0.77, roasm: 0.80, sym: '₫',    code: 'VND', noDecimal: true }
  };

  var countryNames = Object.keys(countries).sort();

  // Array of [name, cpc_mult, ctr_mult, conv_mult, roas_mult]
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.72, 1.35, 1.18, 1.32],
    ['Automotive',                             1.88, 0.72, 0.48, 0.85],
    ['Banking & Finance',                      2.15, 0.62, 0.65, 0.78],
    ['Beauty & Salons',                        0.78, 1.22, 1.12, 1.45],
    ['Crypto & Web3',                          1.92, 0.85, 0.55, 0.72],
    ['Dating',                                 1.15, 1.18, 1.85, 1.25],
    ['Education',                              0.92, 0.82, 0.98, 1.05],
    ['Electronics (E-Commerce)',               1.12, 0.98, 0.88, 0.95],
    ['Entertainment & Media',                  0.58, 1.48, 1.42, 1.15],
    ['Fitness & Gyms',                         0.85, 1.15, 0.92, 1.18],
    ['Flights',                                1.32, 0.88, 0.42, 1.85],
    ['Food & Beverage',                        0.62, 1.25, 1.35, 1.55],
    ['Furniture & Home Décor (E-Commerce)',    1.18, 0.95, 0.72, 0.92],
    ['Gaming',                                 0.68, 1.42, 1.28, 1.35],
    ['Healthcare',                             1.68, 0.75, 0.72, 0.88],
    ['Health & Wellness (E-Commerce)',         0.92, 1.12, 1.05, 1.28],
    ['Home Appliances (E-Commerce)',           1.22, 0.88, 0.78, 0.88],
    ['Home Services',                          1.52, 0.78, 0.65, 0.95],
    ['Hotels',                                 1.28, 0.92, 0.58, 1.95],
    ['Insurance',                              2.52, 0.55, 0.52, 0.72],
    ['Jewelry & Accessories (E-Commerce)',     1.08, 1.15, 0.85, 1.42],
    ['Jobs & Recruitment',                     1.42, 0.88, 1.05, 0.82],
    ['Legal',                                  2.82, 0.52, 0.45, 0.68],
    ['Logistics',                              1.58, 0.72, 0.68, 0.88],
    ['Moving & Cleaning Services',             1.48, 0.82, 0.75, 1.05],
    ['Non-Profit & Charity',                   0.45, 1.32, 1.65, 1.15],
    ['Online Courses & EdTech',                0.82, 1.05, 1.15, 1.22],
    ['Pet Products (E-Commerce)',              0.72, 1.28, 1.22, 1.38],
    ['Property',                               1.95, 0.68, 0.42, 0.75],
    ['Restaurants & Food Delivery',            0.65, 1.32, 1.45, 1.65],
    ['Skincare (E-Commerce)',                  0.88, 1.25, 1.12, 1.35],
    ['Software & SaaS',                        1.72, 0.82, 0.75, 0.92],
    ['Sports & Outdoors (E-Commerce)',         0.82, 1.18, 1.08, 1.25],
    ['Subscription Boxes',                     0.75, 1.22, 1.18, 1.42],
    ['Toys & Baby (E-Commerce)',               0.68, 1.35, 1.25, 1.32],
    ['Travel',                                 1.15, 0.95, 0.48, 1.75],
    ['Wedding & Events',                       1.12, 1.08, 0.62, 1.15]
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
    channel:     'Meta Ads',
    channelSlug: 'meta-ads',
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
    data:        data
  };
})();
