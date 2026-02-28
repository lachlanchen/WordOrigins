[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# WordOrigins

**Options de langue :** Français (ce fichier)

Un outil pour analyser les étymologies des mots et les visualiser sous forme de graphes interactifs.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Overview

WordOrigins est une application web Python qui vous permet d’explorer l’étymologie (origine et évolution historique) des mots. Elle fournit une analyse détaillée de l’évolution des mots dans le temps, les décompose en éléments constitutifs, retrace récursivement la lignée linguistique de chaque élément, puis affiche le résultat sous forme d’image de graphe dans le navigateur.

### ✨ Fonctionnalités clés

- Analyse étymologique détaillée de n’importe quel mot
- Représentation visuelle des origines des mots sous forme de graphe
- Prise en charge de plusieurs langues, dont l’anglais, le français, l’arabe, le japonais et le chinois
- Interface web interactive pour l’exploration

## Features

| Feature | Details |
|---|---|
| 🔎 Web UI | Search and browse generated etymology graphs |
| 🧠 OpenAI-backed analysis | Uses OpenAI API to produce structured etymology output |
| 💾 Caching | Cached OpenAI responses as timestamped JSON snapshots |
| 🖼️ Artifact generation | Cached JSON and PNG artifacts for previously analyzed words |
| 🌍 Multilingual rendering | CJK + Arabic font support bundled in repository |
| ↔️ Navigation | Next/previous browsing through generated word images |
| 🔌 API support | Endpoint returns PNG output as base64 |

## How It Works

1. Saisissez un mot à analyser.
2. Le système se connecte à l’API d’OpenAI pour effectuer une analyse étymologique approfondie.
3. L’analyseur valide/parse la sortie du modèle en JSON structuré.
4. Les résultats sont mis en cache et transformés en graphe orienté.
5. Le graphe est rendu en PNG et affiché dans l’interface web.
6. Vous pouvez parcourir les mots déjà analysés.

## Project Structure

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

## Prerequisites

- Python 3.8+
- Clé API OpenAI
- Polices requises (incluses dans le dépôt) :
  - Noto Sans CJK Regular
  - Noto Sans Arabic
  - Arial Unicode MS

## Installation

### Setup

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Définissez votre clé API OpenAI comme variable d’environnement :
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notes on dependencies

Le code importe ces packages à l’exécution :
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Hypothèse : `requirements.txt` doit inclure les packages ci-dessus. Si `requirements.txt` est absent de votre copie locale, installez-les manuellement.

## Usage

### Running the Web Application

Démarrez le serveur web Tornado :

```bash
python app.py
```

Ensuite, ouvrez votre navigateur et accédez à `http://localhost:7788`.

### Typical user flow

1. Ouvrez `http://localhost:7788`.
2. Saisissez un mot dans la barre de recherche.
3. L’application analyse et affiche le graphe étymologique.
4. Utilisez les contrôles précédent/suivant pour parcourir les mots générés.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Generates and displays the etymology graph for a word |
| `GET` | `/word/next-word` | Navigate to the next word in the list |
| `GET` | `/word/prev-word` | Navigate to the previous word in the list |
| `GET/POST` | `/get_word_etymology/{word}` | API endpoint to get etymology data as a base64 PNG payload |

### Example API calls

```bash
# Generate/view a word in browser
curl "http://localhost:7788/word/etymology"

# Fetch base64 image payload
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuration

### Environment variables

- `OPENAI_API_KEY` (required): Clé API utilisée par le client Python OpenAI
- `OPENAI_MODEL` (optional): Nom du modèle utilisé par l’analyseur (par défaut `gpt-4-0125-preview`)

### Runtime directories created/used by the app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Components

### WordEtymologyAnalyzer

Se connecte à l’API d’OpenAI pour obtenir des informations étymologiques détaillées pour un mot donné. Inclut une logique de cache et de nouvelle tentative :

- Convertit les mots saisis en minuscules
- Tente de parser robustement la sortie JSON (`json5`)
- Enregistre des snapshots d’analyse horodatés dans `word_etymology_analysis/`
- Consigne les mots traités dans `processed_words.csv`

### EtymologyGraph

Crée des représentations visuelles des données étymologiques à l’aide de NetworkX et Matplotlib :

- Cartographie récursivement les étymologies imbriquées en nœuds/arêtes de graphe orienté
- Calcule un positionnement radial basé sur la profondeur
- Dessine les étiquettes d’arêtes pour part/meaning/example et langue
- Gère le rendu de texte multilingue avec les polices incluses

### Web Application

Serveur web basé sur Tornado qui gère les requêtes et sert l’interface utilisateur :

- Redirige `/` vers `/word/etymology`
- Rend les graphes de mots depuis `static/images/`
- Génère à la demande les analyses/images manquantes

## Examples

### Analyze a new word

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Sorties attendues après la première exécution :

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Browse existing generated words

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technical Details

- L’application stocke des fichiers JSON des mots analysés pour la mise en cache.
- Les images sont générées au format PNG.
- Une gestion spéciale des polices est implémentée pour la prise en charge multilingue.
- La disposition du graphe est calculée selon la profondeur des nœuds et les relations.
- Le dépôt existant inclut des notebooks exploratoires et des artéfacts archivés utilisés pendant le développement.

## Development Notes

- Le point d’entrée principal à l’exécution est `app.py`.
- Les fichiers notebook (`etymology*.ipynb`) sont expérimentaux et peuvent diverger du flux du serveur de production.
- Des chemins legacy/dupliqués (`statics/` vs `static/`, fichiers `.old`) sont conservés pour contexte historique.
- Le fichier `.gitignore` actuel semble contenir des marqueurs de conflit de fusion non résolus ; corrigez cela avant le packaging de release.

## Troubleshooting

| Issue | Resolution |
|---|---|
| `ModuleNotFoundError` on startup | Install missing dependencies: `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| `OPENAI_API_KEY` error or authentication failure | Ensure `OPENAI_API_KEY` is exported in the same shell session where you launch `python app.py` |
| Graph text renders as boxes or missing glyphs | Verify bundled font files are present in expected repository paths |
| No image generated for a word | Check server logs for JSON parse retries/exceptions and confirm network/API access |
| `pip install -r requirements.txt` fails because file is missing | Create a local dependency file from the package list in this README or install packages directly |

## Roadmap

- Ajouter la prise en charge de plus de langues.
- Implémenter des comptes utilisateur pour enregistrer les étymologies favorites.
- Améliorer la visualisation des graphes avec zoom et panoramique.
- Ajouter des informations linguistiques plus détaillées.
- Ajouter un manifeste de dépendances maintenu et une configuration d’environnement reproductible.
- Ajouter des tests pour le parsing de l’analyseur, le comportement du cache et les handlers de routes.

## Contribution

Les contributions sont les bienvenues. Workflow suggéré :

1. Fork the repository.
2. Create a feature branch.
3. Make focused, reviewable changes.
4. Validate by running `python app.py` and checking key routes.
5. Open a pull request with a clear description and screenshots/API samples when relevant.

## Dependencies

- tornado: Framework de serveur web
- openai: Client API OpenAI
- matplotlib: Pour générer les graphes
- networkx: Pour la structure de données en graphe
- PIL/Pillow: Pour le traitement d’images
- numpy: Pour les opérations numériques
- cjkwrap: Pour gérer le retour à la ligne du texte CJK
- json5: Pour un parsing JSON robuste

## License

Apache License 2.0

See [LICENSE](LICENSE) for full terms.

## Acknowledgements

- OpenAI pour les capacités d’analyse linguistique
- Les polices Google Noto pour la prise en charge du texte multilingue
