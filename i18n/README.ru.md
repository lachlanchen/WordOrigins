[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Визуализируйте этимологию слов как многоязычные графы происхождения с использованием OpenAI и кэш-дружелюбного конвейера.


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

## 📘 Обзор

WordOrigins — это веб-утилита на Python для анализа этимологии слов и визуализации языковой родословной в виде ориентированного графа. Она объединяет:

- веб-приложение Tornado;
- анализ этимологии на базе OpenAI;
- структурированный разбор JSON с устойчивой обработкой fallback;
- построение графа через NetworkX + Matplotlib;
- кэшированные выводы для быстрого повторного анализа.

Проект предоставляет веб-интерфейс и API-эндпоинты для генерации и получения артефактов этимологии.

## 📸 Краткий обзор

| Область | Детали |
|---|---|
| 🌐 Доступ | Веб-интерфейс для интерактивного исследования и API для вывода PNG в формате base64 |
| 🧠 Интеллект | Анализ этимологии на основе OpenAI со структурированным разбором JSON |
| 🧰 Повторяемость | Кэшированные JSON и PNG артефакты для каждого обработанного слова |
| 🌍 Поддержка языков | Многоязычный рендеринг для CJK и арабского с поставляемыми шрифтами |

## Возможности

| Функция | Детали |
|---|---|
| 🔎 Веб-интерфейс | Поиск и просмотр сгенерированных графов этимологии |
| 🧠 Анализ с поддержкой OpenAI | Использует OpenAI API для генерации структурированного вывода по этимологии |
| 💾 Кэширование | Сохраняет ответы в виде снимков JSON с меткой времени |
| 🖼️ Генерация артефактов | Экспортирует JSON и PNG артефакты для обработанных слов |
| 🌍 Многоязычный рендеринг | Поддержка CJK + арабского с поставляемыми в репозитории шрифтами |
| ↔️ Навигация | Переключение вперед/назад по сгенерированным изображениям слов |
| 🔌 Поддержка API | Эндпоинт возвращает PNG-вывод как base64 JSON payload |

## 🛠️ Как это работает

1. Пользователь отправляет слово через `/word/{word}` или форму поиска в веб-интерфейсе.
2. Анализатор обращается к OpenAI и проверяет структуру ответа.
3. Разобранные данные нормализуются и сохраняются для повторного использования кэша.
4. Этимологические отношения преобразуются в узлы и рёбра графа.
5. NetworkX и Matplotlib рендерят ориентированный граф в PNG.
6. UI и API возвращают путь к кэшированному изображению и связанную метадату.

## 🗂️ Структура проекта

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

## Предварительные требования

- Python 3.8+
- Учетные данные OpenAI API:
  - `OPENAI_API_KEY` (обязательно)
  - `OPENAI_MODEL` (необязательно, по умолчанию `gpt-4-0125-preview` в текущих рекомендациях)
- Файлы шрифтов, поставляемые в репозиторий, если нужна многоязычная отрисовка

## 🧰 Установка

1. Клонируйте репозиторий.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Создайте и активируйте среду Python (рекомендуется).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Установите зависимости рантайма.

   В этом репозитории отсутствует корневой манифест зависимостей, поэтому установите известные обязательные пакеты напрямую:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Настройте учетные данные.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 Использование

### Запуск веб-приложения

```bash
python app.py
```

Откройте `http://localhost:7788` в браузере.

### Типичный пользовательский поток

1. Откройте `http://localhost:7788/word/etymology`.
2. Введите слово.
3. Подождите анализа (первый запуск может занять больше времени из-за задержек внешнего API).
4. Изучите сгенерированный граф и метаданные.
5. Используйте переходы вперед/назад для просмотра слов из кэша.

### API эндпоинты

| Метод | Эндпоинт | Описание |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Рендерит страницу запрошенной этимологии |
| `GET` | `/word/next-word?word={word}` | Переход к следующему слову в кэше |
| `GET` | `/word/prev-word?word={word}` | Переход к предыдущему слову в кэше |
| `GET/POST` | `/get_word_etymology/{word}` | Возвращает JSON-тело с base64 PNG payload |

### Примеры вызовов API

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Конфигурация

- `OPENAI_API_KEY` (обязателен): учетные данные для анализа запросов.
- `OPENAI_MODEL` (необязательно): переопределение модели для анализатора.
- Каталоги времени выполнения, используемые сервисом:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Примеры

```bash
python app.py
```

Затем откройте:

```text
http://localhost:7788/word/revolution
```

Артефакты, создаваемые при первом анализе:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Компоненты

### WordEtymologyAnalyzer

Расположен в `word_etymology_analyzer.py`, этот компонент:

- Нормализует входные слова.
- Обращается к OpenAI для получения структурированных ответов по этимологии.
- Извлекает/исправляет JSON через `json5`.
- Повторяет неудачные попытки разбора и логирует ошибки для устойчивости.
- Записывает снимки с временными метками в `word_etymology_analysis/`.
- Обновляет индекс `processed_words.csv`.

### EtymologyGraph

Расположен в `etymology_graph.py`, этот компонент:

- Загружает структурированную JSON-этимологию.
- Строит `networkx.DiGraph` с рекурсивными родословными связями.
- Рассчитывает координаты графа с учетом глубины.
- Рендерит помеченные узлы и рёбра графа с учетом многоязычного текста.
- Сохраняет изображения `PNG` для кэша и показа.

### Веб-приложение

В `app.py` приложение Tornado:

- Обрабатывает редирект корня и поведение страницы поиска.
- Выполняет обработку генерации и поиски в кэше.
- Экспонирует маршруты страниц и API по путям `/word/...` и `/get_word_etymology/...`.
- Возвращает JSON с base64-данными изображения для потребителей API.

## 📦 Зависимости

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Заметки по разработке

- Кэширование JSON и изображений помогает избегать лишних повторных запросов к API.
- `index.html` и `index.html.old` сохранены ради совместимости и истории.
- Устаревшие каталоги и артефакты сейчас намеренно остаются (`statics/`, блокноты, архивы).
- `.gitignore` с маркерами конфликтов слияния отмечен как проблема гигиены репозитория вне рамок README.

## 🧯 Устранение неполадок

| Проблема | Решение |
|---|---|
| `ModuleNotFoundError` при старте | Установите отсутствующие пакеты через `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Ошибка аутентификации `OPENAI_API_KEY` | Убедитесь, что переменная экспортирована в той же сессии оболочки, где запускается `python app.py` |
| Отсутствуют/искажены глифы в сгенерированных графах | Убедитесь, что поставляемые шрифты (`Noto Sans`, арабские варианты, Arial Unicode MS) существуют и доступны для чтения |
| Для слова не отображается изображение | Проверьте логи приложения на ошибки разбора JSON или временные ошибки API |
| `pip install -r requirements.txt` не выполняется/не существует | Устанавливайте зависимости напрямую, как указано выше (в текущем репозитории отсутствует корневой манифест) |

## 🗺️ Дорожная карта

- Добавить поддержку дополнительных языков.
- Добавить пользовательские аккаунты для избранной этимологии.
- Улучшить навигацию по графу с зумированием/перемещением.
- Дополнить каждый узел графа лингвистическими метаданными.
- Добавить поддерживаемый манифест зависимостей и воспроизводимую настройку окружения.
- Добавить тесты для разбора анализатора, поведения кэша и обработчиков маршрутов.

## 🤝 Вклад

1. Сделайте форк репозитория.
2. Создайте feature-ветку.
3. Вносите сфокусированные, удобные для проверки изменения.
4. Проверьте, запустив `python app.py`, и убедитесь в корректности ключевых маршрутов.
5. Откройте PR с воспроизводимыми инструкциями и примерами скриншотов/API.

## 🙌 Благодарности

- OpenAI за возможности анализа на базе языковых моделей.
- Сообщество разработчиков шрифтов Google Noto за поддержку многоязычного рендеринга.

## Лицензия

Apache License 2.0  
См. [LICENSE](LICENSE) для полного текста.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
