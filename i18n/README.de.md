[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

Ein Tool zur Analyse von Wortetymologien und zur Visualisierung als interaktive Graphen.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

<a id="overview"></a>
## Überblick

WordOrigins ist eine Python-Webanwendung, mit der du die Etymologie (Herkunft und historische Entwicklung) von Wörtern erkunden kannst. Sie liefert eine detaillierte Analyse, wie sich Wörter im Laufe der Zeit entwickelt haben, zerlegt sie in ihre Bestandteile, verfolgt rekursiv die sprachliche Abstammung jedes Teils und rendert das Ergebnis als Graphbild zur Anzeige im Browser.

### ✨ Hauptfunktionen

- Detaillierte Etymologieanalyse für beliebige Wörter
- Visuelle Graphdarstellung der Wortherkunft
- Unterstützung mehrerer Sprachen, darunter Englisch, Französisch, Arabisch, Japanisch und Chinesisch
- Interaktive Weboberfläche zur Erkundung

<a id="features"></a>
## Funktionen

| Funktion | Details |
|---|---|
| 🔎 Web-UI | Suche und Durchsuchen erzeugter Etymologie-Graphen |
| 🧠 OpenAI-gestützte Analyse | Verwendet die OpenAI API, um strukturierte Etymologie-Ausgaben zu erzeugen |
| 💾 Caching | Zwischenspeicherung von OpenAI-Antworten als JSON-Snapshots mit Zeitstempel |
| 🖼️ Artefakt-Erzeugung | Zwischengespeicherte JSON- und PNG-Artefakte für zuvor analysierte Wörter |
| 🌍 Mehrsprachiges Rendering | CJK- und Arabisch-Schriftunterstützung im Repository gebündelt |
| ↔️ Navigation | Weiter-/Zurück-Navigation durch erzeugte Wortbilder |
| 🔌 API-Unterstützung | Endpunkt liefert PNG-Ausgabe als Base64 |

## So funktioniert es

1. Gib ein Wort ein, das du analysieren möchtest.
2. Das System verbindet sich mit der OpenAI API, um eine tiefgehende Etymologieanalyse durchzuführen.
3. Der Analyzer validiert/parst die Modellausgabe in strukturiertes JSON.
4. Ergebnisse werden zwischengespeichert und in einen gerichteten Graphen umgewandelt.
5. Der Graph wird als PNG gerendert und in der Weboberfläche angezeigt.
6. Du kannst durch zuvor analysierte Wörter blättern.

## Projektstruktur

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

<a id="prerequisites"></a>
## Voraussetzungen

- Python 3.8+
- OpenAI API key
- Benötigte Schriften (im Repository enthalten):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Setup

1. Repository klonen:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. Deinen OpenAI API key als Umgebungsvariable setzen:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Hinweise zu Abhängigkeiten

Der Code importiert diese Pakete zur Laufzeit:
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Annahme: `requirements.txt` sollte die oben genannten Pakete enthalten. Falls `requirements.txt` in deiner lokalen Kopie fehlt, installiere sie manuell.

## Nutzung

### Webanwendung starten

Starte den Tornado-Webserver:

```bash
python app.py
```

Öffne anschließend im Browser `http://localhost:7788`.

### Typischer Ablauf

1. Öffne `http://localhost:7788`.
2. Gib ein Wort in das Suchfeld ein.
3. Die App analysiert das Wort und rendert den Etymologie-Graphen.
4. Nutze Zurück/Weiter, um durch erzeugte Wörter zu blättern.

<a id="api-endpoints"></a>
### API-Endpunkte

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Erzeugt und zeigt den Etymologie-Graphen für ein Wort |
| `GET` | `/word/next-word` | Zum nächsten Wort in der Liste navigieren |
| `GET` | `/word/prev-word` | Zum vorherigen Wort in der Liste navigieren |
| `GET/POST` | `/get_word_etymology/{word}` | API-Endpunkt, um Etymologie-Daten als Base64-PNG-Payload zu erhalten |

### Beispiel-API-Aufrufe

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Konfiguration

### Umgebungsvariablen

- `OPENAI_API_KEY` (required): API key used by the OpenAI Python client
- `OPENAI_MODEL` (optional): model name used by analyzer (defaults to `gpt-4-0125-preview`)

### Laufzeitverzeichnisse, die von der App erstellt/verwendet werden

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Komponenten

### WordEtymologyAnalyzer

Stellt eine Verbindung zur OpenAI API her, um detaillierte Etymologieinformationen für ein gegebenes Wort abzurufen. Enthält Caching- und Retry-Logik:

- Konvertiert Eingabewörter in Kleinbuchstaben
- Versucht JSON-Ausgaben robust zu parsen (`json5`)
- Speichert Analyse-Snapshots mit Zeitstempel in `word_etymology_analysis/`
- Protokolliert verarbeitete Wörter in `processed_words.csv`

<a id="etymologygraph"></a>
### EtymologyGraph

Erstellt visuelle Darstellungen von Etymologie-Daten mit NetworkX und Matplotlib:

- Bildet verschachtelte Etymologie rekursiv in gerichtete Graphknoten/-kanten ab
- Berechnet tiefenbasierte radiale Positionierung
- Zeichnet Beschriftungen für Teil/Bedeutung/Beispiel sowie Sprachkanten
- Unterstützt mehrsprachiges Text-Rendering mit den gebündelten Schriften

### Webanwendung

Ein Tornado-basierter Webserver, der Anfragen verarbeitet und die Benutzeroberfläche ausliefert:

- Leitet `/` auf `/word/etymology` um
- Rendert Wortgraphen aus `static/images/`
- Erzeugt fehlende Analysen/Bilder bei Bedarf

## Beispiele

### Ein neues Wort analysieren

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Erwartete Ausgaben nach dem ersten Lauf:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Vorhandene erzeugte Wörter durchsuchen

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technische Details

- Die Anwendung speichert JSON-Dateien analysierter Wörter zum Caching.
- Bilder werden als PNG-Dateien erzeugt.
- Für mehrsprachige Unterstützung ist eine spezielle Schriftbehandlung implementiert.
- Das Graph-Layout wird auf Basis von Knotentiefe und Beziehungen berechnet.
- Das bestehende Repository enthält explorative Notebooks und archivierte Artefakte aus der Entwicklung.

## Hinweise zur Entwicklung

- Der primäre Laufzeit-Einstiegspunkt ist `app.py`.
- Notebook-Dateien (`etymology*.ipynb`) sind experimentell und können vom Produktions-Serverfluss abweichen.
- Es gibt Legacy-/Duplikatpfade (`statics/` vs `static/`, `.old`-Dateien), die aus historischem Kontext beibehalten werden.
- Die aktuelle `.gitignore` scheint ungelöste Merge-Conflict-Marker zu enthalten; dies vor Release-Packaging bereinigen.

## Fehlerbehebung

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` on startup | Install missing dependencies: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` error or authentication failure | Ensure `OPENAI_API_KEY` is exported in the same shell session where you launch `python app.py` |
| Graph text renders as boxes or missing glyphs | Verify bundled font files are present in expected repository paths |
| No image generated for a word | Check server logs for JSON parse retries/exceptions and confirm network/API access |
| `pip install -r requirements.txt` fails because file is missing | Create a local dependency file from the package list in this README or install packages directly |

## Roadmap

- Unterstützung für weitere Sprachen hinzufügen.
- Benutzerkonten implementieren, um bevorzugte Etymologien zu speichern.
- Graphvisualisierung mit Zoom und Schwenken verbessern.
- Detailliertere linguistische Informationen ergänzen.
- Ein gepflegtes Abhängigkeits-Manifest und reproduzierbares Environment-Setup hinzufügen.
- Tests für Analyzer-Parsing, Caching-Verhalten und Route-Handler ergänzen.

## Beitrag

Beiträge sind willkommen. Empfohlener Ablauf:

1. Fork des Repositorys erstellen.
2. Einen Feature-Branch anlegen.
3. Fokussierte, gut reviewbare Änderungen umsetzen.
4. Durch Ausführen von `python app.py` und Prüfen zentraler Routen validieren.
5. Einen Pull Request mit klarer Beschreibung und, falls relevant, Screenshots/API-Beispielen öffnen.

## Abhängigkeiten

- tornado: Webserver-Framework
- openai: OpenAI API-Client
- matplotlib: Zur Grapherzeugung
- networkx: Für die Graph-Datenstruktur
- PIL/Pillow: Für Bildverarbeitung
- numpy: Für numerische Operationen
- cjkwrap: Für CJK-Textumbruch
- json5: Für robustes JSON-Parsing

## Lizenz

Apache License 2.0

Siehe [LICENSE](LICENSE) für die vollständigen Bedingungen.

## Danksagungen

- OpenAI für die Bereitstellung der linguistischen Analysefunktionen
- Google-Noto-Schriften für mehrsprachige Textunterstützung
