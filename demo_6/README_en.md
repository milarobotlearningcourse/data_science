# Demo 6: Images as data, from filters to convolutional networks

[Version française](README.md)

To a computer, a photo is just an array of numbers. This demo starts from those numbers: with OpenCV, we transform them, filter them and extract **features** from them (contrast, edges, gradients), as in classic computer vision. It ends with a small **convolutional network** trained on handwritten digits: it learns filters similar to ours, and we measure what our tools bring it when labelled data is scarce. It accompanies lectures 16 and 16b on computer vision.

**The notebook is available in French for now. The English version will follow.**

## Notebook

| Notebook | Français | Colab | English |
|---|---|---|---|
| **01 — From filters to convolutional networks** | [Ouvrir](notebooks/fr/01_caracteristiques_images_cnn.ipynb) | [Open in Colab](https://colab.research.google.com/github/milarobotlearningcourse/data_science/blob/main/demo_6/notebooks/fr/01_caracteristiques_images_cnn.ipynb) | Coming soon |

| Section | Content | Suggested time |
|---|---|---|
| Introduction | Goals, image processing vs computer vision, the CV pipeline | 5 min |
| A. An image is an array | Pixels and channels, the `uint8` type, reading with OpenCV and the BGR trap, HSV colour space | 10 min |
| B. Transforming each pixel | Point operations, histograms, thresholding (Otsu, adaptive), morphology to count coins | 10 min |
| C. Filtering: convolution | Moving average by hand, a gallery of kernels, denoising, correlation vs convolution, separable filters, equivariance | 15 min |
| D. Edges, a first feature | Derivative of a profile, smoothing before differentiating, Sobel, gradient orientation, Canny | 12 min |
| E. Warping and augmenting | Interpolation, rotation, perspective, data augmentation | 8 min |
| F. From features to a convolutional network | Pixels as features, Sobel as a PyTorch layer, a CNN on MNIST, its filters, augmentation and our filters with 500 labels | 20 min |

The notebook has four **À vous** exercises, each with a reference answer to open after trying: BGR → RGB by hand, writing the convolution, Cutout, and our filters as the network’s first layer. The first and third come from the old IFT6758 lab 9 (2020).

## Setup and data

The notebook works on macOS, Linux and Windows, with no graphics card required. **Google Colab is the easiest option:** OpenCV, scikit-image and PyTorch are already installed. Otherwise, use the shared environment described in the [repository README](../README_en.md), with this demo’s dependency group:

```sh
git pull --ff-only
uv sync --group vision
```

Sections A to E only need OpenCV and scikit-image, which are part of the shared dependencies: `uv sync` is enough. The `vision` group adds PyTorch and torchvision for section F. On Linux, PyTorch also downloads the CUDA libraries (about 5 GB), even without an NVIDIA card: prefer Colab if your connection or disk space is limited.

The images in sections A to E come from `skimage.data` and ship with scikit-image: nothing to download. Section F downloads the [MNIST](https://yann.lecun.com/exdb/mnist/) digits (about 12 MB) into `data/raw/` at the root of the repository (a folder ignored by Git). Training in section F takes about a minute on a recent laptop.

<sub>Prepared by Jaydan Aladro</sub>
