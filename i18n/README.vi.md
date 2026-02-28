[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

Một công cụ để phân tích từ nguyên học và trực quan hóa chúng thành các đồ thị tương tác.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Overview

WordOrigins là một ứng dụng web Python cho phép bạn khám phá từ nguyên (nguồn gốc và quá trình phát triển lịch sử) của các từ. Ứng dụng cung cấp phân tích chi tiết về cách từ ngữ tiến hóa theo thời gian, tách chúng thành các thành phần cấu tạo, đệ quy truy vết dòng dõi ngôn ngữ của từng thành phần, rồi kết xuất kết quả thành ảnh đồ thị để xem trong trình duyệt.

### ✨ Tính năng chính

- Phân tích từ nguyên chi tiết cho bất kỳ từ nào
- Biểu diễn trực quan nguồn gốc từ bằng đồ thị
- Hỗ trợ nhiều ngôn ngữ, gồm tiếng Anh, tiếng Pháp, tiếng Ả Rập, tiếng Nhật và tiếng Trung
- Giao diện web tương tác để khám phá

## Features

| Tính năng | Chi tiết |
|---|---|
| 🔎 Web UI | Tìm kiếm và duyệt các đồ thị từ nguyên đã tạo |
| 🧠 Phân tích dựa trên OpenAI | Sử dụng OpenAI API để tạo đầu ra từ nguyên học có cấu trúc |
| 💾 Bộ nhớ đệm | Lưu phản hồi OpenAI dưới dạng JSON có dấu thời gian |
| 🖼️ Tạo artifact | Lưu đệm các artifact JSON và PNG cho các từ đã phân tích trước đó |
| 🌍 Kết xuất đa ngôn ngữ | Hỗ trợ font CJK + Ả Rập được đóng gói sẵn trong kho |
| ↔️ Điều hướng | Duyệt ảnh từ tiếp theo/trước đó đã tạo |
| 🔌 Hỗ trợ API | Endpoint trả về đầu ra PNG ở dạng base64 |

## Cách hoạt động

1. Nhập từ bạn muốn phân tích.
2. Hệ thống kết nối tới API của OpenAI để thực hiện phân tích từ nguyên chuyên sâu.
3. Bộ phân tích xác thực/phân tích cú pháp đầu ra mô hình thành JSON có cấu trúc.
4. Kết quả được lưu đệm và chuyển thành đồ thị có hướng.
5. Đồ thị được kết xuất thành PNG và hiển thị trên giao diện web.
6. Bạn có thể duyệt các từ đã phân tích trước đó.

## Cấu trúc dự án

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
- OpenAI API key
- Các font cần thiết (đã bao gồm trong repository):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Cài đặt

### Thiết lập

1. Clone repository:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Cài đặt dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Thiết lập OpenAI API key làm biến môi trường:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Ghi chú về dependencies

Mã nguồn import các package sau khi chạy:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Giả định: `requirements.txt` nên bao gồm các package ở trên. Nếu bản sao cục bộ của bạn thiếu `requirements.txt`, hãy cài thủ công các package này.

## Sử dụng

### Chạy ứng dụng web

Khởi động Tornado web server:

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập `http://localhost:7788`.

### Luồng sử dụng điển hình

1. Mở `http://localhost:7788`.
2. Nhập một từ vào ô tìm kiếm.
3. Ứng dụng phân tích và kết xuất đồ thị từ nguyên.
4. Dùng các nút trước/tiếp theo để duyệt các từ đã tạo.

### API Endpoints

| Method | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Tạo và hiển thị đồ thị từ nguyên cho một từ |
| `GET` | `/word/next-word` | Điều hướng sang từ kế tiếp trong danh sách |
| `GET` | `/word/prev-word` | Điều hướng về từ trước đó trong danh sách |
| `GET/POST` | `/get_word_etymology/{word}` | API endpoint để lấy dữ liệu từ nguyên dưới dạng payload PNG base64 |

### Ví dụ gọi API

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Cấu hình

### Biến môi trường

- `OPENAI_API_KEY` (bắt buộc): API key được OpenAI Python client sử dụng
- `OPENAI_MODEL` (tùy chọn): tên model mà bộ phân tích sử dụng (mặc định là `gpt-4-0125-preview`)

### Thư mục runtime được ứng dụng tạo/sử dụng

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Thành phần

### WordEtymologyAnalyzer

Kết nối tới API của OpenAI để lấy thông tin từ nguyên chi tiết cho một từ nhất định. Có sẵn cơ chế caching và retry:

- Chuyển từ đầu vào về chữ thường
- Cố gắng phân tích cú pháp đầu ra JSON một cách bền vững (`json5`)
- Lưu ảnh chụp phân tích có dấu thời gian trong `word_etymology_analysis/`
- Ghi lại các từ đã xử lý trong `processed_words.csv`

### EtymologyGraph

Tạo biểu diễn trực quan dữ liệu từ nguyên bằng NetworkX và Matplotlib:

- Ánh xạ đệ quy từ nguyên lồng nhau thành các node/cạnh của đồ thị có hướng
- Tính toán vị trí theo dạng bán kính dựa trên độ sâu
- Vẽ nhãn thành phần/nghĩa/ví dụ và nhãn cạnh ngôn ngữ
- Xử lý kết xuất văn bản đa ngôn ngữ bằng các font đã đóng gói

### Ứng dụng web

Tornado-based web server xử lý request và phục vụ giao diện người dùng:

- Chuyển hướng `/` sang `/word/etymology`
- Kết xuất đồ thị từ từ `static/images/`
- Tạo phân tích/ảnh còn thiếu theo nhu cầu

## Ví dụ

### Phân tích một từ mới

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Đầu ra dự kiến sau lần chạy đầu tiên:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Duyệt các từ đã tạo sẵn

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Chi tiết kỹ thuật

- Ứng dụng lưu các tệp JSON của từ đã phân tích để làm bộ nhớ đệm.
- Ảnh được tạo dưới dạng tệp PNG.
- Có triển khai xử lý font đặc biệt để hỗ trợ đa ngôn ngữ.
- Bố cục đồ thị được tính toán dựa trên độ sâu và quan hệ giữa các node.
- Repository hiện có các notebook khám phá và artifact lưu trữ dùng trong quá trình phát triển.

## Ghi chú phát triển

- Entrypoint runtime chính là `app.py`.
- Các tệp notebook (`etymology*.ipynb`) mang tính thử nghiệm và có thể khác với luồng server production.
- Có các đường dẫn legacy/trùng lặp (`statics/` so với `static/`, các tệp `.old`) được giữ lại vì lý do lịch sử.
- `.gitignore` hiện tại có vẻ chứa marker xung đột hợp nhất chưa được xử lý; nên dọn dẹp trước khi đóng gói phát hành.

## Khắc phục sự cố

| Vấn đề | Cách xử lý |
|---|---|
| `ModuleNotFoundError` khi khởi động | Cài đặt dependencies còn thiếu: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Lỗi `OPENAI_API_KEY` hoặc thất bại xác thực | Đảm bảo `OPENAI_API_KEY` được export trong cùng phiên shell nơi bạn chạy `python app.py` |
| Văn bản trong đồ thị hiển thị thành ô vuông hoặc thiếu ký tự | Xác minh các tệp font đi kèm tồn tại ở đúng đường dẫn mong đợi trong repository |
| Không tạo được ảnh cho một từ | Kiểm tra log server để tìm lỗi retry/exception khi parse JSON và xác nhận truy cập mạng/API |
| `pip install -r requirements.txt` thất bại vì thiếu tệp | Tạo tệp dependency cục bộ từ danh sách package trong README này hoặc cài trực tiếp các package |

## Lộ trình

- Thêm hỗ trợ cho nhiều ngôn ngữ hơn.
- Triển khai tài khoản người dùng để lưu các từ nguyên yêu thích.
- Cải thiện trực quan hóa đồ thị với zoom và panning.
- Bổ sung thông tin ngôn ngữ học chi tiết hơn.
- Bổ sung dependency manifest được duy trì và thiết lập môi trường có thể tái lập.
- Bổ sung test cho phân tích cú pháp bộ phân tích, hành vi caching và route handlers.

## Đóng góp

Hoan nghênh đóng góp. Quy trình được đề xuất:

1. Fork repository.
2. Tạo feature branch.
3. Thực hiện các thay đổi tập trung, dễ review.
4. Xác thực bằng cách chạy `python app.py` và kiểm tra các route chính.
5. Mở pull request với mô tả rõ ràng, kèm screenshot/mẫu API khi phù hợp.

## Dependencies

- tornado: Web server framework
- openai: OpenAI API client
- matplotlib: For generating graphs
- networkx: For graph data structure
- PIL/Pillow: For image processing
- numpy: For numerical operations
- cjkwrap: For handling CJK text wrapping
- json5: For robust JSON parsing

## Giấy phép

Apache License 2.0

Xem [LICENSE](LICENSE) để biết đầy đủ điều khoản.

## Lời cảm ơn

- OpenAI vì đã cung cấp năng lực phân tích ngôn ngữ
- Google Noto fonts cho hỗ trợ văn bản đa ngôn ngữ
