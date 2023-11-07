---
title: About Us
layout: default
permalink: /about/
people:
- venkvis
- bharath
- abhutani
- awadell
- amalss
- shangzhu
---

## The Team
<section class="people project-people">
    {% for uname in page.people %}
        {% assign person = site.data.people[uname] %}
        {% include person.html person=person image=true%}
    {% endfor %}
</section>
