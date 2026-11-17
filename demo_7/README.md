# Démo 7 : un micro VLM, poser une question à une photo

[English version](README_en.md)

Un **modèle vision-langage** (VLM) reçoit une image et du texte, et répond par du texte. Cette démo en construit un tout petit à partir du GPT de la [démo 5](../demo_5/README.md) : d’abord un **Vision Transformer** qui lit une image découpée en morceaux, puis un modèle qui place l’image et la question dans une même séquence et écrit la réponse, un caractère à la fois. Le code vient du dépôt [`micro_vlm`](https://github.com/milarobotlearningcourse/micro_vlm) du cours, adapté du nanoGPT d’Andrej Karpathy.

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — Un micro VLM** | [Ouvrir](notebooks/fr/01_micro_vlm.ipynb) | [Ouvrir dans Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_7/notebooks/fr/01_micro_vlm.ipynb) | À venir |

| Section | Contenu |
|---|---|
| Introduction | Ce que nous construisons, le parcours en quatre étapes, le plan |
| 1. Préparer les données | Photos à 64 × 64, questions et réponses, caractères comme tokens |
| 2. Du Transformer (nanoGPT) au ViT | Encodeur sans masque, patches, positions, token de classe, un ViT qui s’entraîne |
| 3. Les modèles vision-langage (VLM) | Le texte dans la même séquence que l’image, masque par blocs, *padding*, batchs de sous-chaînes |
| 4. Entraîner le modèle | Réglages, perte de départ, un court entraînement suivi en direct |
| 5. Encoder le texte avec T5 | Ce que les vrais VLM réutilisent (sans code) |
| 6. Générer des réponses | Poser des questions sur des photos jamais vues, comparer à une réponse donnée sans regarder la photo |

Le notebook contient huit blocs marqués `TODO`, que nous complétons ensemble pendant la séance. Tant qu’un bloc n’est pas rempli, les cellules qui en dépendent échouent. Le [corrigé](notebooks/fr/01_micro_vlm_solution.ipynb) est le même notebook, avec les huit blocs remplis.

## Configuration et données

**Google Colab est le plus simple :** choisissez un GPU, et la première cellule installe les deux petits paquets qui manquent (`python-box` et `einops`). Sinon, utilisez l’environnement commun décrit dans le [README du dépôt](../README.md), avec le groupe de dépendances de cette démo :

```sh
git pull --ff-only
uv sync --group vlm
```

Le notebook choisit tout seul un GPU NVIDIA, sinon le GPU d’un Mac récent, sinon le CPU. Sur Linux, PyTorch télécharge aussi les bibliothèques CUDA (environ 5 Go), même sans carte NVIDIA : préférez alors Colab si votre connexion ou votre disque sont limités.

Les données sont une copie à 64 × 64 pixels de [VQAv2-small](https://huggingface.co/datasets/merve/vqav2-small) : [`gberseth/vqav2-small-64px`](https://huggingface.co/datasets/gberseth/vqav2-small-64px), 21 388 questions, 266 Mo, téléchargés une fois dans le cache de Hugging Face. Le fichier [`conf/micro-vlm-64pix.yaml`](conf/micro-vlm-64pix.yaml) est celui du dépôt d’origine, sans changement.

<sub>Préparé par Jaydan Aladro, à partir du dépôt `micro_vlm` du cours</sub>
