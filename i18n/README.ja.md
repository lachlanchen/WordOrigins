[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

単語の語源を分析し、インタラクティブなグラフとして可視化するためのツールです。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Overview

WordOrigins は Python 製の Web アプリケーションで、単語の語源（起源と歴史的な変遷）を探索できます。単語が時代を通じてどのように発展したかを詳細に分析し、構成要素へ分解し、各要素の言語的系譜を再帰的にたどり、その結果をブラウザで閲覧できるグラフ画像として描画します。

### ✨ Key Features

- 任意の単語に対する詳細な語源分析
- 単語の起源を視覚化するグラフ表現
- 英語、フランス語、アラビア語、日本語、中国語を含む多言語対応
- 探索しやすいインタラクティブな Web インターフェース

## Features

| Feature | Details |
|---|---|
| 🔎 Web UI | 生成された語源グラフを検索・閲覧 |
| 🧠 OpenAI-backed analysis | OpenAI API を利用して構造化された語源出力を生成 |
| 💾 Caching | OpenAI レスポンスをタイムスタンプ付き JSON スナップショットとしてキャッシュ |
| 🖼️ Artifact generation | 既に分析済みの単語について JSON と PNG の成果物をキャッシュ |
| 🌍 Multilingual rendering | リポジトリ同梱の CJK + アラビア語フォントをサポート |
| ↔️ Navigation | 生成済み単語画像の前後移動に対応 |
| 🔌 API support | エンドポイントが PNG 出力を base64 で返却 |

## How It Works

1. 分析したい単語を入力します。
2. システムが OpenAI API に接続し、深い語源分析を実行します。
3. アナライザーがモデル出力を検証・解析して構造化 JSON に変換します。
4. 結果をキャッシュし、有向グラフへ変換します。
5. グラフを PNG として描画し、Web インターフェースに表示します。
6. 以前に分析した単語を順に閲覧できます。

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
- OpenAI API キー
- 必要フォント（リポジトリに同梱）:
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Setup

1. リポジトリをクローン:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 依存関係をインストール:
   ```bash
   pip install -r requirements.txt
   ```

3. OpenAI API キーを環境変数として設定:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notes on dependencies

コードは実行時に以下のパッケージをインポートします:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

前提: `requirements.txt` には上記パッケージが含まれている必要があります。ローカル環境に `requirements.txt` がない場合は、手動でインストールしてください。

## Usage

### Running the Web Application

Tornado Web サーバーを起動します:

```bash
python app.py
```

その後、ブラウザで `http://localhost:7788` を開いてください。

### Typical user flow

1. `http://localhost:7788` を開きます。
2. 検索ボックスに単語を入力します。
3. アプリが語源グラフを分析・描画します。
4. 前へ/次へ操作で生成済み単語を閲覧します。

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 単語の語源グラフを生成して表示 |
| `GET` | `/word/next-word` | リスト内の次の単語へ移動 |
| `GET` | `/word/prev-word` | リスト内の前の単語へ移動 |
| `GET/POST` | `/get_word_etymology/{word}` | 語源データを base64 PNG ペイロードとして取得する API エンドポイント |

### Example API calls

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuration

### Environment variables

- `OPENAI_API_KEY` (required): OpenAI Python クライアントで使用する API キー
- `OPENAI_MODEL` (optional): アナライザーが使用するモデル名（デフォルトは `gpt-4-0125-preview`）

### Runtime directories created/used by the app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Components

### WordEtymologyAnalyzer

指定した単語に対する詳細な語源情報を取得するために OpenAI API へ接続します。キャッシュとリトライロジックを含みます:

- 入力単語を小文字化
- JSON 出力を堅牢にパース（`json5`）
- タイムスタンプ付き分析スナップショットを `word_etymology_analysis/` に保存
- 処理済み単語を `processed_words.csv` に記録

### EtymologyGraph

NetworkX と Matplotlib を使って語源データの可視化を作成します:

- ネストされた語源情報を再帰的に有向グラフのノード/エッジへマッピング
- 深さベースの放射状レイアウトを計算
- 部分/意味/例および言語エッジラベルを描画
- 同梱フォントで多言語テキスト描画を処理

### Web Application

Tornado ベースの Web サーバーがリクエスト処理と UI 配信を担当します:

- `/` を `/word/etymology` へリダイレクト
- `static/images/` から単語グラフを描画
- 不足している分析結果/画像をオンデマンド生成

## Examples

### Analyze a new word

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

初回実行後に想定される出力:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Browse existing generated words

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technical Details

- アプリケーションはキャッシュのため、分析済み単語の JSON ファイルを保存します。
- 画像は PNG ファイルとして生成されます。
- 多言語サポートのため、特別なフォント処理を実装しています。
- グラフレイアウトはノードの深さと関係性に基づいて計算されます。
- リポジトリには開発時に使用した実験用ノートブックとアーカイブ成果物が含まれます。

## Development Notes

- 主な実行エントリーポイントは `app.py` です。
- ノートブックファイル（`etymology*.ipynb`）は実験用であり、本番サーバーフローと異なる場合があります。
- 歴史的経緯で残しているレガシー/重複パス（`statics/` vs `static/`、`.old` ファイル）があります。
- 現在の `.gitignore` には未解決のマージ競合マーカーが含まれているようです。リリース前に整理してください。

## Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` on startup | 不足している依存関係をインストール: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` error or authentication failure | `python app.py` を起動する同じシェルセッションで `OPENAI_API_KEY` が export 済みか確認 |
| Graph text renders as boxes or missing glyphs | 同梱フォントファイルが想定されるリポジトリパスに存在するか確認 |
| No image generated for a word | サーバーログで JSON パースのリトライ/例外を確認し、ネットワーク/API 接続を確認 |
| `pip install -r requirements.txt` fails because file is missing | この README のパッケージ一覧をもとにローカル依存ファイルを作成するか、各パッケージを直接インストール |

## Roadmap

- さらに多くの言語をサポート。
- お気に入り語源を保存するユーザーアカウントを実装。
- ズームやパンに対応したグラフ可視化を改善。
- より詳細な言語学情報を追加。
- 保守された依存マニフェストと再現可能な環境セットアップを追加。
- アナライザーパーサー、キャッシュ挙動、ルートハンドラー向けテストを追加。

## Contribution

コントリビューションを歓迎します。推奨ワークフロー:

1. リポジトリをフォークします。
2. 機能ブランチを作成します。
3. レビューしやすい、焦点の明確な変更を行います。
4. `python app.py` を実行して主要ルートを確認し、検証します。
5. 明確な説明と、必要に応じてスクリーンショット/API サンプルを添えて Pull Request を作成します。

## Dependencies

- tornado: Web サーバーフレームワーク
- openai: OpenAI API クライアント
- matplotlib: グラフ生成用
- networkx: グラフデータ構造
- PIL/Pillow: 画像処理
- numpy: 数値計算
- cjkwrap: CJK テキスト折り返し処理
- json5: 堅牢な JSON パース

## License

Apache License 2.0

See [LICENSE](LICENSE) for full terms.

## Acknowledgements

- 言語分析機能を提供する OpenAI
- 多言語テキストサポートを提供する Google Noto fonts
