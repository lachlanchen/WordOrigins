[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Visualize word etymology as multilingual provenance graphs using an OpenAI-backed, cache-friendly workflow.

**Language options:** English (this file)

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

## 📘 Overview

WordOrigins is a Python web utility for analyzing word etymology and visualizing linguistic lineage as a directed graph. It combines:

- A Tornado web application.
- OpenAI-powered etymology analysis.
- Structured JSON parsing with resilient fallback handling.
- Graph generation via NetworkX + Matplotlib.
- Cached outputs for fast repeat analysis.

It provides both a browser interface and API endpoints for generating and retrieving etymology artifacts.

## 📸 Quick Snapshot

| Area | Details |
|---|---|
| 🌐 Access | Web UI for interactive exploration and API for base64 PNG output |
| 🧠 Intelligence | OpenAI-powered etymology analysis with structured JSON parsing |
| 🧰 Reproducibility | Cached JSON + PNG artifacts for each processed word |
| 🌍 Language Support | Multi-language rendering for CJK and Arabic with bundled fonts |

## Features

| Feature | Details |
|---|---|
| 🔎 Web UI | Search and browse generated etymology graphs |
| 🧠 OpenAI-backed analysis | Uses OpenAI API to produce structured etymology output |
| 💾 Caching | Stores responses with timestamped JSON snapshots |
| 🖼️ Artifact generation | Exports JSON and PNG artifacts for processed words |
| 🌍 Multilingual rendering | CJK + Arabic support with bundled fonts in-repo |
| ↔️ Navigation | Next/previous browsing through generated word images |
| 🔌 API support | Endpoint returns PNG output as base64 JSON payload |

## 🛠️ How It Works

1. User submits a word through `/word/{word}` or the web search form.
2. The analyzer calls OpenAI and validates response structure.
3. Parsed data is normalized and persisted for cache reuse.
4. Etymology relationships are converted into graph nodes/edges.
5. NetworkX and Matplotlib render a directed graph as a PNG.
6. UI and API surface the cached image path and related metadata.

## 🗂️ Project Structure

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

## Prerequisites

- Python 3.8+
- OpenAI API credentials:
  - `OPENAI_API_KEY` (required)
  - `OPENAI_MODEL` (optional, defaults to `gpt-4-0125-preview` in existing guidance)
- Font files shipped in repository if you need multilingual rendering

## 🧰 Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Create and activate a Python environment (recommended).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install runtime libraries.

   Because no root dependency manifest exists in this repository, install the known runtime requirements directly:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Configure credentials.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 Usage

### Run the Web App

```bash
python app.py
```

Open `http://localhost:7788` in your browser.

### Typical User Flow

1. Open `http://localhost:7788/word/etymology`.
2. Enter a word.
3. Wait for analysis (first run may take longer due to external API latency).
4. Explore the generated graph and metadata.
5. Use next/previous navigation to browse cached words.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Renders a page for the requested etymology |
| `GET` | `/word/next-word?word={word}` | Navigate to the next word in the cache |
| `GET` | `/word/prev-word?word={word}` | Navigate to the previous word in the cache |
| `GET/POST` | `/get_word_etymology/{word}` | Returns a JSON body with base64 PNG payload |

### Example API Calls

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Configuration

- `OPENAI_API_KEY` (required): credentials for analysis requests.
- `OPENAI_MODEL` (optional): model override for the analyzer.
- Runtime directories used by the service:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Examples

```bash
python app.py
```

Then open:

```text
http://localhost:7788/word/revolution
```

Artifacts created for first-time analysis:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Components

### WordEtymologyAnalyzer

Located in `word_etymology_analyzer.py`, this component:

- Normalizes input words.
- Calls OpenAI for structured etymology responses.
- Extracts/repairs JSON payloads with `json5`.
- Retries failed parse attempts and records failures for resilience.
- Writes timestamped snapshots to `word_etymology_analysis/`.
- Updates `processed_words.csv` index.

### EtymologyGraph

Located in `etymology_graph.py`, this component:

- Loads structured etymology JSON.
- Builds a `networkx.DiGraph` with recursive ancestry relationships.
- Computes depth-aware graph coordinates.
- Renders labeled graph nodes and edges with multilingual text handling.
- Saves `PNG` images for caching and presentation.

### Web Application

In `app.py`, the Tornado app:

- Serves root redirect and search page behavior.
- Handles generation and cache lookup workflows.
- Exposes page and API routes under `/word/...` and `/get_word_etymology/...`.
- Returns JSON payloads containing base64 image data for API consumers.

## 📦 Dependencies

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Development Notes

- JSON and image caching avoids unnecessary repeated API calls.
- `index.html` and `index.html.old` are preserved for compatibility/history.
- Legacy directories and artifacts are currently intentionally present (`statics/`, notebooks, archives).
- A `.gitignore` file with merge-conflict markers was noted as an upstream hygiene issue outside README scope.

## 🧯 Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` at startup | Install missing packages with `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` authentication error | Ensure the variable is exported in the same shell session running `python app.py` |
| Missing/garbled glyphs in generated graphs | Confirm bundled fonts (`Noto Sans`, Arabic font variants, Arial Unicode MS) exist and are readable |
| No image appears for a word | Check app logs for JSON parse failures or transient API errors |
| `pip install -r requirements.txt` fails/does not exist | Install dependencies directly as listed above (current repo does not contain a root manifest) |

## 🗺️ Roadmap

- Add support for more languages.
- Add user accounts for favorite etymologies.
- Improve graph navigation with zooming/panning interactions.
- Enrich linguistic metadata in each graph node.
- Add a maintained dependency manifest and reproducible environment setup.
- Add tests for analyzer parsing, cache behavior, and route handlers.

## 🤝 Contribution

1. Fork the repository.
2. Create a feature branch.
3. Make focused, reviewable changes.
4. Validate by running `python app.py` and verifying key routes.
5. Open a PR with reproducible instructions and screenshots/API examples.

## 🙌 Acknowledgements

- OpenAI for language-model based analysis capabilities.
- Google Noto font family contributors for multilingual rendering support.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License

Apache License 2.0  
See [LICENSE](LICENSE) for full terms.
