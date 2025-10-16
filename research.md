---
layout: default
title: Research
permalink: /research/
---

<section class="container section-research mb-5">
  <div class="row">
    <div class="col-12">
      <h1 class="section-title">Research Thrusts</h1>
      <p class="text-muted mb-4">Explore our core directions and how they connect to real scientific challenges.</p>
    </div>
  </div>
  <div class="row align-items-stretch">
  {% assign visible = site.projects | where_exp: "p", "p.published != false" %}
  {% assign weighted = visible | where_exp: "p", "p.weight != nil" | sort: 'weight' %}
  {% assign unweighted = visible | where_exp: "p", "p.weight == nil" | sort: 'title' %}
  {% assign projects = weighted | concat: unweighted %}
  {% for p in projects %}
      <div class="col-12 col-md-6 col-lg-6 mb-4 d-flex align-items-stretch" style="padding: 0 10px;">
        <div class="h-100 d-flex" style="width:100%;">
          {% include project-card.html project=p %}
        </div>
      </div>
    {% endfor %}
  </div>
</section>
---
layout: default
title: Research
permalink: /research/
---

<!-- Placeholder page for Research. Content to be added later. -->
