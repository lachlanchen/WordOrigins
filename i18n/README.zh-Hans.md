[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

一个用于分析词源并将其可视化为交互式图谱的工具。

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#先决条件)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#概览)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-端点)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#功能)

![Word Origins Demo](word_origins.jpg)

## 概览

WordOrigins 是一个 Python Web 应用，可用于探索单词的词源（起源与历史演变）。它会对单词随时间的演化过程进行详细分析，将其拆解为组成部分，递归追踪每个部分的语言谱系，并把结果渲染为图像，在浏览器中展示。

### ✨ 核心特性

- 对任意单词进行详细词源分析
- 以图谱形式可视化展示词源关系
- 支持多语言，包括英语、法语、阿拉伯语、日语和中文
- 提供可交互的 Web 界面用于探索

## 功能

| 功能 | 说明 |
|---|---|
| 🔎 Web UI | 搜索并浏览已生成的词源图谱 |
| 🧠 OpenAI 支持的分析 | 使用 OpenAI API 生成结构化词源输出 |
| 💾 缓存 | 以带时间戳的 JSON 快照缓存 OpenAI 响应 |
| 🖼️ 产物生成 | 为已分析单词缓存 JSON 与 PNG 产物 |
| 🌍 多语言渲染 | 仓库内置 CJK + 阿拉伯语字体支持 |
| ↔️ 导航 | 在已生成的单词图片间进行上一项/下一项浏览 |
| 🔌 API 支持 | 端点以 base64 返回 PNG 输出 |

## 工作原理

1. 输入你要分析的单词。
2. 系统连接 OpenAI 的 API 执行深度词源分析。
3. 分析器将模型输出校验/解析为结构化 JSON。
4. 结果会被缓存并转换为有向图。
5. 图谱被渲染为 PNG 并显示在 Web 界面中。
6. 你可以浏览之前已分析的单词。

## 项目结构

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Tornado Web 服务器入口
├─ word_etymology_analyzer.py          # 基于 OpenAI 的词源分析 + 缓存
├─ etymology_graph.py                  # NetworkX + Matplotlib 图谱生成
├─ utils.py                            # 图像/纹理辅助工具
├─ templates/
│  ├─ index.html                       # 主界面
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # 主要渲染 PNG 输出
├─ statics/
│  └─ images/                          # 历史遗留的重复图片目录
├─ jsons/                              # 按单词存储的 JSON 与图像产物
├─ word_etymology_analysis/            # 带时间戳的模型响应缓存
├─ processed_words.csv                 # 已处理单词日志
├─ i18n/                               # 用于多语言 README/文档文件
├─ archived_code/                      # 历史 notebook/代码
├─ archived_data/                      # 历史 JSON 输出
├─ etymology*.ipynb                    # Notebook 实验
├─ Noto Sans CJK Regular/              # 内置 CJK 字体
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # 内置阿拉伯语 + Noto 字体族
└─ arial-unicode-ms.ttf                # 支持 Unicode 的字体
```

## 先决条件

- Python 3.8+
- OpenAI API key
- 必需字体（仓库已包含）：
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

3. 将 OpenAI API key 设置为环境变量：
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 依赖说明

代码在运行时会导入以下包：
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

假设：`requirements.txt` 应包含上述包。如果你的本地副本缺少 `requirements.txt`，请手动安装这些依赖。

## 用法

### 运行 Web 应用

启动 Tornado Web 服务器：

```bash
python app.py
```

然后在浏览器中访问 `http://localhost:7788`。

### 典型用户流程

1. 打开 `http://localhost:7788`。
2. 在搜索框中输入单词。
3. 应用会分析并渲染词源图谱。
4. 使用上一项/下一项控件浏览已生成的单词。

### API 端点

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 生成并显示某个单词的词源图谱 |
| `GET` | `/word/next-word` | 导航到列表中的下一个单词 |
| `GET` | `/word/prev-word` | 导航到列表中的上一个单词 |
| `GET/POST` | `/get_word_etymology/{word}` | 以 base64 PNG 载荷返回词源数据的 API 端点 |

### API 调用示例

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 配置

### 环境变量

- `OPENAI_API_KEY`（必需）：OpenAI Python 客户端使用的 API key
- `OPENAI_MODEL`（可选）：分析器使用的模型名称（默认为 `gpt-4-0125-preview`）

### 应用创建/使用的运行时目录

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 组件

### WordEtymologyAnalyzer

连接 OpenAI 的 API，获取给定单词的详细词源信息。包含缓存与重试逻辑：

- 将输入单词转为小写
- 稳健解析 JSON 输出（`json5`）
- 将带时间戳的分析快照保存到 `word_etymology_analysis/`
- 将已处理单词记录到 `processed_words.csv`

### EtymologyGraph

使用 NetworkX 和 Matplotlib 创建词源数据的可视化表示：

- 递归地将嵌套词源映射为有向图节点/边
- 计算基于深度的径向布局
- 绘制词素/含义/示例与语言边标签
- 使用内置字体处理多语言文本渲染

### Web Application

基于 Tornado 的 Web 服务器，负责处理请求并提供用户界面：

- 将 `/` 重定向到 `/word/etymology`
- 从 `static/images/` 渲染词图
- 按需生成缺失的分析结果/图像

## 示例

### 分析一个新单词

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

首次运行后的预期输出：

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 浏览已有生成单词

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 技术细节

- 应用会将已分析单词的 JSON 文件存储用于缓存。
- 图像以 PNG 文件生成。
- 已实现针对多语言支持的特殊字体处理。
- 图布局基于节点深度和关系进行计算。
- 仓库中包含开发期间使用的探索性 notebook 与归档产物。

## 开发说明

- 主要运行入口是 `app.py`。
- Notebook 文件（`etymology*.ipynb`）属于实验性质，可能与生产服务器流程有差异。
- 存在历史遗留/重复路径（`statics/` 与 `static/`、`.old` 文件），保留用于历史上下文。
- 当前 `.gitignore` 似乎包含未清理的合并冲突标记；发布前应先清理。

## 故障排查

| 问题 | 解决方案 |
|---|---|
| 启动时报 `ModuleNotFoundError` | 安装缺失依赖：`pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 错误或认证失败 | 确保在启动 `python app.py` 的同一 shell 会话中已导出 `OPENAI_API_KEY` |
| 图上的文本显示为方块或缺字 | 检查内置字体文件是否存在于预期仓库路径 |
| 某个单词未生成图像 | 检查服务器日志中的 JSON 解析重试/异常，并确认网络/API 可访问 |
| 因缺少文件导致 `pip install -r requirements.txt` 失败 | 根据本 README 的包列表创建本地依赖文件，或直接安装这些包 |

## 路线图

- 增加更多语言支持。
- 实现用户账户以保存收藏词源。
- 改进图谱可视化（缩放和平移）。
- 添加更详细的语言学信息。
- 添加可维护的依赖清单和可复现的环境配置。
- 为分析器解析、缓存行为和路由处理器添加测试。

## 贡献

欢迎贡献。建议工作流：

1. Fork 仓库。
2. 创建功能分支。
3. 提交聚焦且易于评审的改动。
4. 通过运行 `python app.py` 并检查关键路由完成验证。
5. 发起 Pull Request，并在相关情况下提供清晰描述与截图/API 示例。

## 依赖

- tornado: Web server framework
- openai: OpenAI API client
- matplotlib: For generating graphs
- networkx: For graph data structure
- PIL/Pillow: For image processing
- numpy: For numerical operations
- cjkwrap: For handling CJK text wrapping
- json5: For robust JSON parsing

## 许可证

Apache License 2.0

完整条款见 [LICENSE](LICENSE)。

## 致谢

- 感谢 OpenAI 提供语言分析能力
- 感谢 Google Noto 字体提供多语言文本支持
