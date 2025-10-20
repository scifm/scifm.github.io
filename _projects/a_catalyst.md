---
title: Foundation Models for Molecules
layout: project
card-title: Molecular Discovery
card-content: |
  We’re training BERT-based models to accelerate material discovery and enable Generative AI for molecular design.
card-image: /assets/img/incite_image_mb.png
people:
- abhutani
- awadell
---

{% capture fm_body %}
Current energy storage materials development is hindered by expensive experiments that limit exploration to the vast space of known synthesizable materials. Therefore, current research has only focused on a very limited design space, hindering the effective development of batteries for electric vehicles, grid storage, and electric aircraft applications. To address the unique demands of these applications, such as high energy density, safety, scalability, and power density, it is essential to explore a much larger chemical space than the few hundred that are currently considered due to the high cost of experiments and physics simulations.
{% endcapture %}

{% include row-image-text.html
   src="/assets/img/incite_image_mb.png"
   alt="Flowchart of our proposed workflow"
   title="Foundation Models for Molecules"
   lead="We’re training BERT-based models to accelerate material discovery and enable Generative AI for molecular design."
   body=fm_body
   image_side="left"
   hr=false
%}