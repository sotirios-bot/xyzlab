# new-tutorial

Build a new video tutorial page for the XYZ Lab site.

## Step 1 — Collect details via form

Use the `AskUserQuestion` tool with these questions:

**Q1 — Pillar page** (which pillar does this tutorial belong to?)
Options:
- PPC — description: "google-ads · google-ads-editor · meta-ads · tiktok-ads · microsoft-ads · linkedin-ads · pinterest-ads · reddit-ads"
- Analytics — description: "google-analytics · google-tag-manager · data-studio"
- AI Tools — description: "claude · chatgpt"
- SEO & eCommerce — description: "seo · shopify"

**Q2 — Title + URL + Video** (ask user to type three lines via "Other"):
- Line 1: pillar slug (e.g. google-ads)
- Line 2: tutorial title (e.g. How to Add Call Assets in Google Ads)
- Line 3: page slug (e.g. call-assets)
Options: show one format-hint option + "Other"

**Q3 — YouTube video URL**
Options: two format examples + "Other" for them to paste actual URL

**Q4 — Step-by-step instructions**
Options: one format hint + "Other" for them to paste all steps

## Step 2 — Parse the inputs

From the answers extract:
- `pillar_slug` — e.g. `google-ads`
- `title` — exact H1 text
- `page_slug` — URL segment, fix any typos (e.g. "tacking" → "tracking")
- `video_id` — extract from YouTube URL (youtu.be/VIDEO_ID or watch?v=VIDEO_ID)
- `steps` — list of step strings

## Step 3 — Generate the page

Create `/home/user/xyzlab/{pillar_slug}/{page_slug}/index.html` using the
structure of `/home/user/xyzlab/google-ads/tracking-template/index.html`
as the reference template. Adapt:

- `<title>`, meta description, OG/Twitter tags → use tutorial title
- canonical URL → `https://xyzlab.com/{pillar_slug}/{page_slug}/`
- VideoObject JSON-LD → use extracted video_id, today's date, tutorial title
- og:image / twitter:image → `https://img.youtube.com/vi/{video_id}/maxresdefault.jpg`
- Breadcrumb → Home › {Pillar} Tutorials › {short breadcrumb title}
- H1 → tutorial title with `<span class="highlight">` on the key noun/phrase
- hero-sub → 1-sentence summary of what the tutorial covers
- iframe src → `https://www.youtube.com/embed/{video_id}?list={pillar_playlist_id}&rel=0&modestbranding=1`
- Steps section h2 → same as H1
- Step items → one `.step-item` per step provided; add sub-bullets for any
  steps that include notes/details
- FAQ → generate 5–6 relevant questions and answers based on the tutorial topic
- Related tutorials → pick 3 relevant pages from the site:
  - Prefer other tutorial sub-pages under the same pillar
  - Fall back to the pillar page itself and the pillar's course page
- Footer nav → use the correct `../../` prefix depth (2 levels deep for all
  pillar sub-pages)

Pillar playlist IDs for the iframe:
- google-ads: PLCRsBzkyVfUWek5G0qatJWuwYTpmtje_x
- google-ads-editor: PLCRsBzkyVfUVWaoENjvezLrtvEhD5r6uE
- meta-ads: PLCRsBzkyVfUVo5Ho0gwnhIKDeJcZEE99k
- tiktok-ads: PLCRsBzkyVfUXJbSFS5zLzKQLoQR2bSDL9
- pinterest-ads: PLCRsBzkyVfUXLd77fR_67ygCvMPg3ZFnv
- linkedin-ads: PLCRsBzkyVfUU4sJswlipX5kV-Ec2EQJW4
- reddit-ads: PLCRsBzkyVfUVHGtJMv_Ru7pEXDYAktdW_
- microsoft-ads: PLCRsBzkyVfUVeWWkiPagY-MnsWSJeocsN
- google-analytics: PLCRsBzkyVfUWnJ44nfHLs48NIMe2Bfxoh
- google-tag-manager: PLCRsBzkyVfUXqTjJUoZ1O1tSMhKoknMDN
- data-studio: PLCRsBzkyVfUXt5QOGCdzWW3ZDcXMXK2yA
- claude: PLCRsBzkyVfUUX2m1wdR5FL29UqdY1Cfdy
- chatgpt: PLCRsBzkyVfUWQvMd7LP-ck4x0YMGmudbw
- seo: PLCRsBzkyVfUWB7NDT9m9lky-3YoprGp1D
- shopify: PLCRsBzkyVfUVKcCtGW_3Bei4jZgyj31Si

## Step 4 — Update pillar page tutorial list

Add a new `.tutorial-list-item` entry to
`/home/user/xyzlab/{pillar_slug}/index.html` inside the `.tutorial-list` div,
using the play icon SVG, tutorial title, and a one-line description.

## Step 5 — Update sitemap

Add `<url><loc>https://xyzlab.com/{pillar_slug}/{page_slug}/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>`
to `/home/user/xyzlab/sitemap.xml` in the appropriate section.

## Step 6 — Commit and push live

```
git add {new file} {pillar index} sitemap.xml
git commit -m "Add {title} tutorial page"
git checkout gh-pages && git merge claude/build-marketing-homepage-BWVwx --no-edit && git push origin gh-pages
git checkout claude/build-marketing-homepage-BWVwx && git push -u origin claude/build-marketing-homepage-BWVwx
```
