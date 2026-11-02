# Demo 5: Building a GPT from scratch

[Version française](README.md)

This demo builds a Transformer line by line, using only PyTorch and its basic building blocks, then trains it to write fake Shakespeare. It follows Andrej Karpathy’s video, [*Let’s build GPT: from scratch, in code, spelled out*](https://www.youtube.com/watch?v=kCc8FmEb1nY), and the paper [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762). We build the paper’s **decoder**, as GPT does.

**The notebook is available in French for now. The English version will follow.**

## Watch

These two 3Blue1Brown videos give the visual intuition that the notebook then makes concrete:

1. [Transformers, the tech behind LLMs (Chapter 5)](https://www.youtube.com/watch?v=wjZofJX0v4M), before you start.
2. [Attention in transformers, step-by-step (Chapter 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc), before section C.

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — A GPT from scratch** | [Ouvrir](notebooks/fr/01_gpt_from_scratch.ipynb) | [Open in Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_5/notebooks/fr/01_gpt_from_scratch.ipynb) | Coming soon |

## Setup and data

The notebook works on macOS, Linux and Windows, with no graphics card required. **Google Colab is the easiest option:** nothing to install, and a free GPU speeds up training. Otherwise, use the shared environment described in the [repository README](../README_en.md), with this demo’s dependency group:

```sh
git pull --ff-only
uv sync --group gpt
```

On Linux, PyTorch also downloads the CUDA libraries (about 5 GB), even without an NVIDIA card, so prefer Colab if your connection or disk space is limited.

A CPU is enough: on a recent laptop the whole notebook runs in under 5 minutes, and slower CPUs will take longer. The optional full configuration in section E needs a GPU.

`datasets/input.txt` is the *Tiny Shakespeare* file from Karpathy’s repository, copied unchanged: about one million characters from Shakespeare’s plays. On Colab, the notebook downloads it directly from [Karpathy’s repository](https://github.com/karpathy/ng-video-lecture).

The code is based on Andrej Karpathy’s [`ng-video-lecture`](https://github.com/karpathy/ng-video-lecture) (MIT license).

<sub>Prepared by Jaydan Aladro</sub>
