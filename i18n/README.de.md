[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Visualisieren Sie die Herkunft von Wörtern als mehrsprachige Provenienz-Graphen in einem OpenAI-gestützten, cache-freundlichen Workflow.

**Sprachoptionen:** Englisch (diese Datei)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#voraussetzungen)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#bestandteile)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](#lizenz)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpunkte)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#funktionen)
[![GitHub last commit](https://img.shields.io/github/last-commit/lachlanchen/WordOrigins?color=blue)](https://github.com/lachlanchen/WordOrigins/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/lachlanchen/WordOrigins?color=red)](https://github.com/lachlanchen/WordOrigins/issues)
[![GitHub repo size](https://img.shields.io/github/repo-size/lachlanchen/WordOrigins?color=yellow)](https://github.com/lachlanchen/WordOrigins)

![Word Origins Demo](word_origins.jpg)

## 📘 Übersicht

WordOrigins ist eine Python-Web-Anwendung zur Analyse der Wortherkunft und zur Visualisierung sprachlicher Abstammung als gerichteten Graphen. Es kombiniert:

- Eine Tornado-Webanwendung.
- OpenAI-gestützte etymologische Analyse.
- Strukturierte JSON-Verarbeitung mit robuster Fallback-Logik.
- Graphenerstellung via NetworkX + Matplotlib.
- Zwischengespeicherte Ausgaben für schnelle Wiederholungsanalysen.

Es stellt sowohl eine Browseroberfläche als auch API-Endpunkte zum Generieren und Abrufen etymologischer Artefakte bereit.

## 📸 Kurzübersicht

| Bereich | Details |
|---|---|
| 🌐 Zugriff | Web-UI für interaktive Erkundung und API für Base64-PNG-Ausgabe |
| 🧠 Intelligenz | OpenAI-gestützte etymologische Analyse mit strukturierter JSON-Verarbeitung |
| 🧰 Reproduzierbarkeit | Getaktete JSON- und PNG-Artefakte für jedes verarbeitete Wort |
| 🌍 Sprachunterstützung | Mehrsprachige Darstellung für CJK- und Arabisch-Texte mit gebündelten Schriftarten |

## Funktionen

| Funktion | Details |
|---|---|
| 🔎 Web-UI | Suche und Durchsuchen erzeugter Etymologie-Graphen |
| 🧠 OpenAI-gestützte Analyse | Nutzt die OpenAI-API, um strukturierte etymologische Ausgaben zu erzeugen |
| 💾 Caching | Speichert Antworten mit mit Zeitstempel versehenen JSON-Snapshots |
| 🖼️ Artefakterstellung | Exportiert JSON- und PNG-Artefakte für verarbeitete Wörter |
| 🌍 Mehrsprachiges Rendering | CJK + Arabisch mit im Repository enthaltenen Schriftarten |
| ↔️ Navigation | Vorwärts-/Rückwärtsnavigation durch generierte Wortbilder |
| 🔌 API-Support | Endpunkt liefert PNG-Ausgabe als Base64-JSON-Payload |

## 🛠️ Funktionsweise

1. Der Nutzer übermittelt ein Wort über `/word/{word}` oder das Web-Suchformular.
2. Der Analysator ruft OpenAI auf und validiert die Antwortstruktur.
3. Die analysierten Daten werden normalisiert und zur Cache-Nutzung gespeichert.
4. Etymologische Beziehungen werden in Graph-Knoten und -Kanten umgewandelt.
5. NetworkX und Matplotlib rendern einen gerichteten Graphen als PNG.
6. UI und API stellen den gecachten Bildpfad und zugehörige Metadaten bereit.

## 🗂️ Projektstruktur

```text
WordOrigins/
├─ app.py                     # Tornado web app (aktueller Einstiegspunkt)
├─ app.py.old                 # Ältere App-Variante
├─ word_etymology_analyzer.py # OpenAI-gestützte Analyse + Retry-/Caching-Logik
├─ etymology_graph.py         # Graphaufbau und PNG-Rendering
├─ utils.py                   # Bild-/Schriftart-/Hilfsfunktionen
├─ templates/
│  ├─ index.html              # Haupt-Web-UI
│  ├─ index.html.old          # Ältere Template-Variante
│  └─ carousel_items.html     # Wiederverwendbares UI-Fragment
├─ static/
│  └─ images/                 # Primäre Laufzeit-PNG-Ausgaben
├─ statics/
│  └─ images/                 # Veralteter doppelter Bildordner
├─ images/                    # Screenshot-/Demo-Dateien
├─ jsons/                     # JSON pro Wort + gecachte Daten
├─ word_etymology_analysis/   # Cache mit zeitgestempelten Modellantworten
├─ processed_words.csv         # Index verarbeiteter Wörter
├─ i18n/                      # Übersetzte README-Dateien
├─ archived_code/             # Historische Notebooks und Skripte
├─ archived_data/             # Historische JSON-Snapshots
├─ Noto Sans CJK Regular/     # Gebündelte Schriftarten
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/
├─ arial-unicode-ms.ttf       # Gebündelte Unicode-Schriftart
├─ etymology*.ipynb           # Entwicklungsnotebooks
├─ LICENSE
└─ .auto-readme-work/         # Pipeline-Artefakte
```

## Voraussetzungen

- Python 3.8+
- OpenAI API-Anmeldedaten:
  - `OPENAI_API_KEY` (erforderlich)
  - `OPENAI_MODEL` (optional, standardmäßig `gpt-4-0125-preview` nach bestehender Anleitung)
- Schriftdateien im Repository, sofern Mehrsprachigkeit benötigt wird

## 🧰 Installation

1. Repository klonen.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Python-Umgebung erstellen und aktivieren (empfohlen).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Laufzeitbibliotheken installieren.

   Da im Repository kein Root-Dependency-Manifest existiert, installieren Sie die bekannten Laufzeitanforderungen direkt:

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Zugangsdaten konfigurieren.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # optionale Überschreibung
   ```

## 🚀 Nutzung

### Web-App starten

```bash
python app.py
```

Öffnen Sie `http://localhost:7788` im Browser.

### Typischer Nutzerfluss

1. Öffnen Sie `http://localhost:7788/word/etymology`.
2. Geben Sie ein Wort ein.
3. Warten Sie auf die Analyse (der erste Lauf kann wegen externer API-Latenz länger dauern).
4. Erkunden Sie den generierten Graphen und zugehörige Metadaten.
5. Nutzen Sie Vorwärts-/Rückwärts-Navigation, um zwischengespeicherte Wörter durchzublättern.

### API-Endpunkte

| Methode | Endpunkt | Beschreibung |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Rendert eine Seite für die gewünschte Etymologie |
| `GET` | `/word/next-word?word={word}` | Zum nächsten Wort im Cache navigieren |
| `GET` | `/word/prev-word?word={word}` | Zum vorherigen Wort im Cache navigieren |
| `GET/POST` | `/get_word_etymology/{word}` | Gibt einen JSON-Body mit Base64-PNG-Payload zurück |

### Beispielhafte API-Aufrufe

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Konfiguration

- `OPENAI_API_KEY` (erforderlich): Zugriffsdaten für Analyseanfragen.
- `OPENAI_MODEL` (optional): Modellüberschreibung für den Analysator.
- Laufzeitverzeichnisse, die vom Dienst genutzt werden:
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Beispiele

```bash
python app.py
```

Danach öffnen Sie:

```text
http://localhost:7788/word/revolution
```

Artefakte, die bei der Erstanalyse erzeugt werden:

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Bestandteile

### WordEtymologyAnalyzer

In `word_etymology_analyzer.py` definiert, diese Komponente:

- Normalisiert Eingabewörter.
- Ruft OpenAI für strukturierte etymologische Antworten auf.
- Extrahiert/ repariert JSON-Payloads mit `json5`.
- Wiederholt fehlgeschlagene Parse-Versuche und protokolliert Fehler für Robustheit.
- Schreibt zeitgestempelte Snapshots nach `word_etymology_analysis/`.
- Aktualisiert den `processed_words.csv`-Index.

### EtymologyGraph

In `etymology_graph.py` definiert, diese Komponente:

- Lädt strukturierte etymologische JSON-Daten.
- Erstellt einen `networkx.DiGraph` mit rekursiven Abstammungsbeziehungen.
- Berechnet tiefenbasierte Graph-Koordinaten.
- Rendert beschriftete Knoten und Kanten mit mehrsprachiger Textbehandlung.
- Speichert `PNG`-Bilder für Caching und Darstellung.

### Webanwendung

In `app.py`, die Tornado-App:

- Verarbeitet Root-Weiterleitung und Suchseiten-Verhalten.
- Handhabt Erstellungs- und Cache-Lookup-Workflows.
- Stellt Seiten- und API-Routen unter `/word/...` und `/get_word_etymology/...` bereit.
- Gibt JSON-Payloads mit Base64-Bilddaten für API-Verbraucher zurück.

## 📦 Abhängigkeiten

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Entwicklungshinweise

- JSON- und Bild-Caching verhindert unnötig wiederholte API-Aufrufe.
- `index.html` und `index.html.old` werden aus Kompatibilitäts-/Historiegründen beibehalten.
- Legacy-Verzeichnisse und Artefakte sind derzeit bewusst vorhanden (`statics/`, Notebooks, Archive).
- Eine `.gitignore`-Datei mit Merge-Konfliktmarkierungen wurde als übergeordnetes Hygiene-Problem außerhalb des README-Kontexts festgestellt.

## 🧯 Fehlerbehebung

| Problem | Lösung |
|---|---|
| `ModuleNotFoundError` beim Start | Fehlende Pakete mit `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` installieren |
| Authentifizierungsfehler bei `OPENAI_API_KEY` | Stellen Sie sicher, dass die Variable im selben Shell-Session-Kontext exportiert ist, in dem `python app.py` läuft |
| Fehlende/verzerrte Glyphen in generierten Graphen | Vergewissern Sie sich, dass gebündelte Schriften (`Noto Sans`, Arabisch-Varianten, Arial Unicode MS) vorhanden und lesbar sind |
| Kein Bild für ein Wort vorhanden | Prüfen Sie die App-Logs auf JSON-Parsing-Fehler oder vorübergehende API-Fehler |
| `pip install -r requirements.txt` schlägt fehl/existiert nicht | Abhängigkeiten direkt wie oben installieren (aktuelles Repo enthält kein Root-Manifest) |

## 🗺️ Roadmap

- Unterstützung für weitere Sprachen hinzufügen.
- Nutzerkonten für bevorzugte Etymologien ergänzen.
- Graph-Navigation um Zoom-/Pan-Interaktionen verbessern.
- Sprachliche Metadaten in jedem Graphknoten anreichern.
- Ein gepflegtes Abhängigkeitsmanifest und reproduzierbaren Umgebungspaketaufbau ergänzen.
- Tests für Analyzer-Parsing, Cache-Verhalten und Routenhandler hinzufügen.

## 🤝 Beitrag

1. Forken Sie das Repository.
2. Erstellen Sie einen Feature-Branch.
3. Nehmen Sie fokussierte, prüfbare Änderungen vor.
4. Validieren Sie die Änderungen mit `python app.py` und prüfen Sie die wichtigsten Routen.
5. Öffnen Sie eine PR mit reproduzierbaren Anweisungen sowie Screenshots/API-Beispielen.

## 🙌 Danksagungen

- OpenAI für analysefähige Sprachmodell-Funktionalität.
- Mitwirkenden der Google Noto Font-Familie für mehrsprachiges Rendering.

## Lizenz

Apache License 2.0  
Siehe [LICENSE](LICENSE) für die vollständigen Bedingungen.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
