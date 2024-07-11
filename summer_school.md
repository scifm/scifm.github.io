---
layout: tabs
title: "Summer School 2024"
image: assets/img/SciFM24_summer_school.svg
---
<div class="tab-content" id="pills-tabContent">
    <div class="tab-pane fade show active" id="about" role="tabpanel" aria-labelledby="pills-about-tab"> 
        {% include blurb.html item=site.data.descriptions.summer_school%}
        <div style="overflow-x: scroll;">
        <h2> Tutorials </h2>
        <p>
            We've made our course content available on GitHub at <a href="https://github.com/scifm/summer-school-2024">scifm/summer-school-2024</a>, licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0.html">Apache 2.0 license</a>.
            You'll find pre-worked examples covering topics such as tokenization and neural scaling laws, along with demonstrations of vision transformers and diffusion models tailored for scientific applications.
        </p>
        <h2> Apply to Participate! </h2>
            <p> Fill in the google form below or access it <a href="https://forms.gle/vvFfDUnd93nMyKi36"> here.</a> </p>
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdLoh_ETU7P8R36OT-hjgWnTHwiIl8UFIrH4hOhwWocdwKLCg/viewform?embedded=true" width="640" height="1812" frameborder="0" marginheight="0" marginwidth="0">Loading…
            </iframe>
        </div>
    </div>
    <div class="tab-pane fade" id="organizers" role="tabpanel" aria-labelledby="pills-organizers-tab">
        <section>
        {% include role-organizer.html role="organizer" image=true%}
        </section>
        <section>
        {% include role-organizer.html role="hack" image=true%}
        </section>
    </div>
    <div class="tab-pane fade" id="hackathon" role="tabpanel" aria-labelledby="pills-hackathon-tab">
        {% include  blurb.html item=site.data.descriptions.hackathon %}
    </div>
    <div class="tab-pane fade" id="schedule" role="tabpanel" aria-labelledby="pills-schedule-tab">
        {% include schedule.html %}
    </div>
</div>
