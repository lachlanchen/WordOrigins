[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Opciones de idioma:** Español (este archivo)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

Una herramienta para analizar etimologías de palabras y visualizarlas como grafos interactivos.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Resumen rápido

| Área | Detalles |
|---|---|
| 🌐 Acceso | Interfaz web para exploración interactiva y API para salida de PNG en base64 |
| 🧠 Inteligencia | Análisis etimológico con OpenAI y parseado de JSON estructurado |
| 🧰 Reproducibilidad | JSON + artefactos PNG en caché para cada palabra procesada |
| 🌍 Soporte de idioma | Renderizado multilingüe para CJK y árabe con fuentes incluidas |

## Visión general

WordOrigins es una aplicación web en Python que te permite explorar la etimología (origen y desarrollo histórico) de palabras. Proporciona un análisis detallado de cómo evolucionaron con el tiempo, descompone cada palabra en sus componentes, rastrea recursivamente la genealogía lingüística de cada parte y muestra el resultado como imagen de grafo en el navegador.

### ✨ Funciones principales

- Análisis etimológico detallado de cualquier palabra
- Representación visual en grafo de orígenes de palabras
- Soporte para múltiples idiomas, incluyendo inglés, francés, árabe, japonés y chino
- Interfaz web interactiva para explorar resultados

## Funciones

| Función | Detalles |
|---|---|
| 🔎 Interfaz web | Buscar y navegar gráficos de etimología generados |
| 🧠 Análisis con OpenAI | Usa la API de OpenAI para producir salida etimológica estructurada |
| 💾 Caché | Respuestas en caché de OpenAI como instantáneas JSON con marca temporal |
| 🖼️ Generación de artefactos | JSON y PNG en caché para palabras analizadas previamente |
| 🌍 Renderizado multilingüe | Soporte de fuentes para CJK + árabe incluido en el repositorio |
| ↔️ Navegación | Avance y retroceso por las imágenes de palabras generadas |
| 🔌 Soporte de API | Endpoint que devuelve salida PNG en base64 |

## Cómo funciona

1. Introduce la palabra que quieres analizar.
2. El sistema se conecta a la API de OpenAI para realizar un análisis etimológico profundo.
3. El analizador valida y analiza la salida del modelo a JSON estructurado.
4. Los resultados se almacenan en caché y se transforman en un grafo dirigido.
5. El grafo se renderiza como PNG y se muestra en la interfaz web.
6. Puedes navegar palabras analizadas anteriormente.

## Estructura del proyecto

```text
WordOrigins/
├─ README.md
├─ LICENSE
├─ app.py                              # Punto de entrada del servidor Tornado
├─ word_etymology_analyzer.py          # Análisis etimológico con OpenAI + caché
├─ etymology_graph.py                  # Generación de grafos con NetworkX + Matplotlib
├─ utils.py                            # Utilidades para imágenes/texturas
├─ templates/
│  ├─ index.html                       # Interfaz principal
│  ├─ index.html.old                   # Variante heredada de plantilla
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Salidas PNG renderizadas
├─ statics/
│  └─ images/                          # Carpeta de imágenes duplicada por herencia
├─ jsons/                              # Artefactos JSON e imagen por palabra
├─ word_etymology_analysis/            # Caché de respuestas del modelo con marca temporal
├─ processed_words.csv                  # Registro de palabras procesadas
├─ i18n/                               # Archivos README/docs multilingües
├─ archived_code/                      # Cuadernos/código histórico
├─ archived_data/                      # Salidas JSON históricas
├─ etymology*.ipynb                    # Experimentos en notebook
├─ Noto Sans CJK Regular/              # Fuente CJK incluida
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/         # Familias de fuentes árabes + Noto incluidas
└─ arial-unicode-ms.ttf                # Fuente compatible con Unicode
```

## Requisitos previos

- Python 3.8+
- Clave de API de OpenAI
- Fuentes requeridas (incluidas en el repositorio):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Instalación

### Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar tu clave de OpenAI como variable de entorno:
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

Suposición: `requirements.txt` debería incluir los paquetes anteriores. Si `requirements.txt` no existe en tu copia local, instala estos paquetes manualmente.

## Uso

### Ejecutar la aplicación web

Iniciar el servidor web de Tornado:

```bash
python app.py
```

Luego abre tu navegador y ve a `http://localhost:7788`.

### Flujo típico de usuario

1. Abre `http://localhost:7788`.
2. Escribe una palabra en la barra de búsqueda.
3. La aplicación analiza y renderiza el grafo etimológico.
4. Usa los controles anterior/siguiente para navegar palabras generadas.

### Endpoints de API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Genera y muestra el grafo etimológico de una palabra |
| `GET` | `/word/next-word` | Navega a la siguiente palabra en la lista |
| `GET` | `/word/prev-word` | Navega a la palabra anterior en la lista |
| `GET/POST` | `/get_word_etymology/{word}` | Endpoint de API para obtener datos etimológicos como carga base64 PNG |

### Ejemplos de llamadas API

```bash
# Generar/mostrar una palabra en el navegador
curl "http://localhost:7788/word/etymology"

# Obtener la imagen base64
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuración

### Variables de entorno

- `OPENAI_API_KEY` (obligatoria): clave usada por el cliente de Python de OpenAI
- `OPENAI_MODEL` (opcional): nombre de modelo usado por el analizador (por defecto `gpt-4-0125-preview`)

### Directorios de ejecución creados/usados por la app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Componentes

### WordEtymologyAnalyzer

Se conecta a la API de OpenAI para obtener información etimológica detallada para una palabra dada. Incluye lógica de caché y reintentos:

- Normaliza palabras de entrada y convierte a minúsculas
- Intenta parsear la salida JSON de forma robusta (`json5`)
- Guarda instantáneas de análisis con marca temporal en `word_etymology_analysis/`
- Registra las palabras procesadas en `processed_words.csv`

### EtymologyGraph

Crea representaciones visuales de datos etimológicos con NetworkX y Matplotlib:

- Mapea recursivamente la etimología anidada en nodos y bordes de grafo dirigido
- Calcula posiciones radiales según la profundidad
- Dibuja etiquetas de parte/significado/ejemplo y bordes de idioma
- Gestiona el renderizado multilingüe con fuentes incluidas

### Aplicación web

Un servidor web basado en Tornado que gestiona solicitudes y sirve la interfaz de usuario:

- Redirige `/` a `/word/etymology`
- Renderiza grafos de palabras desde `static/images/`
- Genera análisis/imágenes faltantes bajo demanda

## Ejemplos

### Analizar una palabra nueva

```bash
python app.py
# luego abre http://localhost:7788/word/revolution
```

Resultados esperados tras la primera ejecución:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Navegar palabras existentes ya generadas

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Detalles técnicos

- La aplicación guarda archivos JSON de palabras analizadas para caché.
- Las imágenes se generan como archivos PNG.
- Se implementa manejo especial de fuentes para el soporte multilingüe.
- El diseño del grafo se calcula según la profundidad de nodos y relaciones.
- El repositorio actual incluye notebooks exploratorios y artefactos archivados usados durante el desarrollo.

## Notas de desarrollo

- El punto de entrada principal en tiempo de ejecución es `app.py`.
- Los archivos de notebook (`etymology*.ipynb`) son experimentales y pueden diferir del flujo del servidor de producción.
- Hay rutas duplicadas/legadas (`statics/` frente a `static/`, archivos `.old`) conservadas por contexto histórico.
- El `.gitignore` actual parece contener marcadores de conflicto sin resolver; límpialo antes de empaquetar para publicación.

## Solución de problemas

| Problema | Resolución |
|---|---|
| `ModuleNotFoundError` al iniciar | Instala las dependencias que faltan: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Error de `OPENAI_API_KEY` o fallo de autenticación | Asegúrate de exportar `OPENAI_API_KEY` en la misma sesión de terminal desde la que ejecutas `python app.py` |
| El texto del grafo aparece como cuadros o falta de glifos | Verifica que los archivos de fuente incluidos estén presentes en las rutas esperadas del repositorio |
| No se genera imagen para una palabra | Revisa los registros del servidor por reintentos/excepciones del parseo JSON y confirma el acceso a red/API |
| `pip install -r requirements.txt` falla porque falta el archivo | Crea un fichero local de dependencias desde la lista de paquetes de este README o instala los paquetes directamente |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Hoja de ruta

- Añadir soporte para más idiomas.
- Implementar cuentas de usuario para guardar etimologías favoritas.
- Mejorar la visualización de grafos con zoom y paneo.
- Añadir información lingüística más detallada.
- Añadir un manifiesto de dependencias mantenido y un entorno reproducible.
- Añadir pruebas para el parseo del analizador, comportamiento de caché y controladores de rutas.

## Contribución

Las contribuciones son bienvenidas. Flujo sugerido:

1. Haz un fork del repositorio.
2. Crea una rama de características.
3. Realiza cambios focalizados y revisables.
4. Valida ejecutando `python app.py` y comprobando rutas clave.
5. Abre un pull request con una descripción clara y capturas/API relevantes cuando aplique.

## Dependencias

- tornado: Framework de servidor web
- openai: Cliente de API de OpenAI
- matplotlib: Para generar grafos
- networkx: Para estructura de datos de grafos
- PIL/Pillow: Para procesamiento de imágenes
- numpy: Para operaciones numéricas
- cjkwrap: Para envoltura de texto de CJK
- json5: Para parseo robusto de JSON

## Agradecimientos

- OpenAI por proporcionar las capacidades de análisis lingüístico
- Google Noto por las fuentes para soporte multilingüe

## Licencia

Apache License 2.0

Ver [LICENSE](LICENSE) para ver los términos completos.
