[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Sprachoptionen:** Deutsch (diese Datei)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

Ein Tool zur Analyse von Wortetymologien und zur Visualisierung als interaktive Graphen.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Kurzübersicht

| Bereich | Details |
|---|---|
| 🌐 Zugriff | Web-UI für interaktive Erkundung und API für Base64-PNG-Ausgabe |
| 🧠 Intelligenz | OpenAI-gestützte Etymologieanalyse mit strukturierter JSON-Verarbeitung |
| 🧰 Reproduzierbarkeit | Zwischengespeicherte JSON- und PNG-Artefakte für jedes verarbeitete Wort |
| 🌍 Sprachunterstützung | Mehrsprachige Darstellung für CJK- und Arabisch-Texte mit enthaltenen Schriftarten |

<a id="overview"></a>
## Überblick

WordOrigins ist eine Python-Webanwendung, mit der du die Etymologie (Herkunft und historische Entwicklung) von Wörtern untersuchen kannst. Sie liefert eine detaillierte Analyse darüber, wie Wörter sich im Laufe der Zeit entwickelt haben, zerlegt sie in einzelne Bestandteile, verfolgt rekursiv die sprachliche Abstammung jedes Bestandteils und rendert das Ergebnis als Graphbild für die Anzeige im Browser.

### ✨ Hauptmerkmale

- Detaillierte Etymologieanalyse beliebiger Wörter
- Visuelle Graphendarstellung von Wortherkünften
- Unterstützung mehrerer Sprachen, darunter Englisch, Französisch, Arabisch, Japanisch und Chinesisch
- Interaktive Weboberfläche zur Erkundung

<a id="features"></a>
## Funktionen

| Merkmal | Details |
|---|---|
| 🔎 Web-UI | Suche und durchsuche generierte Etymologiegraphen |
| 🧠 OpenAI-gestützte Analyse | Verwendet die OpenAI API, um strukturierte Etymologie-Ausgaben zu erzeugen |
| 💾 Zwischenspeicherung | Gespeicherte OpenAI-Antworten als zeitgestempelte JSON-Snapshots |
| 🖼️ Artefakterstellung | Gespeicherte JSON- und PNG-Artefakte für bereits analysierte Wörter |
| 🌍 Mehrsprachiges Rendering | CJK- und Arabisch-Schriftunterstützung im Repository enthalten |
| ↔️ Navigation | Vorwärts-/Rückwärts-Navigation durch generierte Wortbilder |
| 🔌 API-Unterstützung | Endpunkt gibt PNG-Ausgabe als Base64 zurück |

## So funktioniert es

1. Gib ein Wort ein, das du analysieren möchtest.
2. Das System verbindet sich mit der API von OpenAI, um eine tiefgehende Etymologieanalyse durchzuführen.
3. Der Analyzer validiert/parst die Modellausgabe zu strukturiertem JSON.
4. Die Ergebnisse werden zwischengespeichert und in einen gerichteten Graphen umgewandelt.
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
│  ├─ index.html.old                   # Legacy template variant
│  └─ carousel_items.html
├─ static/
│  └─ images/                          # Primary rendered PNG outputs
├─ statics/
│  └─ images/                          # Legacy duplicate image folder
├─ jsons/                              # Per-word JSON and image artifacts
├─ word_etymology_analysis/            # Timestamped model response cache
├─ processed_words.csv                  # Processed word log
├─ i18n/                               # Multilingual README/docs files
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
- OpenAI-API-Schlüssel
- Erforderliche Schriften (im Repository enthalten):
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Einrichtung

1. Repository klonen:
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. OpenAI-API-Schlüssel als Umgebungsvariable setzen:
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

Annahme: In `requirements.txt` sollten die oben genannten Pakete enthalten sein. Wenn `requirements.txt` in deiner lokalen Kopie fehlt, installiere diese manuell.

## Nutzung

### Starten der Webanwendung

Starte den Tornado-Webserver:

```bash
python app.py
```

Öffne anschließend deinen Browser und navigiere zu `http://localhost:7788`.

### Typischer Benutzungsablauf

1. Öffne `http://localhost:7788`.
2. Gib ein Wort in das Suchfeld ein.
3. Die App analysiert und rendert den Etymologie-Graphen.
4. Nutze die Steuerung Vorherige/Nächste, um zwischen generierten Wörtern zu wechseln.

<a id="api-endpoints"></a>
### API-Endpunkte

| Methode | Endpunkt | Beschreibung |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Erzeugt und zeigt den Etymologiegraphen für ein Wort |
| `GET` | `/word/next-word` | Zum nächsten Wort in der Liste wechseln |
| `GET` | `/word/prev-word` | Zum vorherigen Wort in der Liste wechseln |
| `GET/POST` | `/get_word_etymology/{word}` | API-Endpunkt für Etymologiedaten als Base64-PNG-Payload |

### Beispielhafte API-Aufrufe

```bash
# Ein Wort im Browser erzeugen/anzeigen
curl "http://localhost:7788/word/etymology"

# Base64-Bild-Payload abrufen
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Konfiguration

### Umgebungsvariablen

- `OPENAI_API_KEY` (erforderlich): API-Schlüssel, der vom OpenAI-Python-Client verwendet wird
- `OPENAI_MODEL` (optional): Modellname, den der Analyzer nutzt (Standard: `gpt-4-0125-preview`)

### Laufzeitverzeichnisse, die von der App erstellt/verwendet werden

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Komponenten

### WordEtymologyAnalyzer

Verbindet sich mit der API von OpenAI, um für ein angegebenes Wort detaillierte Etymologieinformationen zu erhalten. Enthält Caching- und Wiederholungslogik:

- Setzt Eingabewörter in Kleinbuchstaben und normalisiert sie
- Versucht, JSON-Ausgaben robust zu parsen (`json5`)
- Speichert zeitgestempelte Analyse-Snapshots in `word_etymology_analysis/`
- Protokolliert verarbeitete Wörter in `processed_words.csv`

<a id="etymologygraph"></a>
### EtymologyGraph

Erstellt visuelle Darstellungen von Etymologiedaten mit NetworkX und Matplotlib:

- Bildet verschachtelte Etymologie rekursiv in gerichtete Graph-Knoten und -Kanten ab
- Berechnet eine tiefenbasierte radiale Positionierung
- Zeichnet Knoten-/Bedeutungs-/Beispielbeschriftungen sowie Sprach-Kantenbeschriftungen
- Unterstützt mehrsprachiges Text-Rendering mit den mitgelieferten Schriftarten

### Webanwendung

Ein Tornado-basierter Webserver, der Anfragen verarbeitet und die Benutzeroberfläche bereitstellt:

- Leitet `/` nach `/word/etymology` weiter
- Rendert Wortgraphen aus `static/images/`
- Erzeugt bei Bedarf fehlende Analysen/Bilder

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

### Bestehende generierte Wörter durchsuchen

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technische Details

- Die Anwendung speichert JSON-Dateien analysierter Wörter zum Caching.
- Bilder werden als PNG-Dateien erzeugt.
- Spezielle Schriftverarbeitung ist für die Mehrsprachigkeit implementiert.
- Das Graph-Layout wird anhand von Knotentiefe und Beziehungen berechnet.
- Das bestehende Repository enthält explorative Notebooks und archivierte Artefakte aus der Entwicklung.

## Entwicklungsnotizen

- Primärer Laufzeiteinstiegspunkt ist `app.py`.
- Notebook-Dateien (`etymology*.ipynb`) sind experimentell und können vom Produktionsfluss des Servers abweichen.
- Es gibt Legacy-/Doppelpfade (`statics/` vs `static/`, `.old`-Dateien), die aus historischem Kontext erhalten wurden.
- Die aktuelle `.gitignore` scheint ungelöste Merge-Conflict-Marker zu enthalten; bereinige dies vor der Release-Paketierung.

## Fehlerbehebung

| Problem | Lösung |
|---|---|
| `ModuleNotFoundError` beim Start | Fehlende Abhängigkeiten installieren: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY`-Fehler oder Authentifizierungsfehler | Stelle sicher, dass `OPENAI_API_KEY` in derselben Shell-Sitzung exportiert ist, in der du `python app.py` startest |
| Graph-Text wird als Kästchen angezeigt oder Glyphe fehlen | Stelle sicher, dass die mitgelieferten Schriftdateien an den erwarteten Repository-Pfaden vorhanden sind |
| Für ein Wort wird kein Bild erstellt | Prüfe die Server-Logs auf JSON-Parse-Wiederholungsversuche/Ausnahmen und prüfe Netzwerk-/API-Zugriff |
| `pip install -r requirements.txt` schlägt fehl, da die Datei fehlt | Erstelle eine lokale Abhängigkeitsdatei aus der Paketliste in dieser README oder installiere die Pakete direkt |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Roadmap

- Unterstützung für weitere Sprachen hinzufügen.
- Benutzerkonten implementieren, um bevorzugte Etymologien zu speichern.
- Graph-Visualisierung mit Zoom und Schwenken verbessern.
- Detailliertere linguistische Informationen hinzufügen.
- Ein gepflegtes Abhängigkeits-Manifest und eine reproduzierbare Umgebungskonfiguration ergänzen.
- Tests für Analyzer-Parsing, Cache-Verhalten und Route-Handler ergänzen.

## Beitrag

Beiträge sind willkommen. Vorgeschlagener Workflow:

1. Fork des Repositorys erstellen.
2. Einen Feature-Branch anlegen.
3. Konzentrierte, reviewbare Änderungen vornehmen.
4. Validiere durch Ausführen von `python app.py` und Überprüfung zentraler Routen.
5. Eröffne einen Pull Request mit einer klaren Beschreibung und bei Relevanz Screenshots/API-Beispiele.

## Abhängigkeiten

- tornado: Webserver-Framework
- openai: OpenAI API-Client
- matplotlib: Zum Erzeugen von Diagrammen
- networkx: Für die Graph-Datenstruktur
- PIL/Pillow: Für die Bildverarbeitung
- numpy: Für numerische Operationen
- cjkwrap: Für den Umgang mit Zeilenumbrüchen in CJK-Texten
- json5: Für robustes JSON-Parsing

## Danksagungen

- OpenAI für die bereitgestellte linguistische Analysefunktionalität
- Google Noto-Schriften für die mehrsprachige Textunterstützung

## Lizenz

Apache License 2.0

Siehe [LICENSE](LICENSE) für die vollständigen Bedingungen.
