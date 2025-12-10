---
title: Autonomous Labs for Electrolyte Discovery
layout: project
card-title: Autonomous Labs
card-content: |
    Clio: An Autonomous Lab for Aqueous and Non-aqueous Electrolyte Discovery.
card-image: /assets/img/lab.svg
weight: 10
people:
- lithium
- tiz
- cyhalek

hero_ctas:
  - label: Read the Paper
    url: https://www.nature.com/articles/s41467-022-32938-1
    style: btn-paper
    target: _blank
    rel: noopener noreferrer
  - label: Check the Code
    url: https://github.com/BattModels/Clio
    style: btn-code
    target: _blank
    rel: noopener noreferrer
---

{% capture hero_body %}
Electrolytes are fundamental to the function of batteries. They transport ions between the electrodes, while remaining inert in the harsh electrochemical environment the electrodes create. Designing electrolytes is a challenging, multidimensional problem that is unique from typical materials discovery or molecular design efforts. For one, a candidate electrolyte must satisfy tens of properties simultaneously. Second, the design space is immense. Electrolytes are chemical mixtures consisting of organic molecules and inorganic salt. Thus, designing an electrolyte formulation for Li-ion batteries involves the combinatorial challenge of selecting a small number of organic molecules and a lithium-containing inorganic salt from a seemingly endless number of options, while accurately predicting all the key properties for each candidate formulation.

Materials discovery and commercialization can be accelerated with robotic, high-throughput labs called “self-driving labs”.
These robotic labs not only conduct experiments but also integrate machine learning and artificial intelligence to autonomously decide what experiment to conduct next, just like a human scientist would.
{% endcapture %}

{% include blocks/hero.html
    eyebrow="Clio: An Autonomous Lab for Aqueous and Non-aqueous Electrolyte Discovery"
    title="Autonomous Labs for Electrolyte Discovery"
    lead="A significant step towards accelerating materials discovery, design, and optimization using foundation models."
    body=hero_body
    image="/assets/img/auto_lab/auto_lab_main.svg"
    image_alt="Clio overview visual"
    image_position="right"
    copy_col="col-lg-9 col-xl-6"
    media_col="col-lg-3 col-xl-6"
    max_height="400px"
    object_fit="contain"
%}

{% capture Clio_body %}
The Clio self-driving lab integrates multiple experimental modules — including high-precision balances, viscometers, potentiostats, and peristaltic pumps — under a shared software framework, ElyteOS. Clio can characterize both aqueous and non-aqueous liquid formulations, and is a flow-through and modular setup, with flexibility to add additional instrumentation. It autonomously prepares electrolytes, performs electrochemical measurements, and characterizes their properties (density, conductivity and viscosity) without human supervision. Each experimental iteration is logged, version-controlled, and automatically stored in a cloud-accessible database.

When coupled with Bayesian optimization, Clio autonomously identified six high-conductivity electrolyte mixtures within only 42 experiments, demonstrating a more than fivefold acceleration compared to human-driven exploration. The resulting data have demonstrated strong agreement between predictive thermodynamic models and experimental measurements, highlighting the system’s capacity for closed-loop validation. To further enhance predictive capability, the DiffMix framework embeds physical equations into a neural-network backbone, allowing gradients to propagate through physical constraints. When coupled to Clio, DiffMix achieved an 18.8% improvement in ionic conductivity within ten autonomous iterations—demonstrating for the first time a gradient-based optimization loop between differentiable AI models and robotic experimentation.
{% endcapture %}

{% capture Clio_children %}
{% include blocks/figure.html
    src="/assets/img/auto_lab/Clio.svg"
    alt="Clio autonomous lab"
    caption="Schematic of the Clio characterization module, which autonomously prepares liquid formulations, and characterizes their conductivity and viscosity. It integrates multiple experimental modules — including high-precision balances, viscometers, potentiostats, and peristaltic pumps — under a shared software framework, ElyteOS."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="Clio: An autonomous lab for battery electrolytes"
    body=Clio_body
    children=Clio_children
%}

{% capture SALSA %}
The SALSA solubility module complements Clio. It is an autonomous high-throughput solubility measurement system that captures real-time dissolution curves in aqueous and non-aqueous media. SALSA can rapidly evaluate solubility in mixed solvents, which can then be combined to predict the solution synthesis conditions of higher component materials. In combination, Clio and SALSA constitute a modular self-driving lab ecosystem capable of measuring conductivity, viscosity, density, surface tension, and solubility—core physical properties essential for electrolyte design. 

ElyteOS controls the Clio and SALSA characterization platforms. It translates experiment requests into executable sequences and manages asynchronous data logging. When users remotely submit a request and specify fabrication and characterization parameters for a liquid formulation, ElyteOS executes the experiments and returns structured data to the cloud database.
{% endcapture %}

{% capture SALSA %}
{% include blocks/figure.html
    src="/assets/img/auto_lab/SALSA.svg"
    alt="SALSA module"
    caption="The SALSA solubility measurement module."
%}
{% endcapture %}

{% include blocks/text-section.html
    title="The SALSA solubility module"
    body=SALSA
    children=SALSA_children
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