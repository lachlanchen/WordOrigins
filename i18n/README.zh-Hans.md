[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

一个用于分析词源并将其可视化为交互式图谱的工具。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#先决条件)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#概览)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-端点)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#功能)

![Word Origins Demo](word_origins.jpg)

## 快速速览

| 区域 | 说明 |
|---|---|
| 🌐 访问方式 | 提供网页界面用于交互式浏览，同时提供可输出 base64 PNG 的 API |
| 🧠 智能化 | OpenAI 驱动的词源分析，并进行结构化 JSON 解析 |
| 🧰 可复现性 | 为每个已处理单词缓存 JSON 与 PNG 产物 |
| 🌍 语言支持 | 针对中日韩与阿拉伯语提供内置字体的多语言渲染 |

## 概览

WordOrigins 是一个 Python 网页应用，可让你探索单词的词源（起源与历史演变）。它会详细分析单词随时间变化的过程，将其拆解为词素，递归追溯每个词素的语言渊源，并将结果渲染为浏览器可查看的图像。

### ✨ 核心特性

- 对任意单词进行详细的词源分析
- 通过图形展示单词来源关系
- 支持包括英语、法语、阿拉伯语、日语和中文在内的多语言
- 提供可交互的网页界面用于探索

## 功能

| 功能 | 说明 |
|---|---|
| 🔎 Web UI | 搜索并浏览已生成的词源图谱 |
| 🧠 OpenAI 辅助分析 | 使用 OpenAI API 生成结构化词源输出 |
| 💾 缓存 | 将 OpenAI 响应缓存为带时间戳的 JSON 快照 |
| 🖼️ 产物生成 | 为已分析单词缓存 JSON 与 PNG 产物 |
| 🌍 多语言渲染 | 仓库内置 CJK + 阿拉伯文字体支持 |
| ↔️ 导航 | 可在已生成的单词图片中向前/向后浏览 |
| 🔌 API 支持 | 端点返回 base64 PNG 输出 |

## 工作原理

1. 输入你想分析的单词。
2. 系统连接 OpenAI API，执行深度词源分析。
3. 分析器对模型输出进行验证/解析，转为结构化 JSON。
4. 结果会被缓存并转换为有向图。
5. 图谱渲染为 PNG 后显示在网页界面。
6. 你可以浏览历史上已分析过的单词。

## 项目结构

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

## 先决条件

- Python 3.8+
- OpenAI API 密钥
- 所需字体（仓库中已包含）：
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## 安装

### 设置

1. 克隆仓库：
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 将 OpenAI API Key 设置为环境变量：
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 依赖说明

运行时会导入以下包：
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

假设：`requirements.txt` 应包含上述包。如果本地副本缺少 `requirements.txt`，请手动安装这些依赖。

## 使用方法

### 运行网页应用

启动 Tornado 服务器：

```bash
python app.py
```

然后在浏览器中打开 `http://localhost:7788`。

### 典型使用流程

1. 打开 `http://localhost:7788`。
2. 在搜索框输入单词。
3. 应用会分析并渲染该词源图。
4. 使用上一个/下一个控件浏览生成过的单词。

### API 端点

| 方法 | 端点 | 说明 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 生成并展示单词的词源图 |
| `GET` | `/word/next-word` | 跳转到列表中的下一个单词 |
| `GET` | `/word/prev-word` | 跳转到列表中的上一个单词 |
| `GET/POST` | `/get_word_etymology/{word}` | 获取词源数据，返回 base64 PNG 载荷 |

### API 调用示例

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 配置

### 环境变量

- `OPENAI_API_KEY`（必填）：OpenAI Python 客户端使用的 API key
- `OPENAI_MODEL`（可选）：分析器使用的模型名称（默认 `gpt-4-0125-preview`）

### 运行时目录（由应用创建或使用）

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 组件

### WordEtymologyAnalyzer

连接 OpenAI API 获取指定单词的详细词源信息，包含缓存与重试逻辑：

- 将输入单词标准化为小写
- 使用 `json5` 进行更稳健的 JSON 输出解析
- 将带时间戳的分析快照保存到 `word_etymology_analysis/`
- 在 `processed_words.csv` 中记录已处理的单词

### EtymologyGraph

使用 NetworkX 与 Matplotlib 根据词源数据创建可视化结果：

- 递归映射嵌套词源到有向图节点和边
- 计算基于深度的径向布局位置
- 绘制词素/含义/示例与语言边标签
- 使用内置字体处理多语言文本渲染

### Web Application

基于 Tornado 的网页服务器，处理请求并提供用户界面：

- 将 `/` 重定向到 `/word/etymology`
- 从 `static/images/` 读取并展示单词图谱
- 按需生成缺失的分析与图片

## 示例

### 分析新词

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

首次运行后的预期输出：

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 浏览已生成的历史单词

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 技术细节

- 应用会为已分析的单词存储 JSON 文件用于缓存。
- 图片以 PNG 文件形式生成。
- 已实现特殊字体处理以支持多语言。
- 图谱布局按节点深度和关系计算。
- 仓库中包含开发阶段使用的探索性 notebook 与归档产物。

## 开发说明

- 主要运行入口是 `app.py`。
- Notebook 文件（`etymology*.ipynb`）为实验用途，可能与生产服务流程不同。
- 仓库保留了历史遗留路径（`statics/` 与 `static/`，`.old` 文件）以便追溯。
- 当前 `.gitignore` 似乎包含未解决的合并冲突标记；发布前应先清理。

## 故障排查

| 问题 | 解决方案 |
|---|---|
| 启动时出现 `ModuleNotFoundError` | 安装缺失依赖：`pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 错误或认证失败 | 确保在运行 `python app.py` 的同一 shell 会话中导出了 `OPENAI_API_KEY` |
| 图形文本显示为方块或缺字 | 确认仓库内字体文件在预期路径下存在 |
| 某个单词没有生成图片 | 检查服务器日志中的 JSON 解析重试/异常，并确认网络/API 可用 |
| `pip install -r requirements.txt` 因文件缺失而失败 | 根据本 README 的清单创建本地依赖文件，或直接安装相关包 |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 路线图

- 增加更多语言支持。
- 实现用户账号，用于收藏喜爱的词源。
- 改进图谱可视化，加入缩放与平移。
- 补充更深入的语言学信息。
- 增加可维护的依赖清单与可复现环境配置。
- 为分析器解析、缓存行为与路由处理器补充测试。

## 贡献

欢迎贡献。建议流程：

1. Fork 仓库。
2. 创建 feature 分支。
3. 做聚焦且便于 review 的改动。
4. 通过运行 `python app.py` 并检查关键路由进行验证。
5. 提交 Pull Request，写清变更说明，并在相关时附上截图/API 示例。

## 依赖项

- tornado：网页服务器框架
- openai：OpenAI API 客户端
- matplotlib：用于生成图形
- networkx：用于图结构处理
- PIL/Pillow：图像处理
- numpy：数值计算
- cjkwrap：处理 CJK 文本换行
- json5：增强 JSON 解析稳定性

## 致谢

- OpenAI，提供语言分析能力
- Google Noto 字体，提供多语种文本支持

## 许可证

Apache License 2.0

详见 [LICENSE](LICENSE) 了解完整条款。
