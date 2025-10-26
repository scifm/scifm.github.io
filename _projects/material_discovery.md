---
title: Materials Intelligence
layout: project
card-title: Materials Intelligence
card-content: |
    Foundation models for inorganic crystals that respect symmetry and physics.

card-image: /assets/img/grid.svg
people: []
hero_ctas:
  - label: Read the Paper
    url: https://arxiv.org/abs/2506.17345
    style: btn-paper
    target: _blank
    rel: noopener noreferrer
  - label: Check the Code
    url: https://github.com/ChangwenXu98/CLOUD
    style: btn-code
    target: _blank
    rel: noopener noreferrer
---

{% capture hero_body %}
We know that the world’s next great battery, catalyst, or semiconductor hides somewhere in the endless space of possible crystals — but exploring that space with density functional theory (DFT) or experiments is impossibly slow. What if we could give materials the foundation models that transformed natural language — models that learn the “grammar of crystals” and can generalize to new compounds, new conditions, and even new physics? That question led us to **CLOUD** — a large-scale transformer built to understand the rules that nature writes in symmetry and composition. But to teach such a model, we first needed a new language for crystals themselves.
{% endcapture %}

{% include blocks/hero.html
    eyebrow="Materials Intelligence"
    title="Scientific Foundation Model for Inorganic Crystals"
    lead="Accelerating materials design with foundation models that know symmetry, physics, and crystal chemistry."
    body=hero_body
    image="/assets/img/cloud_bigpic.png"
    image_alt="Materials Intelligence visual"
    image_position="right"
    copy_col="col-lg-8 col-xl-7"
  media_col="col-lg-4 col-xl-5"
%}

{% capture scope_body %}
The first roadblock we hit was representation. How do you show a neural network what a crystal is without drowning it in atomic coordinates? Coordinates are costly — every DFT calculation can take hours, and yet they only describe one snapshot of a structure. Worse, they hide the very thing that defines crystals: symmetry.

So we asked a simple question — *what if we speak the language crystals actually use*? This led us to design **SCOPE (Symmetry-Consistent Ordered Parameter Encoding)** — a coordinate-free representation that encodes the **space group’s generator strings**, **Wyckoff positions**, and **composition**. Instead of feeding positions in 3D space, SCOPE captures the rules of repetition — the mathematical symmetries that define how a motif repeats infinitely in the crystal lattice.

In essence, SCOPE tells the model *how the structure wants to be, not just where the atoms are*. That design choice made all the difference: CLOUD could now learn from over 6 million crystals at scale, discovering recurring symmetry–property patterns that no human could manually encode. The attention maps later confirmed what we hoped — the model was indeed “looking” where the physics lives: the symmetry tokens.
{% endcapture %}

{% capture scope_children %}
{% include blocks/figure.html
    src="/assets/img/scope.png"
    alt="SCOPE representation diagram"
    caption="Figure 1: Illustration of SCOPE representation. SCOPE consists of space group generator strings, Wyckoff position symbols, and material compositions."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="**SCOPE**: Symmetry-consistent String Representation for Crystals"
    body=scope_body
    children=scope_children
%}

{% capture cloud_body %}
Built on a **BERT-style transformer**, CLOUD is pre-trained on **6.3 million** crystals from the OPTIMADE database through masked language modeling, then fine-tuned for property prediction tasks. Across eight benchmark datasets (MatBench), CLOUD consistently outperforms prior coordinate-free and structure-based models. It even rivals graph neural networks (GNNs) that use full atomic coordinates — all while being far more efficient. When tested on out-of-distribution and defective structures (UnconvBench), CLOUD’s symmetry-centric design shines, capturing global patterns that traditional GNNs miss.

Foundation models are known to follow predictable scaling laws — larger models trained on more data yield smoother improvements. CLOUD obeys the same rule. Its loss scales with model and data size following Hoffmann’s power law with exponents (a ≈ 0.45, b ≈ 0.55) — strikingly close to those found in large language models. This means the frontier of materials prediction can be pushed simply by scaling data and compute, just as GPT scaling advanced natural language understanding.
{% endcapture %}

{% capture cloud_children %}
{% include blocks/figure.html
    src="/assets/img/cloud_results.png"
    alt="CLOUD benchmark results"
    caption="Figure 2: Summary of fine-tuning results on benchmark datasets."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="**CLOUD**: Crystal Foundation Model"
    body=cloud_body
    children=cloud_children
%}

{% capture debye_body %}
After building CLOUD, we faced a deeper question: could we move beyond predicting numbers and actually embed physics into learning itself? In most machine learning models, accuracy can come at the cost of physical meaning. For instance, a network might predict a correct heat capacity value at one temperature but fail entirely at another — violating the thermodynamic laws that govern matter.

To fix this, we merged CLOUD with one of the simplest yet most powerful physical laws: the Debye model for heat capacity. In this hybrid framework — CLOUD-DEBYE — the neural network predicts the Debye temperature, and the Debye equation computes heat capacity and internal energy as a function of temperature. Because the entire pipeline is differentiable, CLOUD learns to align its predictions with the physics, not against it.

This wasn’t just an academic experiment. It was our attempt to close the loop between data and theory, between prediction and understanding. The result was striking: CLOUD-DEBYE not only beat state-of-the-art graph models on accuracy but produced thermodynamically consistent curves across temperatures — even for materials it had never seen.

It was the moment when the model stopped just learning from data and started reasoning with physics.
{% endcapture %}

{% capture debye_children %}
{% include blocks/figure.html
    src="/assets/img/cloud_debye_new.png"
    alt="CLOUD-DEBYE integration diagram"
    caption="Figure 3: Integration of physics laws with CLOUD. CLOUD outputs the Debye temperature Θ and the Debye model predicts Cᵥ using Θ as input under different temperatures."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="**CLOUD-DEBYE**: Where SciFM Meets Physics"
    body=debye_body
    children=debye_children
%}

{% include blocks/embed.html
    src="/cloud_debye_interactive.html"
    title="CLOUD-DEBYE interactive heat capacity explorer"
    height=640
%}

{% capture perspective_body %}
CLOUD began as an effort to make crystal modeling more scalable — and is now evolving into a framework for autonomous scientific reasoning. Building on the same philosophy that shaped SCOPE and CLOUD-DEBYE, we aim to develop foundation models that *understand* materials through physics, not just data. Our next direction is toward multi-modal models that integrate textual, structural, and thermodynamic information, alongside specialized variants for key physical phenomena. We are also beginning to leverage generative models to explore and propose new crystal candidates under different physical conditions.

Beyond individual models, the broader vision is a *MaterialsGPT ecosystem* — uniting foundation models, reasoning agents, and knowledge graphs to generate, simulate, and interpret materials under arbitrary conditions. These models won’t just predict — they’ll design, test, and learn autonomously through closed-loop pipelines that connect learning, simulation, and experimentation.

In short, CLOUD is not just a model — it is the first step toward a thinking framework for materials science: one that learns the structure of nature, obeys its laws, and scales with human curiosity.
{% endcapture %}

{% include blocks/text-section.html
    title="Perspective"
    body=perspective_body
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

