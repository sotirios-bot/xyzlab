/* Shared benchmark table — reused by all channel benchmark pages */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var D = window.BENCHMARK_DATA;
    if (!D) return;

    var G        = window.BENCHMARK_GATE; // optional — set per channel page
    var FREE_ROWS = 8;
    var hasCPM   = !D.hideCPM;

    /* ── Always locked when gate is present ────────────────────── */
    var isUnlocked = !G;

    /* ── Inline country select styles ──────────────────────────── */
    var _s = document.createElement('style');
    _s.textContent = 'select.bm-cpill{display:inline-block;appearance:none;-webkit-appearance:none;background-color:rgba(8,191,173,.12);background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2210%22%20height%3D%226%22%20viewBox%3D%220%200%2010%206%22%3E%3Cpath%20d%3D%22M0%200l5%206%205-6z%22%20fill%3D%22%2308bfad%22%2F%3E%3C%2Fsvg%3E");background-repeat:no-repeat;background-position:right .55rem center;color:var(--primary);border:1.5px solid rgba(8,191,173,.35);border-radius:6px;padding:.05rem 1.8rem .15rem .55rem;font:inherit;font-weight:800;font-size:inherit;line-height:inherit;vertical-align:baseline;cursor:pointer;transition:background-color .15s,border-color .15s;}select.bm-cpill:hover{background-color:rgba(8,191,173,.22);border-color:var(--primary);}select.bm-cpill:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(8,191,173,.15);}p.bm-teaser-stat{display:inline-block;margin-top:.85rem;background:rgba(8,191,173,.1);border:1.5px solid rgba(8,191,173,.25);border-radius:8px;padding:.4rem .95rem;font-size:.875rem;color:#0a7a72;font-weight:500;}p.bm-teaser-stat strong{font-weight:800;color:var(--primary);}.bm-delivery-note{margin-top:.75rem;font-size:.8rem;color:#94a3b8;}';
    document.head.appendChild(_s);

    /* ── DOM refs ───────────────────────────────────────────────── */
    var countryEl  = document.getElementById('bm-country');
    var industryEl = document.getElementById('bm-industry');
    var h1El       = document.getElementById('bm-h1');
    var subEl      = document.getElementById('bm-sub');
    var theadEl    = document.getElementById('bm-thead');
    var tbodyEl    = document.getElementById('bm-tbody');
    var dlBtn      = document.getElementById('bm-download');
    var countLbl   = document.getElementById('bm-count');
    var paywallEl  = document.getElementById('bm-paywall');

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
    var pc = window.BENCHMARK_COUNTRY || urlP.get('country'), pi = urlP.get('industry');
    if (pc && D.countries.indexOf(pc) !== -1) countryEl.value = pc;
    if (pi && D.industries.indexOf(pi) !== -1) industryEl.value = pi;

    /* ── Paywall UI ─────────────────────────────────────────────── */
    applyGateUI();

    function applyGateUI() {
      if (!G) return;
      var gateWrap = document.querySelector('.bm-gate-wrap');
      if (paywallEl) paywallEl.style.display = 'flex';
      if (gateWrap)  gateWrap.classList.add('is-locked');
      if (dlBtn)   { dlBtn.disabled = true; }
      if (dlBtn && !dlBtn.parentElement.classList.contains('bm-btn-tip-wrap')) {
        var wrap = document.createElement('div');
        wrap.className = 'bm-btn-tip-wrap';
        dlBtn.parentNode.insertBefore(wrap, dlBtn);
        wrap.appendChild(dlBtn);
        var tip = document.createElement('span');
        tip.className = 'bm-btn-tip';
        tip.innerHTML = '&#128274; <a href="#bm-paywall">Unlock for ' + G.price + '</a> to use';
        wrap.appendChild(tip);
      }
    }

    /* ── Render ─────────────────────────────────────────────────── */
    render();
    countryEl.addEventListener('change', render);
    industryEl.addEventListener('change', render);

    /* ── Inline country select → sync + re-render ───────────────── */
    h1El.addEventListener('change', function (e) {
      if (e.target.classList && e.target.classList.contains('bm-cpill')) {
        countryEl.value = e.target.value;
        render();
      }
    });

    function render() {
      var country  = countryEl.value;
      var industry = industryEl.value;
      var curr     = D.currencies ? D.currencies[country] : null;
      var isAll    = industry === 'All Industries';

      if (!window.BENCHMARK_STATIC_URL) {
        var url = new URL(window.location.href);
        url.searchParams.set('country', country);
        url.searchParams.set('industry', industry);
        history.replaceState({}, '', url);
      }

      if (!window.BENCHMARK_STATIC_H1) {
        var pillOpts = D.countries.map(function (c) { return '<option value="' + c + '"' + (c === country ? ' selected' : '') + '>' + c + '</option>'; }).join('');
        h1El.innerHTML = D.channel + ' Benchmarks in <select class="bm-cpill">' + pillOpts + '</select>' + (isAll ? '' : ' for ' + industry);
      }
      subEl.textContent = 'Average ' + D.channel + (D.channelDesc ? ' (' + D.channelDesc + ')' : '') +
        ' performance in ' + country + (isAll ? ' across all industries' : ' for the ' + industry + ' industry') +
        (curr ? '. Figures in ' + curr.code + ' (' + curr.sym.trim() + ').' : '.');
      document.title = D.channel + ' Benchmarks in ' + country + (isAll ? '' : ' for ' + industry) + ' | XYZ Lab';

      if (D.columns) {
        /* ── Generic column mode (SEO, TikTok Ads, etc.) ────── */
        theadEl.innerHTML = '<tr><th class="col-ind">Industry</th>' +
          D.columns.map(function (col) {
            var sub = col.subheadCurrCode ? (curr ? curr.code : '') : col.subhead;
            return '<th>' + col.head + (sub ? '<br><span class="col-curr">' + sub + '</span>' : '') + '</th>';
          }).join('') + '</tr>';

        tbodyEl.innerHTML = D.industries.map(function (ind, idx) {
          var d       = D.data[country][ind];
          var locked  = !isUnlocked && G && idx >= 2;
          var classes = [];
          if (ind === industry) classes.push('bm-hi');
          if (locked)           classes.push('bm-blurred');
          var cls = classes.length ? ' class="' + classes.join(' ') + '"' : '';
          return '<tr' + cls + '><td class="col-ind">' + ind + '</td>' +
            D.columns.map(function (col) {
              return '<td>' + formatCell(d[col.key], col, curr) + '</td>';
            }).join('') + '</tr>';
        }).join('');
      } else {
        /* ── PPC column mode (Meta Ads, Google Ads, etc.) ────── */
        theadEl.innerHTML = '<tr>' +
          '<th class="col-ind">Industry</th>' +
          '<th>CTR</th>' +
          '<th>CPC</th>' +
          (hasCPM ? '<th>CPM</th>' : '') +
          '<th>Conv.&nbsp;Rate</th>' +
          '<th>CPA</th>' +
          '<th>ROAS <span class="roas-tip" title="Return on ad spend — indicative average. Actual ROAS varies significantly by product margin and average order value.">&#9432;</span></th>' +
          '</tr>';

        tbodyEl.innerHTML = D.industries.map(function (ind, idx) {
          var d       = D.data[country][ind];
          var locked  = !isUnlocked && G && idx >= 2;
          var classes = [];
          if (ind === industry) classes.push('bm-hi');
          if (locked)           classes.push('bm-blurred');
          var cls = classes.length ? ' class="' + classes.join(' ') + '"' : '';
          return '<tr' + cls + '>' +
            '<td class="col-ind">' + ind + '</td>' +
            '<td>' + pct(d.ctr) + '</td>' +
            '<td>' + money(d.cpc, curr.sym, curr.noDecimal) + '</td>' +
            (hasCPM ? '<td>' + money(d.cpm, curr.sym, curr.noDecimal) + '</td>' : '') +
            '<td>' + pct(d.conv_rate) + '</td>' +
            '<td>' + money(d.cpa, curr.sym, curr.noDecimal) + '</td>' +
            '<td>' + d.roas.toFixed(2) + 'x</td>' +
            '</tr>';
        }).join('');
      }

      if (countLbl) countLbl.textContent = D.industries.length + ' industries';

      if (!isAll) {
        var hiRow = tbodyEl.querySelector('.bm-hi');
        if (hiRow) setTimeout(function () { hiRow.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 100);
      }

      renderTeaser(country, curr);
    }

    function renderTeaser(country, curr) {
      var teaserEl = document.getElementById('bm-teaser');
      if (!teaserEl) {
        teaserEl = document.createElement('p');
        teaserEl.id = 'bm-teaser';
        teaserEl.className = 'bm-teaser-stat';
        var sub = document.getElementById('bm-sub');
        if (sub && sub.parentNode) sub.parentNode.insertBefore(teaserEl, sub.nextSibling);
      }
      var allData = D.data[country] && D.data[country]['All Industries'];
      if (!allData) { teaserEl.style.display = 'none'; return; }
      var metric, value;
      if (D.columns) {
        var col = D.columns[0];
        metric = col.head;
        value  = formatCell(allData[col.key], col, curr);
      } else {
        metric = 'CTR';
        value  = pct(allData.ctr);
      }
      teaserEl.style.display = '';
      teaserEl.innerHTML = 'Average ' + metric + ' across all industries in ' + country + ': <strong>' + value + '</strong>';
    }

    /* ── Formatters ─────────────────────────────────────────────── */
    function pct(v)            { return v.toFixed(2) + '%'; }
    function money(v, sym, nd) { return (nd || v >= 100) ? sym + Math.round(v) : sym + v.toFixed(2); }
    function numFmt(v)         { return Math.round(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
    function slugify(s)        { return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''); }

    function formatCell(v, col, curr) {
      switch (col.fmt) {
        case 'pct':   return pct(v);
        case 'money': return money(v, curr ? curr.sym : '', curr ? curr.noDecimal : false);
        case 'num':   return numFmt(v);
        case 'score': return Math.round(v).toString();
        case 'roas':  return v.toFixed(2) + 'x';
        default:      return String(v);
      }
    }

    /* ── Data builders ──────────────────────────────────────────── */
    function buildCSV(country) {
      var curr = D.currencies ? D.currencies[country] : null;
      if (D.columns) {
        var hdr  = ['Industry'].concat(D.columns.map(function (c) {
          return c.subheadCurrCode && curr ? c.head + ' (' + curr.code + ')' : c.head;
        })).join(',');
        var rows = D.industries.map(function (ind) {
          var d = D.data[country][ind];
          return ['"' + ind + '"'].concat(D.columns.map(function (col) {
            return formatCell(d[col.key], col, null);
          })).join(',');
        });
        return hdr + '\n' + rows.join('\n');
      }
      var cols = ['Industry', 'CTR', 'CPC (' + curr.code + ')'];
      if (hasCPM) cols.push('CPM (' + curr.code + ')');
      cols.push('Conv. Rate', 'CPA (' + curr.code + ')', 'ROAS');
      var rows = D.industries.map(function (ind) {
        var d = D.data[country][ind];
        var cells = ['"' + ind + '"', pct(d.ctr), money(d.cpc, '', curr.noDecimal)];
        if (hasCPM) cells.push(money(d.cpm, '', curr.noDecimal));
        cells.push(pct(d.conv_rate), money(d.cpa, '', curr.noDecimal), d.roas.toFixed(2) + 'x');
        return cells.join(',');
      });
      return cols.join(',') + '\n' + rows.join('\n');
    }

    function buildTSV(country) {
      var curr = D.currencies ? D.currencies[country] : null;
      if (D.columns) {
        var hdr  = ['Industry'].concat(D.columns.map(function (c) {
          return c.subheadCurrCode && curr ? c.head + ' (' + curr.code + ')' : c.head;
        })).join('\t');
        var rows = D.industries.map(function (ind) {
          var d = D.data[country][ind];
          return [ind].concat(D.columns.map(function (col) {
            return formatCell(d[col.key], col, null);
          })).join('\t');
        });
        return hdr + '\n' + rows.join('\n');
      }
      var cols = ['Industry', 'CTR', 'CPC (' + curr.code + ')'];
      if (hasCPM) cols.push('CPM (' + curr.code + ')');
      cols.push('Conv. Rate', 'CPA (' + curr.code + ')', 'ROAS');
      var rows = D.industries.map(function (ind) {
        var d = D.data[country][ind];
        var cells = [ind, pct(d.ctr), money(d.cpc, curr.sym, curr.noDecimal)];
        if (hasCPM) cells.push(money(d.cpm, curr.sym, curr.noDecimal));
        cells.push(pct(d.conv_rate), money(d.cpa, curr.sym, curr.noDecimal), d.roas.toFixed(2) + 'x');
        return cells.join('\t');
      });
      return cols.join('\t') + '\n' + rows.join('\n');
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
    if (dlBtn) {
      dlBtn.addEventListener('click', function () {
        if (G) return;
        downloadAllCountries();
      });
    }
  });
})();
