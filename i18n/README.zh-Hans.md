[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 使用 OpenAI 加持、并支持缓存友好的工作流，将词源分析可视化为多语种的溯源有向图。

**语言选项：** 中文（简体）（本文件）

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#components)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](#license)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## 📘 概览

WordOrigins 是一个用于分析词源并将词汇历史关系可视化为有向图的 Python Web 工具。它集成了：

- 一个 Tornado Web 应用。
- 由 OpenAI 提供能力的词源分析。
- 带有容错回退机制的结构化 JSON 解析。
- 使用 NetworkX + Matplotlib 的图形生成。
- 针对重复分析的缓存输出，显著加快后续处理。

它同时提供浏览器界面与 API 端点，用于生成并检索词源相关产物。

## 📸 快速概览

| 区域 | 说明 |
|---|---|
| 🌐 访问方式 | 提供用于交互探索的 Web UI，以及返回 base64 PNG 的 API |
| 🧠 智能分析 | 使用 OpenAI 进行词源分析，并执行结构化 JSON 解析 |
| 🧰 可复现性 | 为每个已处理词条缓存 JSON 与 PNG 成果 |
| 🌍 语言支持 | 针对 CJK 与阿拉伯语的多语言渲染，仓库内置字体 |

## <a id="features"></a>功能

| 功能 | 说明 |
|---|---|
| 🔎 Web UI | 搜索并浏览已生成的词源图 |
| 🧠 OpenAI 驱动分析 | 使用 OpenAI API 生成结构化词源输出 |
| 💾 缓存 | 保存带时间戳的响应快照 |
| 🖼️ 成果导出 | 导出已处理词条的 JSON 与 PNG 产物 |
| 🌍 多语言渲染 | 仓库内置字体支持 CJK 与阿拉伯语 |
| ↔️ 导航 | 通过上一页/下一页浏览已生成词条的图像 |
| 🔌 API 支持 | 端点返回含 base64 图像的 JSON 载荷 |

## 🛠️ 工作原理

1. 用户通过 `/word/{word}` 或网页搜索表单提交词条。
2. 分析器调用 OpenAI 并校验返回结构。
3. 解析后的数据会被标准化并持久化，以便复用缓存。
4. 词源关系会被转为图节点与边。
5. NetworkX 与 Matplotlib 将有向图渲染为 PNG。
6. 前端与 API 返回缓存图像路径及相关元数据。

## 🗂️ 项目结构

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

## <a id="prerequisites"></a>先决条件

- Python 3.8+
- OpenAI API 凭据：
  - `OPENAI_API_KEY`（必填）
  - `OPENAI_MODEL`（可选，现有说明默认 `gpt-4-0125-preview`）
- 如需多语言渲染，请确保仓库中包含所需字体文件

## 🧰 安装

1. 克隆仓库。

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 创建并激活 Python 环境（建议）。

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. 安装运行时依赖。

   因本仓库尚无根级依赖清单，请直接安装已知运行时依赖：

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. 配置凭据。

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 使用

### 启动 Web 应用

```bash
python app.py
```

在浏览器中打开 `http://localhost:7788`。

### 典型使用流程

1. 打开 `http://localhost:7788/word/etymology`。
2. 输入待查询词条。
3. 等待分析完成（首次运行可能因外部 API 延迟而更久）。
4. 浏览生成的图与元数据。
5. 使用上一页/下一页导航浏览缓存中的词条。

### <a id="api-endpoints"></a>API 端点

| 方法 | 端点 | 说明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 渲染指定词条的词源页面 |
| `GET` | `/word/next-word?word={word}` | 在缓存中跳转到下一个词条 |
| `GET` | `/word/prev-word?word={word}` | 在缓存中跳转到上一个词条 |
| `GET/POST` | `/get_word_etymology/{word}` | 返回包含 base64 PNG 的 JSON 载荷 |

### API 调用示例

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ 配置

- `OPENAI_API_KEY`（必填）：分析请求所需凭据。
- `OPENAI_MODEL`（可选）：覆盖分析器使用的模型。
- 服务运行时使用的目录：
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 示例

```bash
python app.py
```

然后打开：

```text
http://localhost:7788/word/revolution
```

首次分析会生成以下产物：

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## <a id="components"></a>组件

### WordEtymologyAnalyzer

位于 `word_etymology_analyzer.py` 的此组件：

- 规范化输入词条。
- 调用 OpenAI 获取结构化词源响应。
- 使用 `json5` 提取/修复 JSON 负载。
- 重试失败的解析尝试并记录失败以提高弹性。
- 将带时间戳的快照写入 `word_etymology_analysis/`。
- 更新 `processed_words.csv` 索引。

### <a id="etymologygraph"></a>EtymologyGraph

位于 `etymology_graph.py` 的此组件：

- 加载结构化词源 JSON。
- 使用递归祖先关系构建 `networkx.DiGraph`。
- 计算具备深度感知的图坐标。
- 渲染带标签的节点与边，并处理多语言文字。
- 保存用于缓存与展示的 `PNG` 图像。

### Web 应用

在 `app.py` 中，Tornado 应用：

- 提供根路径重定向与搜索页行为。
- 处理生成与缓存查询流程。
- 在 `/word/...` 与 `/get_word_etymology/...` 下暴露页面与 API 路由。
- 为 API 调用者返回包含 base64 图片数据的 JSON 负载。

## 📦 依赖项

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 开发说明

- JSON 与图像缓存可避免不必要的重复 API 调用。
- 为兼容与历史追溯保留了 `index.html` 与 `index.html.old`。
- 历史目录和产物目前是有意保留的（如 `statics/`、notebook、archives）。
- 发现 `.gitignore` 中有未清理的合并冲突标记，属于 README 范围外的仓库整洁问题。

## 🧯 故障排查

| 问题 | 解决方式 |
|---|---|
| 启动时报 `ModuleNotFoundError` | 使用 `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` 安装缺失依赖 |
| `OPENAI_API_KEY` 认证错误 | 确保在执行 `python app.py` 的同一 shell 会话中导出该变量 |
| 生成图中出现缺字/乱码 | 确认仓库内字体文件（`Noto Sans`、阿拉伯语字体变体、`Arial Unicode MS`）存在且可读取 |
| 某个词条无图像显示 | 检查应用日志中的 JSON 解析失败或瞬时 API 异常 |
| `pip install -r requirements.txt` 失败或不存在 | 按上述列表直接安装依赖（当前仓库未包含根级清单） |

## 🗺️ 路线图

- 增加更多语言支持。
- 增加用户账户用于收藏常用词源。
- 改进图形导航，加入缩放与平移交互。
- 丰富每个图节点的语言学元数据。
- 补充可维护的依赖清单并实现可复现的环境配置。
- 为解析器、缓存行为及路由处理补充测试。

## 🤝 贡献

1. Fork 仓库。
2. 创建功能分支。
3. 进行聚焦且易于评审的改动。
4. 运行 `python app.py` 进行验证，并检查关键路由。
5. 提交 PR 时附带可复现步骤和截图/API 示例。

## 🙌 致谢

- 感谢 OpenAI 提供基于语言模型的分析能力。
- 感谢 Google Noto 字体家族贡献者为多语言渲染提供支持。

## <a id="license"></a>授权

Apache License 2.0  
详见 [LICENSE](LICENSE) 获取完整条款。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
