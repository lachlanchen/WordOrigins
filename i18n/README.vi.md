[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Trực quan hóa nguồn gốc từ vựng như một đồ thị phả hệ ngôn ngữ bằng quy trình hướng cache, có hỗ trợ bởi OpenAI.

**Tùy chọn ngôn ngữ:** English (this file)

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

## 📘 Tổng quan

WordOrigins là một tiện ích web Python để phân tích nguồn gốc từ và trực quan hóa dòng dõi ngôn ngữ dưới dạng đồ thị có hướng. Công cụ này kết hợp:

- Ứng dụng web Tornado.
- Phân tích ngữ nguyên bởi OpenAI.
- Phân tích cú pháp JSON có cấu trúc với cơ chế dự phòng linh hoạt.
- Tạo đồ thị qua NetworkX + Matplotlib.
- Lưu kết quả vào cache để phân tích lặp lại nhanh hơn.

Nó cung cấp cả giao diện trình duyệt và các endpoint API để tạo ra và truy xuất tài nguyên về nguồn gốc từ.

## 📸 Ảnh nhanh

| Khu vực | Chi tiết |
|---|---|
| 🌐 Truy cập | Giao diện Web cho phép khám phá tương tác và API trả về ảnh PNG base64 |
| 🧠 Trí tuệ | Phân tích ngữ nguyên bằng OpenAI với phân tích JSON có cấu trúc |
| 🧰 Tính tái lập | JSON + PNG được cache cho mỗi từ đã xử lý |
| 🌍 Hỗ trợ ngôn ngữ | Hiển thị đa ngôn ngữ cho CJK và tiếng Ả Rập với font được đóng gói |

## Tính năng

| Tính năng | Chi tiết |
|---|---|
| 🔎 Giao diện Web | Tìm kiếm và duyệt đồ thị nguồn gốc đã tạo |
| 🧠 Phân tích dựa trên OpenAI | Sử dụng API OpenAI để tạo đầu ra nguồn gốc có cấu trúc |
| 💾 Bộ nhớ đệm | Lưu phản hồi cùng snapshot JSON có timestamp |
| 🖼️ Sinh artefact | Xuất artefact JSON và PNG cho các từ đã xử lý |
| 🌍 Kết xuất đa ngôn ngữ | Hỗ trợ CJK + Arabic bằng font đóng gói trong repo |
| ↔️ Điều hướng | Duyệt từ trước/sau thông qua hình ảnh từ đã tạo |
| 🔌 Hỗ trợ API | Endpoint trả về ảnh PNG dưới dạng payload JSON mã hóa base64 |

## 🛠️ Cách hoạt động

1. Người dùng gửi một từ thông qua `/word/{word}` hoặc form tìm kiếm trên web.
2. Bộ phân tích gọi OpenAI và xác thực cấu trúc phản hồi.
3. Dữ liệu đã phân tích được chuẩn hóa và lưu lại để tái sử dụng cache.
4. Quan hệ ngữ nguyên được chuyển thành các nút và cạnh của đồ thị.
5. NetworkX và Matplotlib render đồ thị có hướng thành PNG.
6. Giao diện UI và API hiển thị đường dẫn ảnh cache cùng metadata liên quan.

## 🗂️ Cấu trúc dự án

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

## Yêu cầu môi trường

- Python 3.8+
- Thông tin đăng nhập API OpenAI:
  - `OPENAI_API_KEY` (bắt buộc)
  - `OPENAI_MODEL` (không bắt buộc, mặc định `gpt-4-0125-preview` theo hướng dẫn hiện tại)
- Font cần thiết đi kèm repository nếu bạn cần hiển thị đa ngôn ngữ

## 🧰 Cài đặt

1. Clone repository.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Tạo và kích hoạt môi trường Python (khuyến nghị).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Cài đặt các thư viện runtime.

   Vì repository này chưa có manifest phụ thuộc gốc, hãy cài trực tiếp các gói runtime đã biết:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Cấu hình thông tin đăng nhập.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 Sử dụng

### Chạy ứng dụng Web

```bash
python app.py
```

Mở `http://localhost:7788` trong trình duyệt của bạn.

### Luồng sử dụng điển hình

1. Mở `http://localhost:7788/word/etymology`.
2. Nhập một từ.
3. Đợi quá trình phân tích (lần chạy đầu tiên có thể lâu hơn do độ trễ của API bên ngoài).
4. Khám phá đồ thị và metadata đã được tạo.
5. Dùng điều hướng trước/sau để duyệt các từ đã cache.

### Endpoints API

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Render một trang cho ngữ nguyên của từ đã yêu cầu |
| `GET` | `/word/next-word?word={word}` | Điều hướng sang từ tiếp theo trong cache |
| `GET` | `/word/prev-word?word={word}` | Điều hướng sang từ trước đó trong cache |
| `GET/POST` | `/get_word_etymology/{word}` | Trả về body JSON kèm payload PNG mã hóa base64 |

### Ví dụ gọi API

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Cấu hình

- `OPENAI_API_KEY` (bắt buộc): thông tin xác thực cho các request phân tích.
- `OPENAI_MODEL` (không bắt buộc): override mô hình cho bộ phân tích.
- Các thư mục runtime được ứng dụng sử dụng:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Ví dụ

```bash
python app.py
```

Sau đó mở:

```text
http://localhost:7788/word/revolution
```

Các artefact được tạo cho lần phân tích đầu tiên:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Thành phần

### WordEtymologyAnalyzer

Nằm trong `word_etymology_analyzer.py`, thành phần này:

- Chuẩn hóa từ đầu vào.
- Gọi OpenAI để lấy phản hồi ngữ nguyên theo cấu trúc.
- Trích xuất/sửa chữa payload JSON với `json5`.
- Thử lại khi parse thất bại và ghi nhận lỗi để tăng độ bền.
- Ghi snapshot có timestamp vào `word_etymology_analysis/`.
- Cập nhật chỉ mục `processed_words.csv`.

### EtymologyGraph

Nằm trong `etymology_graph.py`, thành phần này:

- Nạp JSON nguồn gốc đã cấu trúc.
- Xây `networkx.DiGraph` với quan hệ tổ tiên đệ quy.
- Tính toán tọa độ đồ thị theo độ sâu.
- Render các nút và cạnh có nhãn với xử lý văn bản đa ngôn ngữ.
- Lưu ảnh `PNG` cho caching và trình bày.

### Ứng dụng Web

Trong `app.py`, ứng dụng Tornado:

- Phục vụ redirect trang gốc và hành vi trang tìm kiếm.
- Xử lý quy trình sinh và tra cứu cache.
- Công khai route cho trang và API tại `/word/...` và `/get_word_etymology/...`.
- Trả về payload JSON chứa dữ liệu ảnh base64 cho người dùng API.

## 📦 Dependencies

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Ghi chú phát triển

- Bộ nhớ đệm JSON và hình ảnh giúp tránh gọi API lặp lại không cần thiết.
- `index.html` và `index.html.old` được giữ lại vì tính tương thích và lịch sử.
- Các thư mục và artefact kế thừa hiện được giữ cố ý (`statics/`, notebooks, archives).
- Tệp `.gitignore` có dấu hiệu còn marker xung đột hợp nhất và nằm ngoài phạm vi sửa README.

## 🧯 Xử lý sự cố

| Vấn đề | Cách khắc phục |
|---|---|
| `ModuleNotFoundError` khi khởi chạy | Cài thiếu package với `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Lỗi xác thực `OPENAI_API_KEY` | Đảm bảo biến đã được export trong cùng phiên terminal đang chạy `python app.py` |
| Thiếu/méo lỗi chữ trong đồ thị sinh ra | Kiểm tra font đi kèm (`Noto Sans`, biến thể Arabic, Arial Unicode MS) có tồn tại và có quyền đọc |
| Không có ảnh hiển thị cho một từ | Kiểm tra log ứng dụng để phát hiện lỗi parse JSON hoặc lỗi API tạm thời |
| `pip install -r requirements.txt` thất bại/không tồn tại | Cài dependency trực tiếp như trên (repo hiện tại không có manifest gốc) |

## 🗺️ Roadmap

- Bổ sung thêm hỗ trợ ngôn ngữ.
- Thêm tài khoản người dùng cho việc lưu các ngữ nguyên yêu thích.
- Cải thiện điều hướng đồ thị với tương tác zoom/pan.
- Bổ sung metadata ngôn ngữ phong phú hơn trong mỗi node đồ thị.
- Thêm file manifest phụ thuộc được quản lý và thiết lập môi trường tái lập.
- Bổ sung tests cho parser analyzer, hành vi cache và route handlers.

## 🤝 Đóng góp

1. Fork repository.
2. Tạo branch tính năng.
3. Thực hiện thay đổi nhỏ gọn, dễ review.
4. Kiểm tra bằng cách chạy `python app.py` và xác thực các route quan trọng.
5. Tạo PR kèm hướng dẫn tái lập, ảnh chụp màn hình/API examples.

## 🙌 Lời cảm ơn

- OpenAI vì khả năng phân tích dựa trên language model.
- Những đóng góp của cộng đồng font chữ Google Noto cho hỗ trợ hiển thị đa ngôn ngữ.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License

Apache License 2.0  
Xem [LICENSE](LICENSE) để biết đầy đủ điều khoản.
