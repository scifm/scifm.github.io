---
title: Foundation Models for PDEs
layout: project
card-title: Partial Differential Equations
weight: 11
card-content: | 
    Creating surrogate physics models by finetuning a foundation model trained on multiple PDEs.
people: []
card-image: /assets/img/water.svg
cta_links:
  - label: LaDCast
    url: https://arxiv.org/abs/2506.09193
    style: btn-paper
    target: _blank
    rel: noopener noreferrer
  - label: DiffusionReconstruct
    url: https://doi.org/10.1016/j.cma.2024.117623
    style: btn-code
    target: _blank
    rel: noopener noreferrer
---

{% comment %} ---------- HERO (unchanged) ---------- {% endcomment %}
{% capture hero_body %}
Score-based diffusion models offer a unified, probabilistic framework for solving forward and inverse problems in scientific computing. Our team demonstrates their effectiveness for robust uncertainty quantification (UQ) in two key applications: field reconstruction and large-scale weather forecasting. The benefits of utilizing generative models for scientific computing can be summarized as follow:

- High-frequency detail recovery  
- Ensemble sampling at scale  
- Unbiased uncertainty quantification  
- Robustness to noise
{% endcapture %}

{% include blocks/hero.html
    eyebrow="Partial Differential Equations"
    title="Foundation Models for PDEs"
    lead="Surrogate physics models powered by diffusion-based generative learning across forward and inverse problems."
    body=hero_body
    image="/assets/img/pde_hero.png"
    image_alt="Overview of PDE foundation model"
    image_position="right"
    copy_col="col-lg-8 col-xl-7"
    media_col="col-lg-4 col-xl-5"
%}

{% comment %} ---------- SECTION 1: Forward — LaDCast ---------- {% endcomment %}

{%- capture forward_children_1 -%}
  {% include blocks/figure.html
      src="/assets/img/pde_fig1_new.png"
      alt="LaDCast overview"
  %}
{%- endcapture -%}
{% include blocks/text-section.html
    title="Forward — LaDCast"
    body=""
    children=forward_children_1
%}

{% capture forward_body_2 %}
For forward problems, we introduce **LaDCast**, the first latent diffusion model for global weather forecasting. Trained on the ERA5 reanalysis dataset (1979–2017, 121×240 grid), LaDCast employs a deep compression autoencoder (DC-AE) with modified CNN kernels to efficiently encode large-scale atmospheric data. The model achieves performance comparable to the state-of-the-art probabilistic numerical weather prediction system (IFS-ENS) without requiring perturbed initial conditions and demonstrates superior skill in precipitation prediction.
{% endcapture %}
{%- capture forward_children_2 -%}
  {% include blocks/figure.html
      src="/assets/img/pde_fig2_new.png"
      alt="LaDCast architecture"
  %}
{%- endcapture -%}
{% include blocks/text-section.html
    body=forward_body_2
    children=forward_children_2
%}

{% capture forward_body_3 %}
A 15-day forecast can be generated in under one minute on a single H100 GPU, with multiple ensemble members produced in parallel. This enables computationally efficient, scalable, and low-bias uncertainty quantification for autoregressive predictions.
{% endcapture %}
{%- capture forward_children_3 -%}
  {% include blocks/figure.html
      src="/assets/img/pde_fig3_new.png"
      alt="LaDCast performance"
  %}
{%- endcapture -%}
{% include blocks/text-section.html
    body=forward_body_3
    children=forward_children_3
%}

{% comment %} ---------- SECTION 2: Inverse — DiffusionReconstruct ---------- {% endcomment %}

{%- capture inverse_children_1 -%}
  {% include blocks/figure.html
      src="/assets/img/pde_fig4_new.png"
      alt="DiffusionReconstruct overview"
  %}
{%- endcapture -%}
{% include blocks/text-section.html
    title="Inverse — DiffusionReconstruct"
    body=""
    children=inverse_children_1
%}

{% capture inverse_body_2 %}
The model reconstructs global fields from sparse data by generating an ensemble of plausible realizations. Our work presents a diffusion-based framework for reconstructing spatial and spatio-temporal fields from sparse and noisy sensor observations. Unlike traditional deterministic reconstruction methods, this probabilistic formulation enables the model to capture the underlying uncertainty and variability inherent in sparsely observed systems.
{% endcapture %}
{%- capture inverse_children_2 -%}
  {% include blocks/figure.html
      src="/assets/img/pde_fig5.png"
      alt="DiffusionReconstruct results"
  %}
{%- endcapture -%}
{% include blocks/text-section.html
    body=inverse_body_2
    children=inverse_children_2
%}

{% capture inverse_body_3 %}
Built upon a UNet backbone with cross-attention, the model effectively integrates spatial context from sparse measurements to infer full-field structures. This design allows the network to represent multiple plausible realizations rather than memorizing specific patterns, providing robustness against noise and incomplete observations.
{% endcapture %}
{% include blocks/text-section.html
    body=inverse_body_3
%}

{% comment %} ---------- FINAL CTAs ---------- {% endcomment %}
{% capture cta_children %}
  {% include blocks/cta-group.html
      class="justify-content-center"
      buttons=page.cta_links
  %}
{% endcapture %}
{% include blocks/text-section.html
    class="text-center"
    children=cta_children
%}
