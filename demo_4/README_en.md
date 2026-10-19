# Demo 4: validating, measuring uncertainty, and putting it all together

[Version française](README.md)

This demo is meant for **self-study**. The first two notebooks introduce the tools for evaluating a model honestly: cross-validation, hyperparameter search, pipelines and bootstrap confidence intervals. The third brings them together in a complete project that predicts which *Titanic* passengers survived.

## Notebooks

| Notebook | What you learn and do | English | Français |
|---|---|---|---|
| **01 — Validation and hyperparameter search** | See why a single data split is not enough. Use (stratified) cross-validation, tune an SVM with `GridSearchCV` and `RandomizedSearchCV`, then chain PCA and logistic regression in a `Pipeline` without data leakage. | [Open](notebooks/en/01_validation_and_hyperparameter_search.ipynb) | [Ouvrir](notebooks/fr/01_validation_and_hyperparameter_search.ipynb) |
| **02 — Bootstrap confidence intervals** | Resample with replacement, use the out-of-bag rows as a test set, compute a confidence interval for a classifier's accuracy and for a regression slope, and compare it with the classical formula. | [Open](notebooks/en/02_bootstrap_confidence_intervals.ipynb) | [Ouvrir](notebooks/fr/02_bootstrap_confidence_intervals.ipynb) |
| **03 — Titanic, end to end** | Explore the data, engineer features, gather preprocessing in one function, compare eight classifiers, combine them in a vote, validate with cross-validation, and produce a Kaggle submission file. Six exercises (Q1 to Q6) with reference answers. | [Open](notebooks/en/03_titanic_end_to_end.ipynb) | [Ouvrir](notebooks/fr/03_titanic_end_to_end.ipynb) |

Follow the order of the table: notebook 03 reuses ideas from notebooks 01 and 02 (exercises Q4 and Q6 depend on them). Each exercise has an empty cell for your work and a **reference answer** to open after trying.

## Setup and data

Use the shared environment described in the [repository README](../README_en.md): `git pull`, then `uv sync` from the root. This demo adds **seaborn** to the dependencies, so run `uv sync` again if your environment predates demo 4. The notebooks also work in Google Colab: follow the setup section at the top of each one.

The datasets ship in [`datasets/`](datasets/), so nothing needs to be downloaded locally.

| File | Contents | Used in |
|---|---|---|
| `titanic-train.csv` | 891 passengers with the target `Survived` | 03 |
| `titanic-test.csv` | 418 passengers without the target (scored by Kaggle) | 03 |
| `diabetes.csv` | Pima Indians diabetes: 768 patients, 8 measurements and the target (no header row) | 02 |
| `sat-gpa.csv` | SAT score and university GPA of 84 students | 02 |

The handwritten digits in notebook 01 come with scikit-learn. Notebook 03 saves its submission file to `data/processed/titanic_submission.csv` at the repository root (a folder ignored by Git). Submitting to [Kaggle](https://www.kaggle.com/c/titanic) is optional and requires a free account.

These notebooks come from IFT6758 labs 5 and 6 (2020 and 2022), updated for current versions of pandas, scikit-learn and seaborn. The originals remain in the previous-labs archive.

<sub>Prepared by Jaydan Aladro</sub>
