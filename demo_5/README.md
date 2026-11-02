# Démo 5 : construire un GPT à partir de zéro

[English version](README_en.md)

Cette démo construit un Transformer ligne par ligne, avec seulement PyTorch et ses briques de base, puis l’entraîne à écrire du faux Shakespeare. Elle suit la vidéo d’Andrej Karpathy, [*Let’s build GPT: from scratch, in code, spelled out*](https://www.youtube.com/watch?v=kCc8FmEb1nY), et l’article [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762). Nous construisons le **décodeur** de l’article, comme GPT.

## À regarder

Ces deux vidéos de 3Blue1Brown donnent l’intuition visuelle que le notebook rend ensuite concrète :

1. [Transformers, the tech behind LLMs (chapitre 5)](https://www.youtube.com/watch?v=wjZofJX0v4M), avant de commencer.
2. [Attention in transformers, step-by-step (chapitre 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc), avant la section C.

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — Un GPT à partir de zéro** | [Ouvrir](notebooks/fr/01_gpt_from_scratch.ipynb) | [Ouvrir dans Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_5/notebooks/fr/01_gpt_from_scratch.ipynb) | À venir |

| Section | Contenu | Durée indicative |
|---|---|---|
| Introduction | Objectifs, vidéos et schéma de l’architecture | 5 min |
| A. Du texte aux nombres | Corpus, tokeniseur par caractères, séparation entraînement/validation, batchs | 10 min |
| B. Le bigramme | Modèle de référence, entropie croisée, génération, évaluation | 15 min |
| C. L’attention | De la moyenne à l’auto-attention : `tril`, softmax, requêtes, clés et valeurs, mise à l’échelle | 35 min |
| D. Vers le Transformer | Têtes multiples, *feed-forward*, blocs, connexions résiduelles, normalisation et dropout, chaque ajout étant mesuré | 30 min |
| E. Notre GPT | Modèle complet, courbes, génération, poids d’attention | 15 min |
| F. Retour à l’article | Différences avec l’article et lien avec ChatGPT | 5 min |
| G. Et pour les images ? | Un Vision Transformer sur des chiffres manuscrits, avec les mêmes blocs | 5 min |

Le notebook compte cinq exercices **À vous**, chacun avec une réponse de référence à ouvrir après avoir essayé. Si le temps manque, la section G peut se lire à la maison.

## Configuration et données

Le notebook fonctionne sur macOS, Linux et Windows, sans carte graphique. **Google Colab est le plus simple :** rien à installer, et un GPU gratuit accélère les entraînements. Sinon, utilisez l’environnement commun décrit dans le [README du dépôt](../README.md), avec le groupe de dépendances de cette démo :

```sh
git pull --ff-only
uv sync --group gpt
```

Sur Linux, PyTorch télécharge aussi les bibliothèques CUDA (environ 5 Go), même sans carte NVIDIA : préférez alors Colab si votre connexion ou votre disque sont limités.

Un CPU suffit : sur un ordinateur portable récent, le notebook complet s’exécute en moins de 5 minutes, dont environ 1 min 30 pour le plus gros modèle. Un CPU moins rapide prendra plus de temps. La configuration complète de la section E, facultative, demande un GPU.

`datasets/input.txt` est le fichier *Tiny Shakespeare* du dépôt de Karpathy, copié tel quel : environ un million de caractères tirés de pièces de Shakespeare. Le modèle écrit donc en anglais, même si le notebook est en français. Sur Colab, le notebook le télécharge directement depuis le [dépôt de Karpathy](https://github.com/karpathy/ng-video-lecture).

Le code s’inspire de [`ng-video-lecture`](https://github.com/karpathy/ng-video-lecture) d’Andrej Karpathy (licence MIT). Il remplace l’ancien laboratoire sur les Transformers, qui s’arrêtait avant la fin du modèle.

<sub>Préparé par Jaydan Aladro</sub>
