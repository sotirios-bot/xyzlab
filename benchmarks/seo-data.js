(function () {
  function r(v, d) { return Math.round(v * Math.pow(10, d)) / Math.pow(10, d); }

  var BASE_TRAFFIC = 8500;
  var BASE_CTR     = 3.80;
  var BASE_BL      = 62;
  var BASE_KD      = 45;
  var BASE_DA      = 42;

  // trafficm = market size for organic search
  // ctrm     = organic CTR adjustment
  // compm    = competition level (KD, DA, backlinks)
  var countries = {
    'Argentina':    { trafficm: 0.22, ctrm: 0.88, compm: 0.62 },
    'Australia':    { trafficm: 0.35, ctrm: 1.05, compm: 0.85 },
    'Bahrain':      { trafficm: 0.04, ctrm: 0.85, compm: 0.68 },
    'Brazil':       { trafficm: 0.72, ctrm: 0.88, compm: 0.72 },
    'Canada':       { trafficm: 0.42, ctrm: 1.05, compm: 0.88 },
    'Denmark':      { trafficm: 0.10, ctrm: 1.02, compm: 0.78 },
    'France':       { trafficm: 0.48, ctrm: 0.92, compm: 0.82 },
    'Germany':      { trafficm: 0.55, ctrm: 0.95, compm: 0.88 },
    'Hong Kong':    { trafficm: 0.10, ctrm: 0.92, compm: 0.78 },
    'India':        { trafficm: 1.45, ctrm: 0.88, compm: 0.70 },
    'Indonesia':    { trafficm: 0.55, ctrm: 0.85, compm: 0.65 },
    'Ireland':      { trafficm: 0.08, ctrm: 1.05, compm: 0.82 },
    'Italy':        { trafficm: 0.32, ctrm: 0.90, compm: 0.75 },
    'Japan':        { trafficm: 0.72, ctrm: 0.80, compm: 0.75 },
    'Malaysia':     { trafficm: 0.14, ctrm: 0.90, compm: 0.68 },
    'Mexico':       { trafficm: 0.35, ctrm: 0.85, compm: 0.68 },
    'Netherlands':  { trafficm: 0.15, ctrm: 0.98, compm: 0.80 },
    'New Zealand':  { trafficm: 0.10, ctrm: 1.05, compm: 0.75 },
    'Norway':       { trafficm: 0.10, ctrm: 1.02, compm: 0.78 },
    'Philippines':  { trafficm: 0.22, ctrm: 0.90, compm: 0.68 },
    'Poland':       { trafficm: 0.18, ctrm: 0.88, compm: 0.68 },
    'Qatar':        { trafficm: 0.05, ctrm: 0.85, compm: 0.72 },
    'Saudi Arabia': { trafficm: 0.14, ctrm: 0.82, compm: 0.68 },
    'Singapore':    { trafficm: 0.08, ctrm: 0.95, compm: 0.82 },
    'South Africa': { trafficm: 0.15, ctrm: 0.90, compm: 0.65 },
    'South Korea':  { trafficm: 0.32, ctrm: 0.82, compm: 0.72 },
    'Spain':        { trafficm: 0.30, ctrm: 0.88, compm: 0.75 },
    'Sweden':       { trafficm: 0.14, ctrm: 1.02, compm: 0.78 },
    'Switzerland':  { trafficm: 0.10, ctrm: 0.98, compm: 0.82 },
    'Thailand':     { trafficm: 0.20, ctrm: 0.85, compm: 0.65 },
    'Turkiye':      { trafficm: 0.28, ctrm: 0.88, compm: 0.68 },
    'UAE':          { trafficm: 0.10, ctrm: 0.88, compm: 0.78 },
    'UK':           { trafficm: 0.62, ctrm: 1.05, compm: 0.92 },
    'USA':          { trafficm: 1.00, ctrm: 1.00, compm: 1.00 },
    'Vietnam':      { trafficm: 0.18, ctrm: 0.82, compm: 0.62 }
  };

  var countryNames = Object.keys(countries).sort();

  // [name, trafficm, ctrm, backlinkm, kdm, dam]
  var industries = [
    ['All Industries',                         1.00, 1.00, 1.00, 1.00, 1.00],
    ['Apparel (E-Commerce)',                   1.35, 1.05, 1.15, 1.12, 1.10],
    ['Automotive',                             1.25, 0.92, 1.35, 1.28, 1.30],
    ['Banking & Finance',                      0.85, 0.80, 1.85, 1.65, 1.60],
    ['Beauty & Salons',                        1.42, 1.15, 0.85, 0.88, 0.82],
    ['Crypto & Web3',                          0.75, 0.88, 1.65, 1.55, 1.45],
    ['Dating',                                 0.95, 1.08, 0.92, 0.90, 0.88],
    ['Education',                              1.65, 1.12, 1.05, 1.02, 1.05],
    ['Electronics (E-Commerce)',               1.48, 1.02, 1.45, 1.38, 1.35],
    ['Entertainment & Media',                  2.25, 1.38, 0.75, 0.72, 0.70],
    ['Fitness & Gyms',                         1.35, 1.18, 0.88, 0.85, 0.82],
    ['Flights',                                1.55, 0.78, 1.75, 1.68, 1.70],
    ['Food & Beverage',                        1.82, 1.35, 0.72, 0.70, 0.68],
    ['Furniture & Home Décor (E-Commerce)',    1.28, 1.05, 1.12, 1.08, 1.05],
    ['Gaming',                                 2.05, 1.42, 1.25, 1.22, 1.18],
    ['Healthcare',                             1.45, 0.88, 1.55, 1.48, 1.45],
    ['Health & Wellness (E-Commerce)',         1.38, 1.12, 0.95, 0.92, 0.88],
    ['Home Appliances (E-Commerce)',           1.22, 1.02, 1.08, 1.05, 1.02],
    ['Home Services',                          0.85, 1.15, 0.78, 0.82, 0.78],
    ['Hotels',                                 1.45, 0.82, 1.65, 1.55, 1.52],
    ['Insurance',                              0.78, 0.72, 2.05, 1.82, 1.78],
    ['Jewelry & Accessories (E-Commerce)',     1.32, 1.08, 1.05, 1.02, 0.98],
    ['Jobs & Recruitment',                     1.48, 0.95, 1.42, 1.35, 1.32],
    ['Legal',                                  0.72, 0.75, 1.92, 1.75, 1.72],
    ['Logistics',                              0.68, 0.88, 1.18, 1.12, 1.08],
    ['Moving & Cleaning Services',             0.82, 1.12, 0.72, 0.75, 0.72],
    ['Non-Profit & Charity',                   0.88, 1.22, 0.55, 0.55, 0.55],
    ['Online Courses & EdTech',                1.42, 1.05, 1.08, 1.05, 1.02],
    ['Pet Products (E-Commerce)',              1.35, 1.18, 0.88, 0.85, 0.82],
    ['Property',                               1.32, 0.85, 1.62, 1.52, 1.48],
    ['Restaurants & Food Delivery',            1.62, 1.32, 0.72, 0.72, 0.70],
    ['Skincare (E-Commerce)',                  1.38, 1.15, 0.92, 0.88, 0.85],
    ['Software & SaaS',                        0.92, 0.88, 1.48, 1.42, 1.38],
    ['Sports & Outdoors (E-Commerce)',         1.45, 1.12, 1.02, 0.98, 0.95],
    ['Subscription Boxes',                     0.95, 1.08, 0.85, 0.82, 0.80],
    ['Toys & Baby (E-Commerce)',               1.32, 1.15, 0.92, 0.88, 0.85],
    ['Travel',                                 1.85, 0.85, 1.78, 1.65, 1.62],
    ['Wedding & Events',                       1.28, 1.20, 0.82, 0.80, 0.78]
  ];

  var data = {};
  var industryNames = industries.map(function (i) { return i[0]; });

  countryNames.forEach(function (cname) {
    var cm = countries[cname];
    data[cname] = {};
    industries.forEach(function (ind) {
      var iname = ind[0], itm = ind[1], ictrm = ind[2], iblm = ind[3], ikdm = ind[4], idam = ind[5];
      data[cname][iname] = {
        traffic:   Math.round(BASE_TRAFFIC * cm.trafficm * itm),
        ctr:       r(BASE_CTR * cm.ctrm * ictrm, 2),
        backlinks: Math.round(BASE_BL * cm.compm * iblm),
        kd:        Math.min(98, Math.round(BASE_KD * cm.compm * ikdm)),
        da:        Math.min(95, Math.round(BASE_DA * cm.compm * idam))
      };
    });
  });

  window.BENCHMARK_DATA = {
    channel:     'SEO',
    channelDesc: 'Organic Search',
    channelSlug: 'seo',
    updated:     'Q2 2026',
    countries:   countryNames,
    industries:  industryNames,
    columns: [
      { key: 'traffic',   head: 'Monthly Organic Traffic', fmt: 'num'   },
      { key: 'ctr',       head: 'Organic CTR',             fmt: 'pct'   },
      { key: 'backlinks', head: 'Backlinks for P1',        fmt: 'num'   },
      { key: 'kd',        head: 'Keyword Difficulty',          subhead: '/ 100', fmt: 'score' },
      { key: 'da',        head: 'Domain Authority',            subhead: '/ 100', fmt: 'score' }
    ],
    data: data
  };
})();
