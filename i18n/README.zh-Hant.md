[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

一個用於分析單字詞源，並將結果視覺化為互動式圖譜的工具。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#先決條件)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#總覽)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-端點)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#功能)

![Word Origins Demo](word_origins.jpg)

## 總覽

WordOrigins 是一個 Python Web 應用程式，可用來探索單字的詞源（起源與歷史演變）。它會詳細分析單字如何隨時間發展，拆解其組成部分，遞迴追蹤每個部分的語言譜系，並將結果渲染為圖像，方便在瀏覽器中查看。

### ✨ 核心特色

- 針對任意單字進行詳細詞源分析
- 以圖譜方式視覺化單字起源
- 支援多種語言，包括英文、法文、阿拉伯文、日文與中文
- 提供可互動探索的 Web 介面

## 功能

| 功能 | 說明 |
|---|---|
| 🔎 Web UI | 搜尋並瀏覽已產生的詞源圖譜 |
| 🧠 OpenAI 驅動分析 | 使用 OpenAI API 產生結構化詞源輸出 |
| 💾 快取 | 將 OpenAI 回應快取為帶時間戳記的 JSON 快照 |
| 🖼️ 產物生成 | 為已分析單字快取 JSON 與 PNG 產物 |
| 🌍 多語言渲染 | 儲存庫內建 CJK + 阿拉伯文字體支援 |
| ↔️ 導覽 | 可在已產生的單字圖片間前後切換 |
| 🔌 API 支援 | 端點可回傳 base64 編碼的 PNG 輸出 |

## 運作方式

1. 輸入你要分析的單字。
2. 系統連線至 OpenAI API 執行深度詞源分析。
3. 分析器會將模型輸出驗證/解析為結構化 JSON。
4. 結果會被快取並轉換為有向圖。
5. 圖譜會被渲染為 PNG，並顯示在 Web 介面中。
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

## 先決條件

- Python 3.8+
- OpenAI API key
- 必要字體（已包含於儲存庫中）：
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## 安裝

### 設定

1. 複製儲存庫：
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 將 OpenAI API key 設為環境變數：
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 相依套件說明

程式碼在執行時會匯入以下套件：
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

假設：`requirements.txt` 應包含上述套件。若你的本機副本缺少 `requirements.txt`，請手動安裝這些套件。

## 使用方式

### 執行 Web 應用程式

啟動 Tornado Web 伺服器：

```bash
python app.py
```

接著開啟瀏覽器並前往 `http://localhost:7788`。

### 典型使用流程

1. 開啟 `http://localhost:7788`。
2. 在搜尋框輸入單字。
3. 應用程式會分析並渲染詞源圖譜。
4. 使用上一個/下一個控制項瀏覽已生成單字。

### API 端點

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 產生並顯示某個單字的詞源圖譜 |
| `GET` | `/word/next-word` | 導覽到列表中的下一個單字 |
| `GET` | `/word/prev-word` | 導覽到列表中的上一個單字 |
| `GET/POST` | `/get_word_etymology/{word}` | 以 base64 PNG 載荷回傳詞源資料的 API 端點 |

### API 呼叫範例

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 設定

### 環境變數

- `OPENAI_API_KEY`（必要）：OpenAI Python client 使用的 API key
- `OPENAI_MODEL`（選填）：分析器使用的模型名稱（預設為 `gpt-4-0125-preview`）

### 應用程式建立/使用的執行期目錄

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 元件

### WordEtymologyAnalyzer

連線至 OpenAI API，為指定單字取得詳細詞源資訊。包含快取與重試邏輯：

- 將輸入單字轉為小寫
- 穩健解析 JSON 輸出（`json5`）
- 將帶時間戳記的分析快照存入 `word_etymology_analysis/`
- 將已處理單字記錄於 `processed_words.csv`

### EtymologyGraph

使用 NetworkX 與 Matplotlib 建立詞源資料的視覺化表示：

- 將巢狀詞源資料遞迴映射為有向圖節點/邊
- 計算基於深度的放射狀位置
- 繪製詞素/含義/例句與語言邊標籤
- 使用內建字體處理多語言文字渲染

### Web Application

基於 Tornado 的 Web 伺服器，負責處理請求並提供使用者介面：

- 將 `/` 重新導向到 `/word/etymology`
- 從 `static/images/` 渲染單字圖譜
- 依需求產生缺失的分析結果/圖片

## 範例

### 分析新單字

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

首次執行後的預期輸出：

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
- 圖片會以 PNG 檔案生成。
- 針對多語言支援實作了特殊字體處理。
- 圖譜版面配置會依節點深度與關係計算。
- 目前儲存庫包含開發期間使用的探索型 notebooks 與封存產物。

## 開發備註

- 主要執行入口為 `app.py`。
- Notebook 檔案（`etymology*.ipynb`）屬於實驗性內容，可能與正式伺服器流程不一致。
- 專案中保留了歷史遺留/重複路徑（`statics/` 與 `static/`、`.old` 檔案）供歷史參考。
- 目前 `.gitignore` 看起來含有尚未解決的 merge conflict 標記；請在正式封裝前清理。

## 疑難排解

| 問題 | 解決方式 |
|---|---|
| 啟動時出現 `ModuleNotFoundError` | 安裝缺少的相依套件：`pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 錯誤或驗證失敗 | 確認你在執行 `python app.py` 的同一個 shell session 中已匯出 `OPENAI_API_KEY` |
| 圖譜文字顯示成方框或缺字 | 確認內建字體檔案存在於儲存庫預期路徑 |
| 某個單字沒有產生圖片 | 檢查伺服器日誌中的 JSON 解析重試/例外，並確認網路/API 可用 |
| `pip install -r requirements.txt` 因缺少檔案而失敗 | 依本 README 的套件清單建立本機相依檔，或直接逐一安裝套件 |

## 路線圖

- 新增更多語言支援。
- 實作使用者帳號以儲存喜愛的詞源。
- 改進圖譜視覺化，加入縮放與平移。
- 補充更詳細的語言學資訊。
- 新增可維護的相依性清單與可重現的環境設定。
- 新增分析器解析、快取行為與路由處理器測試。

## 貢獻

歡迎貢獻。建議流程：

1. Fork 儲存庫。
2. 建立功能分支。
3. 進行聚焦且易於審查的變更。
4. 透過執行 `python app.py` 並檢查關鍵路由完成驗證。
5. 建立 Pull Request，附上清楚說明；若適用可提供截圖/API 範例。

## 相依套件

- tornado：Web 伺服器框架
- openai：OpenAI API client
- matplotlib：用於生成圖譜
- networkx：圖資料結構
- PIL/Pillow：影像處理
- numpy：數值運算
- cjkwrap：處理 CJK 文字換行
- json5：穩健 JSON 解析

## 授權

Apache License 2.0

完整條款請參見 [LICENSE](LICENSE)。

## 致謝

- OpenAI 提供語言分析能力
- Google Noto 字體提供多語系文字支援
