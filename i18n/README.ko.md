[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Language options:** 한국어 (이 파일)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

단어의 어원(기원과 역사적 전개)을 분석하고 대화형 그래프로 시각화하는 도구입니다.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## 빠른 개요

| 항목 | 세부 사항 |
|---|---|
| 🌐 접근 | 대화형 탐색을 위한 웹 UI와 Base64 PNG 출력을 제공하는 API |
| 🧠 지능 | 구조화된 JSON 파싱을 포함한 OpenAI 기반 어원 분석 |
| 🧰 재현성 | 처리된 각 단어에 대해 타임스탬프 JSON 및 PNG 산출물을 캐시 |
| 🌍 언어 지원 | 저장소에 포함된 CJK 및 아랍어 폰트로 다국어 렌더링 |

## 개요

WordOrigins는 단어의 어원(기원과 역사적 변화)을 탐색할 수 있게 해주는 Python 웹 애플리케이션입니다. 시간이 흐르며 단어가 어떻게 발전했는지에 대한 자세한 분석을 제공하고, 단어를 구성 요소로 분해한 뒤 각 요소의 언어적 계보를 재귀적으로 추적해 결과를 브라우저에서 볼 수 있는 그래프 이미지로 렌더링합니다.

### ✨ 주요 기능

- 임의의 단어에 대한 상세한 어원 분석
- 단어 기원의 시각적 그래프 표현
- 영어, 프랑스어, 아랍어, 일본어, 중국어를 포함한 다국어 지원
- 탐색을 위한 대화형 웹 인터페이스

## 기능

| 기능 | 세부 사항 |
|---|---|
| 🔎 웹 UI | 생성된 어원 그래프를 검색하고 탐색 |
| 🧠 OpenAI 기반 분석 | OpenAI API를 사용해 구조화된 어원 분석 결과 생성 |
| 💾 캐싱 | OpenAI 응답을 타임스탬프 JSON 스냅샷으로 캐시 |
| 🖼️ 산출물 생성 | 이전 분석 단어에 대한 JSON과 PNG 산출물을 캐시 |
| 🌍 다국어 렌더링 | 저장소에 포함된 CJK + 아랍어 폰트 지원 |
| ↔️ 탐색 | 생성된 단어 이미지 사이를 이전/다음으로 이동 |
| 🔌 API 지원 | 엔드포인트가 PNG 결과를 Base64로 반환 |

## 동작 방식

1. 분석할 단어를 입력합니다.
2. 시스템이 OpenAI API에 연결해 깊은 어원 분석을 수행합니다.
3. 분석기가 모델 출력을 검증/파싱해 구조화된 JSON으로 변환합니다.
4. 결과를 캐시한 뒤 방향성 그래프로 변환합니다.
5. 그래프를 PNG로 렌더링해 웹 인터페이스에 표시합니다.
6. 이전에 분석된 단어를 이어서 탐색할 수 있습니다.

## 프로젝트 구조

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Tornado 웹 서버 진입점
├─ word_etymology_analyzer.py          # OpenAI 기반 어원 분석 + 캐싱
├─ etymology_graph.py                  # NetworkX + Matplotlib 그래프 생성
├─ utils.py                            # 이미지/텍스처 유틸리티
├─ templates/
│  ├─ index.html                       # 메인 UI
│  ├─ index.html.old                   # 기존 템플릿 변형
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # 기본 렌더링 PNG 출력
├─ statics/
│  └─ images/                          # 레거시 중복 이미지 폴더
├─ jsons/                              # 단어별 JSON 및 이미지 산출물
├─ word_etymology_analysis/            # 타임스탬프 기반 모델 응답 캐시
├─ processed_words.csv                 # 처리된 단어 로그
├─ i18n/                               # 다국어 README/문서 파일
├─ archived_code/                      # 과거 노트북/코드
├─ archived_data/                      # 과거 JSON 출력물
├─ etymology*.ipynb                    # 노트북 실험
├─ Noto Sans CJK Regular/              # 번들된 CJK 폰트
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # 번들된 아랍어 + Noto 폰트군
└─ arial-unicode-ms.ttf                # 유니코드 지원 폰트
```

## 필수 조건

- Python 3.8+
- OpenAI API 키
- 필수 폰트(저장소에 포함됨):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## 설치

### 설정

1. 저장소 복제:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

3. OpenAI API 키를 환경 변수로 설정:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### 의존성 참고

실행 시 다음 패키지를 import합니다:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

가정: `requirements.txt`에는 위 패키지가 포함되어 있어야 합니다. 로컬 복사본에 `requirements.txt`가 없으면 수동으로 설치하세요.

## 사용법

### 웹 애플리케이션 실행

Tornado 웹 서버 시작:

```bash
python app.py
```

그다음 브라우저에서 `http://localhost:7788`로 이동합니다.

### 일반 사용자 흐름

1. `http://localhost:7788`를 엽니다.
2. 검색창에 단어를 입력합니다.
3. 앱이 어원 그래프를 분석해 렌더링합니다.
4. 이전/다음 컨트롤을 사용해 생성된 단어를 탐색합니다.

### API 엔드포인트

| 메서드 | 엔드포인트 | 설명 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 단어의 어원 그래프 생성 및 표시 |
| `GET` | `/word/next-word` | 목록에서 다음 단어로 이동 |
| `GET` | `/word/prev-word` | 목록에서 이전 단어로 이동 |
| `GET/POST` | `/get_word_etymology/{word}` | 어원 데이터를 Base64 PNG payload로 반환하는 API 엔드포인트 |

### API 호출 예시

```bash
# 브라우저에서 단어 생성/조회
curl "http://localhost:7788/word/etymology"

# Base64 이미지 payload 가져오기
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 구성

### 환경 변수

- `OPENAI_API_KEY` (필수): OpenAI Python 클라이언트가 사용하는 API 키
- `OPENAI_MODEL` (선택): 분석기에 사용되는 모델 이름(기본값 `gpt-4-0125-preview`)

### 앱에서 생성/사용되는 런타임 디렉터리

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 구성 요소

### WordEtymologyAnalyzer

지정한 단어의 상세 어원 정보를 얻기 위해 OpenAI API에 연결합니다. 캐싱 및 재시도 로직을 포함합니다:

- 입력 단어를 소문자로 정규화
- JSON 출력을 `json5`로 강건하게 파싱 시도
- `word_etymology_analysis/`에 타임스탬프 분석 스냅샷 저장
- `processed_words.csv`에 처리된 단어 기록

### EtymologyGraph

NetworkX와 Matplotlib을 사용해 어원 데이터를 시각화합니다:

- 중첩된 어원을 재귀적으로 방향성 그래프의 노드/엣지로 매핑
- 깊이 기반 방사형 배치 계산
- 구성 요소/의미/예시 및 언어 엣지 라벨 렌더링
- 번들 폰트로 다국어 텍스트 렌더링 처리

### 웹 애플리케이션

요청을 처리하고 사용자 인터페이스를 제공하는 Tornado 기반 웹 서버:

- `/`를 `/word/etymology`로 리다이렉트
- `static/images/`에서 단어 그래프 렌더링
- 누락된 분석/이미지를 필요 시 생성

## 예시

### 새 단어 분석

```bash
python app.py
# 그런 다음 http://localhost:7788/word/revolution 열기
```

최초 실행 후 예상 출력:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 기존 생성 단어 탐색

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 기술 세부 정보

- 앱은 분석된 단어의 JSON 파일을 캐싱 용도로 저장합니다.
- 이미지는 PNG 파일로 생성됩니다.
- 다국어 지원을 위해 특수 폰트 처리 로직이 구현되어 있습니다.
- 그래프 레이아웃은 노드 깊이와 관계에 기반해 계산됩니다.
- 현재 저장소에는 개발 중 사용된 실험용 노트북과 보관된 산출물이 포함되어 있습니다.

## 개발 노트

- 기본 런타임 진입점은 `app.py`입니다.
- 노트북 파일(`etymology*.ipynb`)은 실험용이며 실제 서버 흐름과 다를 수 있습니다.
- 레거시/중복 경로(`statics/` 대비 `static/`, `.old` 파일)는 역사적 맥락 유지를 위해 보존됩니다.
- 현재 `.gitignore`에 해결되지 않은 병합 충돌 마커가 남아 있는 것으로 보이므로 릴리스 패키징 전에 정리해야 합니다.

## 문제 해결

| 문제 | 해결 방법 |
|---|---|
| 시작 시 `ModuleNotFoundError` 발생 | 누락된 의존성을 설치: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 오류 또는 인증 실패 | `python app.py`를 실행하는 동일한 셸 세션에서 `OPENAI_API_KEY`가 export되었는지 확인 |
| 그래프 텍스트가 네모(□)로 표시되거나 글리프가 누락됨 | 번들 폰트 파일이 저장소의 예상 경로에 있는지 확인 |
| 단어 이미지가 생성되지 않음 | 서버 로그에서 JSON 파싱 재시도/예외를 확인하고 네트워크/API 접근을 점검 |
| `pip install -r requirements.txt` 실행 실패(파일 없음) | 이 README의 패키지 목록으로 로컬 의존성 파일을 만들거나 패키지를 직접 설치 |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 로드맵

- 더 많은 언어 지원 추가
- 즐겨찾는 어원을 저장할 수 있는 사용자 계정 구현
- 줌/팬 기능을 가진 그래프 시각화 개선
- 더 상세한 언어학 정보 추가
- 유지 보수 가능한 의존성 매니페스트와 재현 가능한 환경 구성 추가
- 분석기 파싱, 캐싱 동작, 라우트 핸들러에 대한 테스트 추가

## 기여

기여를 환영합니다. 권장 워크플로우:

1. 저장소를 포크합니다.
2. 기능 브랜치를 만듭니다.
3. 집중되고 검토 가능한 변경을 수행합니다.
4. `python app.py`를 실행해 주요 라우트를 확인하며 검증합니다.
5. 필요 시 명확한 설명과 스크린샷/API 샘플과 함께 Pull Request를 만듭니다.

## 의존성

- tornado: 웹 서버 프레임워크
- openai: OpenAI API 클라이언트
- matplotlib: 그래프 생성용
- networkx: 그래프 데이터 구조 처리
- PIL/Pillow: 이미지 처리
- numpy: 수치 연산
- cjkwrap: CJK 텍스트 줄 바꿈 처리
- json5: 안정적인 JSON 파싱

## 감사의 글

- 언어 분석 기능을 제공하는 OpenAI
- 다국어 텍스트 지원을 위한 Google Noto 폰트

## 라이선스

Apache License 2.0

자세한 내용은 [LICENSE](LICENSE)를 참조하세요.
