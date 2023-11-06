---
title: Scientific Foundation Models
layout: default
---

<!-- ## The Challenge
Current energy storage materials development is hindered by expensive experiments that limit exploration to the vast space of known synthesizable materials. Therefore, current research has only focused on a very limited design space space hindering the effective development of batteries for electric vehicles, grid storage, and electric aircraft applications. To address the unique demands of these applications, such as high energy density, safety, scalability, and power density, it is essential to explore a much larger chemical space than the few hundred that are currently considered due to the high cost of experiments and physics simulations. -->

### Why Scientific Foundation Models?
Foundation models refers to large machine learning models trained on vast diverse datasets and generalizable to on a wide range of prediction or generation tasks. In contrast to conventional machine learning models, which are optimized to perform a single task, a foundation model serves as a “prior” or “foundation” upon which other models can be built. This prior is learnt using self-supervised pre-training strategies which leverage unlabeled datasets. The representations learnt by the pre-trained foundation model can then be applied to a wide range of downstream tasks, after finetuning a limited number of the model's parameters on a smaller labelled dataset. This ability to leverage unlabelled data is particularly useful in scientific domains where the scope of supervised machine learning methods is limited to due the scarcity of labelled data and the high cost of experiments or computational simulations to needed label datasets.


<!-- /.row -->
<div class="row">
    {% for p in site.projects %}
        {% include project-card.html project=p %}
    {% endfor %}
</div>
<!-- /.row -->
