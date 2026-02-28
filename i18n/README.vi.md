[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Tùy chọn ngôn ngữ:** Tiếng Việt (tệp này)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

Một công cụ để phân tích từ nguyên của từ ngữ và trực quan hóa chúng dưới dạng đồ thị tương tác.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Bức tranh nhanh

| Khu vực | Chi tiết |
|---|---|
| 🌐 Truy cập | Giao diện web để khám phá tương tác và API để xuất PNG dạng base64 |
| 🧠 Trí tuệ | Phân tích từ nguyên bằng OpenAI với cú pháp JSON có cấu trúc |
| 🧰 Tái tạo | JSON + PNG được lưu đệm cho mỗi từ đã xử lý |
| 🌍 Hỗ trợ ngôn ngữ | Hỗ trợ nhiều ngôn ngữ cho CJK và Arabic với bộ font đi kèm |

## Tổng quan

WordOrigins là ứng dụng web Python cho phép bạn khám phá nguồn gốc ngôn ngữ (etymology) của các từ. Ứng dụng cung cấp phân tích chi tiết về quá trình biến đổi của từ theo thời gian, chia tách chúng thành các phần cấu trúc, truy vết đệ quy nguồn gốc ngôn ngữ của từng phần, sau đó hiển thị kết quả dưới dạng ảnh đồ thị để xem trong trình duyệt.

### ✨ Tính năng nổi bật

- Phân tích từ nguyên chi tiết cho mọi từ
- Biểu diễn trực quan nguồn gốc từ qua đồ thị
- Hỗ trợ nhiều ngôn ngữ gồm tiếng Anh, Pháp, Arabic, Nhật và Trung
- Giao diện web tương tác để người dùng khám phá

## Tính năng

| Tính năng | Chi tiết |
|---|---|
| 🔎 Giao diện web | Tìm kiếm và duyệt các đồ thị từ nguyên đã tạo |
| 🧠 Phân tích dựa trên OpenAI | Sử dụng API của OpenAI để tạo đầu ra từ nguyên có cấu trúc |
| 💾 Bộ nhớ đệm | Lưu phản hồi OpenAI dưới dạng JSON có dấu thời gian |
| 🖼️ Tạo artifact | Lưu đệm artifact JSON và PNG cho các từ đã phân tích trước đó |
| 🌍 Kết xuất đa ngôn ngữ | Hỗ trợ font CJK và Arabic được đóng gói trong kho |
| ↔️ Điều hướng | Duyệt qua ảnh từ trước/sau đã tạo |
| 🔌 Hỗ trợ API | Endpoint trả về ảnh PNG dạng base64 |

## Cách hoạt động

1. Nhập từ cần phân tích.
2. Hệ thống kết nối với API của OpenAI để thực hiện phân tích từ nguyên sâu.
3. Bộ phân tích xác thực và chuyển đầu ra mô hình sang JSON có cấu trúc.
4. Kết quả được lưu đệm và chuyển thành đồ thị có hướng.
5. Đồ thị được kết xuất thành PNG và hiển thị trong giao diện web.
6. Bạn có thể duyệt các từ đã được phân tích trước đó.

## Cấu trúc dự án

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Điểm khởi chạy của máy chủ web Tornado
├─ word_etymology_analyzer.py          # Phân tích từ nguyên + cache bằng OpenAI
├─ etymology_graph.py                  # Tạo đồ thị với NetworkX + Matplotlib
├─ utils.py                            # Tiện ích xử lý ảnh/texture
├─ templates/
│  ├─ index.html                       # Giao diện UI chính
│  ├─ index.html.old                   # Phiên bản template cũ
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Ảnh PNG đầu ra đã render chính
├─ statics/
│  └─ images/                          # Thư mục ảnh trùng lặp dùng cho tương thích cũ
├─ jsons/                              # Artifact JSON và hình ảnh cho từng từ
├─ word_etymology_analysis/            # Cache phản hồi mô hình có dấu thời gian
├─ processed_words.csv                  # Nhật ký các từ đã xử lý
├─ i18n/                               # Tập tin README/tài liệu đa ngôn ngữ
├─ archived_code/                      # Notebook và mã nguồn lịch sử
├─ archived_data/                      # Kết quả JSON lịch sử
├─ etymology*.ipynb                    # Các thí nghiệm trong notebook
├─ Noto Sans CJK Regular/              # Font CJK đi kèm
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # Bộ font Arabic + Noto đi kèm
└─ arial-unicode-ms.ttf                # Font hỗ trợ Unicode
```

## Điều kiện tiên quyết

- Python 3.8+
- Khóa API của OpenAI
- Các font bắt buộc (đã có sẵn trong kho):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Cài đặt

### Thiết lập

1. Sao chép kho mã:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Cài đặt các phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```

3. Thiết lập khóa OpenAI API dưới dạng biến môi trường:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Ghi chú về phụ thuộc

Mã nguồn import các gói sau khi chạy:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Giả định: `requirements.txt` cần chứa các gói ở trên. Nếu bản sao cục bộ của bạn thiếu `requirements.txt`, hãy cài thủ công các gói này.

## Cách sử dụng

### Chạy ứng dụng web

Khởi động máy chủ Tornado:

```bash
python app.py
```

Sau đó mở trình duyệt và đi tới `http://localhost:7788`.

### Luồng sử dụng điển hình

1. Mở `http://localhost:7788`.
2. Nhập một từ vào ô tìm kiếm.
3. Ứng dụng sẽ phân tích và hiển thị đồ thị từ nguyên.
4. Dùng điều khiển trước/sau để duyệt các từ đã tạo.

### API Endpoints

| Method | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Tạo và hiển thị đồ thị từ nguyên cho một từ |
| `GET` | `/word/next-word` | Di chuyển tới từ kế tiếp trong danh sách |
| `GET` | `/word/prev-word` | Di chuyển về từ trước đó trong danh sách |
| `GET/POST` | `/get_word_etymology/{word}` | Endpoint API để lấy dữ liệu từ nguyên dưới dạng payload PNG base64 |

### Ví dụ gọi API

```bash
# Tạo/xem một từ trên trình duyệt
curl "http://localhost:7788/word/etymology"

# Lấy payload ảnh base64
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Cấu hình

### Biến môi trường

- `OPENAI_API_KEY` (bắt buộc): khóa API mà OpenAI Python client sử dụng
- `OPENAI_MODEL` (tùy chọn): tên mô hình mà module phân tích dùng (mặc định `gpt-4-0125-preview`)

### Thư mục runtime được tạo/sử dụng bởi ứng dụng

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Các thành phần

### WordEtymologyAnalyzer

Kết nối đến API của OpenAI để lấy thông tin từ nguyên chi tiết cho một từ. Bao gồm logic cache và thử lại:

- Chuyển từ đầu vào về chữ thường và chuẩn hóa
- Thử phân tích cú pháp JSON đầu ra một cách bền vững (`json5`)
- Lưu ảnh phân tích có dấu thời gian trong `word_etymology_analysis/`
- Ghi nhận các từ đã xử lý vào `processed_words.csv`

### EtymologyGraph

Tạo biểu diễn trực quan cho dữ liệu từ nguyên bằng NetworkX và Matplotlib:

- Ánh xạ đệ quy phần từ nguyên lồng nhau thành các nút/cạnh của đồ thị có hướng
- Tính toán vị trí tâm theo độ sâu
- Vẽ nhãn phần/nghĩa/ví dụ và nhãn cạnh ngôn ngữ
- Xử lý kết xuất văn bản đa ngôn ngữ với font đi kèm

### Ứng dụng web

Máy chủ web dựa trên Tornado xử lý request và phục vụ giao diện:

- Chuyển hướng `/` về `/word/etymology`
- Kết xuất đồ thị từ trong `static/images/`
- Tạo phân tích/hình ảnh còn thiếu theo yêu cầu

## Ví dụ

### Phân tích một từ mới

```bash
python app.py
# sau đó mở http://localhost:7788/word/revolution
```

Kết quả dự kiến sau lần chạy đầu tiên:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Duyệt các từ đã được tạo

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Chi tiết kỹ thuật

- Ứng dụng lưu các tệp JSON của từ đã phân tích để làm cache.
- Ảnh được tạo dưới dạng tệp PNG.
- Có xử lý font đặc biệt cho hỗ trợ đa ngôn ngữ.
- Bố cục đồ thị được tính toán dựa trên độ sâu nút và quan hệ.
- Kho mã hiện có notebook thăm dò và artifact lưu trữ dùng trong quá trình phát triển.

## Ghi chú phát triển

- Điểm khởi chạy runtime chính là `app.py`.
- Tệp notebook (`etymology*.ipynb`) mang tính thử nghiệm và có thể khác với luồng server production.
- Có các đường dẫn trùng lặp/legacy (`statics/` so với `static/`, các tệp `.old`) được giữ vì lý do lịch sử.
- `.gitignore` hiện tại dường như chứa marker giải quyết xung đột chưa được xử lý; nên dọn dẹp trước khi đóng gói phát hành.

## Khắc phục sự cố

| Vấn đề | Cách khắc phục |
|---|---|
| `ModuleNotFoundError` khi khởi động | Cài phụ thuộc còn thiếu: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Lỗi `OPENAI_API_KEY` hoặc lỗi xác thực | Kiểm tra `OPENAI_API_KEY` đã được export trong cùng phiên terminal khi bạn chạy `python app.py` |
| Văn bản đồ thị hiển thị thành ô vuông hoặc thiếu glyph | Kiểm tra các tệp font đã được đóng gói có tồn tại đúng đường dẫn trong kho |
| Không có hình cho một từ | Kiểm tra logs máy chủ để xem lỗi/retry parse JSON và xác nhận quyền truy cập mạng/API |
| `pip install -r requirements.txt` lỗi vì thiếu file | Tạo file phụ thuộc cục bộ từ danh sách package trong README này hoặc cài trực tiếp các package |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Lộ trình

- Bổ sung hỗ trợ thêm ngôn ngữ.
- Triển khai tài khoản người dùng để lưu các từ nguyên yêu thích.
- Cải tiến trực quan hóa đồ thị với phóng to/di chuyển.
- Thêm thông tin ngôn ngữ học chi tiết hơn.
- Thêm manifest phụ thuộc được duy trì và setup môi trường tái lập.
- Thêm kiểm thử cho xử lý phân tích, hành vi cache và route handlers.

## Đóng góp

Mọi đóng góp đều được hoan nghênh. Quy trình gợi ý:

1. Fork repository.
2. Tạo một nhánh feature.
3. Thực hiện thay đổi có phạm vi rõ ràng và dễ review.
4. Kiểm tra bằng cách chạy `python app.py` và kiểm tra các route chính.
5. Tạo pull request với mô tả rõ ràng và screenshot/mẫu API khi phù hợp.

## Dependencies

- tornado: Khung máy chủ web
- openai: Client OpenAI API
- matplotlib: Dùng để tạo đồ thị
- networkx: Dùng cho cấu trúc dữ liệu đồ thị
- PIL/Pillow: Dùng cho xử lý ảnh
- numpy: Cho các phép toán số
- cjkwrap: Xử lý gói chữ CJK
- json5: Phân tích cú pháp JSON theo cách bền vững

## Lời cảm ơn

- OpenAI vì đã cung cấp khả năng phân tích ngôn ngữ
- Google Noto fonts cho hỗ trợ văn bản đa ngôn ngữ

## Giấy phép

Apache License 2.0

Xem [LICENSE](LICENSE) để đọc toàn bộ điều khoản.
