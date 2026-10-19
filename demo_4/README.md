# Démo 4 : valider, mesurer l’incertitude et tout mettre ensemble

[English version](README_en.md)

Cette démo est à faire **en autonomie**. Les deux premiers notebooks présentent les outils pour évaluer un modèle honnêtement : la validation croisée, la recherche d’hyperparamètres, les pipelines et les intervalles de confiance par bootstrap. Le troisième les réunit dans un projet complet de prédiction de la survie des passagers du *Titanic*.

## Notebooks

| Notebook | Ce qu’on apprend et réalise | Français | English |
|---|---|---|---|
| **01 — Validation et recherche d’hyperparamètres** | Voir pourquoi une seule séparation des données ne suffit pas. Utiliser la validation croisée (stratifiée), régler un SVM avec `GridSearchCV` et `RandomizedSearchCV`, puis enchaîner PCA et régression logistique dans un `Pipeline` sans fuite de données. | [Ouvrir](notebooks/fr/01_validation_and_hyperparameter_search.ipynb) | [Open](notebooks/en/01_validation_and_hyperparameter_search.ipynb) |
| **02 — Intervalles de confiance par bootstrap** | Rééchantillonner avec remise, utiliser les observations hors sac comme ensemble de test, calculer un intervalle de confiance pour l’accuracy d’un classifieur et pour la pente d’une régression, puis le comparer à la formule classique. | [Ouvrir](notebooks/fr/02_bootstrap_confidence_intervals.ipynb) | [Open](notebooks/en/02_bootstrap_confidence_intervals.ipynb) |
| **03 — Titanic, de bout en bout** | Explorer les données, créer des variables, regrouper le prétraitement dans une fonction, comparer huit classifieurs, combiner un vote, valider par validation croisée et produire un fichier de soumission Kaggle. Six exercices (Q1 à Q6) avec réponses de référence. | [Ouvrir](notebooks/fr/03_titanic_end_to_end.ipynb) | [Open](notebooks/en/03_titanic_end_to_end.ipynb) |

Suivez l’ordre du tableau : le notebook 03 réutilise les notions des notebooks 01 et 02 (les exercices Q4 et Q6 en dépendent). Chaque exercice comporte une cellule vide pour votre travail et une **réponse de référence** à ouvrir après avoir essayé.

## Configuration et données

Utilisez l’environnement commun décrit dans le [README du dépôt](../README.md) : `git pull`, puis `uv sync` à la racine. Cette démo ajoute **seaborn** aux dépendances; relancez donc `uv sync` si votre environnement date d’avant la démo 4. Les notebooks fonctionnent aussi dans Google Colab : suivez la section de configuration au début de chacun.

Les jeux de données sont fournis dans [`datasets/`](datasets/) : aucun téléchargement n’est nécessaire en local.

| Fichier | Contenu | Utilisé dans |
|---|---|---|
| `titanic-train.csv` | 891 passagers avec la variable cible `Survived` | 03 |
| `titanic-test.csv` | 418 passagers sans la cible (évalués par Kaggle) | 03 |
| `diabetes.csv` | Diabète des Indiens Pima : 768 patientes, 8 mesures et la cible (sans ligne d’en-tête) | 02 |
| `sat-gpa.csv` | Score SAT et moyenne universitaire (GPA) de 84 étudiants | 02 |

Les chiffres manuscrits du notebook 01 sont fournis par scikit-learn. Le notebook 03 enregistre le fichier de soumission dans `data/processed/titanic_submission.csv`, à la racine du dépôt (dossier ignoré par Git). Soumettre à [Kaggle](https://www.kaggle.com/c/titanic) est facultatif et nécessite un compte gratuit.

Ces notebooks proviennent des laboratoires 5 et 6 d’IFT6758 (2020 et 2022), mis à jour pour les versions actuelles de pandas, scikit-learn et seaborn. Les originaux restent dans les archives des anciens laboratoires.

<sub>Préparé par Jaydan Aladro</sub>
