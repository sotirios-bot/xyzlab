/* Shared benchmark table — reused by all channel benchmark pages */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var D = window.BENCHMARK_DATA;
    if (!D) return;

    var G = window.BENCHMARK_GATE; // optional — set per channel page
    var FREE_ROWS = 8;

    /* ── Unlock state ───────────────────────────────────────────── */
    var isUnlocked = !G;
    var triggerDownload = false;

    if (G) {
      var initParams = new URLSearchParams(window.location.search);
      if (initParams.get('unlocked') === '1') {
        localStorage.setItem(G.storageKey, '1');
        isUnlocked    = true;
        triggerDownload = true;
        initParams.delete('unlocked');
        history.replaceState({}, '', window.location.pathname + (initParams.toString() ? '?' + initParams.toString() : ''));
      } else {
        isUnlocked = localStorage.getItem(G.storageKey) === '1';
      }
    }

    /* ── DOM refs ───────────────────────────────────────────────── */
    var countryEl  = document.getElementById('bm-country');
    var industryEl = document.getElementById('bm-industry');
    var h1El       = document.getElementById('bm-h1');
    var subEl      = document.getElementById('bm-sub');
    var theadEl    = document.getElementById('bm-thead');
    var tbodyEl    = document.getElementById('bm-tbody');
    var copyBtn    = document.getElementById('bm-copy');
    var dlBtn      = document.getElementById('bm-download');
    var countLbl   = document.getElementById('bm-count');
    var paywallEl  = document.getElementById('bm-paywall');
    var successEl  = document.getElementById('bm-success');

    /* ── Populate dropdowns ─────────────────────────────────────── */
    D.countries.forEach(function (c) {
      var o = document.createElement('option'); o.value = o.textContent = c;
      countryEl.appendChild(o);
    });
    D.industries.forEach(function (i) {
      var o = document.createElement('option'); o.value = o.textContent = i;
      industryEl.appendChild(o);
    });

    var urlP = new URLSearchParams(window.location.search);
    var pc = urlP.get('country'), pi = urlP.get('industry');
    if (pc && D.countries.indexOf(pc) !== -1) countryEl.value = pc;
    if (pi && D.industries.indexOf(pi) !== -1) industryEl.value = pi;

    /* ── Paywall UI ─────────────────────────────────────────────── */
    applyGateUI();

    function applyGateUI() {
      if (!G) return;
      var gateWrap = document.querySelector('.bm-gate-wrap');
      if (isUnlocked) {
        if (paywallEl) paywallEl.style.display = 'none';
        if (gateWrap)  gateWrap.classList.remove('is-locked');
        if (copyBtn)   copyBtn.disabled = false;
        if (dlBtn)     dlBtn.disabled   = false;
      } else {
        if (paywallEl) paywallEl.style.display = 'flex';
        if (gateWrap)  gateWrap.classList.add('is-locked');
        if (copyBtn) { copyBtn.disabled = true; copyBtn.title = 'Unlock to copy'; }
        if (dlBtn)   { dlBtn.disabled   = true; dlBtn.title   = 'Unlock to download'; }
      }
    }

    /* ── Success banner + auto-download ────────────────────────── */
    if (triggerDownload) {
      if (successEl) {
        successEl.style.display = 'flex';
        setTimeout(function () {
          successEl.style.opacity = '0';
          setTimeout(function () { successEl.style.display = 'none'; }, 700);
        }, 9000);
      }
      setTimeout(downloadAllCountries, 600);
    }

    /* ── Render ─────────────────────────────────────────────────── */
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

      h1El.innerHTML    = D.channel + ' Benchmarks in <span class="highlight">' + country + '</span>' + (isAll ? '' : ' for ' + industry);
      subEl.textContent = 'Average ' + D.channel + ' (Facebook & Instagram Ads) performance in ' + country + (isAll ? ' across all industries' : ' for the ' + industry + ' industry') + '. Figures in ' + curr.code + ' (' + curr.sym.trim() + ').';
      document.title    = D.channel + ' Benchmarks in ' + country + (isAll ? '' : ' for ' + industry) + ' (' + D.updated + ') | XYZ Lab';

      theadEl.innerHTML = '<tr>' +
        '<th class="col-ind">Industry</th>' +
        '<th>CTR</th>' +
        '<th>CPC<br><span class="col-curr">' + curr.code + '</span></th>' +
        '<th>CPM<br><span class="col-curr">' + curr.code + '</span></th>' +
        '<th>Conv.&nbsp;Rate</th>' +
        '<th>CPA<br><span class="col-curr">' + curr.code + '</span></th>' +
        '<th>ROAS <span class="roas-tip" title="Return on ad spend — indicative average. Actual ROAS varies significantly by product margin and average order value.">&#9432;</span></th>' +
        '</tr>';

      tbodyEl.innerHTML = D.industries.map(function (ind, idx) {
        var d       = D.data[country][ind];
        var locked  = !isUnlocked && G && idx >= FREE_ROWS;
        var classes = [];
        if (ind === industry) classes.push('bm-hi');
        if (locked)           classes.push('bm-blurred');
        var cls = classes.length ? ' class="' + classes.join(' ') + '"' : '';
        return '<tr' + cls + '>' +
          '<td class="col-ind">' + ind + '</td>' +
          '<td>' + pct(d.ctr) + '</td>' +
          '<td>' + money(d.cpc, curr.sym) + '</td>' +
          '<td>' + money(d.cpm, curr.sym) + '</td>' +
          '<td>' + pct(d.conv_rate) + '</td>' +
          '<td>' + money(d.cpa, curr.sym) + '</td>' +
          '<td>' + d.roas.toFixed(2) + 'x</td>' +
          '</tr>';
      }).join('');

      if (countLbl) countLbl.textContent = D.industries.length + ' industries';

      if (!isAll) {
        var hiRow = tbodyEl.querySelector('.bm-hi');
        if (hiRow) setTimeout(function () { hiRow.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 100);
      }
    }

    /* ── Formatters ─────────────────────────────────────────────── */
    function pct(v)        { return v.toFixed(2) + '%'; }
    function money(v, sym) { return v >= 100 ? sym + Math.round(v) : sym + v.toFixed(2); }
    function slugify(s)    { return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''); }

    /* ── Data builders ──────────────────────────────────────────── */
    function buildCSV(country) {
      var curr = D.currencies[country];
      var hdr  = ['Industry', 'CTR', 'CPC (' + curr.code + ')', 'CPM (' + curr.code + ')', 'Conv. Rate', 'CPA (' + curr.code + ')', 'ROAS'].join(',');
      var rows = D.industries.map(function (ind) {
        var d = D.data[country][ind];
        return ['"' + ind + '"', pct(d.ctr), money(d.cpc, ''), money(d.cpm, ''), pct(d.conv_rate), money(d.cpa, ''), d.roas.toFixed(2) + 'x'].join(',');
      });
      return hdr + '\n' + rows.join('\n');
    }

    function buildTSV(country) {
      var curr = D.currencies[country];
      var hdr  = ['Industry', 'CTR', 'CPC (' + curr.code + ')', 'CPM (' + curr.code + ')', 'Conv. Rate', 'CPA (' + curr.code + ')', 'ROAS'].join('\t');
      var rows = D.industries.map(function (ind) {
        var d = D.data[country][ind];
        return [ind, pct(d.ctr), money(d.cpc, curr.sym), money(d.cpm, curr.sym), pct(d.conv_rate), money(d.cpa, curr.sym), d.roas.toFixed(2) + 'x'].join('\t');
      });
      return hdr + '\n' + rows.join('\n');
    }

    /* ── Downloads ──────────────────────────────────────────────── */
    function downloadAllCountries() {
      if (typeof JSZip !== 'undefined') {
        var zip = new JSZip();
        D.countries.forEach(function (country) {
          zip.file(D.channelSlug + '-benchmarks-' + slugify(country) + '-' + D.updated.toLowerCase().replace(/\s+/g, '-') + '.csv', buildCSV(country));
        });
        zip.generateAsync({ type: 'blob' }).then(function (blob) {
          triggerDownloadBlob(blob, D.channelSlug + '-benchmarks-all-countries-' + D.updated.toLowerCase().replace(/\s+/g, '-') + '.zip');
        });
      } else {
        triggerDownloadBlob(
          new Blob([buildCSV(countryEl.value)], { type: 'text/csv;charset=utf-8;' }),
          D.channelSlug + '-benchmarks-' + slugify(countryEl.value) + '-' + D.updated.toLowerCase().replace(/\s+/g, '-') + '.csv'
        );
      }
    }

    function triggerDownloadBlob(blob, filename) {
      var burl = URL.createObjectURL(blob);
      var a    = document.createElement('a');
      a.href   = burl;
      a.download = filename;
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      URL.revokeObjectURL(burl);
    }

    /* ── Button events ──────────────────────────────────────────── */
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        if (!isUnlocked && G) return;
        navigator.clipboard.writeText(buildTSV(countryEl.value)).then(function () {
          var orig = copyBtn.textContent;
          copyBtn.textContent = 'Copied!';
          setTimeout(function () { copyBtn.textContent = orig; }, 2000);
        });
      });
    }

    if (dlBtn) {
      dlBtn.addEventListener('click', function () {
        if (!isUnlocked && G) return;
        downloadAllCountries();
      });
    }
  });
})();
