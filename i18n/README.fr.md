[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# WordOrigins

> 🎯 Visualiser l’étymologie des mots comme des graphes de provenance multilingues via un flux de travail fondé sur OpenAI et optimisé pour le cache.

**Options de langue :** Français (ce fichier)

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

## 📘 Aperçu

WordOrigins est un utilitaire web Python pour analyser l’étymologie des mots et visualiser leur lignée linguistique sous forme de graphe orienté. Il combine :

- Une application web Tornado.
- Une analyse étymologique alimentée par OpenAI.
- Une analyse JSON structurée avec gestion de repli robuste.
- Une génération de graphes via NetworkX + Matplotlib.
- Des sorties mises en cache pour des analyses répétées rapides.

Il fournit une interface navigateur et des endpoints d’API pour générer et récupérer les artefacts d’étymologie.

## 📸 Vue d’ensemble rapide

| Domaine | Détails |
|---|---|
| 🌐 Accès | UI web pour l’exploration interactive et API pour la sortie PNG base64 |
| 🧠 Intelligence | Analyse étymologique basée sur OpenAI avec parsing JSON structuré |
| 🧰 Reproductibilité | Artefacts JSON + PNG mis en cache pour chaque mot traité |
| 🌍 Prise en charge linguistique | Rendu multilingue pour CJK et arabe avec polices incluses |

## Fonctionnalités

| Fonctionnalité | Détails |
|---|---|
| 🔎 Interface web | Rechercher et parcourir les graphes d’étymologie générés |
| 🧠 Analyse assistée par OpenAI | Utilise l’API OpenAI pour produire une sortie étymologique structurée |
| 💾 Cache | Stocke les réponses avec des instantanés JSON horodatés |
| 🖼️ Génération d’artefacts | Exporte les artefacts JSON et PNG pour les mots traités |
| 🌍 Rendu multilingue | Prise en charge CJK + arabe avec polices intégrées au dépôt |
| ↔️ Navigation | Navigation précédent/suivant entre les images de mots générés |
| 🔌 Support API | L’endpoint renvoie un PNG encodé en base64 dans un JSON |

## 🛠️ Comment ça marche

1. L’utilisateur soumet un mot via `/word/{word}` ou le formulaire de recherche web.
2. L’analyseur appelle OpenAI et valide la structure de la réponse.
3. Les données parsées sont normalisées et enregistrées pour réutilisation du cache.
4. Les relations étymologiques sont converties en nœuds/arêtes de graphe.
5. NetworkX et Matplotlib rendent un graphe orienté au format PNG.
6. L’UI et l’API exposent le chemin d’image en cache et les métadonnées associées.

## 🗂️ Structure du projet

```text
WordOrigins/
├─ app.py                     # Application web Tornado (point d’entrée actuel)
├─ app.py.old                 # Variante legacy de l’application
├─ word_etymology_analyzer.py # Analyse OpenAI + logique retry/cache
├─ etymology_graph.py         # Construction de graphe et rendu PNG
├─ utils.py                   # Utilitaires images/polices
├─ templates/
│  ├─ index.html              # UI web principale
│  ├─ index.html.old          # Variante legacy de template
│  └─ carousel_items.html     # Fragment d’UI réutilisable
├─ static/
│  └─ images/                 # PNGs principaux générés à l’exécution
├─ statics/
│  └─ images/                 # Dossier d’images dupliqué legacy
├─ images/                    # Actifs de démo/capture
├─ jsons/                     # JSON générés par mot + cache
├─ word_etymology_analysis/   # Cache des réponses modèle horodatées
├─ processed_words.csv         # Index des mots traités
├─ i18n/                      # Fichiers README traduits
├─ archived_code/             # Notebooks et scripts historiques
├─ archived_data/             # Instantanés JSON historiques
├─ Noto Sans CJK Regular/     # Ressources de polices incluses
├─ Noto_Sans/
├─ Noto_Sans,Noto_Sans_Arabic/
├─ arial-unicode-ms.ttf       # Police Unicode incluse
├─ etymology*.ipynb           # Notebooks de développement
├─ LICENSE
└─ .auto-readme-work/         # Artefacts de pipeline
```

## Prérequis

- Python 3.8+
- Identifiants API OpenAI :
  - `OPENAI_API_KEY` (obligatoire)
  - `OPENAI_MODEL` (optionnel, par défaut `gpt-4-0125-preview` dans les indications existantes)
- Fichiers de polices inclus dans le dépôt si vous avez besoin du rendu multilingue

## 🧰 Installation

1. Cloner le dépôt.

   ```bash
   git clone https://github.com/lachlanchen/WordOrigins.git
   cd WordOrigins
   ```

2. Créer et activer un environnement Python (recommandé).

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Installer les bibliothèques runtime.

   Aucun manifeste de dépendances racine n’existe dans ce dépôt, installez donc directement les dépendances requises :

   ```bash
   pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5
   ```

4. Configurer les identifiants.

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export OPENAI_MODEL=gpt-4-0125-preview   # remplacement optionnel
   ```

## 🚀 Utilisation

### Lancer l’application web

```bash
python app.py
```

Ouvrez `http://localhost:7788` dans votre navigateur.

### Parcours utilisateur type

1. Ouvrez `http://localhost:7788/word/etymology`.
2. Entrez un mot.
3. Attendez l’analyse (la première exécution peut être plus longue à cause de la latence externe de l’API).
4. Explorez le graphe et les métadonnées générés.
5. Utilisez la navigation précédent/suivant pour parcourir les mots mis en cache.

### Endpoints API

| Méthode | Endpoint | Description |
|---|---|---|
| `GET` | `/word/{word_to_analyze}` | Affiche une page pour l’étymologie demandée |
| `GET` | `/word/next-word?word={word}` | Navigue vers le mot suivant dans le cache |
| `GET` | `/word/prev-word?word={word}` | Navigue vers le mot précédent dans le cache |
| `GET/POST` | `/get_word_etymology/{word}` | Renvoie un JSON avec une charge utile PNG base64 |

### Exemples d’appels API

```bash
curl "http://localhost:7788/word/etymology"
curl "http://localhost:7788/word/next-word?word=etymology"
curl "http://localhost:7788/word/prev-word?word=etymology"
curl "http://localhost:7788/get_word_etymology/etymology"
```

## ⚙️ Configuration

- `OPENAI_API_KEY` (obligatoire) : identifiants pour les requêtes d’analyse.
- `OPENAI_MODEL` (optionnel) : remplacement de modèle pour l’analyse.
- Répertoires d’exécution utilisés par le service :
  - `jsons/`
  - `static/images/`
  - `word_etymology_analysis/`
  - `processed_words.csv`

## 🧪 Exemples

```bash
python app.py
```

Puis ouvrez :

```text
http://localhost:7788/word/revolution
```

Artefacts créés lors d’une première analyse :

- `jsons/revolution.json`
- `static/images/revolution.png`
- `word_etymology_analysis/revolution-<timestamp>.json`

## Components

### WordEtymologyAnalyzer

Situé dans `word_etymology_analyzer.py`, ce composant :

- Normalise les mots en entrée.
- Appelle OpenAI pour obtenir des réponses étymologiques structurées.
- Extrait/répare les payloads JSON avec `json5`.
- Réessaie les tentatives de parsing échouées et enregistre les erreurs pour la résilience.
- Écrit des instantanés horodatés dans `word_etymology_analysis/`.
- Met à jour l’index `processed_words.csv`.

### EtymologyGraph

Situé dans `etymology_graph.py`, ce composant :

- Charge le JSON d’étymologie structuré.
- Construit un `networkx.DiGraph` avec des relations d’ascendance récursives.
- Calcule les coordonnées de graphe sensibles à la profondeur.
- Rend les nœuds et arêtes étiquetés avec gestion multilingue du texte.
- Sauvegarde des images `PNG` pour le cache et la présentation.

### Application web

Dans `app.py`, l’application Tornado :

- Sert la redirection racine et le comportement de page de recherche.
- Gère les flux de génération et de recherche dans le cache.
- Expose les routes page et API sous `/word/...` et `/get_word_etymology/...`.
- Renvoie des payloads JSON contenant des données d’image base64 pour les consommateurs API.

## 📦 Dépendances

- `tornado`
- `openai`
- `matplotlib`
- `networkx`
- `numpy`
- `Pillow`
- `cjkwrap`
- `json5`

## 🧱 Notes de développement

- Le cache JSON et d’images évite les appels API répétés inutiles.
- `index.html` et `index.html.old` sont conservés pour la compatibilité et l’historique.
- Les répertoires et artefacts hérités sont actuellement présents intentionnellement (`statics/`, notebooks, archives).
- Un fichier `.gitignore` avec marqueurs de conflit de fusion a été signalé comme un problème de qualité hors périmètre README.

## 🧯 Dépannage

| Problème | Résolution |
|---|---|
| `ModuleNotFoundError` au démarrage | Installez les paquets manquants avec `pip install tornado openai matplotlib networkx numpy pillow cjkwrap json5` |
| Erreur d’authentification `OPENAI_API_KEY` | Assurez-vous que la variable est exportée dans la même session shell que celle exécutant `python app.py` |
| Glyphes manquants/illisibles dans les graphes générés | Vérifiez que les polices incluses (`Noto Sans`, variantes arabes, Arial Unicode MS) sont présentes et lisibles |
| Aucune image n’apparaît pour un mot | Vérifiez les logs de l’application pour des échecs de parsing JSON ou des erreurs API transitoires |
| Échec de `pip install -r requirements.txt` / fichier absent | Installez directement les dépendances listées ci-dessus (ce dépôt ne contient pas de manifeste racine) |



## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
