(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  // Shopify store performance averages (cross-industry, USA baseline)
  // Figures represent blended performance across paid + organic + email traffic.
  // CPA is the blended cost to acquire a paying customer across all marketing channels.
  var BASE_CVR    = 2.50;  // %
  var BASE_CPA    = 42.0;  // USD — blended cost per acquisition (all channels)
  var BASE_ROAS   = 3.20;  // x   — blended return on ad spend
  var BASE_CAR    = 70.0;  // %   — cart abandonment rate (higher = worse)
  var BASE_MARGIN = 35.0;  // %   — net profit margin after COGS, shipping, returns

  // cvrm   = CVR multiplier (eCommerce maturity, purchasing behaviour)
  // cpam   = CPA cost multiplier (exchange rate + local ad market costs)
  // roasm  = ROAS multiplier (ad efficiency in local market)
  // carm   = Cart abandonment multiplier (>1 = more abandonment)
  // marginm = Profit margin multiplier (competition, logistics, taxes)
  var countries = {
    'Argentina':    { cvrm: 0.58, cpam: 412.0,  roasm: 0.72, carm: 1.22, marginm: 0.72, sym: 'AR$',  code: 'ARS' },
    'Australia':    { cvrm: 0.88, cpam: 1.24,   roasm: 0.88, carm: 1.03, marginm: 0.90, sym: 'AU$',  code: 'AUD' },
    'Bahrain':      { cvrm: 0.72, cpam: 0.169,  roasm: 0.80, carm: 1.08, marginm: 0.85, sym: 'BHD ', code: 'BHD' },
    'Brazil':       { cvrm: 0.64, cpam: 1.55,   roasm: 0.82, carm: 1.18, marginm: 0.78, sym: 'R$',   code: 'BRL' },
    'Canada':       { cvrm: 0.92, cpam: 1.18,   roasm: 0.90, carm: 1.01, marginm: 0.95, sym: 'CA$',  code: 'CAD' },
    'Denmark':      { cvrm: 0.85, cpam: 11.34,  roasm: 0.87, carm: 1.02, marginm: 0.92, sym: 'DKK ', code: 'DKK' },
    'France':       { cvrm: 0.76, cpam: 0.506,  roasm: 0.78, carm: 1.07, marginm: 0.85, sym: '€',    code: 'EUR' },
    'Germany':      { cvrm: 0.80, cpam: 0.62,   roasm: 0.82, carm: 1.09, marginm: 0.80, sym: '€',    code: 'EUR' },
    'Hong Kong':    { cvrm: 0.82, cpam: 4.301,  roasm: 0.85, carm: 1.06, marginm: 0.88, sym: 'HK$',  code: 'HKD' },
    'India':        { cvrm: 0.60, cpam: 8.25,   roasm: 1.10, carm: 1.20, marginm: 0.68, sym: '₹',    code: 'INR' },
    'Indonesia':    { cvrm: 0.52, cpam: 1031.0, roasm: 0.92, carm: 1.28, marginm: 0.62, sym: 'Rp ',  code: 'IDR', noDecimal: true },
    'Ireland':      { cvrm: 0.90, cpam: 0.77,   roasm: 0.90, carm: 1.01, marginm: 0.92, sym: '€',    code: 'EUR' },
    'Italy':        { cvrm: 0.72, cpam: 0.386,  roasm: 0.75, carm: 1.10, marginm: 0.82, sym: '€',    code: 'EUR' },
    'Japan':        { cvrm: 0.72, cpam: 72.0,   roasm: 0.70, carm: 1.12, marginm: 0.80, sym: '¥',    code: 'JPY', noDecimal: true },
    'Malaysia':     { cvrm: 0.65, cpam: 2.06,   roasm: 0.82, carm: 1.15, marginm: 0.75, sym: 'RM ',  code: 'MYR' },
    'Mexico':       { cvrm: 0.62, cpam: 10.31,  roasm: 0.80, carm: 1.18, marginm: 0.78, sym: 'MX$',  code: 'MXN' },
    'Netherlands':  { cvrm: 0.88, cpam: 0.552,  roasm: 0.90, carm: 1.00, marginm: 0.90, sym: '€',    code: 'EUR' },
    'New Zealand':  { cvrm: 0.85, cpam: 1.122,  roasm: 0.85, carm: 1.03, marginm: 0.88, sym: 'NZ$',  code: 'NZD' },
    'Norway':       { cvrm: 0.88, cpam: 18.56,  roasm: 0.88, carm: 1.01, marginm: 0.95, sym: 'NOK ', code: 'NOK' },
    'Philippines':  { cvrm: 0.55, cpam: 6.19,   roasm: 0.85, carm: 1.25, marginm: 0.68, sym: '₱',    code: 'PHP' },
    'Poland':       { cvrm: 0.70, cpam: 1.134,  roasm: 0.78, carm: 1.10, marginm: 0.80, sym: 'zł',   code: 'PLN' },
    'Qatar':        { cvrm: 0.75, cpam: 2.111,  roasm: 0.82, carm: 1.07, marginm: 0.88, sym: 'QAR ', code: 'QAR' },
    'Saudi Arabia': { cvrm: 0.68, cpam: 1.950,  roasm: 0.80, carm: 1.12, marginm: 0.85, sym: 'SAR ', code: 'SAR' },
    'Singapore':    { cvrm: 0.80, cpam: 0.837,  roasm: 0.87, carm: 1.05, marginm: 0.90, sym: 'S$',   code: 'SGD' },
    'South Africa': { cvrm: 0.58, cpam: 5.15,   roasm: 0.75, carm: 1.20, marginm: 0.72, sym: 'R ',   code: 'ZAR' },
    'South Korea':  { cvrm: 0.78, cpam: 567.0,  roasm: 0.82, carm: 1.08, marginm: 0.82, sym: '₩',    code: 'KRW', noDecimal: true },
    'Spain':        { cvrm: 0.75, cpam: 0.368,  roasm: 0.78, carm: 1.08, marginm: 0.82, sym: '€',    code: 'EUR' },
    'Sweden':       { cvrm: 0.88, cpam: 14.43,  roasm: 0.88, carm: 1.02, marginm: 0.92, sym: 'SEK ', code: 'SEK' },
    'Switzerland':  { cvrm: 0.88, cpam: 2.06,   roasm: 0.93, carm: 0.97, marginm: 1.12, sym: 'CHF ', code: 'CHF' },
    'Thailand':     { cvrm: 0.55, cpam: 7.700,  roasm: 0.82, carm: 1.22, marginm: 0.70, sym: '฿',    code: 'THB' },
    'Turkiye':      { cvrm: 0.62, cpam: 5.760,  roasm: 0.78, carm: 1.15, marginm: 0.75, sym: '₺',    code: 'TRY' },
    'UAE':          { cvrm: 0.76, cpam: 3.12,   roasm: 0.87, carm: 1.06, marginm: 0.90, sym: 'AED ', code: 'AED' },
    'UK':           { cvrm: 0.95, cpam: 0.61,   roasm: 0.95, carm: 0.97, marginm: 0.92, sym: '£',    code: 'GBP' },
    'USA':          { cvrm: 1.00, cpam: 1.00,   roasm: 1.00, carm: 1.00, marginm: 1.00, sym: '$',    code: 'USD' },
    'Vietnam':      { cvrm: 0.48, cpam: 8247.0, roasm: 0.85, carm: 1.32, marginm: 0.62, sym: '₫',    code: 'VND', noDecimal: true }
  };

  var countryNames = Object.keys(countries).sort();

  // [name, cpa_m, cvr_m, roas_m, car_m, margin_m]
  // Shopify works across all verticals but shines in physical & digital product eCommerce.
  // Non-eCommerce industries (Legal, Logistics, etc.) represent service/booking use cases.
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   0.82, 1.15, 0.88, 1.10, 0.72],
    ['Automotive',                             2.25, 0.28, 0.65, 1.22, 0.52],
    ['Banking & Finance',                      1.75, 0.45, 0.88, 1.18, 1.48],
    ['Beauty & Salons',                        0.68, 1.32, 1.18, 1.02, 1.08],
    ['Crypto & Web3',                          1.42, 0.52, 0.80, 1.28, 0.62],
    ['Dating',                                 0.95, 0.88, 0.95, 1.12, 0.88],
    ['Education',                              0.72, 1.08, 1.28, 1.05, 1.42],
    ['Electronics (E-Commerce)',               0.92, 0.85, 0.92, 1.15, 0.38],
    ['Entertainment & Media',                  0.62, 1.12, 1.22, 1.02, 1.48],
    ['Fitness & Gyms',                         0.78, 1.12, 1.15, 1.05, 0.92],
    ['Flights',                                1.52, 0.52, 0.65, 1.32, 0.32],
    ['Food & Beverage',                        0.65, 1.28, 1.08, 0.92, 0.58],
    ['Furniture & Home Décor (E-Commerce)',    0.88, 0.72, 0.92, 1.22, 0.65],
    ['Gaming',                                 0.72, 1.15, 1.12, 1.05, 0.75],
    ['Healthcare',                             0.85, 0.88, 1.15, 1.05, 1.18],
    ['Health & Wellness (E-Commerce)',         0.72, 1.28, 1.28, 0.95, 1.12],
    ['Home Appliances (E-Commerce)',           1.05, 0.68, 0.78, 1.25, 0.35],
    ['Home Services',                          1.12, 0.65, 0.82, 1.15, 0.78],
    ['Hotels',                                 1.22, 0.58, 0.75, 1.35, 0.52],
    ['Insurance',                              1.52, 0.42, 0.82, 1.25, 1.55],
    ['Jewelry & Accessories (E-Commerce)',     0.82, 0.88, 1.08, 1.20, 1.25],
    ['Jobs & Recruitment',                     1.15, 0.55, 0.80, 1.15, 0.88],
    ['Legal',                                  1.82, 0.38, 0.65, 1.28, 1.32],
    ['Logistics',                              1.25, 0.55, 0.75, 1.18, 0.62],
    ['Moving & Cleaning Services',             0.92, 0.72, 0.88, 1.12, 0.75],
    ['Non-Profit & Charity',                   0.42, 1.42, 1.52, 0.82, 0.42],
    ['Online Courses & EdTech',                0.68, 1.15, 1.38, 0.95, 1.55],
    ['Pet Products (E-Commerce)',              0.68, 1.28, 1.22, 0.92, 0.92],
    ['Property',                               1.62, 0.32, 0.72, 1.38, 0.42],
    ['Restaurants & Food Delivery',            0.58, 1.32, 1.12, 0.88, 0.45],
    ['Skincare (E-Commerce)',                  0.68, 1.35, 1.28, 0.95, 1.15],
    ['Software & SaaS',                        0.85, 0.88, 1.22, 1.05, 1.68],
    ['Sports & Outdoors (E-Commerce)',         0.78, 1.12, 1.10, 1.05, 0.78],
    ['Subscription Boxes',                     0.65, 1.18, 1.32, 0.90, 0.92],
    ['Toys & Baby (E-Commerce)',               0.68, 1.22, 1.08, 1.05, 0.68],
    ['Travel',                                 1.15, 0.58, 0.78, 1.32, 0.48],
    ['Wedding & Events',                       0.92, 0.75, 0.95, 1.20, 0.88]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], cpa_m = ind[1], cvr_m = ind[2], roas_m = ind[3], car_m = ind[4], margin_m = ind[5];
      var cvr    = r(BASE_CVR    * cm.cvrm    * cvr_m,    2);
      var cpa    = r(BASE_CPA    * cm.cpam    * cpa_m,    2);
      var roas   = r(BASE_ROAS   * cm.roasm   * roas_m,   2);
      var car    = r(Math.min(95, BASE_CAR    * cm.carm   * car_m),    1);
      var margin = r(BASE_MARGIN * cm.marginm * margin_m, 1);
      data[cname][iname] = { cvr: cvr, cpa: cpa, roas: roas, car: car, margin: margin };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'Shopify',
    channelDesc: 'eCommerce Store Performance',
    channelSlug: 'shopify',
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
      { key: 'cvr',    head: 'Conv. Rate',         fmt: 'pct'   },
      { key: 'cpa',    head: 'CPA',                fmt: 'money' },
      { key: 'roas',   head: 'ROAS',               fmt: 'roas'  },
      { key: 'car',    head: 'Cart Abandonment',   fmt: 'pct'   },
      { key: 'margin', head: 'Profit Margin',      fmt: 'pct'   }
    ],
    data: data
  };
})();
