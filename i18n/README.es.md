[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Visualiza la etimología de palabras como grafos de procedencia multilingües mediante un flujo de trabajo compatible con caché y potenciado por OpenAI.

**Opciones de idioma:** Español (este archivo)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#requisitos-previos)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#componentes)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](#licencia)
[![API](https://img.shields.io/badge/API-REST-orange)](#endpoints-de-api)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etimologia-de-grafo)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#características)
[![GitHub last commit](https://img.shields.io/github/last-commit/lachlanchen/WordOrigins?color=blue)](https://github.com/lachlanchen/WordOrigins/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/lachlanchen/WordOrigins?color=red)](https://github.com/lachlanchen/WordOrigins/issues)
[![GitHub repo size](https://img.shields.io/github/repo-size/lachlanchen/WordOrigins?color=yellow)](https://github.com/lachlanchen/WordOrigins)

![Word Origins Demo](word_origins.jpg)

## 📘 Resumen

WordOrigins es una utilidad web en Python para analizar la etimología de palabras y visualizar la genealogía lingüística como un grafo dirigido. Combina:

- Una aplicación web con Tornado.
- Análisis de etimología con tecnología OpenAI.
- Parseo estructurado de JSON con recuperación ante fallos.
- Generación de grafos mediante NetworkX + Matplotlib.
- Salidas en caché para análisis repetidos rápidos.

Proporciona tanto una interfaz de navegador como endpoints de API para generar y recuperar artefactos de etimología.

## 📸 Resumen rápido

| Área | Detalles |
|---|---|
| 🌐 Acceso | UI web para exploración interactiva y API para salida PNG en base64 |
| 🧠 Inteligencia | Análisis de etimología con OpenAI y parseo JSON estructurado |
| 🧰 Reproducibilidad | Artefactos JSON + PNG en caché para cada palabra procesada |
| 🌍 Soporte de idiomas | Renderizado multilingüe para CJK y árabe con fuentes incluidas |

## Características

| Característica | Detalles |
|---|---|
| 🔎 UI web | Busca y explora grafos de etimología generados |
| 🧠 Análisis con OpenAI | Usa la API de OpenAI para producir salidas de etimología estructuradas |
| 💾 Caché | Almacena respuestas con instantáneas JSON con marca temporal |
| 🖼️ Generación de artefactos | Exporta artefactos JSON y PNG para palabras procesadas |
| 🌍 Renderizado multilingüe | Soporte para CJK + árabe con fuentes locales en el repositorio |
| ↔️ Navegación | Navegación anterior/siguiente a través de imágenes de palabras generadas |
| 🔌 Soporte de API | El endpoint devuelve la imagen PNG como payload JSON en base64 |

## 🛠️ Cómo funciona

1. El usuario envía una palabra a través de `/word/{word}` o el formulario de búsqueda web.
2. El analizador llama a OpenAI y valida la estructura de la respuesta.
3. Los datos parseados se normalizan y se persisten para reutilizar la caché.
4. Las relaciones etimológicas se convierten en nodos y aristas del grafo.
5. NetworkX y Matplotlib renderizan un grafo dirigido como PNG.
6. La UI y la API exponen la ruta de imagen en caché y metadatos relacionados.

## 🗂️ Estructura del proyecto

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
│  └─ carousel_items.html      # Reusable UI fragment
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

## Requisitos previos

- Python 3.8+
- Credenciales de la API de OpenAI:
  - `OPENAI_API_KEY` (obligatorio)
  - `OPENAI_MODEL` (opcional, por defecto `gpt-4-0125-preview` en la guía actual)
- Archivos de fuentes incluidos en el repositorio si necesitas renderizado multilingüe

## 🧰 Instalación

1. Clona el repositorio.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Crea y activa un entorno de Python (recomendado).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las librerías de ejecución.

   Como no existe un manifiesto de dependencias raíz en este repositorio, instala los requisitos de ejecución conocidos directamente:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Configura las credenciales.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # override opcional
   ```

## 🚀 Uso

### Ejecutar la aplicación web

```bash
python app.py
```

Abre `http://localhost:7788` en tu navegador.

### Flujo típico de uso

1. Abre `http://localhost:7788/word/etymology`.
2. Ingresa una palabra.
3. Espera el análisis (la primera ejecución puede tardar más por la latencia de la API externa).
4. Explora el grafo y los metadatos generados.
5. Usa la navegación anterior/siguiente para recorrer las palabras en caché.

### Endpoints de API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Renderiza una página para la etimología solicitada |
| `GET` | `/word/next-word?word={word}` | Navega a la siguiente palabra en caché |
| `GET` | `/word/prev-word?word={word}` | Navega a la palabra anterior en caché |
| `GET/POST` | `/get_word_etymology/{word}` | Devuelve un JSON con payload PNG en base64 |

### Ejemplos de llamadas API

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Configuración

- `OPENAI_API_KEY` (obligatorio): credenciales para solicitudes de análisis.
- `OPENAI_MODEL` (opcional): sustitución de modelo para el analizador.
- Directorios de ejecución usados por el servicio:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Ejemplos

```bash
python app.py
```

Después abre:

```text
http://localhost:7788/word/revolution
```

Artefactos creados en el primer análisis:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Componentes

### WordEtymologyAnalyzer

Ubicado en `word_etymology_analyzer.py`, este componente:

- Normaliza las palabras de entrada.
- Llama a OpenAI para respuestas etimológicas estructuradas.
- Extrae/repara cargas JSON con `json5`.
- Reintenta intentos de análisis fallidos y registra fallos para mayor robustez.
- Escribe instantáneas con marca temporal en `word_etymology_analysis/`.
- Actualiza el índice `processed_words.csv`.

### EtymologyGraph

Ubicado en `etymology_graph.py`, este componente:

- Carga el JSON etimológico estructurado.
- Construye un `networkx.DiGraph` con relaciones recursivas de parentesco.
- Calcula coordenadas de grafo conscientes de profundidad.
- Renderiza nodos y aristas con etiquetas con manejo multilingüe de texto.
- Guarda imágenes `PNG` para caché y presentación.

### Aplicación web

En `app.py`, la aplicación Tornado:

- Sirve redirección a raíz y comportamiento de página de búsqueda.
- Gestiona flujos de generación y consulta en caché.
- Expone rutas de página y de API bajo `/word/...` y `/get_word_etymology/...`.
- Devuelve cargas JSON con datos de imagen en base64 para consumidores de API.

## 📦 Dependencias

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Notas de desarrollo

- La caché de JSON e imágenes evita llamadas repetidas innecesarias a la API.
- `index.html` y `index.html.old` se conservan para compatibilidad/historial.
- Los directorios y artefactos heredados están presentes de forma intencional (`statics/`, notebooks, archivos históricos).
- Se detectó una `.gitignore` con marcadores de conflicto de fusión como un problema de higiene previo fuera del alcance de este README.

## 🧯 Solución de problemas

| Problema | Resolución |
|---|---|
| `ModuleNotFoundError` al iniciar | Instala paquetes faltantes con `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Error de autenticación de `OPENAI_API_KEY` | Verifica que la variable esté exportada en la misma sesión de shell que ejecuta `python app.py` |
| Faltan/garabatos en glifos de la imagen generada | Confirma que existan y sean legibles las fuentes incluidas (`Noto Sans`, variantes árabes, Arial Unicode MS) |
| No aparece ninguna imagen para una palabra | Revisa los registros de la app por fallos de parseo de JSON o errores transitorios de API |
| `pip install -r requirements.txt` falla/no existe | Instala las dependencias directamente como se mostró arriba (el repositorio actual no contiene un manifiesto raíz) |

## 🗺️ Hoja de ruta

- Añadir soporte para más idiomas.
- Añadir cuentas de usuario para guardar etimologías favoritas.
- Mejorar la navegación del grafo con interacciones de zoom/pan.
- Enriquecer los metadatos lingüísticos en cada nodo de grafo.
- Añadir un manifiesto de dependencias mantenido y configuración reproducible del entorno.
- Añadir pruebas para parseo del analizador, comportamiento de caché y controladores de ruta.

## 🤝 Contribución

1. Haz un fork del repositorio.
2. Crea una rama de características.
3. Realiza cambios enfocados y revisables.
4. Valida ejecutando `python app.py` y verificando las rutas clave.
5. Abre una PR con instrucciones reproducibles y ejemplos de pantalla/API.

## 🙌 Agradecimientos

- OpenAI por las capacidades de análisis basadas en modelos de lenguaje.
- Los colaboradores de la familia de fuentes Google Noto por el soporte de renderizado multilingüe.

## Licencia

Apache License 2.0  
Consulta [LICENSE](LICENSE) para ver los términos completos.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
