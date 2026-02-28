[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 OpenAI 기반의 캐시 친화형 워크플로우로 단어의 어원을 다국어 계보 그래프로 시각화합니다.

**언어 옵션:** 한국어 (이 파일)

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

## 📘 개요

WordOrigins는 단어의 어원을 분석하고, 언어 계보를 방향성 그래프로 시각화하는 Python 웹 유틸리티입니다. 다음을 결합합니다.

- Tornado 웹 애플리케이션
- OpenAI 기반의 어원 분석
- 장애 내성이 있는 구조화 JSON 파싱
- NetworkX + Matplotlib 기반 그래프 생성
- 빠른 반복 분석을 위한 캐시 출력

브라우저 인터페이스와 API 엔드포인트를 모두 제공해 어원 아티팩트를 생성하고 조회할 수 있습니다.

## 📸 빠른 스냅샷

| 영역 | 세부 정보 |
|---|---|
| 🌐 접근성 | 대화형 탐색이 가능한 웹 UI와 Base64 PNG 출력을 반환하는 API |
| 🧠 지능형 분석 | OpenAI 기반 어원 분석과 구조화 JSON 파싱 |
| 🧰 재현성 | 처리된 각 단어에 대해 JSON + PNG 아티팩트 캐시 |
| 🌍 언어 지원 | 번들 폰트로 CJK 및 아랍어 다국어 렌더링 |

## 기능

| 기능 | 세부 정보 |
|---|---|
| 🔎 웹 UI | 생성된 어원 그래프를 검색하고 탐색 |
| 🧠 OpenAI 기반 분석 | OpenAI API를 사용해 구조화된 어원 결과 생성 |
| 💾 캐싱 | 타임스탬프가 포함된 JSON 스냅샷을 저장 |
| 🖼️ 아티팩트 생성 | 처리된 단어의 JSON 및 PNG 아티팩트 내보내기 |
| 🌍 다국어 렌더링 | 저장소에 번들된 CJK + 아랍어 폰트 지원 |
| ↔️ 탐색 | 생성된 단어 이미지 간 이전/다음 이동 |
| 🔌 API 지원 | PNG 출력을 base64 JSON 페이로드로 반환하는 엔드포인트 |

## 🛠️ 작동 방식

1. 사용자가 `/word/{word}` 또는 웹 검색 폼을 통해 단어를 제출합니다.
2. 분석기가 OpenAI를 호출해 응답 구조를 검증합니다.
3. 파싱된 데이터는 정규화되어 캐시 재사용용으로 저장됩니다.
4. 어원 관계가 그래프의 노드/엣지로 변환됩니다.
5. NetworkX와 Matplotlib이 방향성 그래프를 PNG로 렌더링합니다.
6. UI와 API가 캐시된 이미지 경로 및 관련 메타데이터를 제공합니다.

## 🗂️ 프로젝트 구조

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

## 필수 조건

- Python 3.8+
- OpenAI API 자격 증명:
  - `OPENAI_API_KEY` (필수)
  - `OPENAI_MODEL` (선택, 기본값은 기존 가이드에 따라 `gpt-4-0125-preview`)
- 다국어 렌더링이 필요할 경우 저장소에 포함된 폰트 파일

## 🧰 설치

1. 저장소를 클론합니다.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Python 가상 환경을 만들고 활성화합니다(권장).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. 런타임 라이브러리를 설치합니다.

   이 저장소에는 루트 의존성 매니페스트가 없으므로, 알려진 실행 요구사항을 직접 설치하세요.

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. 자격 증명을 설정합니다.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optional override
   ```

## 🚀 사용법

### 웹 앱 실행

```bash
python app.py
```

브라우저에서 `http://localhost:7788`을 엽니다.

### 일반적인 사용자 흐름

1. `http://localhost:7788/word/etymology`를 엽니다.
2. 단어를 입력합니다.
3. 분석을 기다립니다. (최초 실행은 외부 API 지연으로 시간이 더 걸릴 수 있음)
4. 생성된 그래프와 메타데이터를 확인합니다.
5. 다음/이전 탐색으로 캐시 단어를 둘러봅니다.

### API 엔드포인트

| 메서드 | 엔드포인트 | 설명 |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | 요청한 단어의 어원 페이지 렌더링 |
| `GET` | `/word/next-word?word={word}` | 캐시에서 다음 단어로 이동 |
| `GET` | `/word/prev-word?word={word}` | 캐시에서 이전 단어로 이동 |
| `GET/POST` | `/get_word_etymology/{word}` | base64 PNG 페이로드가 포함된 JSON 반환 |

### API 호출 예시

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ 설정

- `OPENAI_API_KEY` (필수): 분석 요청용 자격 증명.
- `OPENAI_MODEL` (선택): 분석기에서 사용할 모델 오버라이드.
- 서비스에서 사용하는 런타임 디렉터리:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 예시

```bash
python app.py
```

다음 주소를 엽니다:

```text
http://localhost:7788/word/revolution
```

최초 분석에서 생성되는 아티팩트:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Components

### WordEtymologyAnalyzer

`word_etymology_analyzer.py`에 구현된 이 컴포넌트는 다음 작업을 수행합니다.

- 입력 단어를 정규화합니다.
- OpenAI를 호출해 구조화된 어원 응답을 생성합니다.
- `json5`를 사용해 JSON 페이로드를 추출/복구합니다.
- 파싱 실패를 재시도하고 복원력 강화를 위해 실패 이력을 기록합니다.
- `word_etymology_analysis/`에 타임스탬프가 포함된 스냅샷을 기록합니다.
- `processed_words.csv` 인덱스를 업데이트합니다.

### EtymologyGraph

`etymology_graph.py`에 구현된 이 컴포넌트는 다음 작업을 수행합니다.

- 구조화된 어원 JSON을 로드합니다.
- 재귀적 조상 관계로 `networkx.DiGraph`를 구성합니다.
- 깊이를 반영한 그래프 좌표를 계산합니다.
- 다국어 텍스트 처리와 함께 라벨이 있는 노드/엣지를 렌더링합니다.
- 캐시 및 표시용 `PNG` 이미지를 저장합니다.

### 웹 애플리케이션

`app.py`의 Tornado 앱은:

- 루트 리디렉션 및 검색 페이지 동작을 처리합니다.
- 생성 및 캐시 조회 워크플로우를 처리합니다.
- `/word/...` 및 `/get_word_etymology/...` 경로의 페이지/API 라우트를 노출합니다.
- API 소비자를 위해 base64 이미지 데이터를 포함한 JSON 페이로드를 반환합니다.

## 📦 의존성

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 개발 노트

- JSON 및 이미지 캐싱으로 불필요한 반복 API 호출을 줄입니다.
- `index.html`과 `index.html.old`는 호환성과 이력 유지를 위해 유지됩니다.
- 레거시 디렉터리와 산출물(`statics/`, 노트북, 아카이브)이 현재 의도적으로 유지되어 있습니다.
- 병합 충돌 마커가 포함된 `.gitignore`는 README 범위를 벗어난 상위 저장소 관리 이슈입니다.

## 🧯 문제 해결

| 문제 | 해결 방법 |
|---|---|
| 시작 시 `ModuleNotFoundError` 발생 | `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5`로 누락 패키지 설치 |
| `OPENAI_API_KEY` 인증 오류 | `python app.py`를 실행하는 동일한 셸 세션에서 변수가 export되었는지 확인 |
| 생성된 그래프에서 글꼴/문자가 깨지거나 누락됨 | 번들 폰트(`Noto Sans`, 아랍어 폰트 변형, `Arial Unicode MS`)가 존재하고 읽을 수 있는지 확인 |
| 단어에 이미지가 나타나지 않음 | 앱 로그에서 JSON 파싱 실패나 일시적 API 오류를 확인 |
| `pip install -r requirements.txt` 실패/존재하지 않음 | 현재 레포지토리에 루트 매니페스트가 없으므로 위 의존성 패키지를 직접 설치 |

## 🗺️ 로드맵

- 추가 언어 지원
- 즐겨찾기 어원을 위한 사용자 계정 추가
- 줌/팬 방식 상호작용으로 그래프 탐색 개선
- 각 그래프 노드의 언어 메타데이터 강화
- 유지되는 의존성 매니페스트 및 재현 가능한 환경 구성 추가
- 분석기 파싱, 캐시 동작, 라우트 핸들러에 대한 테스트 추가

## 🤝 기여

1. 저장소를 포크합니다.
2. 기능 브랜치를 생성합니다.
3. 집중적이고 리뷰 가능한 변경을 만듭니다.
4. `python app.py`를 실행해 핵심 라우트를 검증합니다.
5. 재현 가능한 실행 방법과 스크린샷/API 예시를 포함해 PR을 제출합니다.

## 🙌 감사

- OpenAI: 언어 모델 기반 분석 기능 제공.
- Google Noto 폰트 패밀리 기여자: 다국어 렌더링 지원.

## 라이선스

Apache License 2.0  
자세한 내용은 [LICENSE](LICENSE)를 참고하세요.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
