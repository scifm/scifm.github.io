---
title: Team
layout: default
permalink: /team/
people:
- venkvis
- bharath
- abhutani
- awadell
- amalss
- shangzhu
---

<section class="people">
    {% include role-people.html role="director" image=true%}
</section>
<section class="people">
    {% include role-people.html role="faculty" image=true%}
</section>
<section class="people">
    {% include role-people.html role="team" image=true%}
</section>
<section class="people">
    {% include role-people.html role="colab" image=true%}
</section>

<hr>

## Sponsors
<section class="sponsor-container">
    {% for item in site.data.sponsors %}
    {% assign sponsor = item[1] %}
    {% if sponsor.public %}
    {% include sponsor.html sponsor=sponsor %}
    {% endif %}
    {% endfor %}
</section>
