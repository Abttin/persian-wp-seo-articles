# Rank Math checklist (message -> fix)

Contents: field values to prepare · warning-to-fix table · schema notes · plugin settings · honest expectations

## Field values to prepare for every article

| Field | Rule |
|---|---|
| H1 (post title) | Can be longer than the SEO title; contains the main keyword |
| SEO title | <= ~60 chars, keyword near the start, **ASCII digit** number (e.g. `7`, `1405`); Rank Math flags Persian digits as "no number" |
| Meta description | ~140-160 chars, contains the main keyword |
| Slug (permalink) | Short; English is fine. Only change on an unpublished post, or add a redirect first |
| Focus keyword | Paste the exact phrase (don't type it); press Enter so it becomes a tag |
| Secondary keywords | A few related phrases in the same box (the free version limits how many) |

## Warning -> fix

| Rank Math message | Cause | Fix |
|---|---|---|
| Add focus keyword to SEO title / meta description / beginning of content / content (all together) | Snippet fields empty (Rank Math uses an auto title) or the keyword box text differs from the article (Arabic ي/ك, different word, extra spaces) | Re-paste keyword; paste title and description into Edit Snippet; put the exact phrase in the first paragraph |
| Keyword density low (e.g. 0.06) | Exact phrase used once in ~1,600 words | Add the exact phrase naturally ~8-10 times in total: first paragraph, quick answer, TOC, 2-3 headings, body sentences, conclusion heading + paragraph, FAQ question, image alt. Don't stuff |
| Keyword not found in subheadings | No H2/H3 contains it | Put it in two or three headings (e.g. the first H2, the conclusion H2, the first FAQ question) |
| Add an image with the keyword as alt | No image alt contains the phrase | Put the phrase in one or more alt attributes, naturally |
| SEO title has no number | Persian digits not counted | Use ASCII digits in the title only |
| Keyword not found in URL | Slug is English, keyword is Persian; the check is a plain string match | Either ignore (English slug is valid) or use a Persian slug with hyphens. Persian URLs get percent-encoded when copied. Redirect first if already published |
| 0 outbound links / all nofollow | No external links, or the plugin nofollows them | Add 1-2 authoritative links with `rel="noopener"`; in Rank Math -> General Settings -> Links turn off "Nofollow External Links" |
| Contains a long paragraph | Paragraphs merged because blank lines or `<p>` tags were lost in the editor, or a big text blob (e.g. JSON-LD) counted as text | Ensure a blank line between paragraphs; split paragraphs over ~100 words; as an experiment remove the JSON-LD block and re-check, then use Rank Math's FAQ block instead |
| Content length | Under ~600 words is thin | 1,300-2,000 words is a good range for a guide |

If a warning contradicts what the article actually contains, say so, offer the quick experiment, and don't invent a cause.

## Schema notes

- Rank Math already outputs Article schema. A hand-written FAQ/HowTo JSON-LD block can duplicate Rank Math's own FAQ block or be stripped by WordPress. After publishing, test the URL in Google's Rich Results Test; remove the manual block if it errors or appears as visible text.
- Google has restricted FAQ/HowTo rich results for most sites; schema is harmless and aids structure, but don't promise accordion results.

## Plugin settings worth checking once

- Sitemap on and includes Posts.
- Search Console connected (Analytics).
- Links: "Nofollow External Links" off.
- Image SEO module can fill missing alt automatically; still write alt by hand for key images.

## Honest expectations

- Score >= ~80 is a fine target; 100 is not required and isn't a ranking factor.
- Some checks misfire on Persian (multi-word phrases, density). Don't distort the article to satisfy them.
