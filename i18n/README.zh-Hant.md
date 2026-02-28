[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 使用 OpenAI 加持、具快取友善流程，將詞源分析視覺化為多語言詞源關係有向圖。

**語言選項：** 中文（繁體）（本文件）

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

## 📘 概覽

WordOrigins 是一個用於分析詞源並將詞彙歷史關係視覺化為有向圖的 Python Web 工具。它整合了：

- 一個 Tornado Web 應用。
- 由 OpenAI 提供能力的詞源分析。
- 帶有容錯回退機制的結構化 JSON 解析。
- 使用 NetworkX + Matplotlib 的圖形生成。
- 針對重複分析的快取輸出，顯著加快後續處理。

它同時提供瀏覽器介面與 API 端點，用於生成並擷取詞源成果。

## 📸 快速總覽

| 區域 | 說明 |
|---|---|
| 🌐 存取方式 | 提供用於互動探索的 Web UI，並提供可輸出 base64 PNG 的 API |
| 🧠 智慧分析 | 使用 OpenAI 進行詞源分析，並執行結構化 JSON 解析 |
| 🧰 可重複性 | 為每個已處理詞條快取 JSON 與 PNG 成果 |
| 🌍 語言支援 | 針對 CJK 與阿拉伯文的多語言渲染，內建字型支援 |

## <a id="features"></a>功能

| 功能 | 說明 |
|---|---|
| 🔎 Web UI | 搜尋並瀏覽已生成的詞源圖 |
| 🧠 OpenAI 驅動分析 | 使用 OpenAI API 產生結構化詞源輸出 |
| 💾 快取 | 儲存帶時間戳的回應快照 |
| 🖼️ 成果輸出 | 匯出已處理詞條的 JSON 與 PNG 產物 |
| 🌍 多語言渲染 | 內建字型支援 CJK 與阿拉伯語 |
| ↔️ 導覽 | 透過上一頁/下一頁瀏覽已生成詞條的圖片 |
| 🔌 API 支援 | 端點回傳包含 base64 圖片資料的 JSON 負載 |

## 🛠️ 運作方式

1. 使用者透過 `/word/{word}` 或網頁搜尋表單提交詞條。
2. 分析器呼叫 OpenAI 並驗證回應結構。
3. 解析後的資料會被標準化並持久化，以便重複使用快取。
4. 詞源關係被轉為圖的節點與邊。
5. NetworkX 與 Matplotlib 將有向圖渲染為 PNG。
6. 前端與 API 回傳快取圖片路徑與相關中介資料。

## 🗂️ 專案結構

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

## <a id="prerequisites"></a>先決條件

- Python 3.8+
- OpenAI API 憑證：
  - `OPENAI_API_KEY`（必填）
  - `OPENAI_MODEL`（選填，既有說明預設 `gpt-4-0125-preview`）
- 若需要多語言渲染，請確保倉庫中包含必要字型檔案

## 🧰 安裝

1. 複製儲存庫。

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 建立並啟用 Python 環境（建議）。

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. 安裝執行時相依套件。

   因本儲存庫目前沒有根層級相依清單，請直接安裝既有需求套件：

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. 設定憑證。

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 使用

### 啟動 Web 應用

```bash
python app.py
```

在瀏覽器中開啟 `http://localhost:7788`。

### 典型使用流程

1. 開啟 `http://localhost:7788/word/etymology`。
2. 輸入待查詢詞條。
3. 等待分析完成（首次執行可能因外部 API 延遲而較久）。
4. 瀏覽生成的圖與相關元資料。
5. 使用上一頁/下一頁導覽瀏覽快取中的詞條。

### <a id="api-endpoints"></a>API 端點

| 方法 | 端點 | 說明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 渲染指定詞條的詞源頁面 |
| `GET` | `/word/next-word?word={word}` | 在快取中跳到下一個詞條 |
| `GET` | `/word/prev-word?word={word}` | 在快取中跳到上一個詞條 |
| `GET/POST` | `/get_word_etymology/{word}` | 回傳包含 base64 PNG 的 JSON 負載 |

### API 呼叫範例

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ 設定

- `OPENAI_API_KEY`（必填）：分析請求所需憑證。
- `OPENAI_MODEL`（選填）：覆寫分析器使用的模型。
- 服務執行使用的目錄：
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 範例

```bash
python app.py
```

接著開啟：

```text
http://localhost:7788/word/revolution
```

首次分析會產生：

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## <a id="components"></a>元件

### WordEtymologyAnalyzer

位於 `word_etymology_analyzer.py` 的此元件：

- 規範化輸入詞條。
- 呼叫 OpenAI 取得結構化詞源回應。
- 使用 `json5` 擷取/修復 JSON 負載。
- 重試失敗的解析嘗試並記錄失敗以提高韌性。
- 將帶時間戳的快照寫入 `word_etymology_analysis/`。
- 更新 `processed_words.csv` 索引。

### <a id="etymologygraph"></a>EtymologyGraph

位於 `etymology_graph.py` 的此元件：

- 載入結構化詞源 JSON。
- 使用遞迴祖先關係建構 `networkx.DiGraph`。
- 計算具深度感知的圖坐標。
- 渲染帶標籤的節點與邊並處理多語言文字。
- 保存用於快取與展示的 `PNG` 圖片。

### Web 應用

在 `app.py` 中，Tornado 應用：

- 提供根路徑重導向與搜尋頁行為。
- 處理生成與快取查詢流程。
- 在 `/word/...` 與 `/get_word_etymology/...` 下暴露頁面與 API 路由。
- 為 API 使用者回傳包含 base64 圖片資料的 JSON 負載。

## 📦 依賴套件

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 開發說明

- JSON 與圖片快取可避免不必要的重複 API 呼叫。
- 為相容與歷史追溯保留了 `index.html` 與 `index.html.old`。
- 歷史目錄和產物目前是有意保留的（如 `statics/`、notebooks、archives）。
- 發現 `.gitignore` 中有未清理的合併衝突標記，屬於 README 範圍外的倉庫整潔問題。

## 🧯 故障排除

| 問題 | 解決方式 |
|---|---|
| 啟動時拋出 `ModuleNotFoundError` | 使用 `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` 安裝缺漏的套件 |
| `OPENAI_API_KEY` 驗證錯誤 | 確保在執行 `python app.py` 的同一個 shell 工作階段中設定此變數 |
| 生成圖中出現缺字/亂碼 | 確認倉庫中字型檔（`Noto Sans`、阿拉伯語字型變體、`Arial Unicode MS`）存在且可讀取 |
| 某詞條無圖片顯示 | 檢查應用程式日誌中的 JSON 解析失敗或瞬時 API 錯誤 |
| `pip install -r requirements.txt` 失敗或不存在 | 按上述列表直接安裝相依套件（目前倉庫未包含根層級清單） |



## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
