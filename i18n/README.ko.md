[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

단어의 어원(기원과 역사적 변화)을 분석하고, 이를 인터랙티브 그래프로 시각화하는 도구입니다.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## 개요
<a id="overview"></a>

WordOrigins는 단어의 어원(기원과 역사적 발달)을 탐색할 수 있게 해주는 Python 웹 애플리케이션입니다. 시간이 흐르며 단어가 어떻게 변화했는지 자세히 분석하고, 단어를 구성 요소로 분해한 뒤 각 요소의 언어 계통을 재귀적으로 추적하며, 그 결과를 브라우저에서 확인할 수 있는 그래프 이미지로 렌더링합니다.

### ✨ 핵심 기능

- 임의의 단어에 대한 상세 어원 분석
- 단어 기원을 시각적 그래프로 표현
- 영어, 프랑스어, 아랍어, 일본어, 중국어를 포함한 다국어 지원
- 탐색을 위한 인터랙티브 웹 인터페이스

## 기능
<a id="features"></a>

| 기능 | 상세 |
|---|---|
| 🔎 웹 UI | 생성된 어원 그래프 검색 및 탐색 |
| 🧠 OpenAI 기반 분석 | OpenAI API를 사용해 구조화된 어원 결과 생성 |
| 💾 캐싱 | OpenAI 응답을 타임스탬프 JSON 스냅샷으로 캐시 |
| 🖼️ 산출물 생성 | 이전에 분석한 단어의 JSON 및 PNG 산출물 캐시 |
| 🌍 다국어 렌더링 | 저장소에 포함된 CJK + 아랍어 폰트 지원 |
| ↔️ 내비게이션 | 생성된 단어 이미지를 이전/다음으로 탐색 |
| 🔌 API 지원 | 엔드포인트가 PNG 결과를 base64로 반환 |

## 작동 방식

1. 분석할 단어를 입력합니다.
2. 시스템이 OpenAI API에 연결해 심층 어원 분석을 수행합니다.
3. 분석기가 모델 출력을 검증/파싱해 구조화된 JSON으로 만듭니다.
4. 결과를 캐시하고 방향 그래프로 변환합니다.
5. 그래프를 PNG로 렌더링해 웹 인터페이스에 표시합니다.
6. 이전에 분석한 단어를 탐색할 수 있습니다.

## 프로젝트 구조

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Tornado 웹 서버 진입점
├─ word_etymology_analyzer.py          # OpenAI 기반 어원 분석 + 캐싱
├─ etymology_graph.py                  # NetworkX + Matplotlib 그래프 생성
├─ utils.py                            # 이미지/텍스처 헬퍼 유틸리티
├─ templates/
│  ├─ index.html                       # 메인 UI
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # 기본 렌더링 PNG 출력
├─ statics/
│  └─ images/                          # 레거시 중복 이미지 폴더
├─ jsons/                              # 단어별 JSON 및 이미지 산출물
├─ word_etymology_analysis/            # 타임스탬프 모델 응답 캐시
├─ processed_words.csv                 # 처리된 단어 로그
├─ i18n/                               # 다국어 README/문서 파일용
├─ archived_code/                      # 과거 노트북/코드
├─ archived_data/                      # 과거 JSON 출력
├─ etymology*.ipynb                    # 노트북 실험
├─ Noto Sans CJK Regular/              # 포함된 CJK 폰트
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # 포함된 아랍어 + Noto 폰트군
└─ arial-unicode-ms.ttf                # 유니코드 지원 폰트
```

## 필수 요건
<a id="prerequisites"></a>

- Python 3.8+
- OpenAI API 키
- 필수 폰트(저장소 포함):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## 설치

### 설정

1. 저장소 클론:
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

코드는 런타임에 다음 패키지를 import합니다:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

가정: `requirements.txt`에는 위 패키지가 포함되어 있어야 합니다. 로컬 복사본에 `requirements.txt`가 없다면 수동으로 설치하세요.

## 사용법

### 웹 애플리케이션 실행

Tornado 웹 서버를 시작합니다:

```bash
python app.py
```

그다음 브라우저에서 `http://localhost:7788`로 이동하세요.

### 일반적인 사용자 흐름

1. `http://localhost:7788`를 엽니다.
2. 검색 상자에 단어를 입력합니다.
3. 앱이 어원 그래프를 분석하고 렌더링합니다.
4. 이전/다음 컨트롤로 생성된 단어를 탐색합니다.

### API 엔드포인트
<a id="api-endpoints"></a>

| Method | Endpoint | 설명 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 단어의 어원 그래프를 생성하고 표시 |
| `GET` | `/word/next-word` | 목록의 다음 단어로 이동 |
| `GET` | `/word/prev-word` | 목록의 이전 단어로 이동 |
| `GET/POST` | `/get_word_etymology/{word}` | 어원 데이터를 base64 PNG 페이로드로 반환하는 API 엔드포인트 |

### API 호출 예시

```bash
# 브라우저에서 단어 생성/조회
curl "http://localhost:7788/word/etymology"

# base64 이미지 페이로드 가져오기
curl "http://localhost:7788/get_word_etymology/etymology"
```

## 구성

### 환경 변수

- `OPENAI_API_KEY` (필수): OpenAI Python 클라이언트가 사용하는 API 키
- `OPENAI_MODEL` (선택): 분석기에서 사용하는 모델 이름(기본값 `gpt-4-0125-preview`)

### 앱이 생성/사용하는 런타임 디렉터리

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## 구성 요소

### WordEtymologyAnalyzer

지정한 단어의 상세 어원 정보를 얻기 위해 OpenAI API에 연결합니다. 캐싱 및 재시도 로직을 포함합니다:

- 입력 단어를 소문자로 변환
- JSON 출력을 견고하게 파싱 시도(`json5`)
- `word_etymology_analysis/`에 타임스탬프 분석 스냅샷 저장
- `processed_words.csv`에 처리된 단어 기록

### EtymologyGraph

NetworkX와 Matplotlib을 사용해 어원 데이터의 시각적 표현을 생성합니다:

- 중첩 어원 구조를 재귀적으로 방향 그래프 노드/엣지로 매핑
- 깊이 기반 방사형 위치 계산
- 구성 요소/의미/예시 및 언어 엣지 레이블 그리기
- 포함된 폰트로 다국어 텍스트 렌더링 처리

### 웹 애플리케이션

요청을 처리하고 사용자 인터페이스를 제공하는 Tornado 기반 웹 서버:

- `/`를 `/word/etymology`로 리다이렉트
- `static/images/`의 단어 그래프 렌더링
- 누락된 분석/이미지를 필요 시 생성

## 예시

### 새 단어 분석

```bash
python app.py
# 그런 다음 http://localhost:7788/word/revolution 열기
```

첫 실행 후 예상 출력:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### 기존 생성 단어 탐색

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## 기술 세부 사항

- 애플리케이션은 캐싱을 위해 분석된 단어의 JSON 파일을 저장합니다.
- 이미지는 PNG 파일로 생성됩니다.
- 다국어 지원을 위해 특수 폰트 처리 로직이 구현되어 있습니다.
- 그래프 레이아웃은 노드 깊이와 관계를 기반으로 계산됩니다.
- 현재 저장소에는 개발 중 사용된 실험용 노트북과 보관 산출물이 포함되어 있습니다.

## 개발 노트

- 주요 런타임 진입점은 `app.py`입니다.
- 노트북 파일(`etymology*.ipynb`)은 실험용이며 실제 서버 흐름과 다를 수 있습니다.
- 역사적 맥락을 위해 레거시/중복 경로(`statics/` vs `static/`, `.old` 파일)가 유지됩니다.
- 현재 `.gitignore`에는 미해결 병합 충돌 마커가 있는 것으로 보이므로, 릴리스 패키징 전 정리해야 합니다.

## 문제 해결

| 문제 | 해결 방법 |
|---|---|
| 시작 시 `ModuleNotFoundError` 발생 | 누락된 의존성 설치: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` 오류 또는 인증 실패 | `python app.py`를 실행하는 동일한 셸 세션에서 `OPENAI_API_KEY`가 export되었는지 확인 |
| 그래프 텍스트가 네모(□)로 표시되거나 글리프 누락 | 포함된 폰트 파일이 예상 저장소 경로에 있는지 확인 |
| 단어 이미지가 생성되지 않음 | 서버 로그에서 JSON 파싱 재시도/예외를 확인하고 네트워크/API 접근 가능 여부 확인 |
| `requirements.txt`가 없어 `pip install -r requirements.txt` 실패 | 이 README의 패키지 목록으로 로컬 의존성 파일을 만들거나 패키지를 직접 설치 |

## 로드맵

- 더 많은 언어 지원 추가
- 즐겨찾기 어원을 저장할 수 있는 사용자 계정 구현
- 확대/이동 가능한 그래프 시각화 개선
- 더 상세한 언어학 정보 추가
- 유지 관리되는 의존성 매니페스트와 재현 가능한 환경 구성 추가
- 분석기 파싱, 캐싱 동작, 라우트 핸들러 테스트 추가

## 기여

기여를 환영합니다. 권장 워크플로우:

1. 저장소를 포크합니다.
2. 기능 브랜치를 생성합니다.
3. 검토하기 쉬운, 범위가 명확한 변경을 수행합니다.
4. `python app.py` 실행 및 주요 라우트 확인으로 검증합니다.
5. 필요 시 명확한 설명과 스크린샷/API 샘플을 포함해 Pull Request를 엽니다.

## 의존성

- tornado: 웹 서버 프레임워크
- openai: OpenAI API 클라이언트
- matplotlib: 그래프 생성
- networkx: 그래프 데이터 구조
- PIL/Pillow: 이미지 처리
- numpy: 수치 연산
- cjkwrap: CJK 텍스트 줄바꿈 처리
- json5: 견고한 JSON 파싱

## 라이선스

Apache License 2.0

전체 조건은 [LICENSE](LICENSE)를 참조하세요.

## 감사의 글

- 언어 분석 기능을 제공하는 OpenAI
- 다국어 텍스트 지원을 위한 Google Noto 폰트
