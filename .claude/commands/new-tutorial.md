# new-tutorial

Build a new video tutorial page for the XYZ Lab site.

## Step 1 — Collect details via form

Use the `AskUserQuestion` tool with EXACTLY 2 calls.

**CRITICAL RULES — follow without exception:**
- DO NOT add content suggestions, format hints, or example values in options
- DO NOT pre-fill or guess any field
- The 2 required options per question are there only because the tool forces it — label them clearly as non-choices
- User will always type their answer in the Other field

**Call 1 — Page details (4 questions, one field each)**

Q1 — Pillar page:
question: "Pillar page — Available: google-ads · google-ads-editor · meta-ads · tiktok-ads · microsoft-ads · linkedin-ads · pinterest-ads · reddit-ads · google-analytics · google-tag-manager · data-studio · claude · chatgpt · google-search-console · bing-webmaster-tools · shopify"
options: label "↓ type in Other", description "required placeholder" | label "↓ no choice to make", description "type in Other below"

Q2 — Title:
question: "Tutorial title"
options: label "↓ type in Other", description "required placeholder" | label "↓ no choice to make", description "type in Other below"

Q3 — YouTube video URL:
question: "YouTube video URL"
options: label "↓ paste in Other", description "required placeholder" | label "↓ no choice to make", description "paste in Other below"

Q4 — Page URL slug:
question: "Page URL slug (the part after /pillar-name/, e.g. sitelinks)"
options: label "↓ type in Other", description "required placeholder" | label "↓ no choice to make", description "type in Other below"

**Call 2 — Steps (1 question)**

Q1 — Steps:
question: "Step-by-step instructions — one step per line"
options: label "↓ paste in Other", description "required placeholder" | label "↓ no choice to make", description "paste in Other below"

## Step 2 — Parse the inputs

- `pillar_slug` — Q1 answer from Call 1
- `title` — Q2 answer from Call 1, exact text, no modification
- `video_id` — extract from Q3 answer (youtu.be/VIDEO_ID or watch?v=VIDEO_ID)
- `page_slug` — Q4 answer from Call 1, strip leading slash if present
- `steps` — each line from Call 2, strip leading emoji/numbers

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
- google-search-console: PLCRsBzkyVfUX4Obp-oztYxTzmF2Zhr9HC
- bing-webmaster-tools: PLCRsBzkyVfUXZ2cur4YmtNjG0iyCQjsH8
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
