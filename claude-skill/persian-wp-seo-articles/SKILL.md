---
name: persian-wp-seo-articles
description: End-to-end workflow for writing SEO articles for a WordPress site (especially Persian/Farsi, Rank Math, online-store blogs) and delivering them as paste-ready HTML that survives WordPress. Use this whenever the user wants an article, blog post or buying guide to rank on Google, gives a keyword list or competitor/reference site, mentions Rank Math or Yoast scores, asks for SEO title/meta/slug, internal links, images, FAQ schema, or says things like "مقاله سئو", "مقاله برای سایتم", "رتبه بگیرم", "سئو بیاد بالا" -- even if they never say "skill" or "WordPress". Also use when fixing Rank Math warnings on an existing article or when another AI needs exact edit instructions for an article.
---

# Persian WordPress SEO articles (Rank Math, store blogs)

This skill captures a workflow that was refined over many real iterations with a store owner who publishes articles on WordPress with Rank Math. Following it avoids the failures that cost the most time: broken images, stripped code, fake links, Rank Math warnings that could have been prevented, and claims the site owner can't back up.

Related skills (use alongside, don't duplicate): `persian-writing` for Persian typography and tone details, `seo-geo-aeo` for auditing a live page.

## Core principles (why the rules below exist)

- The owner pastes your output straight into WordPress. Anything WordPress strips or breaks becomes your problem, so build for WordPress's limits from the start (see `references/wordpress-pitfalls.md`).
- Rank Math's score is a checklist, not a ranking factor, but the owner watches it and gets anxious about red items. Prevent the common ones up front (see `references/rank-math-checklist.md`) and be honest that the score is not what ranks pages.
- Trust is the product. Never invent URLs, prices, agency status, warranties, author credentials or statistics. A made-up claim on a store's site is a liability for them.
- Search rankings take weeks to months and depend on authority and links, not just the article. Say so plainly once; don't promise results.

## Workflow

### 1. Intake: ask once, only for what's missing

Collect (from the conversation first, then ask in one short message):

- Topic and the store/site niche; who the readers are (buyers from a shop site?)
- Language and tone. Default for Persian: friendly second person "تو", short sentences, no stiff/bureaucratic phrasing. Confirm if unsure.
- Real URLs: shop page, relevant category pages, earlier articles to link to. Never guess them. If the user doesn't have them, link to the shop page and tell them which category link to send later.
- Image URLs already uploaded to their media library (if any).
- Keyword list and/or a reference competitor article they want to beat.
- Whether the plugin is Rank Math or Yoast.

If the user pastes an AI-generated keyword/site list, use the keywords but treat factual claims in it (e.g. "official agency of brand X") as unverified; don't repeat them.

### 2. Research

- Run web searches for the Persian query to see what ranks, what people ask, and how competitors structure the page. Sites may block automated fetching (`ROBOTS_DISALLOWED`); say so and work from search results and the user's own pasted/uploaded copy. Uploaded HTML can be parsed with bash.
- Keyword work: pick one main keyword (the exact phrase people search) plus secondary, long-tail and question keywords. You usually have no volume data. Say that and suggest checking Search Console, Ahrefs or Semrush; never invent search volumes.
- Study the reference article for structure and gaps (outdated year, vague or wrong claims, missing comparison table, no FAQ, no install/buying checklist). Beat it with accuracy and completeness. Never copy its wording.
- Verify technical facts you state. Hedge what varies ("usually", "معمولاً"). Skip numbers you can't support (especially prices, which change quickly and go stale).
- Find 1-2 real, authoritative external pages to link (Wikipedia pages, manufacturer/standards pages). Only use URLs that actually appeared in search or fetch results.

### 3. Plan

Outline the article around the main keyword and the reader's decision. Pick an honest number for the title if it will say "7 criteria" -- the article must contain exactly that many.

### 4. Write

Use `assets/article-template.html` as the skeleton. Key rules:

- Open with a last-updated date line, then a boxed quick answer (a direct answer in ~35-60 words), then an intro whose first paragraph contains the exact main keyword and a plain definition.
- A short table of contents with `#anchor` links and matching `id`s on the H2s. It helps readers and sometimes earns sitelinks.
- H2/H3 headings phrased as natural questions or decisions, several containing the main keyword or close variants. Under each question heading, give the direct answer first (about 40-60 words), then detail.
- Short paragraphs, 2-4 sentences. Separate every paragraph with a blank line (WordPress merges them otherwise, and Rank Math then reports a "long paragraph").
- Use lists, a comparison table, and numbered steps where content is procedural. Add specifics a competitor lacks (typical ranges, sizes, what to ask the seller, what to test before paying).
- A buying/decision section tied to real situations ("if budget is tight..., if you care about detail...").
- FAQ with 4-6 real questions, answered in 1-3 sentences each.
- Conclusion with a heading that includes the main keyword, and a call to action linking to the shop or category.
- Length: roughly 1,300-2,000 words is a good target; more only if the topic needs it.
- Internal links: 3-4 real ones (shop/category pages, an earlier relevant article), natural anchor text, no repeated identical anchors.
- External links: 1-2 authoritative ones with `target="_blank" rel="noopener"` -- no `nofollow` (Rank Math counts nofollow-only as "no outbound links").
- Main keyword frequency: in a ~1,700-word article, the exact phrase around 8-10 times, spread naturally (first paragraph, quick answer, TOC, two or three headings, a few body sentences, conclusion heading and paragraph, one FAQ question, image alt). That reached roughly 0.5% density on Rank Math without stuffing. Don't chase 1%.
- Persian orthography: correct ی and ک (never Arabic ي ك), half-spaces (ZWNJ) in words like «می‌شود», and consistent «ارتقا» spelling except where a target keyword uses another form.

### 5. Deliver

Return, in this order:

1. A brief note on what you used or ignored from the user's inputs and any honesty caveats (e.g. unverified claims omitted, no prices).
2. **SEO block**: H1, SEO title, meta description, slug, focus keyword, secondary keywords.
   - SEO title: at most ~60 characters, contains the main keyword near the start, and a number written with **ASCII digits** (e.g. `7`, `1405`) because Rank Math ignores Persian digits when checking for a number.
   - Meta description: about 140-160 characters, contains the main keyword, ends with a reason to click.
   - Slug: short, English is fine; see the checklist for the URL warning.
3. The article as one HTML code block ready for a Custom HTML block or the Code editor.
4. Images, delivered as real files when a sandbox is available (see below), plus the exact `<figure><img>` snippet and where it goes.
5. A short numbered to-do list of what only the owner can do (replace link placeholders, upload images, Rank Math settings, indexing).

### Images

- Do not put inline `<svg>` in the article: WordPress strips it for many users, leaving only the text labels. Render diagrams/infographics to **WebP/PNG files**, then give the owner an `<img>` tag with the future media-library URL.
- Use `scripts/make_infographic.py` to build clean Persian card infographics (numbered criteria lists, steps). It needs Pillow with Raqm and a font with Arabic glyphs (DejaVu Sans works). Always open the result and check that the Persian text shapes correctly before delivering.
- Never hotlink or reuse random web photos (copyright, and links rot). Suggest the owner use their own product photos; if none exist, omit the figure rather than leave a broken one.
- Write alt text for every image; put the main keyword in at least one alt, naturally.
- Don't leave `REPLACE-...` placeholders in a final deliverable if you can avoid it. If a link or image URL is unknown, either omit that element or link to the shop page and say exactly what to swap later.
- Check each image is what the article is about (one case: a file named like a "coaxial cable" was offered for an article about coaxial speakers -- same word, different product. Flag mismatches).

### 6. After publishing

- Request indexing in Google Search Console using the **final public URL**, never the `?preview=true` link.
- Submit the sitemap once; add links to the new article from older related posts; test FAQ/HowTo schema with Google's Rich Results Test.
- Review Search Console Performance after 2-4 weeks and write follow-up articles on long-tail questions, each linking back to the pillar article.

## Handling Rank Math feedback

When the owner pastes Rank Math errors, diagnose before editing. A cluster of keyword errors usually means the focus keyword box doesn't match the text (typed with Arabic letters, a different word, stray spaces), so ask them to paste the exact phrase. Use `references/rank-math-checklist.md` for the message-to-fix map. If a warning looks wrong against the content (e.g. "long paragraph" when none is long), say so honestly and give a quick experiment instead of inventing a cause.

## Handing edits to another AI

The owner sometimes passes the article to a different AI to apply changes. Write that instruction as a self-contained prompt: say what must not change, list each edit as "find this exact text -> replace with this exact text" with the surrounding anchor (heading id), require the full corrected code in one code block, and ask for a short report of anything not found. Include the main keyword spelled exactly.

## Files in this skill

- `references/rank-math-checklist.md`: every Rank Math message seen so far and its fix, plus plugin settings.
- `references/wordpress-pitfalls.md`: what WordPress strips or breaks and how to avoid it.
- `assets/article-template.html`: article skeleton with comments.
- `scripts/make_infographic.py`: Persian infographic image generator.
