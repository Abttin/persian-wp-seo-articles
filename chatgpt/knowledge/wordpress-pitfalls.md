# WordPress pitfalls (learned the hard way)

Contents: stripped code · links · images · preview URLs · sites that block automation · RTL and fonts

## Code that gets stripped or broken

- **Inline `<svg>`**: stripped by WordPress's HTML filter (KSES) for users without unfiltered HTML, or by a security plugin. Symptom: the shapes vanish and only the `<text>` labels remain, separated by `<br>`. Fix: render the diagram to WebP/PNG and use `<img>`.
- **`<script type="application/ld+json">`**: may be removed or shown as text. Tell the owner to check the published page and delete the block if it misbehaves.
- **Missing `<p>` tags**: the editor may turn paragraphs into plain text separated by newlines (WordPress adds `<p>` automatically where there's a blank line). Always keep a blank line between paragraphs.
- Heading `id` attributes and `#anchor` links work in a Custom HTML block or the Code editor. The visual editor may drop them if the user toggles back and forth, so tell the owner to paste into the Code editor and avoid switching modes.

## Links

- Never guess internal URLs. Only use ones the owner gave or ones that appeared in tool results. If unknown, link to the shop page and list what to replace later.
- Percent-encoded Persian category URLs (`%d8%a7...`) are fine as given. Copy them exactly.
- Link a new article from older related posts after publishing.

## Images

- Upload to the Media Library, then reference the full URL. The path normally follows `/wp-content/uploads/YYYY/MM/file.webp`; if the image doesn't show, the real URL differs (check the Media Library).
- Prefer WebP; keep PNG as a fallback if the site rejects WebP.
- Include `width`, `height`, `loading="lazy"` and `style="max-width:100%; height:auto;"`.
- Describe content in filenames and alt text. Don't use stock/web photos without rights.
- Check an offered image really matches the topic (e.g. a "coaxial cable" photo is not a coaxial speaker).

## Preview URLs

- `?preview=true&preview_nonce=...` links only work for the logged-in editor. Never submit them to Search Console. Use the final public URL after publishing.

## Sites that block automation

- Many sites (including the owner's own) return `ROBOTS_DISALLOWED` to web fetch. Don't retry; use search results, ask the owner to paste text/links, or parse an uploaded copy.
- The sandbox may have no network: you can't `git clone` or `pip install` from the internet. Tell the owner how to install things themselves (e.g. Download ZIP -> Customize -> Skills -> upload).

## RTL and fonts

- When rendering Persian text into images, Pillow must be built with Raqm (`features.check('raqm')`) and you must pass `direction="rtl"` and `language="fa"`. DejaVu Sans supports Persian letters and Persian digits. Without Raqm, text appears disconnected or reversed.
- Persian digits (۱۲۳) in body text are fine; only the SEO title needs ASCII digits for Rank Math.
