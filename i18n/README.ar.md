[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

أداة لتحليل أصول الكلمات (Etymology) وتمثيلها بصريًا على شكل رسوم بيانية تفاعلية.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

<a id="overview"></a>
## نظرة عامة

WordOrigins تطبيق ويب بلغة Python يتيح لك استكشاف إيتيمولوجيا الكلمات (أصل الكلمة وتطورها التاريخي). يقدّم تحليلًا مفصلًا لكيفية تطور الكلمات عبر الزمن، ويقسّمها إلى أجزائها المكوّنة، ويتتبّع السلسلة اللغوية لكل جزء بشكل تكراري، ثم يعرض النتيجة كصورة رسم بياني لعرضها في المتصفح.

### ✨ الميزات الرئيسية

- تحليل إيتيمولوجي مفصل لأي كلمة
- تمثيل بصري على شكل رسم بياني لأصول الكلمات
- دعم لغات متعددة تشمل الإنجليزية والفرنسية والعربية واليابانية والصينية
- واجهة ويب تفاعلية للاستكشاف

<a id="features"></a>
## الميزات

| الميزة | التفاصيل |
|---|---|
| 🔎 واجهة ويب | البحث وتصفح رسوم الإيتيمولوجيا التي يتم توليدها |
| 🧠 تحليل مدعوم بـ OpenAI | يستخدم OpenAI API لإنتاج مخرجات إيتيمولوجيا منظّمة |
| 💾 التخزين المؤقت | حفظ ردود OpenAI كنسخ JSON مؤرخة زمنيًا |
| 🖼️ توليد المخرجات | تخزين ملفات JSON وصور PNG للكلمات التي تم تحليلها مسبقًا |
| ↔️ التنقل | تصفّح الصور المولدة للكلمات التالية/السابقة |
| 🔌 دعم API | نقطة نهاية تُرجع مخرجات PNG بصيغة base64 |

## طريقة العمل

1. أدخل الكلمة التي تريد تحليلها.
2. يتصل النظام بواجهة OpenAI API لإجراء تحليل إيتيمولوجي عميق.
3. يقوم المحلل بالتحقق/التحليل النحوي لمخرجات النموذج وتحويلها إلى JSON منظّم.
4. يتم تخزين النتائج مؤقتًا وتحويلها إلى رسم بياني موجّه.
5. يُعرَض الرسم البياني كصورة PNG داخل واجهة الويب.
6. يمكنك تصفح الكلمات التي تم تحليلها مسبقًا.

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
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Primary rendered PNG outputs
├─ statics/
│  └─ images/                          # Legacy duplicate image folder
├─ jsons/                              # Per-word JSON and image artifacts
├─ word_etymology_analysis/            # Timestamped model response cache
├─ processed_words.csv                 # Processed word log
├─ i18n/                               # Reserved for multilingual README/docs files
├─ archived_code/                      # Historical notebooks/code
├─ archived_data/                      # Historical JSON outputs
├─ etymology*.ipynb                    # Notebook experiments
├─ Noto Sans CJK Regular/              # Bundled CJK font
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # Bundled Arabic + Noto families
└─ arial-unicode-ms.ttf                # Unicode-supporting font
```

<a id="prerequisites"></a>
## المتطلبات المسبقة

- Python 3.8+
- مفتاح OpenAI API
- الخطوط المطلوبة (مضمنة في المستودع):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## التثبيت

### الإعداد

1. استنسخ المستودع:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. ثبّت الاعتماديات:
   ```bash
   pip install -r requirements.txt
   ```

3. اضبط مفتاح OpenAI API كمتغير بيئة:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### ملاحظات حول الاعتماديات

يقوم الكود باستيراد هذه الحزم أثناء التشغيل:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

افتراض: يجب أن يتضمن `requirements.txt` الحزم المذكورة أعلاه. إذا كان `requirements.txt` مفقودًا في نسختك المحلية، ثبّتها يدويًا.

## الاستخدام

### تشغيل تطبيق الويب

شغّل خادم Tornado:

```bash
python app.py
```

ثم افتح المتصفح وانتقل إلى `http://localhost:7788`.

### مسار الاستخدام المعتاد

1. افتح `http://localhost:7788`.
2. أدخل كلمة في مربع البحث.
3. يقوم التطبيق بتحليل وعرض رسم الإيتيمولوجيا.
4. استخدم عناصر التحكم السابق/التالي لتصفح الكلمات المولدة.

<a id="api-endpoints"></a>
### نقاط نهاية API

| Method | Endpoint | الوصف |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | يولّد ويعرض رسم الإيتيمولوجيا لكلمة |
| `GET` | `/word/next-word` | الانتقال إلى الكلمة التالية في القائمة |
| `GET` | `/word/prev-word` | الانتقال إلى الكلمة السابقة في القائمة |
| `GET/POST` | `/get_word_etymology/{word}` | نقطة API للحصول على بيانات الإيتيمولوجيا كحمولة صورة PNG بصيغة base64 |

### أمثلة على استدعاءات API

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## الإعدادات

### متغيرات البيئة

- `OPENAI_API_KEY` (مطلوب): مفتاح API المستخدم بواسطة عميل OpenAI في Python
- `OPENAI_MODEL` (اختياري): اسم النموذج المستخدم بواسطة المحلل (القيمة الافتراضية `gpt-4-0125-preview`)

### المجلدات التي ينشئها/يستخدمها التطبيق أثناء التشغيل

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## المكونات

### WordEtymologyAnalyzer

يتصل بـ OpenAI API للحصول على معلومات إيتيمولوجية مفصلة لكلمة معينة. يتضمن منطق التخزين المؤقت وإعادة المحاولة:

- يحوّل الكلمات المدخلة إلى أحرف صغيرة
- يحاول تحليل مخرجات JSON بمرونة (`json5`)
- يحفظ لقطات التحليل المؤرخة زمنيًا في `word_etymology_analysis/`
- يسجّل الكلمات المعالَجة في `processed_words.csv`

<a id="etymologygraph"></a>
### EtymologyGraph

ينشئ تمثيلات بصرية لبيانات الإيتيمولوجيا باستخدام NetworkX وMatplotlib:

- يرسم الإيتيمولوجيا المتداخلة بشكل تكراري في عقد/حواف رسم بياني موجّه
- يحسب تموضعًا شعاعيًا مبنيًا على العمق
- يرسم تسميات الجزء/المعنى/المثال وتسميات لغة الحافة
- يتعامل مع عرض النصوص متعددة اللغات باستخدام الخطوط المضمنة

### تطبيق الويب

خادم ويب مبني على Tornado يتعامل مع الطلبات ويقدّم واجهة المستخدم:

- يعيد توجيه `/` إلى `/word/etymology`
- يعرض رسوم الكلمات من `static/images/`
- يولّد التحليلات/الصور المفقودة عند الطلب

## أمثلة

### تحليل كلمة جديدة

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

المخرجات المتوقعة بعد التشغيل الأول:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### تصفح الكلمات المولدة الموجودة

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## تفاصيل تقنية

- يخزّن التطبيق ملفات JSON للكلمات التي تم تحليلها من أجل التخزين المؤقت.
- يتم توليد الصور بصيغة PNG.
- تم تنفيذ معالجة خاصة للخطوط لدعم اللغات المتعددة.
- يُحسب تخطيط الرسم البياني بناءً على عمق العقد والعلاقات بينها.
- يتضمن المستودع دفاتر تجريبية ومخرجات مؤرشفة استُخدمت أثناء التطوير.

## ملاحظات التطوير

- نقطة التشغيل الأساسية وقت التنفيذ هي `app.py`.
- ملفات الدفاتر (`etymology*.ipynb`) تجريبية وقد تختلف عن مسار خادم الإنتاج.
- توجد مسارات قديمة/مكررة (`statics/` مقابل `static/` وملفات `.old`) محفوظة للسياق التاريخي.
- يبدو أن ملف `.gitignore` الحالي يحتوي على علامات تعارض دمج غير محلولة؛ نظّف ذلك قبل تجهيز الإصدار.

## استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
|---|---|
| `ModuleNotFoundError` عند بدء التشغيل | ثبّت الاعتماديات المفقودة: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| خطأ `OPENAI_API_KEY` أو فشل المصادقة | تأكد من تصدير `OPENAI_API_KEY` في نفس جلسة الطرفية التي تشغّل منها `python app.py` |
| ظهور النص في الرسم البياني كمربعات أو رموز ناقصة | تحقّق من وجود ملفات الخطوط المضمنة في مسارات المستودع المتوقعة |
| عدم توليد صورة لكلمة | افحص سجلات الخادم لأخطاء/إعادات محاولة تحليل JSON وتأكد من توفر الشبكة/واجهة API |
| فشل `pip install -r requirements.txt` بسبب غياب الملف | أنشئ ملف اعتماديات محلي من قائمة الحزم في هذا README أو ثبّت الحزم مباشرة |

## خارطة الطريق

- إضافة دعم لمزيد من اللغات.
- تنفيذ حسابات مستخدمين لحفظ الإيتيمولوجيا المفضلة.
- تحسين عرض الرسوم البيانية عبر التكبير/التحريك.
- إضافة معلومات لغوية أكثر تفصيلًا.
- إضافة ملف اعتماديات مُدار وإعداد بيئة قابل لإعادة الإنتاج.
- إضافة اختبارات لتحليل المخرجات وسلوك التخزين المؤقت ومعالجات المسارات.

## المساهمة

المساهمات مرحّب بها. سير عمل مقترح:

1. قم بعمل Fork للمستودع.
2. أنشئ فرعًا لميزة جديدة.
3. نفّذ تغييرات مركّزة وسهلة المراجعة.
4. تحقّق من النتيجة عبر تشغيل `python app.py` وفحص المسارات الأساسية.
5. افتح طلب سحب (Pull Request) بوصف واضح ولقطات شاشة/أمثلة API عند الحاجة.

## الاعتماديات

- tornado: إطار عمل خادم ويب
- openai: عميل OpenAI API
- matplotlib: لتوليد الرسوم البيانية
- networkx: لبنية بيانات الرسم البياني
- PIL/Pillow: لمعالجة الصور
- numpy: للعمليات العددية
- cjkwrap: للتعامل مع التفاف نصوص CJK
- json5: لتحليل JSON بمرونة

## الترخيص

Apache License 2.0

اطّلع على [LICENSE](LICENSE) للشروط الكاملة.

## شكر وتقدير

- OpenAI لتوفير قدرات التحليل اللغوي
- خطوط Google Noto لدعم النصوص متعددة اللغات
