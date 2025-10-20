---
title: Foundation Models for Molecules
layout: project
card-title: Molecular Discovery
card-content: |
    MIST: A Scientific Foundation Model for Molecules and Mixtures.
card-image: /assets/img/incite_image_mb.png
people:
- abhutani
- awadell

hero_ctas:
  - label: Read the Paper
    url: https://openreview.net/forum?id=PFOmiOoRFP
    style: btn-paper
    target: _blank
    rel: noopener noreferrer
  - label: Check the Code
    url: https://github.com/BattModels/smirk
    style: btn-code
    target: _blank
    rel: noopener noreferrer
---

{% capture hero_body %}
Chemical space is astronomically large and profoundly heterogeneous, spanning simple organics, inorganic salts, complex organometallics, and their mixtures.
Traditional discovery workflows such as wet-lab screening and first-principles simulation probe only a small sliver of this space.
Recent progress in foundation models suggests a different path: learn general, transferable representations from vast unlabeled molecular corpora rather than rely on scarce labeled data.
MIST is built for this goal: a single molecular foundation model that resolves isotopic, stereochemical, structural, and electronic nuances, then transfers across tasks and domains, from energy materials to olfaction. By unifying breadth with scientific fidelity, MIST turns chemical space from an intractable search into a navigable landscape for discovery.
{% endcapture %}

{% include blocks/hero.html
    eyebrow="MIST (Molecular Insight SMILES Transformer)"
    title="Foundation Models for Discovery and Exploration in Chemical Space"
    lead="A significant step towards accelerating materials discovery, design, and optimization using foundation models."
    body=hero_body
    image="/assets/img/mist-figures/cover.jpg"
    image_alt="MIST overview visual"
    image_position="right"
    copy_col="col-lg-9 col-xl-6"
    media_col="col-lg-3 col-xl-6"
    max_height="400px"
    object_fit="contain"
%}

{% capture smirk_body %}
Most molecular foundation models use atom-wise tokenization, teating all ``bracketed atoms'' as a single irreducible token. Bracketed atoms represent any atom outside the organic subset or atoms with an explicit nuclear, geometric, or electronic aspect. Treating each fully specified bracketed atom as a single token would require an astronomically large vocabulary; in practice, small vocabularies create coverage gaps.
SMIRK addresses this by further decomposing bracketed atoms in chemically meaningful glyphs.
This yields a tokenizer with complete coverage of the OpenSMILES specification, preserving isotopic and stereochemical information, avoiding information lossy due to out-of-vocabulary tokens, and producing interpretable embeddings for attributes that matter to downstream tasks.
{% endcapture %}

{% capture smirk_children %}
{% include blocks/figure.html
    src="/assets/img/mist-figures/smirk.svg"
    alt="SMIRK tokenizer and mixture embedding"
    caption="SMIRK produces chemically meaningful tokens by decomposing brackets"
%}
{% endcapture %}

{% include blocks/text-section.html
    title="SMIRK: A Better Way to Tokenize SMILES"
    body=smirk_body
    children=smirk_children
%}

{% capture applications %}
The core advantage of a foundation model is that it can be adapted to a wide range of downstream tasks given a small number of labelled examples.
We demonstrate the MIST models' efficacy as scientific foundation models by fine-tuning variants of MIST to predict over 400 properties --- including quantum mechanical, thermodynamic, biochemical, and psychophysical properties --- from a molecule’s SMILES representation.
The MIST encoders are fine-tuned on labelled datasets as small as 200 examples.
The encoders are fine-tuned on single molecule property prediction (classification and regression) tasks by attaching a small two-layer MLP.
They are fine-tuned on mixture property prediction tasks using a physics-informed task network architecture.
These fine-tuned models unlock problem-solving capabilities across vast regions of chemical space at multiple scales, from single-molecule electrolyte solvents and odorants to large chiral organometallic structures and complex multi-component mixtures.
{% endcapture %}

{% capture applications_children %}
{% include blocks/figure.html
    src="/assets/img/mist-figures/electrolytes.png"
    alt="Electrolyte descriptors"
    caption="MIST-28M accurately predicts quantum, chemical, and thermodynamic descriptors for electrolyte design --— including orbital energy levels, Donor Number (DN) and Kamlet-Taft (KT) solvatochromic parameters."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="Applications Across Chemical Space"
    body=applications
    children=applications_children
%}

{% capture interp %}
The promise of scientific foundation models like MIST goes beyond raw predictive accuracy. For exploration, scientists need representations that surface interpretable, concept-aligned features —-- axes in the embedding space that correspond to recognizable scientific quantities or relationships and that can be read and steered to generate hypotheses or diagnose failure modes.

In language and vision, mechanistic interpretability has revealed feature vectors that align with meaningful concepts across tasks and modalities; comparable, systematic efforts for scientific models have been limited. Prior chemistry work has mostly inspected attention maps and low-dimensional projections as qualitative probes of internal behavior.
We took a systematic approach to uncover concept-aligned directions across all layers of MIST. Using lightweight linear readouts and controlled perturbations, we identify axes tied to chemically meaningful ideas, such as drug-likeness attributes, aromaticity, polycyclic aromatic hydrocarbon subclasses and isotopic stability that emerge during self-supervised pretraining and persist under fine-tuning.

By turning latent structure into operational knobs —-- readable directions that can be scored, visualized, or perturbed MIST enables hypothesis generation. In this role, MIST functions not merely as a high-accuracy predictor, but as a practical instrument for discovery and systematic exploration across chemical space.

{% endcapture %}
{% capture interp_children %}
{% include blocks/figure.html
    src="/assets/img/mist-figures/interp.svg"
    alt="Aromaticity and PAH features"
    caption="UMAP projections reveal that the pretrained embeddings encode Polycyclic Aromatic Hydrocarbons classes and ring aromaticitydespite the model never training on labelled examples of these classes, suggesting the existence of chemically coherent structures in MIST's embedding space."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="Learning a Chemically Meaningful Representation"
    body=interp
    children=interp_children
%}

{% capture cta_children %}
{% include blocks/cta-group.html
    class="justify-content-center"
    buttons=page.hero_ctas
%}
{% endcapture %}

{% include blocks/text-section.html
    class="text-center"
    children=cta_children
%}