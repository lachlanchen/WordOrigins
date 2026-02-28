[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 اعرض أصول الكلمات كرسوم ترحيل لغوية متعددة المسارات باستخدام سير عمل مدعوم من OpenAI وسهل التخزين المؤقت.

**خيارات اللغة:** العربية (هذا الملف)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#components)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](#license)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)
[![GitHub last commit](https://img.shields.io/github/last-commit/lachlanchen/WordOrigins?color=blue)](https://github.com/lachlanchen/WordOrigins/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/lachlanchen/WordOrigins?color=red)](https://github.com/lachlanchen/WordOrigins/issues)
[![GitHub repo size](https://img.shields.io/github/repo-size/lachlanchen/WordOrigins?color=yellow)](https://github.com/lachlanchen/WordOrigins)

![Word Origins Demo](word_origins.jpg)

## نظرة عامة

`WordOrigins` هي أداة ويب مكتوبة بلغة Python لتحليل أصول الكلمات وعرض سلسلة النسب اللغوي كرسوم بيانية موجهة. تجمع بين:

- تطبيق ويب مبني على Tornado.
- تحليل أصول الكلمات بواسطة OpenAI.
- تحليل JSON منظم مع معالجة احتياطية متينة.
- توليد الرسوم عبر NetworkX + Matplotlib.
- مخرجات مخزنة مؤقتًا لتحليل أسرع عند التكرار.

توفر واجهة متصفح وواجهات برمجة تطبيقات (API) لإنشاء واسترجاع مخرجات التحليل.

## 📸 لقطة سريعة

| المجال | التفاصيل |
|---|---|
| 🌐 الوصول | واجهة ويب للاستكشاف التفاعلي وواجهة API لإخراج PNG بصيغة base64 |
| 🧠 الذكاء | تحليل أصول كلمات مدعوم من OpenAI مع تحليل JSON منظم |
| 🧰 إعادة الإنتاج | JSON وPNG مخزنة مؤقتًا لكل كلمة يتم تحليلها |

## المزايا

| الميزة | التفاصيل |
|---|---|
| 🔎 واجهة الويب | بحث وتصفح رسومات الأصول التي تم إنشاؤها |
| 🧠 تحليل مدعوم من OpenAI | يستخدم OpenAI API لإنتاج مخرجات أصول منظمة |
| 💾 التخزين المؤقت | يحفظ الردود مع لقطات زمنية لملفات JSON |
| 🖼️ إنشاء المخرجات | يصدر JSON وPNG للكلمات التي تمت معالجتها |
| ↔️ التنقل | زر التالي/السابق للتنقل بين صور الكلمات المنتجة |
| 🔌 دعم API | نقطة نهاية ترجع صورة PNG داخل حمل JSON بصيغة base64 |

## 🛠️ طريقة العمل

1. يرسل المستخدم كلمة عبر `/word/{word}` أو عبر نموذج البحث في الويب.
2. يستدعي المحلل OpenAI ويتحقق من شكل الاستجابة.
3. تُطبّع البيانات المحللة وتُحفظ لإعادة الاستخدام من التخزين المؤقت.
4. تُحوّل علاقات الأصول إلى عقد وحواف في الرسم.
5. يقوم NetworkX وMatplotlib برسم الرسم الموجّه بصيغة PNG.
6. تُعرض واجهة الويب وAPI مسار الصورة المخزّن وبيانات التعريف المرتبطة.

## 🗂️ بنية المشروع

```text
WordOrigins/
├─ app.py                     # Tornado web app (current entrypoint)
├─ app.py.old                 # Legacy app variant
├─ word_etymology_analyzer.py # OpenAI-backed analysis + retry/caching logic
├─ etymology_graph.py         # Graph building and PNG rendering
├─ utils.py                   # Image/font/image helper utilities
├─ templates/
│  ├─ index.html              # Main web UI
│  ├─ index.html.old          # Legacy template variant
│  └─ carousel_items.html     # Reusable UI fragment
├─ static/
│  └─ images/                 # Primary runtime PNG outputs
├─ statics/
│  └─ images/                 # Legacy duplicate image folder
├─ images/                    # Screenshot/demo assets
├─ jsons/                     # Per-word generated JSON + cached data
├─ word_etymology_analysis/   # Timestamped model response cache
├─ processed_words.csv         # Processed word index
├─ i18n/                      # Translated README files
├─ archived_code/             # Historical notebooks and scripts
├─ archived_data/             # Historical JSON snapshots
├─ Noto Sans CJK Regular/     # Bundled font assets
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/
├─ arial-unicode-ms.ttf       # Bundled Unicode font
├─ etymology*.ipynb           # Development notebooks
├─ LICENSE
└─ .auto-readme-work/         # Pipeline artifacts
```

## المتطلبات المسبقة

- Python 3.8+
- مفاتيح OpenAI API:
  - `OPENAI_API_KEY` (مطلوب)
  - `OPENAI_MODEL` (اختياري، القيمة الافتراضية الحالية هي `gpt-4-0125-preview`)
- ملفات الخطوط الموجودة في المستودع إذا احتجت عرضًا متعدد اللغات

## 🧰 التثبيت

1. استنساخ المستودع.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. إنشاء وتفعيل بيئة بايثون (مستحسن).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. تثبيت المكتبات التشغيلية.

   لأن ملف تعيين التبعيات الأساسي غير موجود في هذا المستودع، ثبّت المتطلبات المعروفة مباشرة:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. إعداد مفاتيح الاعتماد.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 الاستخدام

### تشغيل تطبيق الويب

```bash
python app.py
```

افتح `http://localhost:7788` في المتصفح.

### المسار النموذجي للمستخدم

1. افتح `http://localhost:7788/word/etymology`.
2. اكتب كلمة.
3. انتظر التحليل (قد يستغرق أول تنفيذ وقتًا أطول بسبب تأخير API الخارجي).
4. استعرض الرسم البياني والبيانات الوصفية الناتجة.
5. استخدم التنقل السابق/التالي لتصفح الكلمات المخزنة مؤقتًا.

### نقاط نهاية API

| الطريقة | نقطة النهاية | الوصف |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | تعرض صفحة لأصل الكلمة المطلوبة |
| `GET` | `/word/next-word?word={word}` | الانتقال إلى الكلمة التالية في ذاكرة التخزين المؤقت |
| `GET` | `/word/prev-word?word={word}` | الانتقال إلى الكلمة السابقة في ذاكرة التخزين المؤقت |
| `GET/POST` | `/get_word_etymology/{word}` | تُرجع JSON يتضمن صورة PNG بصيغة base64 |

### استدعاءات API النموذجية

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ الإعدادات

- `OPENAI_API_KEY` (مطلوب): بيانات اعتماد طلبات التحليل.
- `OPENAI_MODEL` (اختياري): بديل نموذج للمحلل.
- أدلة التشغيل المستخدمة من الخدمة:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 أمثلة

```bash
python app.py
```

ثم افتح:

```text
http://localhost:7788/word/revolution
```

المخرجات التي تُنشأ عند أول تحليل:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## المكونات

### WordEtymologyAnalyzer

الموجود في `word_etymology_analyzer.py`، هذا المكوّن:

- يطبع/يُطَبِّع الكلمات المدخلة.
- يستدعي OpenAI للحصول على مخرجات أصول منظمة.
- يستخرج/يصلح أحمال JSON عبر `json5`.
- يعيد المحاولة عند فشل التحليل ويسجل حالات الفشل لزيادة المرونة.
- يكتب لقطات زمنية في `word_etymology_analysis/`.
- يُحدث فهرس `processed_words.csv`.

### EtymologyGraph

الموجود في `etymology_graph.py`، هذا المكوّن:

- يحمل JSON الأصول المنظم.
- يبني `networkx.DiGraph` بعلاقات النسب الهرمية.
- يحسب إحداثيات الرسم مع مراعاة العمق.
- يرسم العقد والحواف المسماة مع دعم النصوص متعددة اللغات.
- يحفظ صور `PNG` للتخزين المؤقت والعرض.

### تطبيق الويب

في `app.py`، تطبيق Tornado:

- يخدم إعادة التوجيه من الجذر وصفحة البحث.
- يتعامل مع مسارات الإنشاء والبحث في التخزين المؤقت.
- يعرض مسارات الصفحة وAPI ضمن `/word/...` و`/get_word_etymology/...`.
- يرجع حمولة JSON تحتوي على صورة base64 للمستهلكين عبر API.

## 📦 التبعيات

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 ملاحظات التطوير

- يقلل التخزين المؤقت لـJSON وPNG من استدعاءات API المكررة غير الضرورية.
- تم الاحتفاظ بـ`index.html` و`index.html.old` لاعتبارات التوافق والتاريخ.
- الأدلة والملفات القديمة موجودة بقصد قصدي حاليًا (`statics/`، الدفاتر، الأرشيف).
- تم ملاحظة وجود ملف `.gitignore` به علامات تعارض دمج كمشكلة تنظيمية خارج نطاق هذا الـ README.

## 🧯 استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
|---|---|
| `ModuleNotFoundError` عند الإقلاع | ثبّت الحزم الناقصة عبر `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| خطأ مصادقة `OPENAI_API_KEY` | تأكد من تصدير المتغير في نفس جلسة الطرفية التي تُشغّل `python app.py` فيها |
| لا تظهر صورة لأي كلمة | افحص سجلات التطبيق بحثًا عن أخطاء تحليل JSON أو أخطاء API مؤقتة |
| فشل/عدم وجود `pip install -r requirements.txt` | ثبّت التبعيات مباشرة كما هو مذكور أعلاه (المستودع لا يحتوي حاليا على ملف manifest جذري) |

## 🗺️ خارطة الطريق

- إضافة دعم لمزيد من اللغات.
- إضافة حسابات مستخدمين لمفضلة الأصول.
- تحسين التنقل في الرسوم عبر تفاعلات التكبير/التحريك.
- إغناء البيانات اللغوية في كل عقدة من الرسم البياني.
- إضافة ملف تبعيات مُدار وبيئة تشغيل قابلة للإعادة.
- إضافة اختبارات لتحليل المحلل، وسلوك التخزين المؤقت، ومعالجات المسارات.

## 🤝 المساهمة

1. اعمل fork للمستودع.
2. أنشئ فرع ميزات.
3. نفّذ تغييرات مركزة وسهلة المراجعة.
4. تحقق عبر تشغيل `python app.py` والتأكد من المسارات الأساسية.
5. افتح Pull Request مع تعليمات إعادة التشغيل ولقطات شاشة/أمثلة API.

## 🙌 الإشادات

- OpenAI لقدرات التحليل المستندة إلى نماذج اللغة.
- مساهمو عائلة خطوط Google Noto لدعم العرض متعدد اللغات.

## الترخيص

Apache License 2.0  
See [LICENSE](LICENSE) for full terms.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
