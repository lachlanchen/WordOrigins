[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


**Language options:** English (this file)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

A tool for analyzing word etymologies and visualizing them as interactive graphs.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Quick Snapshot

| Area | Details |
|---|---|
| 🌐 Access | Web UI for interactive exploration and API for base64 PNG output |
| 🧠 Intelligence | OpenAI-powered etymology analysis with structured JSON parsing |
| 🧰 Reproducibility | Cached JSON + PNG artifacts for each processed word |
| 🌍 Language Support | Multi-language rendering for CJK and Arabic with bundled fonts |

## Overview

WordOrigins is a Python web application that allows you to explore the etymology (origin and historical development) of words. It provides detailed analysis of how words evolved over time, breaks them into their component parts, recursively traces each part's linguistic lineage, and renders the result as a graph image for browser viewing.

### ✨ Key Features

- Detailed etymology analysis of any word
- Visual graph representation of word origins
- Support for multiple languages including English, French, Arabic, Japanese, and Chinese
- Interactive web interface for exploration

## Features

| Feature | Details |
|---|---|
| 🔎 Web UI | Search and browse generated etymology graphs |
| 🧠 OpenAI-backed analysis | Uses OpenAI API to produce structured etymology output |
| 💾 Caching | Cached OpenAI responses as timestamped JSON snapshots |
| 🖼️ Artifact generation | Cached JSON and PNG artifacts for previously analyzed words |
| 🌍 Multilingual rendering | CJK + Arabic font support bundled in repository |
| ↔️ Navigation | Next/previous browsing through generated word images |
| 🔌 API support | Endpoint returns PNG output as base64 |

## How It Works

1. Enter a word you want to analyze.
2. The system connects to OpenAI's API to perform deep etymology analysis.
3. The analyzer validates/parses model output into structured JSON.
4. Results are cached and transformed into a directed graph.
5. The graph is rendered as a PNG and displayed in the web interface.
6. You can browse through previously analyzed words.

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

## Prerequisites

- Python 3.8+
- OpenAI API key
- Required fonts (included in the repository):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notes on dependencies

The code imports these packages at runtime:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Assumption: `requirements.txt` should include the packages above. If `requirements.txt` is missing in your local copy, install these manually.

## Usage

### Running the Web Application

Start the Tornado web server:

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:7788`.

### Typical user flow

1. Open `http://localhost:7788`.
2. Enter a word in the search box.
3. The app analyzes and renders the etymology graph.
4. Use previous/next controls to browse generated words.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Generates and displays the etymology graph for a word |
| `GET` | `/word/next-word` | Navigate to the next word in the list |
| `GET` | `/word/prev-word` | Navigate to the previous word in the list |
| `GET/POST` | `/get_word_etymology/{word}` | API endpoint to get etymology data as a base64 PNG payload |

### Example API calls

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuration

### Environment variables

- `OPENAI_API_KEY` (required): API key used by the OpenAI Python client
- `OPENAI_MODEL` (optional): model name used by analyzer (defaults to `gpt-4-0125-preview`)

### Runtime directories created/used by the app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Components

### WordEtymologyAnalyzer

Connects to OpenAI's API to get detailed etymology information for a given word. Includes caching and retry logic:

- Lowers and normalizes input words
- Attempts to parse JSON output robustly (`json5`)
- Saves timestamped analysis snapshots in `word_etymology_analysis/`
- Records processed words in `processed_words.csv`

### EtymologyGraph

Creates visual representations of etymology data using NetworkX and Matplotlib:

- Recursively maps nested etymology into directed graph nodes/edges
- Computes depth-based radial positioning
- Draws part/meaning/example and language edge labels
- Handles multilingual text rendering with bundled fonts

### Web Application

A Tornado-based web server that handles requests and serves the user interface:

- Redirects `/` to `/word/etymology`
- Renders word graphs from `static/images/`
- Generates missing analyses/images on demand

## Examples

### Analyze a new word

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Expected outputs after first run:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Browse existing generated words

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technical Details

- The application stores JSON files of analyzed words for caching.
- Images are generated as PNG files.
- Special font handling is implemented for multilingual support.
- The graph layout is calculated based on node depth and relationships.
- Existing repository includes exploratory notebooks and archived artifacts used during development.

## Development Notes

- Primary runtime entrypoint is `app.py`.
- Notebook files (`etymology*.ipynb`) are experimental and may diverge from production server flow.
- There are legacy/duplicate paths (`statics/` vs `static/`, `.old` files) kept for historical context.
- Current `.gitignore` appears to contain unresolved merge-conflict markers; clean this before release packaging.

## Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` on startup | Install missing dependencies: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` error or authentication failure | Ensure `OPENAI_API_KEY` is exported in the same shell session where you launch `python app.py` |
| Graph text renders as boxes or missing glyphs | Verify bundled font files are present in expected repository paths |
| No image generated for a word | Check server logs for JSON parse retries/exceptions and confirm network/API access |
| `pip install -r requirements.txt` fails because file is missing | Create a local dependency file from the package list in this README or install packages directly |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Roadmap

- Add support for more languages.
- Implement user accounts to save favorite etymologies.
- Improve graph visualization with zooming and panning.
- Add more detailed linguistic information.
- Add a maintained dependency manifest and reproducible environment setup.
- Add tests for analyzer parsing, caching behavior, and route handlers.

## Contribution

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a feature branch.
3. Make focused, reviewable changes.
4. Validate by running `python app.py` and checking key routes.
5. Open a pull request with a clear description and screenshots/API samples when relevant.

## Dependencies

- tornado: Web server framework
- openai: OpenAI API client
- matplotlib: For generating graphs
- networkx: For graph data structure
- PIL/Pillow: For image processing
- numpy: For numerical operations
- cjkwrap: For handling CJK text wrapping
- json5: For robust JSON parsing

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Acknowledgements

- OpenAI for providing the linguistic analysis capabilities
- Google Noto fonts for multilingual text support

## License

Apache License 2.0

See [LICENSE](LICENSE) for full terms.
