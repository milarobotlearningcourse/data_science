# IFT3700 / IFT6758: Demonstrations and Project

This repository contains the course demonstrations and the project milestone guidelines. We will publish new exercises, solutions and guidelines here as the course progresses.

**One Python environment for all demos: run `uv sync` at the root of `ift3700-6758`.** Dependencies are declared in the shared `pyproject.toml`, and their versions are recorded in `uv.lock`. Every demo uses the same `.venv` at the repository root.

The environment uses **Python 3.11**, NumPy 1.26.4, and pandas 1.5.3 for compatibility with PandasAI 2.3.2. For the **RAG and PandasAI** sections of Demo 2, use `uv sync --group llm` instead of `uv sync` to add the dependencies for local models. The other demos do not need them.

## Initial setup

Install **Git** and **uv**. To work in your IDE, also install the **Python** and **Jupyter** extensions.

To install uv on macOS / Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows, in PowerShell:

```powershell
winget install --id=astral-sh.uv -e
```

Reopen the terminal after installation, then check:

```sh
git --version
uv --version
```

Clone the repository once, then install the shared dependencies:

```sh
cd <directory of your choice>
git clone https://github.com/milarobotlearningcourse/data_science.git ift3700-6758
cd ift3700-6758
uv sync
```

`uv sync` creates `.venv` and installs the packages needed for the demos, including notebook tools. uv can download a compatible Python interpreter if needed. The initial installation requires an Internet connection. You do not need to run `uv init`, create a separate environment for each demo, or install packages one by one.

## Before each session: get the latest updates

In a terminal at the root of `ift3700-6758`, run:

```sh
git pull --ff-only
uv sync
```

Do this regularly, especially when a new demo or correction is announced. `git pull` retrieves the files published on GitHub; `uv sync` updates the shared environment if dependencies have changed. You do not need to clone the repository again.

To keep your answers without modifying the distributed notebooks, copy them into a `travail_personnel/` folder at the repository root. This folder is ignored by Git and uses the same environment. If Git refuses a `pull` because you have modified a tracked file, back up your work before resolving the conflict; do not delete your answers to force the update.

## Opening the notebooks

### With VS Code

1. Open the **entire `ift3700-6758` folder**.
2. From the command palette, choose **Python: Select Interpreter**, then select the Python interpreter in **`ift3700-6758/.venv`**.
3. Open the notebook you want in the demo folder.
4. Click **Select Kernel → Python Environments** and choose that same `.venv`.

All demos use this kernel. After updating packages, restart the notebook kernel.

### With JupyterLab in the browser

From the repository root:

```sh
uv run jupyter lab
```

Then open the notebook you want. Stop the server with `Ctrl+C` in the terminal. `uv run` uses the repository's environment without manual activation.

## The demonstrations

| Folder | Contents | Suggested order |
|---|---|---|
| [Demo 1](demo_1/README.md) | Python environments, Git, NumPy, pandas, and a first machine learning example | Notebooks `00`, `01`, `02`, then `03` |
| [Demo 2](demo_2/README.md) | NHL API and cleaning; interactive exploration and visualization (French/English); RAG and PandasAI with local Qwen (English) | Notebooks `01`, `02`, then `04` and `05` (optional, `llm` group) |
| [Previous labs](anciens_labs/README.md) | Materials from previous years, organized by topic and language | See the catalog and compatibility notes |
| [Git tutorials](tutoriels/git/README.md) | French/English slide decks and a hands-on notebook | Standalone resource |
| Python tutorials ([French](tutoriels/python/fr/python.ipynb), [English](tutoriels/python/en/python.ipynb)) | Variables, data structures, functions, and exercises | Standalone introduction |

Demo 1 offers the same lessons in [French](demo_1/notebooks/fr/) and [English](demo_1/notebooks/en/), along with a [slide deck in French](demo_1/intro_data_science_demo_fr.pptx). New demos will be added to this table as the course progresses.

Previous labs are kept as historical references: some APIs, dependencies, and data still need to be adapted before they can be used as active demos with the shared environment. Their catalog specifies the selected versions and available solutions.

The [manual setup workshop](demo_1/python/README_fr.md) explains `venv`, pip, and uv. To use the course notebooks, the `git pull` followed by `uv sync` procedure above is sufficient.

## The project

The guidelines for each project milestone are published in a dedicated folder, in French and English.

| Milestone | Contents | Guidelines |
|---|---|---|
| Milestone 1 | Acquiring and cleaning NHL play-by-play data, an interactive debugging tool, simple visualisations and shot maps; LLM/RAG parts for IFT6758 only | [English](milestone-1/README_en.md) · [French](milestone-1/README_fr.md) |

Parts marked **[IFT6758 only]** in the guidelines do not apply to IFT3700.

## Adding a demo

Add the files in a dedicated folder, then update the table above. If an additional library is needed, run `uv add package-name` **at the repository root** and include `pyproject.toml` and `uv.lock` in the same commit as the demo. For development tools, use `uv add --dev package-name`.

Keep a single uv project at the root: demo folders must not contain their own `pyproject.toml`, `uv.lock`, or `.venv`. Check new notebooks with the shared environment before publishing.

Documentation: [uv installation](https://docs.astral.sh/uv/getting-started/installation/) · [uv projects](https://docs.astral.sh/uv/guides/projects/)

<sub>Prepared by Jaydan Aladro</sub>
