---
layout: default
title: Contact
permalink: /contact/
hero_ctas:
  - label: Join the Community ›
    url: /get-involved/
    style: btn-warning
---
{% capture contact_body %}
Please find our contact details below. If you’d like to visit us, the map provides directions to our offices.

### Address
Michigan Institute for Computational Discovery and Engineering (MICDE)  
3520 Green Ct. Suite 2300  
Ann Arbor, MI 48105

### Email
[micde-contact@umich.edu](mailto:micde-contact@umich.edu)
{% endcapture %}

{% capture contact_cta %}
{% include blocks/cta-group.html buttons=page.hero_ctas class="mt-3" %}
{% endcapture %}

{% capture contact_map %}
{% include blocks/embed.html
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2950.963925218471!2d-83.69400612390267!3d42.30063517119853!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x883cad002d69aff9%3A0x3c7b916a6e7f6618!2sMichigan%20Institute%20for%20Computational%20Discovery%20and%20Engineering%20(MICDE)!5e0!3m2!1sen!2sus!4v1760717130294!5m2!1sen!2sus"
    title="MICDE location"
    height=420
    class="h-100"
    referrerpolicy="no-referrer-when-downgrade"
%}
{% endcapture %}

{% include blocks/split.html
    left_title="Contact Us"
    left_title_tag="h1"
    left_body=contact_body
    left_children=contact_cta
    right_children=contact_map
    right_markdown=false
    left_col="col-lg-7"
    right_col="col-lg-5"
%}
