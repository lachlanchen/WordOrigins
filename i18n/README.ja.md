[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

単語の語源（起源と歴史的な変遷）を分析し、インタラクティブなグラフとして可視化するためのツールです。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## クイックサマリー

| 項目 | 詳細 |
|---|---|
| 🌐 アクセス | 対話型探索用の Web UI と、base64 PNG を返す API |
| 🧠 インテリジェンス | 構造化 JSON 解析を使った OpenAI 駆動の語源分析 |
| 🧰 再現性 | 処理した各単語の JSON と PNG 成果物をキャッシュ |
| 🌍 言語サポート | CJK とアラビア語の組み込みフォントによる多言語描画 |

## 概要

WordOrigins は、Python 製の Web アプリケーションで、単語の語源（起源と歴史的な発展）を探索できます。単語が時間とともにどのように変化したかを詳細に分析し、構成要素に分解したうえで各要素の系譜を再帰的にたどり、ブラウザで閲覧できるグラフ画像として描画します。

### ✨ 主要機能

- 任意の単語の詳細な語源分析
- 単語の起源を可視化するグラフ表現
- 英語、フランス語、アラビア語、日本語、中国語を含む多言語対応
- 探索しやすいインタラクティブな Web インターフェース

## 機能

| 機能 | 詳細 |
|---|---|
| 🔎 Web UI | 生成された語源グラフの検索・表示 |
| 🧠 OpenAI を使った解析 | OpenAI API を用いて構造化された語源データを生成 |
| 💾 キャッシュ | OpenAI の応答をタイムスタンプ付き JSON スナップショットとして保存 |
| 🖼️ 成果物の生成 | 過去に分析済みの単語向けに JSON と PNG をキャッシュ |
| 🌍 多言語レンダリング | リポジトリ同梱の CJK + アラビア語フォント対応 |
| ↔️ ナビゲーション | 生成済み単語画像の前後移動 |
| 🔌 API サポート | エンドポイントは PNG 出力を base64 で返却 |

## 動作の流れ

1. 分析したい単語を入力します。
2. システムは OpenAI の API に接続し、深い語源分析を実行します。
3. アナライザーはモデル出力を検証・解析し、構造化 JSON に変換します。
4. 結果をキャッシュし、方向付きグラフへ変換します。
5. グラフを PNG として描画し、Web インターフェースに表示します。
6. 過去に分析済みの単語を順番に閲覧できます。

## プロジェクト構成

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

## 前提条件

- Python 3.8+
- OpenAI API キー
- 必要フォント（リポジトリに同梱）:
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## インストール

### セットアップ

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```

3. OpenAI API キーを環境変数に設定します。
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 依存関係について

このコードは実行時に次のパッケージをインポートします。
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

前提: `requirements.txt` には上記のパッケージが含まれている必要があります。ローカルコピーに `requirements.txt` がない場合は、これらを手動でインストールしてください。

## 使用方法

### Web アプリケーションの起動

Tornado Web サーバーを起動します。

```bash
python app.py
```

その後、ブラウザで `http://localhost:7788` を開きます。

### 一般的な利用フロー

1. `http://localhost:7788` を開きます。
2. 検索ボックスに単語を入力します。
3. アプリが語源グラフを分析・描画します。
4. 前後のコントロールで生成済みの単語を参照できます。

### API エンドポイント

| メソッド | エンドポイント | 説明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 単語の語源グラフを生成して表示 |
| `GET` | `/word/next-word` | リスト内の次の単語へ移動 |
| `GET` | `/word/prev-word` | リスト内の前の単語へ移動 |
| `GET/POST` | `/get_word_etymology/{word}` | 語源データを base64 PNG ペイロードとして取得する API エンドポイント |

### API 呼び出し例

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 設定

### 環境変数

- `OPENAI_API_KEY`（必須）: OpenAI Python クライアントで使用する API キー
- `OPENAI_MODEL`（任意）: アナライザーで使用するモデル名（デフォルトは `gpt-4-0125-preview`）

### アプリケーションの実行時ディレクトリ

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 構成要素

### WordEtymologyAnalyzer

指定した単語に対して詳細な語源情報を取得するため、OpenAI の API に接続します。キャッシュとリトライのロジックが含まれます。

- 入力単語を小文字化・正規化します。
- JSON 出力を堅牢にパースします（`json5`）。
- タイムスタンプ付きの分析スナップショットを `word_etymology_analysis/` に保存します。
- 処理済み単語を `processed_words.csv` に記録します。

### EtymologyGraph

NetworkX と Matplotlib を使って語源データの可視化を生成します。

- ネストした語源情報を再帰的に有向グラフのノード／エッジへマッピングします。
- 深さベースの放射状配置を計算します。
- 部分・意味・例と言語エッジラベルを描画します。
- 同梱フォントで多言語テキスト描画を扱います。

### Web Application

Tornado ベースの Web サーバーとしてリクエスト処理と UI の提供を担当します。

- `/` を `/word/etymology` にリダイレクトします。
- `static/images/` から単語グラフを描画します。
- 不足している分析結果／画像をオンデマンドで生成します。

## 例

### 新しい単語を分析する

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

初回実行後の想定出力:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 既存の生成単語を閲覧する

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 技術的な詳細

- アプリケーションはキャッシュ用に分析済み単語の JSON ファイルを保存します。
- 画像は PNG ファイルとして生成されます。
- 多言語サポートのために特別なフォント処理を実装しています。
- グラフレイアウトはノードの深さと関係性に基づいて計算されます。
- リポジトリには開発時の探索ノートブックとアーカイブ済みアーティファクトが含まれます。

## 開発メモ

- 主要な実行エントリポイントは `app.py` です。
- Notebook ファイル（`etymology*.ipynb`）は実験用であり、プロダクションのサーバー処理と異なる場合があります。
- `statics/` と `static/` のレガシー重複パスや `.old` ファイルは歴史的理由で残されています。
- 現在の `.gitignore` には未解決のマージコンフリクトマーカーが含まれているようです。リリース前に解消してください。

## トラブルシューティング

| 問題 | 解決策 |
|---|---|
| 起動時に `ModuleNotFoundError` が発生する | 不足している依存関係をインストール: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` のエラーや認証失敗 | `python app.py` を起動する同じシェルセッションで `OPENAI_API_KEY` が export されていることを確認 |
| グラフ文字が□で表示される、または文字欠落する | 同梱フォントファイルが想定のリポジトリパスに存在するか確認 |
| 単語で画像が生成されない | サーバーログで JSON パースのリトライ／例外を確認し、ネットワーク/API 接続を確認 |
| `pip install -r requirements.txt` が失敗する（ファイル不存在） | この README のパッケージ一覧からローカルの依存ファイルを作成するか、直接インストールします |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## ロードマップ

- さらに多くの言語をサポートする。
- お気に入りの語源を保存できるユーザーアカウントを実装する。
- ズーム／パン対応のグラフ可視化を改善する。
- より詳細な言語学情報を追加する。
- 依存関係マニフェストを整備し、再現可能な環境構築を追加する。
- アナライザーのパース処理、キャッシュ挙動、ルートハンドラー向けのテストを追加する。

## コントリビューション

コントリビューションは歓迎です。推奨の進め方:

1. リポジトリをフォークします。
2. フィーチャーブランチを作成します。
3. 焦点を絞った、レビューしやすい変更を行います。
4. `python app.py` を実行して主要ルートを確認し、検証します。
5. 明確な説明を添え、必要に応じてスクリーンショットや API サンプルを付けて pull request を作成します。

## 依存関係

- tornado: Web サーバーフレームワーク
- openai: OpenAI API クライアント
- matplotlib: グラフ生成用
- networkx: グラフデータ構造
- PIL/Pillow: 画像処理
- numpy: 数値計算
- cjkwrap: CJK 文の折り返し処理
- json5: ロバストな JSON パース

## 謝辞

- 言語分析機能を提供する OpenAI
- 多言語テキストサポートを提供する Google Noto fonts

## ライセンス

Apache License 2.0

[LICENSE](LICENSE) を参照して全文をご確認ください。
