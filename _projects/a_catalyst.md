---
title: Foundation Models for Molecules
layout: project
card-title: Molecular Discovery
card-content: |
    We’re training BERT-based models to accelerate material discovery and enable Generative AI for molecular design.

card-image: assets/img/incite_image_mb.png
people:
- abhutani
- awadell
---

![Flowchart of our proposed workflow]({% link assets/img/incite_image_mb.png %})

Current energy storage materials development is hindered by expensive experiments that limit exploration to the vast space of known synthesizable materials. Therefore, current research has only focused on a very limited design space space hindering the effective development of batteries for electric vehicles, grid storage, and electric aircraft applications. To address the unique demands of these applications, such as high energy density, safety, scalability, and power density, it is essential to explore a much larger chemical space than the few hundred that are currently considered due to the high cost of experiments and physics simulations.

Foundation models  offer a solution to both the exploration and evaluation issues: these models use self-supervised pre-training strategies to leverage unlabeled datasets and learn representations of data that can be applied to downstream tasks.  Large unlabeled datasets of billions of synthesizable molecules are readily available. Prior attempts to train FMs for molecular property prediction demonstrate promise, our project will scale up the training of foundation models to the largest available chemical libraries using wafer-scale computing to achieve accuracy similar to quantum mechanical computational methods and apply these to the electrolyte design problem.