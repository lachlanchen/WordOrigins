[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Language options:** 中文（繁體）（本頁）

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

WordOrigins 是一個用來分析詞源並將結果視覺化為互動式圖形的工具。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#先決條件)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#總覽)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-端點)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#功能)

![Word Origins Demo](word_origins.jpg)

## 快速總覽

| 項目 | 說明 |
|---|---|
| 🌐 存取方式 | 提供可互動探索的 Web UI 與輸出 Base64 PNG 的 API |
| 🧠 智能分析 | 利用 OpenAI 進行詞源分析，並以結構化 JSON 解析 |
| 🧰 可重現性 | 每個已處理單字皆會快取 JSON 與 PNG 輸出 |
| 🌍 語言支援 | 內建 CJK 與阿拉伯文字體的多語言渲染 |

## 總覽

WordOrigins 是一個 Python 網頁應用，讓你探索單字的詞源（起源與歷史演變）。它提供單字隨時間演進的詳細分析，將詞素拆解並遞迴追溯每個組成部分的語言脈絡，最後將結果渲染為可在瀏覽器查看的圖形。

### ✨ 核心特色

- 針對任何單字進行深入詞源分析
- 以圖形方式視覺化單字起源
- 支援包括英文、法文、阿拉伯文、日文與中文在內的多種語言
- 提供可互動的網頁介面供探索使用

## 功能

| 功能 | 說明 |
|---|---|
| 🔎 Web UI | 搜尋並瀏覽已產生的詞源圖形 |
| 🧠 OpenAI 支援分析 | 使用 OpenAI API 產生結構化的詞源輸出 |
| 💾 快取機制 | 將 OpenAI 回應快取為帶時間戳的 JSON 快照 |
| 🖼️ 產物產生 | 快取已分析過單字的 JSON 與 PNG 產物 |
| 🌍 多語言渲染 | 倉庫內建 CJK 與阿拉伯文字體支援 |
| ↔️ 導覽 | 可在已產生的單字圖片間前後瀏覽 |
| 🔌 API 支援 | 端點回傳 Base64 PNG 輸出 |

## 運作方式

1. 輸入你想分析的單字。
2. 系統會連線至 OpenAI API 進行深度詞源分析。
3. 分析器驗證並解析模型輸出為結構化 JSON。
4. 結果會被快取並轉換為有向圖。
5. 圖形會被渲染為 PNG，並在網頁介面中顯示。
6. 你可以瀏覽先前已分析過的單字。

## 專案結構

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

## 先決條件

- Python 3.8+
- OpenAI API 金鑰
- 所需字體（已內建於倉庫）：
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## 安裝

### 設定

1. 下載此倉庫：
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 將 OpenAI API 金鑰設為環境變數：
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 相依套件說明

程式在執行時會匯入以下套件：
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

假設：`requirements.txt` 應包含上述套件。若你本機的副本缺少 `requirements.txt`，可依此清單手動安裝。

## 使用方式

### 執行網頁應用程式

啟動 Tornado Web 伺服器：

```bash
python app.py
```

接著打開瀏覽器並前往 `http://localhost:7788`。

### 典型使用流程

1. 開啟 `http://localhost:7788`。
2. 在搜尋框輸入單字。
3. 應用程式會分析並渲染詞源圖形。
4. 使用上一個/下一個控制項來瀏覽已產生的單字。

### API 端點

| 方法 | 端點 | 說明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 產生並顯示某單字的詞源圖形 |
| `GET` | `/word/next-word` | 導覽到清單中的下一個單字 |
| `GET` | `/word/prev-word` | 導覽到清單中的上一個單字 |
| `GET/POST` | `/get_word_etymology/{word}` | 取得以 Base64 PNG 回傳的詞源資料 API 端點 |

### API 呼叫範例

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 組態設定

### 環境變數

- `OPENAI_API_KEY`（必填）：OpenAI Python client 使用的 API key
- `OPENAI_MODEL`（選填）：分析器使用的模型名稱（預設為 `gpt-4-0125-preview`）

### 執行期目錄（由應用程式建立/使用）

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 元件

### WordEtymologyAnalyzer

連線至 OpenAI API，取得指定單字的詳細詞源資訊，並包含快取與重試邏輯：

- 將輸入單字轉為小寫並正規化
- 嘗試穩健解析 JSON 輸出（`json5`）
- 在 `word_etymology_analysis/` 中保存含時間戳記的分析快照
- 將已處理的單字記錄於 `processed_words.csv`

### EtymologyGraph

使用 NetworkX 與 Matplotlib 產生詞源資料的視覺化結果：

- 將巢狀詞源資料遞迴映射為有向圖節點/邊
- 計算基於深度的放射狀佈局
- 繪製詞素/詞義/範例與語言邊界標籤
- 使用內建字體處理多語言文字渲染

### 網頁應用程式

基於 Tornado 的 Web 伺服器，負責處理請求並提供使用者介面：

- 將 `/` 重新導向至 `/word/etymology`
- 從 `static/images/` 渲染單字圖形
- 依需求即時產生缺漏的分析結果與圖像

## 範例

### 分析新單字

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

首次執行後預期輸出：

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 瀏覽既有已生成單字

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 技術細節

- 應用程式會儲存已分析單字的 JSON 檔案作為快取。
- 圖像會以 PNG 格式產生。
- 已針對多語言支援實作專用字體處理。
- 圖形版面配置依節點深度與關係計算。
- 現有倉庫包含開發期間的探索性 notebook 與封存成果。

## 開發備註

- 主要執行進入點為 `app.py`。
- Notebook 檔案（`etymology*.ipynb`）屬於實驗用途，可能與正式伺服器流程不完全一致。
- 倉庫保留了歷史重複路徑（`statics/` 與 `static/`、`.old` 檔案）以供參考。
- 目前 `.gitignore` 似乎包含未解決的 merge conflict 標記；發佈封裝前請先清理。

## 疑難排解

| 問題 | 解決方法 |
|---|---|
| 啟動時出現 `ModuleNotFoundError` | 安裝缺少的套件：`pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 錯誤或驗證失敗 | 確保在執行 `python app.py` 的同一個 shell session 中已匯出 `OPENAI_API_KEY` |
| 圖像文字顯示成方塊或缺字 | 確認內建字體檔案已放置於倉庫預期路徑 |
| 某個單字未生成圖片 | 檢查伺服器日誌中的 JSON 解析重試與例外，並確認網路/API 存取正常 |
| `pip install -r requirements.txt` 因缺檔而失敗 | 依本 README 的套件清單建立本機依賴檔，或直接安裝這些套件 |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 路線圖

- 支援更多語言。
- 實作使用者帳號以保存偏好的詞源結果。
- 改善圖形互動體驗，新增縮放與平移。
- 補充更完整的語言學資訊。
- 加入可維護的依賴清單與可重現的環境建置流程。
- 新增分析器解析、快取行為與路由處理的測試。

## 貢獻

歡迎提交貢獻。建議流程如下：

1. Fork 本倉庫。
2. 建立功能分支。
3. 做出聚焦且易於審閱的變更。
4. 透過執行 `python app.py` 並檢查關鍵路由來驗證。
5. 提交拉取請求，附上清楚的說明與截圖/API 範例（如有需要）。

## 相依套件

- tornado：Web server 框架
- openai：OpenAI API 用戶端
- matplotlib：用於繪製圖形
- networkx：圖資料結構處理
- PIL/Pillow：影像處理
- numpy：數值運算
- cjkwrap：CJK 文字換行處理
- json5：穩健 JSON 解析

## 致謝

- OpenAI 提供語言分析能力
- Google Noto 字體提供多語系文字支援

## 授權

Apache License 2.0

詳見 [LICENSE](LICENSE) 了解完整條款。
