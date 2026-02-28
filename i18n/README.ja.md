[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 OpenAI を活用したキャッシュ効率重視のワークフローで、単語の語源を多言語の系譜グラフとして可視化します。


[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#components)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](#license)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)
[![GitHub last commit](https://img.shields.io/github/last-commit/lachlanchen/WordOrigins?color=blue)](https://github.com/lachlanchen/WordOrigins/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/lachlanchen/WordOrigins?color=red)](https://github.com/lachlanchen/WordOrigins/issues)
[![GitHub repo size](https://img.shields.io/github/repo-size/lachlanchen/WordOrigins?color=yellow)](https://github.com/lachlanchen/WordOrigins)

![Word Origins デモ](word_origins.jpg)

## 📘 概要

WordOrigins は、単語の語源を分析し、言語的系譜を有向グラフとして可視化する Python 製 Web ユーティリティです。次の要素を組み合わせています。

- Tornado Web アプリケーション。
- OpenAI を用いた語源分析。
- フォールトトレラントな復元処理を伴う構造化 JSON 解析。
- NetworkX + Matplotlib によるグラフ生成。
- 高速な再解析のためのキャッシュ済み出力。

ブラウザ UI と API エンドポイントの両方を提供し、語源アーティファクトの生成と取得を行えます。

## 📸 クイックスナップショット

| 項目 | 詳細 |
|---|---|
| 🌐 アクセス | 対話型探索用の Web UI と、Base64 PNG を返す API |
| 🧠 インテリジェンス | 構造化 JSON 解析付きの OpenAI ベース語源分析 |
| 🧰 再現性 | 各単語処理時に JSON + PNG のキャッシュ成果物を作成 |
| 🌍 言語サポート | CJK とアラビア語向けのバンドルフォントによる多言語レンダリング |

## 機能

| 機能 | 詳細 |
|---|---|
| 🔎 Web UI | 生成された語源グラフを検索・閲覧 |
| 🧠 OpenAI 駆動の解析 | OpenAI API を用いて構造化された語源情報を生成 |
| 💾 キャッシュ | タイムスタンプ付き JSON スナップショットを保存 |
| 🖼️ 成果物生成 | 処理済み単語の JSON と PNG 成果物をエクスポート |
| 🌍 多言語レンダリング | リポジトリ内に同梱されたフォントで CJK + アラビア語を対応 |
| ↔️ ナビゲーション | 生成済み単語画像の前後移動 |
| 🔌 API サポート | GET/POST レスポンスとして Base64 PNG を JSON ペイロードで返却 |

## 🛠️ しくみ

1. ユーザーは `/word/{word}` または Web 検索フォームから単語を送信します。
2. アナライザーは OpenAI を呼び出し、応答構造を検証します。
3. 解析結果を正規化し、キャッシュ再利用のために保存します。
4. 語源関係をグラフのノード/エッジに変換します。
5. NetworkX と Matplotlib で有向グラフを PNG として描画します。
6. UI と API がキャッシュ画像のパスと関連メタデータを公開します。

## 🗂️ プロジェクト構成

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

## 必要条件

- Python 3.8+
- OpenAI API の認証情報:
  - `OPENAI_API_KEY` (必須)
  - `OPENAI_MODEL` (任意、既定値は現在のガイダンスで `gpt-4-0125-preview`)
- 多言語表示を行う場合は、リポジトリに同梱されたフォントファイル

## 🧰 インストール

1. リポジトリをクローンします。

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Python 仮想環境を作成して有効化します（推奨）。

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. 実行時ライブラリをインストールします。

   このリポジトリにはルートの依存マニフェストがないため、既知の実行要件を直接インストールします。

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. 認証情報を設定します。

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 使い方

### Web アプリの起動

```bash
python app.py
```

ブラウザで `http://localhost:7788` を開きます。

### 一般的な利用フロー

1. `http://localhost:7788/word/etymology` を開きます。
2. 単語を入力します。
3. 解析結果を待ちます（初回は外部 API の応答時間で時間がかかる場合があります）。
4. 生成されたグラフとメタデータを確認します。
5. 前後移動でキャッシュ済み単語を順番に閲覧します。

### API エンドポイント

| メソッド | エンドポイント | 説明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 指定された語源ページを描画 |
| `GET` | `/word/next-word?word={word}` | キャッシュ内の次の単語へ移動 |
| `GET` | `/word/prev-word?word={word}` | キャッシュ内の前の単語へ移動 |
| `GET/POST` | `/get_word_etymology/{word}` | Base64 PNG ペイロードを含む JSON を返却 |

### API 呼び出し例

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ 設定

- `OPENAI_API_KEY` (必須): 解析リクエストの認証情報。
- `OPENAI_MODEL` (任意): アナライザーのモデル上書き。
- サービスが使用するランタイムディレクトリ:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 使用例

```bash
python app.py
```

次に開きます。

```text
http://localhost:7788/word/revolution
```

初回解析で作成されるアーティファクト:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## コンポーネント

### WordEtymologyAnalyzer

`word_etymology_analyzer.py` 内のこのコンポーネントは次の処理を行います。

- 入力単語を正規化します。
- OpenAI を呼び出して構造化された語源応答を取得します。
- `json5` で JSON ペイロードを抽出・修復します。
- 失敗時のパースをリトライし、回復性を高めるため失敗内容を記録します。
- `word_etymology_analysis/` にタイムスタンプ付きスナップショットを保存します。
- `processed_words.csv` のインデックスを更新します。

### EtymologyGraph

`etymology_graph.py` 内のこのコンポーネントは次の処理を行います。

- 構造化済みの語源 JSON を読み込みます。
- 再帰的な祖先関係で `networkx.DiGraph` を構築します。
- 深さを考慮したグラフ座標を計算します。
- 多言語テキスト処理付きでラベル付きノード・エッジを描画します。
- キャッシュと表示用に `PNG` 画像を保存します。

### Web アプリケーション

`app.py` の Tornado アプリは:

- ルートのリダイレクトと検索ページの振る舞いを提供します。
- 生成処理とキャッシュ参照のワークフローを処理します。
- `/word/...` と `/get_word_etymology/...` 配下でページおよび API ルートを公開します。
- API 利用者向けに Base64 画像データを含む JSON ペイロードを返します。

## 📦 依存関係

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 開発ノート

- JSON と画像のキャッシュにより、不要な API 呼び出しを削減できます。
- `index.html` と `index.html.old` は互換性と履歴保持のために残されています。
- `statics/`、ノートブック、アーカイブは現時点で意図的に残存するレガシーディレクトリと成果物です。
- マージ競合マーカーを含む `.gitignore` は本 README の範囲外で、上流の衛生面の問題として確認されています。

## 🧯 トラブルシューティング

| 問題 | 解決策 |
|---|---|
| 起動時の `ModuleNotFoundError` | `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` で不足パッケージをインストール |
| `OPENAI_API_KEY` 認証エラー | `python app.py` を実行している同じシェルセッションで変数をエクスポート |
| 生成グラフの文字化け/欠け | 同梱フォント（`Noto Sans`、アラビア文字フォント、`Arial Unicode MS`）が存在し、読み取り可能か確認 |
| 単語に対して画像が表示されない | JSON パース失敗や一時的な API エラーについてアプリログを確認 |
| `pip install -r requirements.txt` の失敗・存在しない | 上記の通りに依存関係を直接インストール（現行リポジトリにはルートマニフェストがありません） |

## 🗺️ ロードマップ

- サポート対象言語の拡張。
- お気に入り語源の保存のためのユーザーアカウント追加。
- ズーム・パン操作を伴うグラフ移動の改善。
- 各グラフノードの言語メタデータの充実。
- 依存マニフェストと再現可能な環境構築手順を整備。
- アナライザーのパース、キャッシュ振る舞い、ルートハンドラーのテスト追加。

## 🤝 貢献

1. リポジトリをフォークします。
2. フィーチャーブランチを作成します。
3. 小さくレビューしやすい変更を行います。
4. `python app.py` を実行し、主要ルートを確認して検証します。
5. 再現可能な手順とスクリーンショット/API 例を添えて PR を開きます。

## 🙌 謝辞

- 言語モデルベースの解析能力を提供する OpenAI。
- 多言語レンダリングを支える Google Noto フォントファミリーの貢献者。

## ライセンス

Apache License 2.0  
詳細は[LICENSE](LICENSE)の全文を参照してください。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
