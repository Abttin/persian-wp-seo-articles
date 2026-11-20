# نسخه Claude (Skill)

اسکیل نوشتن مقاله سئو فارسی برای وردپرس (Rank Math).

## نصب
1. فایل `persian-wp-seo-articles.skill` رو دانلود کن.
2. در Claude: Settings ← Customize ← Skills ← آپلود فایل.

یا پوشه `persian-wp-seo-articles/` رو خودت زیپ کن و آپلود کن (فایل `SKILL.md` باید داخل پوشه باشه).

## ساختار
- `SKILL.md`: دستورالعمل اصلی
- `references/`: چک‌لیست Rank Math و مشکلات وردپرس
- `assets/article-template.html`: قالب مقاله
- `scripts/make_infographic.py`: ساخت اینفوگرافیک فارسی (نیاز به Pillow با Raqm)
