[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

Инструмент для анализа этимологии слов и визуализации результатов в виде интерактивных графов.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Overview

WordOrigins — это веб-приложение на Python, которое позволяет изучать этимологию (происхождение и историческое развитие) слов. Оно выполняет подробный анализ эволюции слов, разбирает их на составные части, рекурсивно отслеживает языковую родословную каждой части и отображает результат как изображение графа в браузере.

### ✨ Key Features

- Подробный этимологический анализ любого слова
- Визуальное представление происхождения слова в виде графа
- Поддержка нескольких языков, включая английский, французский, арабский, японский и китайский
- Интерактивный веб-интерфейс для исследования

## Features

| Feature | Details |
|---|---|
| 🔎 Web UI | Поиск и просмотр сгенерированных этимологических графов |
| 🧠 OpenAI-backed analysis | Использует OpenAI API для получения структурированного этимологического вывода |
| 💾 Caching | Кэширует ответы OpenAI как JSON-снимки с временными метками |
| 🖼️ Artifact generation | Кэширует JSON- и PNG-артефакты для ранее проанализированных слов |
| 🌍 Multilingual rendering | Поддержка шрифтов CJK и Arabic включена в репозиторий |
| ↔️ Navigation | Переход к следующему/предыдущему слову среди сгенерированных изображений |
| 🔌 API support | Endpoint возвращает PNG в формате base64 |

## How It Works

1. Введите слово, которое хотите проанализировать.
2. Система подключается к API OpenAI для углубленного этимологического анализа.
3. Анализатор валидирует/разбирает вывод модели в структурированный JSON.
4. Результаты кэшируются и преобразуются в ориентированный граф.
5. Граф рендерится в PNG и отображается в веб-интерфейсе.
6. Можно просматривать ранее проанализированные слова.

## Project Structure

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

## Prerequisites

- Python 3.8+
- OpenAI API key
- Необходимые шрифты (включены в репозиторий):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Setup

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Установите OpenAI API key в переменную окружения:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notes on dependencies

Код импортирует эти пакеты во время выполнения:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Предположение: `requirements.txt` должен включать перечисленные выше пакеты. Если в вашей локальной копии `requirements.txt` отсутствует, установите их вручную.

## Usage

### Running the Web Application

Запустите Tornado web server:

```bash
python app.py
```

Затем откройте в браузере `http://localhost:7788`.

### Typical user flow

1. Откройте `http://localhost:7788`.
2. Введите слово в поле поиска.
3. Приложение выполняет анализ и рендерит этимологический граф.
4. Используйте элементы управления previous/next для просмотра сгенерированных слов.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Генерирует и отображает этимологический граф для слова |
| `GET` | `/word/next-word` | Перейти к следующему слову в списке |
| `GET` | `/word/prev-word` | Перейти к предыдущему слову в списке |
| `GET/POST` | `/get_word_etymology/{word}` | API endpoint для получения данных этимологии как base64 PNG payload |

### Example API calls

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuration

### Environment variables

- `OPENAI_API_KEY` (обязательно): API key, используемый OpenAI Python client
- `OPENAI_MODEL` (опционально): имя модели, используемой анализатором (по умолчанию `gpt-4-0125-preview`)

### Runtime directories created/used by the app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Components

### WordEtymologyAnalyzer

Подключается к API OpenAI для получения подробной этимологической информации по заданному слову. Включает логику кэширования и повторных попыток:

- Приводит входные слова к нижнему регистру
- Пытается надежно разобрать JSON-вывод (`json5`)
- Сохраняет снимки анализа с временными метками в `word_etymology_analysis/`
- Ведет учет обработанных слов в `processed_words.csv`

### EtymologyGraph

Создает визуальные представления этимологических данных с помощью NetworkX и Matplotlib:

- Рекурсивно отображает вложенную этимологию в узлы/ребра ориентированного графа
- Вычисляет радиальное позиционирование на основе глубины
- Отрисовывает подписи частей/значений/примеров и метки языков на ребрах
- Обрабатывает рендеринг многоязычного текста с использованием включенных шрифтов

### Web Application

Веб-сервер на Tornado, который обрабатывает запросы и отдает пользовательский интерфейс:

- Перенаправляет `/` на `/word/etymology`
- Рендерит графы слов из `static/images/`
- Генерирует отсутствующие анализы/изображения по запросу

## Examples

### Analyze a new word

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Ожидаемые результаты после первого запуска:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Browse existing generated words

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technical Details

- Приложение сохраняет JSON-файлы проанализированных слов для кэширования.
- Изображения генерируются в формате PNG.
- Для многоязычной поддержки реализована специальная обработка шрифтов.
- Макет графа вычисляется на основе глубины узлов и связей.
- Текущий репозиторий включает исследовательские notebook-файлы и архивные артефакты, использованные в ходе разработки.

## Development Notes

- Основная точка входа во время выполнения — `app.py`.
- Файлы notebook (`etymology*.ipynb`) являются экспериментальными и могут отличаться от потока production server.
- Есть legacy/duplicate пути (`statics/` vs `static/`, `.old` files), которые сохранены для исторического контекста.
- Текущий `.gitignore`, похоже, содержит неразрешенные маркеры merge-conflict; очистите это перед подготовкой релиза.

## Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` on startup | Установите отсутствующие зависимости: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` error or authentication failure | Убедитесь, что `OPENAI_API_KEY` экспортирован в той же shell-сессии, где вы запускаете `python app.py` |
| Graph text renders as boxes or missing glyphs | Проверьте, что включенные файлы шрифтов присутствуют в ожидаемых путях репозитория |
| No image generated for a word | Проверьте логи сервера на JSON parse retries/exceptions и подтвердите доступ к сети/API |
| `pip install -r requirements.txt` fails because file is missing | Создайте локальный файл зависимостей на основе списка пакетов в этом README или установите пакеты напрямую |

## Roadmap

- Добавить поддержку большего числа языков.
- Реализовать учетные записи пользователей для сохранения избранных этимологий.
- Улучшить визуализацию графов с масштабированием и панорамированием.
- Добавить более подробную лингвистическую информацию.
- Добавить поддерживаемый манифест зависимостей и воспроизводимую настройку окружения.
- Добавить тесты для разбора анализатора, поведения кэширования и обработчиков маршрутов.

## Contribution

Приветствуются любые вклады. Рекомендуемый процесс:

1. Fork the repository.
2. Create a feature branch.
3. Make focused, reviewable changes.
4. Validate by running `python app.py` and checking key routes.
5. Open a pull request with a clear description and screenshots/API samples when relevant.

## Dependencies

- tornado: Фреймворк веб-сервера
- openai: OpenAI API client
- matplotlib: Для генерации графов
- networkx: Для структуры данных графа
- PIL/Pillow: Для обработки изображений
- numpy: Для численных операций
- cjkwrap: Для переноса CJK-текста
- json5: Для надежного разбора JSON

## License

Apache License 2.0

Подробные условия см. в [LICENSE](LICENSE).

## Acknowledgements

- OpenAI за предоставление возможностей лингвистического анализа
- Шрифты Google Noto за поддержку многоязычного текста
