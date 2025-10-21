---
layout: default
title: Get Involved
permalink: /get-involved/
---

{% capture intro_body %}
Join our mailing lists and community — fill out the form below. You can update the fields and processing later (for example, by wiring the form to Mailchimp or a custom endpoint).
{% endcapture %}

{% capture form_block %}
{% include blocks/get-involved-form.html %}
{% endcapture %}

{% capture sidebar_body %}
Email [micde-contact@umich.edu](mailto:micde-contact@umich.edu)

[Contact page](/contact/)
{% endcapture %}

{% include blocks/split.html
    left_title="Get Involved"
    left_title_tag="h1"
    left_lead="Join the SciFM community shaping the future of scientific discovery."
    left_body=intro_body
    left_children=form_block
    right_title="Questions?"
    right_body=sidebar_body
%}
