---
title: Foundation Models for Computational Science
layout: project
card-title: Computational Science
card-content: |
    Intelligent agents for automatic code and workflow generation ready for deployment on exascale computational resources

card-image: assets/img/comp_sci_card.svg
people:
- venkvis
- arvind
---

In the context of foundation models for science, transformer-based methods have shown potential in utilizing structured computational and experimental data to build surrogates that are approaching the accuracy of the methods used to generate those results. In a practical computational science setting, however, there are other significant unstructured computational and experimental data and meta-data available that have previously been unused/unusable. This proposal aims to develop a foundation model for computational science that can utilize large-scale unlabelled/unstructured computational simulation data and metadata (workflows, scripts, log files, etc.), computational data (multi-modal, multi-fidelity), experimental data and metadata, literature, using self-supervised learning.
We're building a CompSciFM that will be knowledgeable in computational sciences—encompassing computational mathematics, algorithms, and workflows—serving as a personal assistant that can significantly enhance productivity and the value of any computational or experimental data generated.
The focus of this project will be on the inner loop of computational sciences, which includes hypothesis creation and evaluation, carried out using various high-fidelity simulation codes and workflows. This process iteratively generates detailed and accurate computational models to evaluate hypotheses, ensuring precise and reliable results through repeated, fine-grained calculations and data processing.

This project aims to develop a sophisticated personal assistant for computational science.  The framework is shown in above, where the scientist interacts with a computational science foundation model (CompSciFM), which is capable of producing code and workflow integrating with large-scale highly-performant codes, which gets executed through the HPC agent.  This is subsequently executed on leadership computing facilities, running and managing exascale computational campaigns producing computational results that will go through a validation loop, and additional loops may be considered depending on the fidelity of the result. CompSciFM will be capable of incorporating multi-fidelity simulations in its workflow to generate the desired fidelity of results for the computational task at hand.  CompSciFM will be capable of interacting with various kinds of domain-specific multi-modal foundation models which will be treated as agents, e.g. [MoLFormer](https://arxiv.org/abs/2106.09553)/[MIST](./catalyst.md) for material science; [GenSLM](./biology.md) for biology.
