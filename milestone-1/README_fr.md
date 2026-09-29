# IFT 6758 Projet : Étape 1

Sortie : 28 septembre 2026  
Date d'échéance : 19 octobre 2026, 23 h 59

L'objectif de cette étape est de vous donner de l'expérience avec les phases de [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling) et [d'analyse exploratoire des données](https://en.wikipedia.org/wiki/Exploratory_data_analysis) d'un projet de science des données. Ce sont souvent les phases où vous passerez la plupart de votre temps dans un projet de science des données. Vous allez acquérir de l'expérience avec certains des outils courants utilisés pour récupérer et manipuler des données, et gagner en confiance dans la création d'outils et de visualisations pour vous aider à comprendre les données avant de vous lancer dans une modélisation plus avancée.

De manière générale, le déroulement de cette étape est d'utiliser [l'API de statistiques de la LNH](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md) pour récupérer des données « play-by-play » pour une période de temps spécifique et de produire des graphiques. Vous allez nettoyer les données play-by-play, puis créer des visualisations simples et interactives à partir de celles-ci. Il y aura un petit nombre de questions qualitatives simples auxquelles répondre tout au long des tâches décrites. Enfin, vous présenterez votre travail sous la forme d'une simple page web statique, créée à l'aide de [Jekyll](https://jekyllrb.com/).

**[IFT6758 seulement]** Vous allez aussi explorer comment utiliser des outils basés sur les grands modèles de langage (LLM) pour simplifier certaines composantes du pipeline, par exemple comment enrichir votre LLM avec de la génération augmentée par récupération (*Retrieval-Augmented Generation*, RAG) pour faciliter la compréhension de la documentation, ou pour créer des visualisations et des résumés simples des données. L'approche générale est d'utiliser LLM+RAG pour simplifier certaines parties du pipeline ; par exemple, fournir la documentation de l'API au LLM et lui demander d'écrire une fonction Python pour télécharger les données, les sauvegarder sur le disque et les charger en mémoire.

**Note : le travail que vous faites dans cette étape sera utile pour les étapes futures, alors assurez-vous que votre code est propre et réutilisable \- vous vous en remercierez plus tard\!**

> [!NOTE]
> **IFT3700 vs IFT6758.** Les deux cours réalisent la même étape, à l'exception des composantes LLM/RAG, qui sont **obligatoires pour IFT6758 seulement**. Chacune de ces parties est identifiée par **[IFT6758 seulement]** ; les étudiant·e·s d'IFT3700 peuvent les ignorer.

- [Une note sur le plagiat](#une-note-sur-le-plagiat)
- [Données de la LNH](#données-de-la-lnh)
  - [Motivation](#motivation)
- [Objectifs d'apprentissage](#objectifs-dapprentissage)
- [Livrables](#livrables)
  - [Détails de soumission](#détails-de-soumission)
- [Configuration du LLM (IFT6758 seulement)](#configuration-du-llm-ift6758-seulement)
  - [Modèle requis](#modèle-requis)
  - [Environnement suggéré : Google Colab T4](#environnement-suggéré--google-colab-t4)
  - [Options d'exécution facultatives](#options-dexécution-facultatives)
  - [Considérations de reproductibilité](#considérations-de-reproductibilité)
- [Tâches et questions](#tâches-et-questions)
  - [0\. Article de blog](#0-article-de-blog)
  - [1\. Acquisition de données (25%)](#1-acquisition-de-données-25)
  - [2\. Outil de débogage interactif (10%)](#2-outil-de-débogage-interactif-10)
  - [3\. Données ordonnées (10%)](#3-données-ordonnées-10)
  - [4\. Visualisations simples (25%)](#4-visualisations-simples-25)
  - [5\. Visualisations avancées : cartes de tirs (30%)](#5-visualisations-avancées--cartes-de-tirs-30)
- [Évaluations de groupe](#évaluations-de-groupe)
  - [Comment les scores influencent votre note](#comment-les-scores-influencent-votre-note)
- [Références utiles](#références-utiles)

## Une note sur le plagiat

Pour les comparaisons avec les LLM ci-dessous (IFT6758 seulement), une « implémentation manuelle » désigne du code écrit par votre équipe sans code généré par un LLM. Déclarez toute aide provenant de l'IA ; votre équipe demeure responsable d'expliquer et de valider tout le code soumis.

L'utilisation de code/modèles provenant de ressources en ligne est acceptable et courante en science des données, mais soyez clair pour citer exactement d'où vous avez pris le code lorsque nécessaire. Un simple extrait d'une ligne qui couvre une syntaxe simple provenant d'un article StackOverflow ou de la documentation d'un package ne justifie probablement pas une citation, mais copier une fonction qui effectue un tas de logique pour créer votre figure, oui. Nous vous faisons confiance pour utiliser votre meilleur jugement dans ces cas, mais si vous avez des doutes, vous pouvez toujours citer la source pour être sûr. Nous effectuerons une détection de plagiat sur votre code et vos livrables, et il vaut mieux prévenir que guérir en citant vos références.

L'intégrité est une attente importante de ce projet de cours et tout cas suspect sera traité conformément à la [politique très stricte](https://integrite.umontreal.ca/reglements/les-reglements-expliques/) de l'Université de Montréal. Le texte complet des règlements de l'université peut être trouvé [ici](https://secretariatgeneral.umontreal.ca/public/secretariatgeneral/documents/doc_officiels/reglements/enseignement/ens30_12-reglement-disciplinaire-plagiat-fraude-etudiants-cycles-superieurs.pdf). Il est de *la responsabilité de l'équipe* de s'assurer que cela est suivi rigoureusement, et des mesures peuvent être prises envers des individus ou envers l'ensemble de l'équipe selon les cas.

## Données de la LNH

Le sujet de ce projet est les données de hockey, en particulier l'API de statistiques de la LNH. Ces données sont très riches ; elles contiennent des informations remontant à plusieurs années, allant des métadonnées de la saison elle-même (par exemple, le nombre de matchs joués), aux classements de la saison, aux statistiques des joueurs par saison, jusqu'aux données d'événements détaillées pour chaque match joué, appelées **données play-by-play**. Si vous n'êtes pas familier avec les données play-by-play, la LNH utilise exactement ces données pour générer ses visualisations play-by-play, dont un exemple est présenté ci-dessous. Pour un seul match, environ 200 à 300 événements sont suivis, généralement limités aux mises au jeu, aux tirs, aux buts, aux arrêts et aux mises en échec (pas de passes ni de position individuelle des joueurs). Notez qu'il existe une manière logique d'attribuer un identifiant unique aux matchs, qui est décrite [ici](https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md#game-ids) (portez attention à la différence entre les matchs de saison régulière et ceux des séries éliminatoires\!).  
![Exemple de données play-by-play](images/fig1-play-by-play-sample.png)  
*Figure 1 : Exemple de données play-by-play pour le match* **2023021190** *au début de la 1re période. Chaque événement contient un identifiant (ex. « FACEOFF », « SHOT », etc.), une description de l'événement, les joueurs impliqués, ainsi que l'emplacement de cet événement sur la glace (dessiné sur la patinoire à l'extrême droite). Les données brutes des événements contiennent plus d'informations que cela. Vous pouvez explorer le play-by-play de ce match [**ici**](https://www.nhl.com/gamecenter/fla-vs-mtl/2024/04/02/2023021190/playbyplay).*

L'heure de l'événement, le type d'événement, l'emplacement, les joueurs impliqués et d'autres informations sont enregistrés pour chaque événement, et les données brutes sont accessibles via l'API play-by-play.  
Par exemple, les données brutes pour un match peuvent être trouvées ici :  
[https://api-web.nhle.com/v1/gamecenter/**{GAME\_ID}**/play-by-play](https://api-web.nhle.com/v1/gamecenter/2022030411/play-by-play)  
Par ex., pour le match **2022030411**, elles se trouvent ici :  
[https://api-web.nhle.com/v1/gamecenter/**2022030411**/play-by-play](https://api-web.nhle.com/v1/gamecenter/2022030411/play-by-play)

Un extrait des données brutes des événements est présenté à la figure 2\. Vous devrez explorer les données et lire la documentation de l'API pour déterminer exactement ce dont vous aurez besoin.  
![Données JSON brutes d'événements provenant de l'API de la LNH](images/fig2-raw-json-events.png)  
*Figure 2 : Données JSON brutes obtenues à partir de l'API de statistiques de la LNH pour les mêmes événements que la figure 1\. Notez qu'il existe d'autres événements entre ceux qui nous intéressent \- ce sera à vous de les explorer\!*  
**Quelques notes/mises en garde sur l'API :**

* L'API a changé lors de la saison 2023-24 ; par conséquent, le [document API non officiel](https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md) très détaillé est malheureusement en grande partie obsolète et ne peut pas être utilisé. De même, une grande partie de la documentation communautaire (ex. sur Reddit, des articles de blog) est aussi obsolète et ne fonctionnera pas.  
* Il existe de nouvelles documentations communautaires de l'API, mais elles sont moins détaillées/complètes que la documentation non officielle de l'ancienne API. Vous pouvez les trouver ici :  
  * [Zmalski's NHL API Reference](https://github.com/Zmalski/NHL-API-Reference)  
  * [dword4's NHL API Doc](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md)  
* Sur une note plus positive, l'interface semble plus propre et plus détaillée (c.-à-d. plus de notes sur les jeux, plus de types d'événements comme les tirs manqués/bloqués avec coordonnées, etc.). Même si comprendre l'API peut être un peu plus difficile, utiliser les données devrait être beaucoup plus facile.

### Motivation

Bien que nous comprenions que certaines personnes ne sont pas fans de sport, nous pensons qu'il s'agit d'un ensemble de données stimulant avec lequel travailler, pour plusieurs raisons :

1. Il s'agit d'un ensemble de données du monde réel utilisé par des data scientists professionnels, dont certains travaillent pour les équipes de la LNH elles-mêmes, tandis que d'autres gèrent leur propre entreprise d'analytique.  
2. Pendant la saison de hockey, les données sont mises à jour en direct pendant les matchs\! Cela vous donne l'occasion d'interagir fréquemment avec de nouvelles données, vous offrant un aperçu de l'importance d'un « pipeline » et d'un code propre et réutilisable dans un workflow de science des données réussi.  
3. Il est très riche, comme mentionné ci-dessus.  
4. Il est « propre » dans le sens où l'API est cohérente et vous n'aurez pas à analyser ou nettoyer des données absurdes.  
5. Il est « désordonné » dans le sens où toutes les données brutes sont en JSON et ne sont pas immédiatement adaptées à un workflow de science des données. Vous devrez « ranger » (*tidy*) les données dans un format utilisable, ce qui constitue une part importante de nombreux projets en science des données. Étant donné que les données sont déjà fournies dans un format cohérent, nous pensons que c'est un bon équilibre entre vous donner du travail pour nettoyer les données, sans être déraisonnable.  
6. Le hockey est souvent un excellent sujet de conversation ici au Canada (et surtout à Montréal). Si vous êtes nouveau au Canada, c'est une excellente façon d'en apprendre un peu sur notre culture :)

Même si vous n'êtes pas un fan de hockey, nous espérons que vous trouverez cette expérience de projet intéressante et éducative. Nous pensons que travailler avec des données du monde réel est plus gratifiant et beaucoup plus représentatif du workflow en science des données que de travailler avec des ensembles de données préparés, comme ceux disponibles sur Kaggle. Si vous êtes particulièrement fier de votre projet, certains des livrables vous apprendront à héberger votre contenu de manière publiquement accessible (via GitHub Pages), ce qui peut vous aider dans vos futures recherches de stage ou d'emploi\!

## Objectifs d'apprentissage

* **Acquisition et nettoyage des données**  
  * Comprendre ce qu'est une API REST  
  * Télécharger des données depuis Internet de manière programmatique avec Python  
  * Mettre en forme les données brutes en tables de données utiles  
  * Se familiariser avec l'idée de « pipelining » de votre travail ; c'est-à-dire créer des composants logiquement séparés tels que :  
    * Télécharger et sauvegarder les données  
    * Charger les données brutes  
    * Traiter les données brutes dans un certain format  
* **Exploration des données**  
  * Explorer les données brutes et comprendre à quoi elles ressemblent  
  * Construire des outils interactifs simples pour vous aider à travailler plus efficacement avec les données  
* **Visualisation et science des données exploratoire**  
  * Acquérir une certaine intuition et répondre à des questions simples sur les données en examinant des visualisations  
  * Utiliser Matplotlib, Seaborn ou Plotly pour créer de belles figures  
  * Créer des figures interactives pour communiquer vos résultats plus efficacement  
* **Intégration des LLM et du RAG [IFT6758 seulement]**  
  * Utiliser le RAG sur la documentation de l'API pour accélérer l'exploration de l'API et l'acquisition des données.  
  * Implémenter de la génération de code assistée par LLM pour des tâches du pipeline (récupération, mise en cache, chargement) et évaluer l'exactitude du modèle par rapport à du code écrit manuellement.  
  * Explorer l'interrogation des données en langage naturel et la visualisation automatisée avec des outils comme PandasAI.

## Livrables

Dépôts modèles (*templates*) sur lesquels travailler :

- [Modèle d'article de blog](https://github.com/milarobotlearningcourse/data_science_blog)  
- [Modèle de projet](https://github.com/milarobotlearningcourse/data_science_project)

Vous devez soumettre **LES DEUX** :

1. Un rapport en style d'article de blog  
2. La base de code **reproductible** de votre équipe ; c'est-à-dire que toutes les figures peuvent être facilement régénérées.

Au lieu d'un rapport traditionnel rédigé en LaTeX, il vous sera demandé de soumettre un article de blog qui contiendra des points de discussion et des figures (interactives\!). Partez du modèle d'article de blog indiqué ci-dessus, donc ne vous inquiétez pas de devoir tout comprendre par vous-même. À haut niveau, vous utiliserez [Jekyll](https://jekyllrb.com/) pour créer une page web statique à partir de [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). C'est une manière très simple de créer des pages au design agréable, et cela pourrait vous être très utile à l'avenir si vous souhaitez écrire des articles de blog, ou enrichir votre CV lors d'une recherche d'emploi. Bien que nous ne déploierons pas ces pages publiquement[^1], [il est très simple d'utiliser GitHub Pages pour publier votre contenu.](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) Vous êtes plus que bienvenus de le faire à la fin du cours\!

### Détails de soumission

Pour soumettre votre projet, vous devez :

- [ ] Publier votre soumission finale de l'étape sur la branche **master** ou **main**  
      (Vous devez le faire avant de télécharger les ZIP\!)  
- [ ] Soumettre un fichier ZIP de votre article de blog sur [Gradescope](https://www.gradescope.ca/courses/39572/assignments/211695)  
- [ ] Soumettre un fichier ZIP de votre base de code sur [Gradescope](https://www.gradescope.ca/courses/39572/assignments/211698)  
- [ ] Ajouter le compte GitHub des auxiliaires d'enseignement d'IFT6758 (**`à venir`**) à votre dépôt en tant que *viewer*

**Note** : Une seule personne par équipe doit soumettre le projet sur Gradescope.  
Pour soumettre une archive ZIP de votre dépôt, vous pouvez la télécharger via l'interface de GitHub :  
![Télécharger un ZIP du dépôt depuis GitHub](images/github-download-zip.png)  
N'oubliez pas que cette méthode ne télécharge pas l'intégralité du dépôt git, mais seulement la branche master ou main. Assurez-vous que tout votre code est commité sur la branche master avant de télécharger les ZIP.

## Configuration du LLM (IFT6758 seulement)

> [!NOTE]
> Toute cette section s'applique à IFT6758 seulement. Les étudiant·e·s d'IFT3700 peuvent passer directement à [Tâches et questions](#tâches-et-questions).

### Modèle requis

Pour toutes les tâches basées sur un LLM dans cette étape, vous devez utiliser **Qwen3-4B-Instruct-2507** (Qwen/Qwen3-4B-Instruct-2507). Le téléchargement du modèle et la configuration de son chargement seront fournis dans le modèle de projet GitHub. Consultez la [fiche officielle du modèle et sa documentation d'utilisation](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) pour les instructions d'utilisation du modèle.

Ce checkpoint est sans mode de réflexion (*non-thinking*), donc aucune configuration du mode de réflexion n'est requise.

### Environnement suggéré : Google Colab T4

Nous suggérons d'utiliser **Hugging Face Transformers avec une inférence en FP16 sur un GPU T4 de Google Colab (16 Go de VRAM)**. Assurez-vous que votre instance Colab est configurée avec l'accélération matérielle GPU et vérifiez que l'appareil qui vous est assigné est bien un GPU T4.

Les poids bruts du modèle sont au format **BF16** (virgule flottante 16 bits). Dans le dépôt de projet fourni, ces poids sont chargés en mode FP16 via dtype=torch.float16. Puisque les deux options utilisent des représentations en virgule flottante 16 bits, cette conversion ne constitue pas une quantification à précision réduite. **Appliquer une quantification est complètement inutile pour ce workflow.**

L'initialisation du réseau nécessite environ **7,7 Go de VRAM**, avec une vitesse d'exécution d'environ **6 tokens générés par seconde**. Gardez en tête que ces valeurs sont simplement des références indicatives plutôt que des garanties strictes : l'empreinte mémoire totale et le débit varient selon la longueur du contexte et l'environnement du système. Notez que la génération nécessite de la mémoire GPU supplémentaire.

### Options d'exécution facultatives

La configuration d'exécution recommandée fournit tout ce qui est nécessaire pour compléter le travail. **L'exploration de techniques de quantification ou de moteurs d'inférence spécialisés est complètement facultative et n'est pas évaluée ; aucun point bonus ne sera accordé pour une exécution plus rapide ou pour l'implémentation de frameworks de déploiement complexes.** Peu importe le framework choisi, vous devez utiliser le checkpoint de poids désigné **Qwen3-4B-Instruct-2507**.

**Exécution sur votre propre matériel.** Vous êtes libres d'exécuter le code sur des GPU locaux dédiés ou sur des machines Apple Silicon, pourvu que votre matériel satisfasse les exigences d'exécution.

**Quantification du modèle.** Si vous souhaitez réduire l'utilisation de la mémoire, vous pouvez tester la quantification 8 bits avec les outils de Hugging Face et la bibliothèque [bitsandbytes](https://huggingface.co/docs/transformers/quantization/bitsandbytes) en utilisant BitsAndBytesConfig(load\_in\_8bit=True). Cela applique une précision réduite **INT8**. Il n'est pas attendu que vous construisiez vos propres algorithmes de quantification. Gardez en tête qu'une précision réduite diminue l'utilisation de la mémoire, mais ne garantit pas une génération de tokens plus rapide.

**Moteurs d'inférence personnalisés.** Vous pouvez aussi explorer des moteurs spécialisés comme [llama.cpp](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html) avec une conversion GGUF 8 bits des mêmes poids exacts pour évaluer les gains de vitesse potentiels sur une configuration locale.

### Considérations de reproductibilité

Peu importe votre configuration matérielle et logicielle, décrivez soigneusement votre environnement d'exécution, les versions des bibliothèques, les paramètres de précision, les formats de quantification et les hyperparamètres de génération afin que votre pipeline et vos résultats demeurent entièrement reproductibles.

## Tâches et questions

Les tâches requises pour l'étape 1 sont décrites ici. Une description générale de ce qui est attendu est fournie au début de chaque tâche. La section **Questions** de chaque tâche détaille le contenu requis dans l'article de blog. Il peut s'agir de questions d'interprétation, ou vous devrez peut-être produire des figures ou des images à inclure dans l'article de blog. Nous essayons d'écrire en **gras** la plupart des éléments requis dans le rapport, mais assurez-vous de répondre à tout ce qui vous est demandé dans chaque question. Nous ne nous attendons pas à de longues réponses ; dans la plupart des cas, quelques phrases suffiront.

### 0\. Article de blog

Créez un article de blog à l'aide du modèle fourni, contenant toutes les figures, réponses et discussions requises mentionnées dans la section précédente. Vous n'aurez pas besoin de déployer l'article de blog pour qu'il soit accessible au public, mais des instructions seront fournies si vous souhaitez mettre en valeur votre superbe projet sur votre CV une fois le cours terminé\!

**Vous DEVEZ le soumettre sous forme d'article de blog\!**

Nous vous suggérons de mettre en place un environnement de travail pour l'article de blog dès le début, car il sera beaucoup plus facile de répondre aux questions et d'ajouter des figures au fur et à mesure que vous avancez dans le projet, plutôt que d'essayer de tout configurer juste avant la date limite\! Une fois votre environnement fonctionnel, il est très simple de travailler avec\!

### 1\. Acquisition de données (25%)

Créez une fonction ou une classe pour télécharger les données play-by-play de la LNH pour la saison régulière et les séries éliminatoires. Le point d'accès principal qui nous intéresse est :

https://api-web.nhle.com/v1/gamecenter/**\[GAME\_ID\]**/play-by-play

Vous devrez lire l'[**ANCIENNE** documentation non officielle de l'API](https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md#game-ids) pour comprendre comment le **GAME\_ID** est formé. Vous pourriez ouvrir ce point d'accès dans votre navigateur pour examiner le JSON brut et l'explorer un peu (Firefox dispose d'un bon visualiseur JSON intégré). ***Notez que ce document est généralement obsolète puisque la LNH est passée à une nouvelle API lors de la saison 2023-24, mais le GAME\_ID est toujours formé de la même façon\!***

Utilisez votre outil pour télécharger les données de la saison 2016-17 jusqu'à la saison 2023-24. Vous pouvez implémenter cela comme vous le souhaitez, mais si vous avez besoin de conseils, voici quelques astuces :

* Il s'agit d'une API publique, et vous devez donc être conscient que quelqu'un d'autre paie pour les requêtes. Vous devriez télécharger les données brutes et les sauvegarder localement, puis utiliser cette copie locale pour en dériver des ensembles de données propres/utilisables.  
    
* **Ne commitez pas** les données (ou de gros fichiers binaires) dans votre dépôt GitHub. C'est une mauvaise pratique : git est fait pour le code, pas pour le stockage de fichiers. Même si cela pourrait être possible pour l'ensemble de données avec lequel vous travaillerez, ce ne le sera probablement pas pour des projets à plus grande échelle en industrie ou en milieu universitaire. Les gros dépôts git deviennent lents à cloner et à utiliser. Notez qu'en raison du fonctionnement de git, une fois qu'un fichier a été commité et poussé, simplement le supprimer et commiter la suppression ne supprime pas réellement le fichier ; il faut réécrire l'historique git, ce qui devient risqué. Une bonne façon d'éviter de commiter des fichiers par accident est d'utiliser un fichier [.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore) et d'y ajouter les motifs de fichiers voulus (comme \*.npy ou \*.pkl).

* Une bonne approche pourrait être de définir une fonction qui accepte l'année cible et un chemin de fichier en argument, puis vérifie si un fichier correspondant à l'ensemble de données que vous allez télécharger existe à l'emplacement spécifié. Si c'est le cas, elle pourrait immédiatement ouvrir le fichier et renvoyer le contenu sauvegardé. Sinon, elle pourrait télécharger le contenu depuis l'API REST et le sauvegarder dans le fichier avant de renvoyer les données. Ainsi, la première fois que vous exécutez cette fonction, elle téléchargera et mettra en cache les données localement, et la fois suivante, elle chargera plutôt les données locales. Envisagez d'utiliser des variables d'environnement pour permettre à chaque membre de l'équipe de spécifier un emplacement différent, et faites en sorte que votre fonction récupère automatiquement l'emplacement spécifié par la variable d'environnement, pour éviter de vous disputer au sujet des chemins dans votre dépôt git.

* Si vous voulez être encore plus sophistiqué, vous pourriez envisager d'intégrer cette logique dans une classe qui implémente la logique suggérée au point précédent. Cela se prête bien à la façon dont les données sont séparées par saisons de hockey, et vous permettrait d'ajouter une logique qui se généraliserait à toute autre saison que vous voudriez analyser, de manière propre et évolutive. Pour être *encore plus sophistiqué*, vous pourriez envisager de surcharger l'opérateur « add » (\_\_add\_\_) de cette classe pour pouvoir combiner les données de plusieurs saisons dans une structure de données commune, et ainsi agréger les données sur plusieurs saisons. Ce n'est absolument ***pas*** **obligatoire**, ce ne sont que quelques idées pour vous inspirer\! Nous vous encourageons à être créatifs et à appliquer vos connaissances en structures de données/POO à la science des données \- cela peut vous faciliter la vie\!

* Écrire des [docstrings](https://betterprogramming.pub/the-guide-to-python-docstrings-3d40340e824b) pour vos fonctions est une bonne habitude à prendre.

> [!IMPORTANT]
> **[IFT6758 seulement] Acquisition de données assistée par LLM \+ RAG**
> * Utilisez un pipeline RAG pour récupérer des extraits pertinents de la documentation fournie de l'API de la LNH et les inclure dans le prompt du LLM. Vous pouvez utiliser une **récupération par mots-clés** (ex. BM25 ou TF–IDF) ou une **récupération par embeddings** à l'aide d'un modèle d'embeddings pré-entraîné. Une base de données vectorielle dédiée n'est pas nécessaire ; les embeddings peuvent être stockés localement et recherchés par similarité cosinus. Sauvegardez l'instantané de la documentation et les extraits récupérés.
> * À l'aide de la documentation récupérée, demandez au modèle Qwen 4B fourni d'écrire une classe ou une fonction Python qui récupère, met en cache localement et charge les données play-by-play pour une saison donnée.

**Questions**

1. **Rédigez un bref tutoriel** expliquant comment votre équipe a téléchargé l'ensemble de données. Imaginez :) que vous cherchiez un guide pour télécharger les données play-by-play ; votre guide devrait vous faire dire « Parfait \- c'est exactement ce que je cherchais\! ». **Incluez votre fonction/classe** et **fournissez un exemple de son utilisation**. Assurez-vous de ne pas seulement démontrer que votre code fonctionne \- c'est aussi un exercice de documentation et de communication de votre implémentation. Cela n'a *pas* besoin d'être extrêmement compliqué, mais nous nous attendons à quelque chose d'un peu plus cohérent et digeste que de simples captures d'écran de vos fonctions/code.  
2. **[IFT6758 seulement]** Comparez le comportement de récupération, de mise en cache et de chargement de votre code manuel et de votre code généré par le LLM à l'aide des mêmes tests : un match connu, un accès au cache sans nouvelle requête, et une requête qui échoue. Vérifiez les deux implémentations par rapport aux résultats attendus. Rapportez les itérations de prompts et toute correction manuelle nécessaire.

### 2\. Outil de débogage interactif (10%)

Lorsqu'on travaille avec de nouvelles données, il est souvent utile de créer des outils interactifs simples pour parcourir les données et prototyper des implémentations. Un outil utile est [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/), qui vous permet de créer très rapidement et facilement des widgets HTML dans une cellule de notebook Jupyter. Un cas d'utilisation courant de ces widgets est de les appliquer comme décorateurs et de les utiliser pour spécifier les arguments d'une fonction. Par exemple, si vous souhaitez récupérer des informations qui se trouvent dans un élément d'un tableau, vous pouvez utiliser un *IntSlider* pour contrôler l'indice passé à cette fonction. Vous pouvez ensuite définir dans cette fonction la logique pour afficher votre image ; si votre liste est une liste de chemins d'images, vous pouvez charger l'image et l'afficher avec matplotlib. Ces widgets peuvent également être imbriqués, ce qui vous offre une grande flexibilité avec très peu d'effort.

**Questions**

1. **Implémentez un ipywidget** (ou un outil interactif de votre choix) qui vous permet de parcourir tous les événements, pour chaque match d'une saison donnée, avec la possibilité de basculer entre la saison régulière et les séries éliminatoires. **Dessinez les coordonnées de l'événement sur l'image de la patinoire fournie**, comme dans l'exemple ci-dessous (vous pouvez simplement afficher les données de l'événement lorsqu'il n'y a pas de coordonnées). Vous pouvez également afficher toute information que vous jugez utile, comme les métadonnées du match/boxscores et les résumés d'événements (mais ce n'est pas obligatoire). **Prenez une capture d'écran de l'outil et ajoutez-la à l'article de blog**, accompagnée du **code de l'outil** et d'une brève description (1-2 phrases) de ce que fait votre outil. Vous n'avez pas à vous soucier d'intégrer l'outil dans l'article de blog.

***Remarque** : Un bon test de cohérence consiste à comparer un match spécifique avec les données disponibles sur le site web de la LNH, dont un exemple se trouve [ici](https://www.nhl.com/gamecenter/wpg-vs-tor/2017/10/04/2017020001/playbyplay). Vous remarquerez que les coordonnées des événements y sont aussi dessinées, ce qui vous permet de vérifier si vos figures sont valides. Pour vous inspirer, une capture d'écran de l'outil que j'ai rapidement créé se trouve ci-dessous. Mis à part la figure, vous n'avez pas besoin de reproduire cette mise en page ; n'hésitez pas à ajouter toute information que vous jugez utile\!*  
![Exemple d'ipywidget interactif](images/ipywidget-example.png)  
*Un exemple de widget interactif que vous pouvez créer pour explorer les données. Celui-ci a été créé avec de simples ipywidgets et matplotlib.*

### 3\. Données ordonnées (10%)

Maintenant que vous avez obtenu et un peu exploré les données, nous devons les formater de manière à faciliter la science des données (c.-à-d. ordonner les données, *tidy data*)\! Nous souhaitons généralement travailler avec de beaux dataframes Pandas plutôt qu'avec des données brutes ; votre tâche ici est donc de traiter les données brutes des événements de chaque match en dataframes utilisables pour les tâches suivantes.

Créez une fonction pour convertir tous les événements de chaque match en un dataframe pandas. Pour cette étape, vous devrez inclure les événements de type « **tirs** » et « **buts** ». Vous pouvez ignorer les **tirs manqués** et les **tirs bloqués** pour l'instant. Pour chaque événement, vous devrez inclure comme caractéristiques (au minimum) : le temps de jeu/la période, l'identifiant du match, l'information sur l'équipe (quelle équipe a effectué le tir), un indicateur si c'est un tir ou un but, les coordonnées sur la glace, le nom du tireur et du gardien de but (ne vous souciez pas des passes décisives pour l'instant), le type de tir, si le tir a été fait dans un filet désert, et si un but a été marqué à forces égales, en désavantage numérique ou en avantage numérique.

Utilisez une ligne par événement retenu, identifiée de manière unique par l'identifiant du match et l'identifiant de l'événement, et incluez la saison et le type de match. Conservez les valeurs non disponibles comme manquantes plutôt que de les traiter comme zéro ou faux. Excluez les valeurs manquantes seulement des analyses qui en ont besoin, et rapportez le nombre d'événements exclus.

**Questions**

1. Dans votre article de blog, **incluez un petit extrait** de votre dataframe final (ex. avec [head(10)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)). Vous pouvez simplement inclure une capture d'écran plutôt que de vous battre pour que les tableaux soient bien formatés en HTML/markdown.  
     
   Vous remarquerez que le champ « force » (c.-à-d. forces égales, avantage numérique, désavantage numérique) n'existe que pour les buts, pas pour les tirs. De plus, il n'inclut pas le nombre réel de joueurs sur la glace (c.-à-d. 5 contre 4, ou 5 contre 3, etc.). **Discutez** de la façon dont vous pourriez ajouter l'information réelle sur la force (c.-à-d. 5 contre 4, etc.) *aux tirs et aux buts*, compte tenu des autres types d'événements (au-delà des tirs et des buts) et des caractéristiques disponibles. Vous n'avez pas besoin de l'implémenter pour cette étape.

2. En quelques phrases, **discutez d'au moins 3 caractéristiques supplémentaires** que vous pourriez envisager de créer à partir des données disponibles dans cet ensemble de données. Nous ne cherchons pas de réponses particulières, mais si vous avez besoin d'inspiration : un tir ou un but pourrait-il être classé comme un [rebond](https://www.youtube.com/watch?v=-0FiO4jjFuA)/[tir en contre-attaque](https://www.youtube.com/watch?v=V2pjERKAc_8) (expliquez comment vous les identifieriez\!) ?  
   1. **[IFT6758 seulement]** Demandez à un LLM de générer la logique de transformation Pandas pour l'une de vos 3 caractéristiques (ex. rebond). En 2–3 phrases, évaluez l'exactitude et la gestion des cas limites du code généré par le LLM par rapport à votre implémentation manuelle.  
   2. **[IFT6758 seulement]** Refaites entièrement le nettoyage des données avec un LLM et comparez le résultat final et le code à votre méthode.

### 4\. Visualisations simples (25%)

Utilisons maintenant les données ordonnées pour créer quelques figures simples sur les données agrégées. Pour chacune des questions ci-dessous, vous devez faire un choix de figure approprié pour montrer la relation demandée. Il existe généralement plusieurs façons correctes de le faire \- si votre figure raconte la bonne histoire, vous obtiendrez tous les points.

**Questions**

1. **Produisez une figure** comparant les types de tirs de toutes les équipes (c.-à-d. agrégez simplement tous les tirs), pour une saison de votre choix. Superposez le nombre de buts au nombre de tirs. Quel semble être le type de tir le plus dangereux (le plus haut pourcentage de buts, pas le plus grand nombre de buts)? Le type de tir le plus courant? Pourquoi avez-vous choisi cette figure? Ajoutez cette figure et cette discussion à votre article de blog.  
     
2. Quelle est la relation entre la distance à laquelle un tir a été effectué et la chance qu'il s'agisse d'un but? **Produisez une figure** pour chaque saison entre 2018-19 et 2020-21 pour répondre à cette question, et ajoutez-la à votre article de blog avec quelques phrases décrivant votre figure. Y a-t-il eu beaucoup de changements au cours de ces trois saisons? Pourquoi avez-vous choisi cette figure?  
     
3. Combinez les informations des sections précédentes pour **produire une figure** qui montre le pourcentage de buts (100 × \# buts / \# tirs) en fonction à la fois de la distance par rapport au filet et de la catégorie de type de tir (vous pouvez choisir une seule saison de votre choix). **Discutez** brièvement de vos observations ; par ex., quels pourraient être les types de tirs les plus dangereux?  
4. **[IFT6758 seulement]** Mettez en place une interface de requêtes par LLM (avec des outils comme PandasAI, une approche *prompt-to-code* maison, ou des appels validés à vos propres fonctions Pandas) pour interroger votre ensemble de données ordonné en langage naturel. PandasAI vous permet de poser des questions sur les données à des LLM et intègre les LLM à d'autres composantes du pipeline, comme la visualisation de données et l'ingénierie de caractéristiques.  
   1. Vous concevrez des prompts et des outils qui permettent au LLM de comprendre des questions sur le hockey, de les convertir en requêtes structurées et de récupérer les réponses dans votre ensemble de données de la LNH.  
   2. Testez des requêtes en convertissant le langage naturel en code ou en appels de fonctions validés, par exemple : « Compare les pourcentages de buts sur tirs du poignet de Montréal et de Toronto en 2020-21 » en une requête que votre code Pandas peut exécuter. Privilégiez la réutilisation de vos fonctions d'analyse vérifiées. Si vous exécutez du code Python généré par un LLM, utilisez un environnement isolé, sans identifiants ni accès à des fichiers personnels.  
   3. Évaluez votre système sur un ensemble fixe de **8 questions d'évaluation**, rédigées avant de commencer à ajuster vos prompts et jamais utilisées pour le développement des prompts. Elles doivent couvrir le filtrage, le regroupement, les pourcentages de buts, les graphiques, et au moins une question à laquelle l'ensemble de données ne permet pas de répondre (ex. sur les passes, qui ne sont pas suivies). Comparez chaque résultat à une réponse de référence que vous avez vérifiée manuellement ; un graphique est correct s'il montre les quantités, le regroupement et la saison demandés. Pour les questions sans réponse possible, le système doit indiquer qu'il ne peut pas répondre plutôt qu'inventer un résultat. **Présentez un tableau** indiquant, pour chaque question : si la première tentative s'est exécutée avec succès, si la réponse/le graphique final est correct, et le nombre de nouvelles tentatives. Discutez d'un succès et d'un échec ou d'une limite ; si aucun échec ne survient, testez une requête supplémentaire plus difficile et discutez-en.

### 5\. Visualisations avancées : cartes de tirs (30%)

Le dernier ensemble de visualisations que vous créerez sont des cartes de tirs pour une équipe donnée de la LNH, pour une année et une saison données. Un excellent exemple de ces graphiques, avec une description détaillée de comment les lire, se trouve sur le [site web de hockeyviz](https://hockeyviz.com/howto/shotMap) (qui est une excellente ressource pour beaucoup de choses en science des données appliquée au hockey). Notez que vous devrez créer ces figures à partir de zéro ; pour cette étape, vous ne pouvez utiliser aucune bibliothèque qui génère des figures spécifiques au domaine (hockey) pour vous. Vous recevrez un exemple d'image de patinoire ayant le bon ratio.

Pour créer ces figures, vous devez :

1. Vous assurer que vous pouvez travailler correctement avec les coordonnées des événements. Cela inclut de vous assurer que les tirs sont du bon côté de la patinoire (en raison des changements de période, ou parce que les équipes commencent de côtés différents pendant un match), ainsi que de pouvoir convertir les coordonnées physiques en coordonnées de pixels sur la figure.  
2. Calculer des statistiques agrégées des emplacements de tirs pour l'ensemble de la ligue afin d'obtenir le *taux de tirs moyen par heure de la ligue*. Pour chaque zone (*bin*) spatiale, divisez le nombre de tirs de toutes les équipes par `2 * nombre de matchs de la ligue` pour cette saison : chaque match contribue deux heures-équipe selon l'hypothèse de 60 minutes. Vous pouvez faire quelques hypothèses simplificatrices :  
   - Vous pouvez supposer que tous les tirs sont à forces égales ; cela signifie que vous pouvez simplement agréger tous les tirs plutôt que de déterminer si un tir a été effectué à forces égales ou non (rappel : Q 4.2).  
   - Vous pouvez supposer que chaque match dure 60 minutes.  
3. Regrouper les tirs par équipe et utiliser le *taux de tirs moyen par heure* de la ligue calculé ci-dessus pour calculer le *taux de tirs excédentaire par heure*. Pour chaque zone, divisez le nombre de tirs de l'équipe par son nombre de matchs dans cette saison, puis soustrayez le taux de la ligue pour cette zone. Rapportez la différence brute en **tirs par heure-équipe**.  
4. Faire des choix appropriés pour regrouper (*binning*) vos données lors de leur affichage. Vous pouvez également envisager d'utiliser des techniques de lissage pour rendre vos cartes de tirs plus lisibles. Une stratégie courante consiste à utiliser l'estimation par noyau (*kernel density estimation*) avec un noyau gaussien.  
5. Rendre le graphique interactif, avec des options pour sélectionner l'**équipe**. La façon la plus simple de le faire est d'utiliser un outil comme plotly ou bokeh. Une petite démo simple de ce que vous pouvez faire avec plotly se trouve [ici](https://plotly.com/python/dropdowns/).  
6. Produire **une figure interactive pour chaque saison de 2016-17 à 2020-21** (inclusivement). Vous devez **seulement créer les figures de la zone offensive** ; vous n'avez rien à faire pour la zone défensive. Comme mentionné ci-dessus, vous pouvez aussi ignorer si un événement s'est produit lors d'un avantage ou d'un désavantage numérique.

[![Exemple de carte de tirs offensive de hockeyviz](images/hockeyviz-shot-map.png)](https://hockeyviz.com/howto/shotMap)  
*Source : [www.hockeyviz.com](http://www.hockeyviz.com). Exemple de carte de tirs offensive pour les Sharks de San Jose, pour la saison 2017-2018. Vous **n'avez pas** besoin de calculer le xGF/60 ni le nombre de minutes passées en zone offensive.*

**Questions**

1. [Exportez les 4 graphiques de zone offensive en HTML](https://plotly.com/python/interactive-html-export/) et **intégrez-les dans votre article de blog**. Votre graphique doit permettre aux utilisateurs de sélectionner n'importe quelle équipe pour la saison sélectionnée.  
   ***Note** : Puisque vous pouvez trouver ces figures sur Internet, répondre à ces questions sans produire ces figures* ne *vous rapportera aucun point\!*  
     
2. **Discutez** (en quelques phrases) de ce que vous pouvez interpréter à partir de ces graphiques.  
     
3. Considérez l'Avalanche du Colorado ; regardez leur carte de tirs pendant la saison 2016-17. **Discutez** de ce que vous pourriez dire sur l'équipe pendant cette saison. Regardez maintenant la carte de tirs de l'Avalanche du Colorado pour la saison 2020-21, et **discutez** de ce que vous pourriez conclure de ces différences. Est-ce que cela a du sens? *Indice : regardez le classement*.  
     
4. Considérez les Sabres de Buffalo, une équipe qui a connu des difficultés ces dernières années, et comparez-les au Lightning de Tampa Bay, une équipe qui a remporté la coupe Stanley deux années de suite. Regardez les cartes de tirs de ces deux équipes pour les saisons 2018-19, 2019-20 et 2020-21. **Discutez** des observations que vous pouvez faire. Y a-t-il quelque chose qui pourrait expliquer le succès du Lightning, ou les difficultés des Sabres? Dans quelle mesure pensez-vous que ces figures donnent un portrait complet?

***Remarque** : le but de cet exercice est de vous familiariser avec l'utilisation des bibliothèques Python standards pour créer des visualisations. Vous ne pouvez pas utiliser d'outil qui crée pour vous des visualisations spécifiques au domaine (c.-à-d. le hockey). Vous êtes libres d'utiliser des bibliothèques standards (matplotlib, seaborn, plotly, bokeh, etc.) pour générer ces graphiques.*

## Évaluations de groupe

En plus de l'évaluation décrite ci-dessus, pour chaque étape, il vous sera demandé d'évaluer la contribution de chacun à cette étape et de fournir une rétroaction constructive à vos coéquipiers, en fonction de leurs forces et de leurs axes d'amélioration potentiels. Les étudiant·e·s qui contribuent peu risquent d'obtenir une mauvaise note et, dans les cas extrêmes, pourraient être retirés du groupe et invités à réaliser les projets individuellement.

Pour une équipe de taille **N**, chaque membre de l'équipe disposera de **N x 20** points à répartir entre tous les membres du groupe (y compris vous-même). Vous attribuerez ensuite à chacun un score entre **10 et 40**, où **10** correspond à un « demi-effort » et **40** à un « effort double ». Dans une situation idéale, tout le monde contribue de manière égale au projet et chacun attribue donc 20 points à chaque coéquipier. Cependant, si certaines personnes ont moins contribué que d'autres, vous pourriez leur attribuer moins de points et donner ces points à celles qui, selon vous, ont davantage contribué. Les cas extrêmes entraîneront un suivi de la part d'un instructeur avec l'équipe pour résoudre toute difficulté potentielle. Cela pourrait inclure un audit de l'historique git de vos dépôts. *Toute tentative de manipuler le système sera traitée manuellement et de manière défavorable\!*

En plus du score, vous donnerez également une **brève rétroaction à vos pairs**, à la fois sur leurs forces et sur leurs axes d'amélioration potentiels. Cette rétroaction sera transmise de manière privée et anonyme à chaque étudiant·e. Vous pouvez donner votre avis selon plusieurs axes, comme leur **travail d'équipe** (communication, fiabilité) et leur **travail technique** (leur contribution et la qualité de leur travail/code). Si vous donnez un score inférieur à 20, vous devez donner une rétroaction constructive sur les aspects à améliorer.

### Comment les scores influencent votre note

* **x** est le score moyen d'un·e étudiant·e (en excluant son propre score), borné entre 10 (« demi-effort ») et 40 (« effort double »).  
* La note d'un·e étudiant·e pour l'étape sera multipliée par le facteur de pondération suivant[^2] :

**Scaling**(**x**) \= 0.41667 \+ 0.0375**x** \- 0.00041667**x**²

* Ce système a été adopté de [Brian Fraser (SFU)](https://opencoursehub.cs.sfu.ca/bfraser/grav-cms/cmpt276/project), qui est lui-même basé sur les [travaux de Bill Gardner](http://www.cs.ubc.ca/wccce/Program03/papers/Gardner-Group/Gardner-Group.htm).

![Exemple de pondération de l'évaluation par les pairs](images/peer-eval-scaling.png)

Votre note finale sera ensuite multipliée par ce facteur de pondération. À titre d'exemple, voici un cas non idéal où la charge de travail n'a pas été répartie équitablement dans le groupe. Prenons un groupe de 4 personnes (**A**, **B**, **C** et **D**) dont la note finale du projet était de 95 % et où tout le monde a donné 20 points à la **personne A**. Sa note ne serait pas affectée (rappelez-vous que votre propre score est exclu) :

**Scaling**((**20** \+ **20** \+ **20**) / 3\) \= 1 \* 95% \= 95%

Cependant, pour ce même groupe, si la **personne B** n'a pas autant contribué, sa note finale pourrait en souffrir :

**Scaling**((**15** \+ **14** \+ **15**) / 3\) \= 0.88 \* 95% \= 83.3%

Peut-être que les **personnes C** et **D** ont compensé, et leurs scores le reflètent \- leurs notes finales pourraient ainsi être rehaussées. Cet exemple est résumé dans le tableau ci-dessous.

En général, nous ne nous attendons pas à ce que les équipes aient des problèmes. Nous espérons qu'en établissant une méthode claire pour s'évaluer mutuellement et en montrant comment cela peut directement affecter votre note, chacun sera incité à coopérer et à contribuer également au projet. En cas de conflit ou de préoccupation au sein du groupe, nous vous encourageons à essayer de le résoudre le plus rapidement possible. Si vous avez besoin du soutien des instructeurs pour résoudre un problème ou une préoccupation, veuillez nous contacter le plus tôt possible.

| Tableau 1 : Exemple d'évaluations de groupe pour une équipe de 4 ayant obtenu 95 % pour cette étape. |  |  |  |  |
| :---- | :---: | :---: | :---: | :---: |
| (vertical) Personne qui a donné le score | (horizontal) Personne à qui le score est attribué |  |  |  |
|  | **A** | **B** | **C** | **D** |
| **A** | 20 | 15 | 21 | 24 |
| **B** | 20 | 15 | 22 | 23 |
| **C** | 20 | 14 | 22 | 24 |
| **D** | 20 | 15 | 21 | 24 |
| **Facteur** | 1.0 | 0.88 | 1.03 | 1.07 |
| **Note finale** | 95% | 83.3% | 97.6% | 101.7**%** |

## Références utiles

**Contenu du cours**

* [IFT6758 Hockey Primer](https://docs.google.com/document/d/1CP4dbReUdLMwtmnU8_lEQDawrh5LkbDuGDM9Sqza6ZA/edit?usp=sharing)  
* [Modèle d'article de blog IFT6758](https://github.com/milarobotlearningcourse/data_science_blog)  
* [Modèle de projet IFT6758](https://github.com/milarobotlearningcourse/data_science_project)

**Documentation de l'API**

* [Zmalski's NHL API Reference](https://github.com/Zmalski/NHL-API-Reference) \- documentation incomplète de la **nouvelle API**  
* [dword4's NHL API Doc](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md) \- une autre référence incomplète pour la **nouvelle API**  
* [Documentation non officielle de l'API de la LNH (ancienne)](https://gitlab.com/dword4/nhlapi/) \- **ancienne API** \- ne fonctionne plus, mais certains formats, comme celui du GAME\_ID, sont toujours valides

**Divers**

* [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) \- un outil utile pour structurer vos dépôts git

[^1]: Une mise en garde concernant GitHub Pages : même si votre dépôt est privé, les pages publiées sont publiques. Vous ne pourrez peut-être même pas publier une page à partir d'un dépôt privé si vous n'avez pas obtenu votre compte GitHub Pro étudiant gratuit. Comme nous ne voulons pas que les groupes puissent voir les pages des autres pendant qu'ils travaillent sur le projet, vous ne devriez pas publier les pages que vous créez, mais plutôt les générer localement.

[^2]: *Les coefficients sont obtenus en ajustant la fonction quadratique y(x) \= a**x**² \+ b**x** \+ c aux points **x** \= 10 → poids \= 0.75 ; **x** \= 20 → poids \= 1.0 ; **x** \= 40 → poids \= 1.25.*
