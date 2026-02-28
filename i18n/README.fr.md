[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


**Options de langue :** Français (ce fichier)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

Un outil pour analyser les étymologies des mots et les visualiser sous forme de graphes interactifs.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#prerequisites)
[![Framework](https://img.shields.io/badge/framework-Tornado-5C2D91)](#overview)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![API](https://img.shields.io/badge/API-REST-orange)](#api-endpoints)
[![Graph](https://img.shields.io/badge/Visualization-NetworkX%20%2B%20Matplotlib-1f6feb)](#etymologygraph)
[![i18n](https://img.shields.io/badge/i18n-multilingual-success)](#features)

![Word Origins Demo](word_origins.jpg)

## Quick Snapshot

| Zone | Détails |
|---|---|
| 🌐 Accès | Interface web pour l'exploration interactive et API pour la sortie PNG en base64 |
| 🧠 Intelligence | Analyse étymologique alimentée par OpenAI avec parsing JSON structuré |
| 🧰 Reproductibilité | JSON et artefacts PNG mis en cache pour chaque mot traité |
| 🌍 Support linguistique | Rendu multilingue pour CJK et arabe avec polices incluses |

## Overview

WordOrigins est une application web Python qui permet d'explorer l'étymologie (l'origine et l'évolution historique) des mots. Elle fournit une analyse détaillée de l'évolution des mots dans le temps, les découpe en parties constitutives, retrace récursivement la lignée linguistique de chaque composant, puis affiche le résultat sous forme de graphique dans le navigateur.

### ✨ Key Features

- Analyse étymologique détaillée de n'importe quel mot
- Représentation graphique visuelle des origines des mots
- Prise en charge de plusieurs langues, dont l'anglais, le français, l'arabe, le japonais et le chinois
- Interface web interactive pour l'exploration

## Features

| Fonctionnalité | Détails |
|---|---|
| 🔎 Web UI | Rechercher et parcourir les graphes d'étymologie générés |
| 🧠 Analyse basée sur OpenAI | Utilise l'API OpenAI pour produire une sortie étymologique structurée |
| 💾 Mise en cache | Réponses OpenAI mises en cache sous forme de JSON horodatés |
| 🖼️ Génération d'artefacts | JSON et PNG mis en cache pour les mots déjà analysés |
| 🌍 Rendu multilingue | Gestion des polices CJK + arabe incluse dans le dépôt |
| ↔️ Navigation | Parcours précédent/suivant des images de mots générées |
| 🔌 Support de l'API | Endpoint retournant une sortie PNG en base64 |

## How It Works

1. Entrez un mot que vous souhaitez analyser.
2. Le système se connecte à l'API OpenAI pour effectuer une analyse étymologique approfondie.
3. L'analyseur valide et parse la sortie du modèle en JSON structuré.
4. Les résultats sont mis en cache et transformés en graphe orienté.
5. Le graphe est rendu en PNG et affiché dans l'interface web.
6. Vous pouvez parcourir les mots précédemment analysés.

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

## Prerequisites

- Python 3.8+
- Clé API OpenAI
- Polices nécessaires (incluses dans le dépôt) :
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

3. Définissez votre clé API OpenAI comme variable d'environnement :
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

### Notes on dependencies

Le code importe les paquets suivants à l'exécution :
- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

Hypothèse : `requirements.txt` doit inclure les paquets ci-dessus. Si `requirements.txt` est absent de votre copie locale, installez-les manuellement.

## Usage

### Running the Web Application

Démarrez le serveur web Tornado :

```bash
python app.py
```

Puis ouvrez votre navigateur et naviguez vers `http://localhost:7788`.

### Typical user flow

1. Ouvrez `http://localhost:7788`.
2. Saisissez un mot dans la zone de recherche.
3. L'application analyse et affiche le graphe étymologique.
4. Utilisez les contrôles précédent/suivant pour parcourir les mots générés.

### API Endpoints

| Méthode | Point de terminaison | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Génère et affiche le graphe étymologique d'un mot |
| `GET` | `/word/next-word` | Naviguer vers le mot suivant dans la liste |
| `GET` | `/word/prev-word` | Naviguer vers le mot précédent dans la liste |
| `GET/POST` | `/get_word_etymology/{word}` | Endpoint API pour obtenir les données étymologiques comme charge utile PNG base64 |

### Example API calls

```bash
# Générer/afficher un mot dans le navigateur
curl "http://localhost:7788/word/etymology"

# Récupérer la charge utile image base64
curl "http://localhost:7788/get_word_etymology/etymology"
```

## Configuration

### Environment variables

- `OPENAI_API_KEY` (obligatoire) : clé API utilisée par le client Python OpenAI
- `OPENAI_MODEL` (facultatif) : nom du modèle utilisé par l'analyseur (par défaut `gpt-4-0125-preview`)

### Runtime directories created/used by the app

- `jsons/`
- `static/images/`
- `word_etymology_analysis/`
- `processed_words.csv`

## Components

### WordEtymologyAnalyzer

Se connecte à l'API OpenAI pour obtenir des informations étymologiques détaillées sur un mot donné. Inclut une logique de cache et de nouvelles tentatives :

- Minimise et normalise les mots saisis
- Tente de parser la sortie JSON de manière robuste (`json5`)
- Enregistre les instantanés d'analyse horodatés dans `word_etymology_analysis/`
- Enregistre les mots traités dans `processed_words.csv`

### EtymologyGraph

Crée des représentations visuelles des données étymologiques avec NetworkX et Matplotlib :

- Cartographie récursivement les étymologies imbriquées en nœuds/arêtes de graphe orienté
- Calcule un positionnement radial basé sur la profondeur
- Dessine les labels de nœud/signification/exemple et les labels de langue sur les arêtes
- Gère le rendu de texte multilingue avec les polices incluses

### Web Application

Un serveur web basé sur Tornado qui traite les requêtes et sert l'interface utilisateur :

- Redirige `/` vers `/word/etymology`
- Rend les graphes de mots depuis `static/images/`
- Génère des analyses/images manquantes à la demande

## Examples

### Analyze a new word

```bash
python app.py
# then open http://localhost:7788/word/revolution
```

Résultats attendus après la première exécution :

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

### Browse existing generated words

```text
http://localhost:7788/word/next-word?word=etymology
http://localhost:7788/word/prev-word?word=etymology
```

## Technical Details

- L'application stocke des fichiers JSON des mots analysés pour le cache.
- Les images sont générées au format PNG.
- Un traitement de police spécial est implémenté pour la prise en charge multilingue.
- La mise en page du graphe est calculée en fonction de la profondeur des nœuds et des relations.
- Le dépôt existant inclut des notebooks exploratoires et des artefacts archivés utilisés pendant le développement.

## Development Notes

- Le point d'entrée principal au runtime est `app.py`.
- Les fichiers notebook (`etymology*.ipynb`) sont expérimentaux et peuvent diverger du flux du serveur de production.
- Il existe des chemins hérités/dupliqués (`statics/` vs `static/`, fichiers `.old`) conservés pour le contexte historique.
- Le `.gitignore` actuel semble contenir des marqueurs de conflit de fusion non résolus ; nettoyez-le avant le conditionnement de la release.

## Troubleshooting

| Problème | Résolution |
|---|---|
| `ModuleNotFoundError` au démarrage | Installez les dépendances manquantes : `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Erreur `OPENAI_API_KEY` ou échec d'authentification | Assurez-vous que `OPENAI_API_KEY` est exporté dans la même session shell où vous lancez `python app.py` |
| Le texte du graphe apparaît sous forme de boîtes ou de glyphes manquants | Vérifiez que les fichiers de polices inclus sont présents aux emplacements attendus dans le dépôt |
| Aucune image générée pour un mot | Vérifiez les journaux du serveur pour les nouvelles tentatives/parsing JSON et confirmez l'accès réseau/API |
| `pip install -r requirements.txt` échoue car le fichier est manquant | Créez un fichier local de dépendances à partir de la liste de paquets de ce README ou installez les paquets directement |

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
