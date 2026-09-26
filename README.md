# IFT3700 / IFT6758 : démonstrations et projet

Ce dépôt regroupe les démonstrations du cours et les consignes des étapes du projet. Nous y publierons les nouveaux exercices, les corrections et les consignes au fil de la session.

**Un seul environnement Python pour toutes les démos : exécutez `uv sync` à la racine de `ift3700-6758`.** Les dépendances sont déclarées dans le `pyproject.toml` commun et leurs versions sont enregistrées dans `uv.lock`. Chaque démo utilise la même `.venv` à la racine.

L’environnement utilise **Python 3.11**, NumPy 1.26.4 et pandas 1.5.3 pour être compatible avec PandasAI 2.3.2. Pour les parties **RAG et PandasAI** de la démo 2, utilisez `uv sync --group llm` à la place de `uv sync` afin d’ajouter les dépendances des modèles locaux. Les autres démos n’en ont pas besoin.

## Première installation

Installez **Git** et **uv**. Pour travailler dans votre IDE, installez aussi les extensions **Python** et **Jupyter**.

Pour installer uv sur macOS / Linux :

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Sur Windows, dans PowerShell :

```powershell
winget install --id=astral-sh.uv -e
```

Rouvrez le terminal après l’installation, puis vérifiez :

```sh
git --version
uv --version
```

Clonez le dépôt une seule fois, puis installez les dépendances communes :

```sh
cd <répertoire de votre choix>
git clone https://github.com/milarobotlearningcourse/data_science.git ift3700-6758
cd ift3700-6758
uv sync
```

`uv sync` crée `.venv` et installe les paquets nécessaires aux démos, y compris les outils de notebook. uv peut télécharger un interpréteur Python compatible si nécessaire. L’installation initiale nécessite une connexion Internet. Il n’est pas nécessaire d’exécuter `uv init`, de créer un environnement par démo ou d’installer les paquets un par un.

## Avant chaque séance : récupérer les nouveautés

Dans un terminal ouvert à la racine de `ift3700-6758`, exécutez :

```sh
git pull --ff-only
uv sync
```

Faites-le régulièrement, notamment lorsqu’on annonce une nouvelle démo ou une correction. `git pull` récupère les fichiers publiés sur GitHub; `uv sync` met à jour l’environnement commun si les dépendances ont changé. Il n’est pas nécessaire de cloner à nouveau le dépôt.

Pour conserver vos réponses sans modifier les notebooks distribués, copiez-les dans un dossier `travail_personnel/` à la racine. Ce dossier est ignoré par Git et utilise le même environnement. Si Git refuse un `pull` parce que vous avez modifié un fichier suivi, sauvegardez votre travail avant de résoudre le conflit; ne supprimez pas vos réponses pour forcer la mise à jour.

## Ouvrir les notebooks

### Avec VS Code

1. Ouvrez le dossier **`ift3700-6758` complet**.
2. Depuis la palette de commandes, choisissez **Python: Select Interpreter**, puis le Python de **`ift3700-6758/.venv`**.
3. Ouvrez le notebook souhaité dans le dossier de la démo.
4. Cliquez sur **Select Kernel → Python Environments** et choisissez cette même `.venv`.

Toutes les démos utilisent ce noyau. Après une mise à jour des paquets, redémarrez le noyau du notebook.

### Avec JupyterLab dans le navigateur

Depuis la racine du dépôt :

```sh
uv run jupyter lab
```

Ouvrez ensuite le notebook souhaité. Arrêtez le serveur avec `Ctrl+C` dans le terminal. `uv run` utilise l’environnement du dépôt sans activation manuelle.

## Les démonstrations

| Dossier | Contenu | Ordre conseillé |
|---|---|---|
| [Démo 1](demo_1/README.md) | Environnements Python, Git, NumPy, pandas et premier exemple d’apprentissage automatique | Notebooks `00`, `01`, `02`, puis `03` |
| [Démo 2](demo_2/README.md) | API NHL et nettoyage; exploration et visualisation interactives (français/anglais); RAG et PandasAI avec Qwen local (anglais) | Notebooks `01`, `02`, puis `04` et `05` (optionnels, groupe `llm`) |
| [Anciens laboratoires](anciens_labs/README.md) | Supports des années précédentes, classés par thème et par langue | Consulter le catalogue et les notes de compatibilité |
| [Tutoriels Git](tutoriels/git/README.md) | Diaporamas français/anglais et notebook pratique | Ressource indépendante |
| Tutoriels Python ([français](tutoriels/python/fr/python.ipynb), [anglais](tutoriels/python/en/python.ipynb)) | Variables, structures de données, fonctions et exercices | Introduction indépendante |

La démo 1 propose les mêmes leçons en [français](demo_1/notebooks/fr/) et en [anglais](demo_1/notebooks/en/), ainsi qu’un [diaporama en français](demo_1/intro_data_science_demo_fr.pptx). Les nouvelles démos seront ajoutées à ce tableau au fil du cours.

Les anciens labos sont conservés comme références historiques : certaines API, dépendances et données restent à adapter avant de les utiliser comme démos actives avec l’environnement commun. Leur catalogue précise les versions retenues et les corrigés disponibles.

L’[atelier de configuration manuelle](demo_1/python/README_fr.md) explique `venv`, pip et uv. Pour utiliser les notebooks du cours, la procédure `git pull` puis `uv sync` ci-dessus suffit.

## Le projet

Les consignes de chaque étape du projet sont publiées dans un dossier dédié, en français et en anglais.

| Étape | Contenu | Consignes |
|---|---|---|
| Étape 1 | Acquisition et nettoyage des données play-by-play de la LNH, outil de débogage interactif, visualisations simples et cartes de tirs; parties LLM/RAG pour IFT6758 seulement | [Français](milestone-1/README_fr.md) · [Anglais](milestone-1/README_en.md) |

Les parties identifiées **[IFT6758 seulement]** dans les consignes ne s’appliquent pas à IFT3700.

## Ajouter une démo

Ajoutez les fichiers dans un dossier dédié, puis complétez le tableau ci-dessus. Si une bibliothèque supplémentaire est nécessaire, lancez `uv add nom-du-paquet` **à la racine du dépôt** et incluez `pyproject.toml` et `uv.lock` dans le même commit que la démo. Pour les outils de développement, utilisez `uv add --dev nom-du-paquet`.

Conservez un seul projet uv à la racine : les dossiers de démo ne doivent pas contenir leur propre `pyproject.toml`, `uv.lock` ou `.venv`. Vérifiez les nouveaux notebooks avec l’environnement commun avant de publier.

Documentation : [installation de uv](https://docs.astral.sh/uv/getting-started/installation/) · [projets uv](https://docs.astral.sh/uv/guides/projects/)

<sub>Préparé par Jaydan Aladro</sub>
