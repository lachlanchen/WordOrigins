[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**خيارات اللغة:** العربية (هذا الملف)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

أداة لتحليل أصول الكلمات وعرضها كرسوم تفاعلية.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#المتطلبات-المسبقة)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#نظرة-عامّة)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#نقاط-النهاية-للـ-API)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#رسم-الاشتقاق-اللغوي)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#الميزات)

![Word Origins Demo](word_origins.jpg)

## لمحة سريعة

| المجال | التفاصيل |
|---|---|
| 🌐 الوصول | واجهة ويب لاستكشاف البيانات بشكل تفاعلي وواجهة برمجة تطبيقات لإخراج PNG بصيغة base64 |
| 🧠 الذكاء | تحليل أصول الكلمات مدعوم بـ OpenAI مع تحليل JSON المنظم |
| 🧰 القابلية للإعادة | حفظ JSON وملفات PNG مؤرشفة لكل كلمة تتم معالجتها |

## نظرة عامة

`WordOrigins` هو تطبيق ويب مكتوب بلغة Python يتيح لك استكشاف أصول الكلمات (تطورها التاريخي). يوفر تحليلاً مفصلاً لكيفية تطور الكلمات عبر الزمن، ويجزئها إلى أجزاء مكوّنة، ثم يتتبع النسب اللغوي لكل جزء بشكل تكراري، ويعرض النتيجة كصورة بيانية قابلة للعرض في المتصفح.

### ✨ الميزات الرئيسية

- تحليل مفصل لأصل أي كلمة
- تمثيل رسومي مرئي لأصول الكلمات
- دعم لعدة لغات تشمل الإنجليزية والفرنسية والعربية واليابانية والصينية
- واجهة ويب تفاعلية للاستكشاف

## الميزات

| الميزة | التفاصيل |
|---|---|
| 🔎 واجهة الويب | بحث وتصفح الرسوم البيانية للأصول التي تم إنشاؤها |
| 🧠 تحليل مدعوم من OpenAI | يستخدم واجهة OpenAI API لإنتاج مخرجات أصول منظمة |
| 💾 التخزين المؤقت | تخزين إجابات OpenAI كردود JSON ضمن لقطات زمنية |
| 🖼️ إنشاء المقتنيات | حفظ JSON وملفات PNG مؤرشفة للكلمات التي تم تحليلها سابقًا |
| ↔️ التصفّح | انتقال للأمام/الخلف بين صور الكلمات المولّدة |
| 🔌 دعم API | نقطة النهاية ترجع صورة PNG بتنسيق base64 |

## كيف يعمل

1. أدخل كلمة تريد تحليلها.
2. يتصل النظام بواجهة OpenAI API لإجراء تحليل عميق للأصل اللغوي.
3. يتحقق المحلّل من صحة مخرجات النموذج ويفسّرها إلى JSON منظم.
4. تُخزَّن النتائج مؤقتًا ثم تتحول إلى رسم بياني موجّه.
5. يُعرض الرسم البياني كصورة PNG في واجهة الويب.
6. يمكنك تصفح الكلمات التي حللتها مسبقًا.

## بنية المشروع

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Tornado web server entrypoint
├─ word_etymology_analyzer.py          # OpenAI-backed etymology analysis + caching
├─ etymology_graph.py                  # NetworkX + Matplotlib graph generation
├─ utils.py                            # Image/texture helper utilities
├─ templates/
│  ├─ index.html                       # Main UI
│  ├─ index.html.old                   # Legacy template variant
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Primary rendered PNG outputs
├─ statics/
│  └─ images/                          # Legacy duplicate image folder
├─ jsons/                              # Per-word JSON and image artifacts
├─ word_etymology_analysis/            # Timestamped model response cache
├─ processed_words.csv                  # Processed word log
├─ i18n/                               # Multilingual README/docs files
├─ archived_code/                      # Historical notebooks/code
├─ archived_data/                      # Historical JSON outputs
├─ etymology*.ipynb                    # Notebook experiments
├─ Noto Sans CJK Regular/              # Bundled CJK font
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # Bundled Arabic + Noto families
└─ arial-unicode-ms.ttf                # Unicode-supporting font
```

## المتطلبات المسبقة

- Python 3.8+
- OpenAI API key
- الخطوط المطلوبة (مضمنة داخل المستودع):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## التثبيت

### الإعداد

1. استنساخ المستودع:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. تثبيت التبعيات:
   ```bash
   pip install -r requirements.txt
   ```

3. تعيين مفتاح OpenAI API كمتغير بيئة:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### ملاحظات التبعيات

يقوم الكود باستيراد الحزم التالية أثناء التشغيل:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

الفرضية: `requirements.txt` يجب أن يتضمن الحزم المذكورة أعلاه. إذا كان الملف مفقودًا في نسختك المحلية، ثبّت هذه الحزم يدويًا.

## الاستخدام

### تشغيل تطبيق الويب

ابدأ تشغيل خادم Tornado:

```bash
python app.py
```

ثم افتح المتصفح واذهب إلى `http://localhost:7788`.

### سيناريو المستخدم النموذجي

1. افتح `http://localhost:7788`.
2. أدخل كلمة في مربع البحث.
3. يحلل التطبيق الكلمات ويعرض رسم أصولها.
4. استخدم أزرار السابق/التالي لتصفح الكلمات المولّدة.

### نقاط نهاية الـ API

| الطريقة | نقطة النهاية | الوصف |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | ينشئ ويعرض رسم أصول الكلمة |
| `GET` | `/word/next-word` | الانتقال إلى الكلمة التالية في القائمة |
| `GET` | `/word/prev-word` | العودة إلى الكلمة السابقة في القائمة |
| `GET/POST` | `/get_word_etymology/{word}` | نقطة نهاية API للحصول على بيانات الأصول كحمولة PNG بصيغة base64 |

### أمثلة استدعاءات API

```bash
# إنشاء/عرض كلمة في المتصفح
curl "http://localhost:7788/word/etymology"

# جلب صورة base64
curl "http://localhost:7788/get_word_etymology/etymology"
```

## الإعدادات

### متغيرات البيئة

- `OPENAI_API_KEY` (مطلوب): مفتاح API المستخدم بواسطة عميل OpenAI Python
- `OPENAI_MODEL` (اختياري): اسم النموذج المستخدم في المحلل (افتراضيًا `gpt-4-0125-preview`)

### أدلة التشغيل المستخدمة/المنشأة بواسطة التطبيق

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## المكونات

### WordEtymologyAnalyzer

يتصل بواجهة OpenAI API للحصول على معلومات مفصلة عن أصول الكلمات. ويضم آلية تخزين مؤقت ومنطق إعادة المحاولة:

- تحويل الكلمات إلى صيغة موحدة وصغيرة
- محاولة تحليل ناتج JSON بشكل متين باستخدام (`json5`)
- حفظ لقطات التحليل مع الطابع الزمني داخل `word_etymology_analysis/`
- تسجيل الكلمات المعالجة داخل `processed_words.csv`

### EtymologyGraph

ينشئ تمثيلات بصرية لبيانات الأصول باستخدام NetworkX وMatplotlib:

- يربط التحليل المتداخل للمراتب اللغوية إلى عقد/روابط في رسم موجه
- يحسب المواضع الشعاعية اعتمادًا على العمق
- يرسم واصفات الجزء/المعنى/المثال ووسوم الروابط اللغوية
- يتعامل مع عرض النص متعدد اللغات باستخدام الخطوط المضمّنة

### تطبيق الويب

خادم ويب مبني على Tornado يتعامل مع الطلبات ويقدم واجهة المستخدم:

- يعيد توجيه `/` إلى `/word/etymology`
- يعرض الرسوم البيانية للكلمات من `static/images/`
- ينشئ التحاليل/الصور المفقودة عند الطلب

## أمثلة

### تحليل كلمة جديدة

```bash
python app.py
# ثم افتح http://localhost:7788/word/revolution
```

المخرجات المتوقعة بعد التشغيل الأول:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### استعراض الكلمات المولدة مسبقًا

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## التفاصيل التقنية

- يحتفظ التطبيق بملفات JSON للكلمات التي تم تحليلها لأغراض التخزين المؤقت.
- يتم إنشاء الصور بصيغة ملفات PNG.
- تم تنفيذ معالجة خاصة للخطوط لدعم لغات متعددة.
- يتم حساب تخطيط الرسم البياني اعتمادًا على عمق العقد والعلاقات.
- المستودع الحالي يتضمن دفاتر استكشافية ومواد أرشيفية استخدمت أثناء التطوير.

## ملاحظات التطوير

- نقطة دخول وقت التشغيل الأساسية هي `app.py`.
- ملفات الـ notebook (`etymology*.ipynb`) تجريبية وقد تختلف عن تدفق خادم الإنتاج.
- توجد مسارات قديمة/مكررة (`statics/` مقابل `static/`، ملفات `.old`) محتفظ بها للسياق التاريخي.
- `.gitignore` الحالي يبدو أنه يحتوي على مؤشرات تعارض غير محلولة في الدمج؛ نظفها قبل التغليف النهائي للإصدار.

## استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
|---|---|
| `ModuleNotFoundError` عند الإقلاع | ثبّت التبعيات الناقصة: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| خطأ `OPENAI_API_KEY` أو فشل في المصادقة | تأكد أن `OPENAI_API_KEY` مُصدّر في نفس جلسة الطرفية التي تطلق منها `python app.py` |
| عرض النص في الرسم يظهر كصناديق أو glyphs مفقودة | تأكد أن ملفات الخطوط المضمّنة موجودة في مسارات المستودع المتوقعة |
| لا يتم توليد صورة لكلمة | افحص سجلات الخادم لعمليات إعادة المحاولة أثناء تحليل JSON وتحقق من وجود اتصال بالشبكة/API |
| فشل أمر `pip install -r requirements.txt` لعدم وجود الملف | أنشئ ملف تبعيات محليًا من قائمة الحزم المذكورة في هذا الدليل أو ثبّت الحزم مباشرة |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## خارطة الطريق

- إضافة دعم لمزيد من اللغات.
- تنفيذ حسابات المستخدمين لحفظ أصول الكلمات المفضلة.
- تحسين عرض الرسوم البيانية مع التكبير/التحريك.
- إضافة معلومات لغوية أكثر تفصيلاً.
- إضافة بيان تبعيات مُصان وبناء بيئة قابلة لإعادة الإنتاج.
- إضافة اختبارات لتحليل JSON، وسلوك التخزين المؤقت، ومعالجات المسارات.

## المساهمة

المساهمات مرحّبة. مقترح سير العمل:

1. اعمل fork للمستودع.
2. أنشئ فرع ميزة.
3. اكتب تغييرات مركزة وقابلة للمراجعة.
4. تحقق من العمل عبر تشغيل `python app.py` وفحص المسارات الرئيسية.
5. افتح طلب سحب مع وصف واضح ولقطات شاشة/عينات API إن لزم.

## التبعية

- tornado: إطار عمل خادم الويب
- openai: عميل OpenAI API
- matplotlib: لإنشاء الرسوم البيانية
- networkx: لبنية البيانات الرسومية
- PIL/Pillow: لمعالجة الصور
- numpy: للعمليات العددية
- cjkwrap: للتعامل مع تغليف النصوص للغات CJK
- json5: لتحليل JSON بشكل متين

## الشكر

- OpenAI لتوفير إمكانيات التحليل اللغوي
- خطوط Google Noto لدعم النصوص متعددة اللغات

## الترخيص

Apache License 2.0

راجع [LICENSE](LICENSE) للاطلاع على الشروط الكاملة.
