# Demo 7: a micro VLM, asking a photo a question

[Version française](README.md)

A **vision language model** (VLM) takes an image and text, and answers with text. This demo builds a very small one from the GPT of [Demo 5](../demo_5/README_en.md): first a **Vision Transformer** that reads an image cut into patches, then a model that puts the image and the question in one sequence and writes the answer, one character at a time. The code comes from the course’s [`micro_vlm`](https://github.com/milarobotlearningcourse/micro_vlm) repository, adapted from Andrej Karpathy’s nanoGPT.

**The notebook is available in French for now. The English version will follow.**

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — A micro VLM** | [Open](notebooks/fr/01_micro_vlm.ipynb) | [Open in Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_7/notebooks/fr/01_micro_vlm.ipynb) | Coming soon |

| Section | Content |
|---|---|
| Introduction | What we build, the flow in four steps, the outline |
| 1. Preparing the data | Photos at 64 × 64, questions and answers, characters as tokens |
| 2. From the Transformer (nanoGPT) to the ViT | Encoder without a mask, patches, positions, class token, a ViT that trains |
| 3. Vision language models (VLM) | Text in the same sequence as the image, block mask, padding, batches of sub-strings |
| 4. Training the model | Settings, starting loss, a short run followed live |
| 5. Encoding text with T5 | What real VLMs reuse (no code) |
| 6. Generating answers | Asking questions about unseen photos, comparing with an answer given without looking at the photo |

The notebook has eight blocks marked `TODO`, which we fill in together during the session. Until a block is filled in, the cells that depend on it fail. The [solution notebook](notebooks/fr/01_micro_vlm_solution.ipynb) is the same notebook with the eight blocks filled in.

## Setup and data

**Google Colab is the easiest option:** pick a GPU, and the first cell installs the two small packages that are missing (`python-box` and `einops`). Otherwise, use the shared environment described in the [repository README](../README_en.md), with this demo’s dependency group:

```sh
git pull --ff-only
uv sync --group vlm
```

The notebook picks an NVIDIA GPU if there is one, otherwise the GPU of a recent Mac, otherwise the CPU. On Linux, PyTorch also downloads the CUDA libraries (about 5 GB), even without an NVIDIA card: prefer Colab if your connection or disk space is limited.

The data is a 64 × 64 pixel copy of [VQAv2-small](https://huggingface.co/datasets/merve/vqav2-small): [`gberseth/vqav2-small-64px`](https://huggingface.co/datasets/gberseth/vqav2-small-64px), 21,388 questions, 266 MB, downloaded once into the Hugging Face cache. The file [`conf/micro-vlm-64pix.yaml`](conf/micro-vlm-64pix.yaml) is the one from the original repository, unchanged.

<sub>Prepared by Jaydan Aladro, from the course’s `micro_vlm` repository</sub>
