---
layout: tabs
title: "Summer School 2024"
image: assets/img/SciFM24_summer_school.svg
---

<div class="tab-content" id="pills-tabContent">
    <div class="tab-pane fade show active" id="about" role="tabpanel" aria-labelledby="pills-about-tab"> 
        {% include blurb.html item=site.data.descriptions.summer_school%}
    </div>
    <div class="tab-pane fade" id="organizers" role="tabpanel" aria-labelledby="pills-organizers-tab">
        <section>
        {% include role-organizer.html image=true%}
        </section>
    </div>
    <div class="tab-pane fade" id="schedule" role="tabpanel" aria-labelledby="pills-schedule-tab">
        {% include schedule.html %}
    </div>
    <div class="tab-pane fade" id="hackathon" role="tabpanel" aria-labelledby="pills-hackathon-tab">
        {% include  blurb.html item=site.data.descriptions.hackathon %}
    </div>
</div>