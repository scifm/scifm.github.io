---
title: Foundation Models for Molecular Discovery
layout: project
card-title: Molecular Discovery
card-content: |
    We're training a BERT-based model on 49B molecules to accelerate material discovery and enable Generative AI for molecular design

card-image: assets/img/incite_image_mb.png
people:
- abhutani
- awadell
---

## The Challenge

![]({% link assets/img/incite_image_mb.png %})

Current energy storage materials development is hindered by expensive experiments that limit exploration to the vast space of known synthesizable materials. Therefore, current research has only focused on a very limited design space space hindering the effective development of batteries for electric vehicles, grid storage, and electric aircraft applications. To address the unique demands of these applications, such as high energy density, safety, scalability, and power density, it is essential to explore a much larger chemical space than the few hundred that are currently considered due to the high cost of experiments and physics simulations.

Foundation models  offer a solution to both the exploration and evaluation issues: these models use self-supervised pre-training strategies to leverage unlabeled datasets and learn representations of data that can be applied to downstream tasks.  Large unlabeled datasets of billions of synthesizable molecules are readily available[^1]. Prior attempts to train FMs for molecular property prediction[^2] demonstrate promise, our project will scale up the training of foundation models to the largest available chemical libraries using wafer-scale computing to achieve accuracy similar to quantum mechanical computational methods and apply these to the electrolyte design problem.

[^1]: For example, [Generating Multibillion Chemical Space of Readily Accessible Screening Compounds](https://doi.org/10.1016/j.isci.2020.101681), [Comparison of Combinatorial Fragment Spaces and Its Application to Ultralarge Make-on-Demand Compound Catalogs](https://doi.org/10.1021/acs.jcim.1c01378) and [SAVI, in silico generation of billions of easily synthesizable compounds through expert-system type rules](https://doi.org/10.1038/s41597-020-00727-4)

[^2]: [Large-Scale Chemical Language Representations Capture Molecular Structure and Properties](https://doi.org/10.48550/arXiv.2106.09553), [Chemformer: a pre-trained transformer for computational chemistry](https://dx.doi.org/10.1088/2632-2153/ac3ffb), [ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction](https://arxiv.org/abs/2010.09885), [ChemBERTa-2: Towards Chemical Foundation Models](https://doi.org/10.48550/arXiv.2209.01712) and [MolCloze: A Unified Cloze-style Self-supervised Molecular Structure Learning Model for Chemical Property Prediction](https://doi.org/10.1109/BIBM52615.2021.9669794)

