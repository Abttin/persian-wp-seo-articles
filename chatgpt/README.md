# نسخه ChatGPT (Custom GPT / Project)

## روش اول: Custom GPT
1. ChatGPT ← Explore GPTs ← Create ← Configure
2. محتوای `GPT-Instructions.txt` رو توی Instructions پیست کن (حدود ۷۰۰۰ کاراکتر، زیر سقف ۸۰۰۰)
3. فایل‌های پوشه `knowledge/` رو توی Knowledge آپلود کن
4. **Web Search** و **Code Interpreter** رو روشن کن
5. برای اینفوگرافیک یه فونت فارسی `.ttf` (مثل Vazirmatn) هم آپلود کن

## روش دوم: Project
محتوای `GPT-Instructions.txt` رو توی Project instructions بذار و فایل‌های `knowledge/` رو به Project اضافه کن.

## محدودیت‌ها
- ساخت Custom GPT معمولاً اشتراک پولی می‌خواد.
- فایل‌های Knowledge با جستجو خونده می‌شن، پس پایبندی به ریزقوانین ممکنه از نسخه Claude کمتر باشه.
- رندر فارسی اینفوگرافیک به فونت و Raqm (یا `arabic_reshaper` + `python-bidi`) بستگی داره؛ خروجی رو حتماً چک کن.
