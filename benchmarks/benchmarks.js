/* Shared benchmark table — reused by all channel benchmark pages */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var D = window.BENCHMARK_DATA;
    if (!D) return;

    var countryEl  = document.getElementById('bm-country');
    var industryEl = document.getElementById('bm-industry');
    var h1El       = document.getElementById('bm-h1');
    var subEl      = document.getElementById('bm-sub');
    var theadEl    = document.getElementById('bm-thead');
    var tbodyEl    = document.getElementById('bm-tbody');
    var copyBtn    = document.getElementById('bm-copy');
    var dlBtn      = document.getElementById('bm-download');
    var countLbl   = document.getElementById('bm-count');

    D.countries.forEach(function (c) {
      var o = document.createElement('option'); o.value = o.textContent = c;
      countryEl.appendChild(o);
    });
    D.industries.forEach(function (i) {
      var o = document.createElement('option'); o.value = o.textContent = i;
      industryEl.appendChild(o);
    });

    var params = new URLSearchParams(window.location.search);
    var pc = params.get('country'), pi = params.get('industry');
    if (pc && D.countries.indexOf(pc) !== -1) countryEl.value = pc;
    if (pi && D.industries.indexOf(pi) !== -1) industryEl.value = pi;

    render();
    countryEl.addEventListener('change', render);
    industryEl.addEventListener('change', render);

    function render() {
      var country  = countryEl.value;
      var industry = industryEl.value;
      var curr     = D.currencies[country];
      var isAll    = industry === 'All Industries';

      var url = new URL(window.location.href);
      url.searchParams.set('country', country);
      url.searchParams.set('industry', industry);
      history.replaceState({}, '', url);

      var loc = isAll ? '' : ' for ' + industry;
      h1El.innerHTML = D.channel + ' Benchmarks in <span class="highlight">' + country + '</span>' + (isAll ? '' : ' for ' + industry);
      subEl.textContent = 'Average ' + D.channel + ' performance in ' + country + (isAll ? ' across all industries' : ' for the ' + industry + ' industry') + ' — ' + D.updated + '. Figures in ' + curr.code + ' (' + curr.sym.trim() + ').';
      document.title = D.channel + ' Benchmarks in ' + country + loc + ' (' + D.updated + ') | XYZ Lab';

      theadEl.innerHTML = '<tr><th class="col-ind">Industry</th><th>CTR</th><th>CPC<br><span class="col-curr">' + curr.code + '</span></th><th>CPM<br><span class="col-curr">' + curr.code + '</span></th><th>Conv.&nbsp;Rate</th><th>CPA<br><span class="col-curr">' + curr.code + '</span></th><th>ROAS <span class="roas-tip" title="Return on ad spend — indicative average. Actual ROAS varies significantly by product margin and average order value.">&#9432;</span></th></tr>';

      tbodyEl.innerHTML = D.industries.map(function (ind) {
        var d  = D.data[country][ind];
        var hi = ind === industry ? ' class="bm-hi"' : '';
        return '<tr' + hi + '><td class="col-ind">' + ind + '</td><td>' + pct(d.ctr) + '</td><td>' + money(d.cpc, curr.sym) + '</td><td>' + money(d.cpm, curr.sym) + '</td><td>' + pct(d.conv_rate) + '</td><td>' + money(d.cpa, curr.sym) + '</td><td>' + d.roas.toFixed(2) + 'x</td></tr>';
      }).join('');

      if (countLbl) countLbl.textContent = D.industries.length + ' industries';

      if (!isAll) {
        var hiRow = tbodyEl.querySelector('.bm-hi');
        if (hiRow) setTimeout(function(){ hiRow.scrollIntoView({behavior:'smooth', block:'nearest'}); }, 100);
      }
    }

    function pct(v) { return v.toFixed(2) + '%'; }
    function money(v, sym) {
      if (v >= 100) return sym + Math.round(v);
      return sym + v.toFixed(2);
    }
    function slugify(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,''); }

    function buildTSV(country) {
      var curr = D.currencies[country];
      var hdr = ['Industry','CTR','CPC ('+curr.code+')','CPM ('+curr.code+')','Conv. Rate','CPA ('+curr.code+')','ROAS'].join('\t');
      var rows = D.industries.map(function(ind){
        var d=D.data[country][ind];
        return [ind, pct(d.ctr), money(d.cpc,curr.sym), money(d.cpm,curr.sym), pct(d.conv_rate), money(d.cpa,curr.sym), d.roas.toFixed(2)+'x'].join('\t');
      });
      return hdr + '\n' + rows.join('\n');
    }
    function buildCSV(country) {
      var curr = D.currencies[country];
      var hdr = ['Industry','CTR','CPC ('+curr.code+')','CPM ('+curr.code+')','Conv. Rate','CPA ('+curr.code+')','ROAS'].join(',');
      var rows = D.industries.map(function(ind){
        var d=D.data[country][ind];
        return ['"'+ind+'"', pct(d.ctr), money(d.cpc,''), money(d.cpm,''), pct(d.conv_rate), money(d.cpa,''), d.roas.toFixed(2)+'x'].join(',');
      });
      return hdr + '\n' + rows.join('\n');
    }

    copyBtn.addEventListener('click', function () {
      var country = countryEl.value;
      navigator.clipboard.writeText(buildTSV(country)).then(function () {
        var orig = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        setTimeout(function () { copyBtn.textContent = orig; }, 2000);
      });
    });

    dlBtn.addEventListener('click', function () {
      var country  = countryEl.value;
      var industry = industryEl.value;
      var csv  = buildCSV(country);
      var blob = new Blob([csv], {type:'text/csv;charset=utf-8;'});
      var burl = URL.createObjectURL(blob);
      var a    = document.createElement('a');
      a.href   = burl;
      a.download = D.channelSlug + '-benchmarks-' + slugify(country) + '-' + D.updated.toLowerCase().replace(/\s+/g,'-') + '.csv';
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      URL.revokeObjectURL(burl);
    });
  });
})();
