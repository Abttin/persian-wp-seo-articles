# Persian WordPress SEO Articles

> ساخته‌شده توسط **CodeMate** 💻 — تیم طراحی سایت و توسعه وب (WordPress، WooCommerce، Elementor و AI)
> Built by **CodeMate**, a small web development team.

دستیار نوشتن مقاله سئو فارسی برای سایت‌های وردپرس با Rank Math (مخصوص بلاگ فروشگاه‌ها). خروجی: HTML آماده پیست در وردپرس + بلوک SEO (عنوان، متا، اسلاگ، کلمه کلیدی) + لیست کارهای باقی‌مانده برای صاحب سایت.

An end-to-end workflow for writing Persian (Farsi) SEO articles for WordPress + Rank Math, delivered as paste-ready HTML that survives WordPress's filters.

## دو نسخه

| نسخه | پوشه | مناسب برای |
|---|---|---|
| Claude Skill | [`claude-skill/`](claude-skill/) | Claude (claude.ai) |
| Custom GPT | [`chatgpt/`](chatgpt/) | ChatGPT |

راه نصب هر کدوم داخل README همون پوشه هست.

## چی یاد می‌گیره
- مراحل کار: ورودی‌ها ← تحقیق ← طرح ← نوشتن ← تحویل
- جلوگیری از هشدارهای رایج Rank Math (تراکم کلمه کلیدی، عدد ASCII در عنوان، لینک خروجی و ...)
- نکات وردپرس: `svg` درون‌خطی حذف می‌شه، پاراگراف‌ها باید خط خالی داشته باشن و ...
- صداقت: لینک، قیمت، آمار یا ادعای نمایندگی جعلی نمی‌سازه

## ساختار
```
persian-wp-seo-articles/
├── LICENSE
├── claude-skill/
│   ├── persian-wp-seo-articles.skill
│   └── persian-wp-seo-articles/   (SKILL.md, references, assets, scripts)
└── chatgpt/
    ├── GPT-Instructions.txt
    └── knowledge/
```

## استفاده و بازخورد
- از تب **Issues** می‌تونی باگ یا پیشنهاد بدی.
- اگه نتیجه‌ای از این ابزار گرفتی یا بهبودی ازش داشتی، خوشحال می‌شیم بدونیم.

## مجوز
MIT. استفاده، تغییر و اشتراک‌گذاری آزاده؛ فقط اسم CodeMate و متن مجوز حفظ بشه. فایل [`LICENSE`](LICENSE) رو ببین.

---
**CodeMate** — Build. Learn. Improve. Repeat. 💻
