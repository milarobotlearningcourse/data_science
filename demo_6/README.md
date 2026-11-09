# Démo 6 : les images comme données, des filtres aux réseaux convolutifs

[English version](README_en.md)

Pour un ordinateur, une photo n’est qu’un tableau de nombres. Cette démo part de ces nombres : avec OpenCV, nous les transformons, nous les filtrons et nous en tirons des **caractéristiques** (contraste, contours, gradients), comme en vision par ordinateur classique. Elle se termine par un petit **réseau convolutif** entraîné sur des chiffres manuscrits : il apprend des filtres semblables aux nôtres, et nous mesurons ce que nos outils lui apportent quand les données étiquetées manquent. Elle accompagne les cours 16 et 16b sur la vision par ordinateur.

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — Des filtres aux réseaux convolutifs** | [Ouvrir](notebooks/fr/01_caracteristiques_images_cnn.ipynb) | [Ouvrir dans Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_6/notebooks/fr/01_caracteristiques_images_cnn.ipynb) | À venir |

| Section | Contenu | Durée indicative |
|---|---|---|
| Introduction | Objectifs, traitement d’images et vision par ordinateur, la chaîne de traitement | 5 min |
| A. Une image, c’est un tableau | Pixels et canaux, type `uint8`, lecture avec OpenCV et piège du BGR, espace HSV | 10 min |
| B. Transformer chaque pixel | Opérations ponctuelles, histogrammes, seuillage (Otsu, adaptatif), morphologie pour compter des pièces | 10 min |
| C. Filtrer : la convolution | Moyenne mobile à la main, galerie de noyaux, débruitage, corrélation et convolution, filtres séparables, équivariance | 15 min |
| D. Les contours, une première caractéristique | Dérivée d’un profil, lisser avant de dériver, Sobel, orientation du gradient, Canny | 12 min |
| E. Déformer et augmenter | Interpolation, rotation, perspective, augmentation de données | 8 min |
| F. Des caractéristiques à un réseau convolutif | Les pixels comme caractéristiques, Sobel comme couche PyTorch, un CNN sur MNIST, ses filtres, l’augmentation et nos filtres avec 500 étiquettes | 20 min |

Le notebook compte quatre exercices **À vous**, chacun avec une réponse de référence à ouvrir après avoir essayé : BGR → RGB à la main, écrire la convolution, Cutout, et nos filtres comme première couche du réseau. Le premier et le troisième viennent de l’ancien laboratoire 9 d’IFT6758 (2020).

## Configuration et données

Le notebook fonctionne sur macOS, Linux et Windows, sans carte graphique. **Google Colab est le plus simple :** OpenCV, scikit-image et PyTorch y sont déjà installés. Sinon, utilisez l’environnement commun décrit dans le [README du dépôt](../README.md), avec le groupe de dépendances de cette démo :

```sh
git pull --ff-only
uv sync --group vision
```

Les sections A à E n’ont besoin que d’OpenCV et de scikit-image, ajoutés aux dépendances communes : `uv sync` suffit. Le groupe `vision` ajoute PyTorch et torchvision pour la section F. Sur Linux, PyTorch télécharge aussi les bibliothèques CUDA (environ 5 Go), même sans carte NVIDIA : préférez alors Colab si votre connexion ou votre disque sont limités.

Les images des sections A à E viennent de `skimage.data` et sont fournies avec scikit-image : aucun téléchargement. La section F télécharge les chiffres [MNIST](https://yann.lecun.com/exdb/mnist/) (environ 12 Mo) dans `data/raw/`, à la racine du dépôt (dossier ignoré par Git). L’entraînement complet de la section F prend environ une minute sur un ordinateur portable récent.

<sub>Préparé par Jaydan Aladro</sub>
