[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

Una herramienta para analizar etimologías de palabras y visualizarlas como grafos interactivos.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisitos)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#descripción-general)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#endpoints-de-api)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#funcionalidades)

![Word Origins Demo](word_origins.jpg)

## Descripción general

WordOrigins es una aplicación web en Python que te permite explorar la etimología (origen y evolución histórica) de las palabras. Ofrece un análisis detallado de cómo evolucionaron las palabras con el tiempo, las descompone en sus partes constituyentes, rastrea de forma recursiva la procedencia lingüística de cada parte y muestra el resultado como una imagen de grafo en el navegador.

### ✨ Funcionalidades clave

- Análisis etimológico detallado de cualquier palabra
- Representación visual en grafo del origen de las palabras
- Soporte para varios idiomas, incluidos inglés, francés, árabe, japonés y chino
- Interfaz web interactiva para explorar

## Funcionalidades

| Funcionalidad | Detalles |
|---|---|
| 🔎 Interfaz web | Busca y navega por los grafos etimológicos generados |
| 🧠 Análisis respaldado por OpenAI | Usa la API de OpenAI para producir salidas etimológicas estructuradas |
| 💾 Caché | Respuestas de OpenAI en caché como instantáneas JSON con marca temporal |
| 🖼️ Generación de artefactos | Artefactos JSON y PNG en caché para palabras analizadas previamente |
| 🌍 Renderizado multilingüe | Soporte de fuentes CJK + árabe incluido en el repositorio |
| ↔️ Navegación | Navegación siguiente/anterior entre imágenes de palabras generadas |
| 🔌 Soporte de API | Endpoint que devuelve salida PNG como base64 |

## Cómo funciona

1. Introduce la palabra que quieres analizar.
2. El sistema se conecta a la API de OpenAI para realizar un análisis etimológico profundo.
3. El analizador valida/parsea la salida del modelo en JSON estructurado.
4. Los resultados se almacenan en caché y se transforman en un grafo dirigido.
5. El grafo se renderiza como PNG y se muestra en la interfaz web.
6. Puedes navegar por palabras analizadas previamente.

## Estructura del proyecto

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Punto de entrada del servidor web Tornado
├─ word_etymology_analyzer.py          # Análisis etimológico con OpenAI + caché
├─ etymology_graph.py                  # Generación de grafos con NetworkX + Matplotlib
├─ utils.py                            # Utilidades auxiliares de imagen/textura
├─ templates/
│  ├─ index.html                       # Interfaz principal
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Salidas PNG renderizadas principales
├─ statics/
│  └─ images/                          # Carpeta heredada duplicada de imágenes
├─ jsons/                              # Artefactos JSON e imagen por palabra
├─ word_etymology_analysis/            # Caché de respuestas del modelo con marca temporal
├─ processed_words.csv                 # Registro de palabras procesadas
├─ i18n/                               # Reservado para README/docs multilingües
├─ archived_code/                      # Notebooks/código históricos
├─ archived_data/                      # Salidas JSON históricas
├─ etymology*.ipynb                    # Experimentos en notebooks
├─ Noto Sans CJK Regular/              # Fuente CJK incluida
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # Familias de fuentes árabe + Noto incluidas
└─ arial-unicode-ms.ttf                # Fuente con soporte Unicode
```

## Prerequisitos

- Python 3.8+
- Clave de API de OpenAI
- Fuentes requeridas (incluidas en el repositorio):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Instalación

### Configuración

1. Clona el repositorio:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Define tu clave de API de OpenAI como variable de entorno:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notas sobre dependencias

El código importa estos paquetes en tiempo de ejecución:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Suposición: `requirements.txt` debería incluir los paquetes anteriores. Si `requirements.txt` falta en tu copia local, instálalos manualmente.

## Uso

### Ejecutar la aplicación web

Inicia el servidor web Tornado:

```bash
python app.py
```

Luego abre tu navegador y ve a `http://localhost:7788`.

### Flujo de usuario típico

1. Abre `http://localhost:7788`.
2. Introduce una palabra en la caja de búsqueda.
3. La app analiza y renderiza el grafo etimológico.
4. Usa los controles anterior/siguiente para navegar por palabras generadas.

### Endpoints de API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Genera y muestra el grafo etimológico de una palabra |
| `GET` | `/word/next-word` | Navega a la siguiente palabra de la lista |
| `GET` | `/word/prev-word` | Navega a la palabra anterior de la lista |
| `GET/POST` | `/get_word_etymology/{word}` | Endpoint de API para obtener datos etimológicos como payload PNG en base64 |

### Ejemplos de llamadas API

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuración

### Variables de entorno

- `OPENAI_API_KEY` (obligatoria): clave API usada por el cliente Python de OpenAI
- `OPENAI_MODEL` (opcional): nombre del modelo usado por el analizador (por defecto `gpt-4-0125-preview`)

### Directorios de ejecución creados/usados por la app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Componentes

### WordEtymologyAnalyzer

Se conecta a la API de OpenAI para obtener información etimológica detallada de una palabra. Incluye lógica de caché y reintentos:

- Convierte las palabras de entrada a minúsculas
- Intenta parsear salida JSON de forma robusta (`json5`)
- Guarda instantáneas de análisis con marca temporal en `word_etymology_analysis/`
- Registra palabras procesadas en `processed_words.csv`

### EtymologyGraph

Crea representaciones visuales de datos etimológicos usando NetworkX y Matplotlib:

- Mapea recursivamente etimologías anidadas en nodos/aristas de grafo dirigido
- Calcula posicionamiento radial basado en profundidad
- Dibuja etiquetas de parte/significado/ejemplo y etiquetas de idioma en aristas
- Gestiona renderizado de texto multilingüe con fuentes incluidas

### Aplicación web

Un servidor web basado en Tornado que maneja solicitudes y sirve la interfaz de usuario:

- Redirige `/` a `/word/etymology`
- Renderiza grafos de palabras desde `static/images/`
- Genera análisis/imágenes faltantes bajo demanda

## Ejemplos

### Analizar una palabra nueva

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Salidas esperadas tras la primera ejecución:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Explorar palabras ya generadas

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Detalles técnicos

- La aplicación almacena archivos JSON de palabras analizadas para caché.
- Las imágenes se generan como archivos PNG.
- Se implementa manejo especial de fuentes para soporte multilingüe.
- El layout del grafo se calcula según profundidad de nodos y relaciones.
- El repositorio actual incluye notebooks exploratorios y artefactos archivados usados durante el desarrollo.

## Notas de desarrollo

- El punto de entrada principal en ejecución es `app.py`.
- Los archivos notebook (`etymology*.ipynb`) son experimentales y pueden divergir del flujo del servidor de producción.
- Hay rutas heredadas/duplicadas (`statics/` vs `static/`, archivos `.old`) mantenidas por contexto histórico.
- El `.gitignore` actual parece contener marcadores de conflicto de merge sin resolver; límpialo antes del empaquetado de release.

## Resolución de problemas

| Problema | Resolución |
|---|---|
| `ModuleNotFoundError` al iniciar | Instala dependencias faltantes: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Error de `OPENAI_API_KEY` o fallo de autenticación | Asegúrate de exportar `OPENAI_API_KEY` en la misma sesión de shell donde ejecutas `python app.py` |
| El texto del grafo aparece como cajas o faltan glifos | Verifica que los archivos de fuentes incluidos estén presentes en las rutas esperadas del repositorio |
| No se genera imagen para una palabra | Revisa logs del servidor para reintentos/excepciones de parseo JSON y confirma acceso de red/API |
| `pip install -r requirements.txt` falla porque falta el archivo | Crea un archivo local de dependencias con la lista de paquetes de este README o instala los paquetes directamente |

## Hoja de ruta

- Añadir soporte para más idiomas.
- Implementar cuentas de usuario para guardar etimologías favoritas.
- Mejorar la visualización del grafo con zoom y paneo.
- Añadir información lingüística más detallada.
- Añadir un manifiesto de dependencias mantenido y configuración de entorno reproducible.
- Añadir tests para parseo del analizador, comportamiento de caché y handlers de rutas.

## Contribución

Las contribuciones son bienvenidas. Flujo de trabajo sugerido:

1. Haz fork del repositorio.
2. Crea una rama de funcionalidad.
3. Realiza cambios enfocados y fáciles de revisar.
4. Valida ejecutando `python app.py` y comprobando rutas clave.
5. Abre un pull request con una descripción clara y capturas/API samples cuando aplique.

## Dependencias

- tornado: Framework de servidor web
- openai: Cliente de API de OpenAI
- matplotlib: Para generar grafos
- networkx: Para estructura de datos de grafos
- PIL/Pillow: Para procesamiento de imágenes
- numpy: Para operaciones numéricas
- cjkwrap: Para manejo de ajuste de línea en texto CJK
- json5: Para parseo JSON robusto

## Licencia

Apache License 2.0

Consulta [LICENSE](LICENSE) para los términos completos.

## Agradecimientos

- OpenAI por proporcionar las capacidades de análisis lingüístico
- Fuentes Google Noto por el soporte de texto multilingüe
