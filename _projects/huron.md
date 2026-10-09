---
title: "Project Huron: AI-Driven Superconductor Discovery"
layout: project
card-title: Project Huron
card-content: |
    An AI scientist searching for superconductors that work under room temperature and moderate pressure.
card-image: /assets/img/huron/huron.svg
people:
- venkvis
- changwex

hero_ctas:
  - label: Read the Announcement
    url: https://record.umich.edu/articles/u-m-researchers-help-launch-national-initiative-to-demonstrate-ais-potential-for-scientific-discovery/
    style: btn-paper
    target: _blank
    rel: noopener noreferrer
---

{% capture hero_body %}
Superconductors carry electricity with zero resistance. One that worked under everyday conditions would change a lot: cheaper MRI machines, power lines that lose nothing in transmission, stronger magnets for fusion reactors and particle accelerators, and better hardware for quantum computers. The trouble is that every superconductor we know of needs extreme conditions. Most must be cooled far below room temperature, and the record-holding hydrides need pressures above a million atmospheres.

**Project Huron** is our attempt to close that gap with AI and advanced computing. Led by SciFM director Venkat Viswanathan, it starts as a focused 18-month effort, with a small team in Ann Arbor working alongside collaborators at national laboratories and universities. It is also the first test case of **Mission Lodestar**, a national initiative to find out what AI can do for scientific discovery.
{% endcapture %}

{% include blocks/hero.html
    eyebrow="Project Huron · Mission Lodestar"
    title="AI-Driven Discovery of Hydride Supercon&shy;ductors"
    lead="Searching for hydride superconductors that reach high temperatures at moderate pressure."
    body=hero_body
    image="/assets/img/huron/superconductivity.png"
    image_alt="Critical temperature of superconductors versus year of discovery, by materials family"
    image_caption="A century of superconductor discovery: critical temperature versus year of discovery for each family of materials. The highlighted box marks our target, superconductivity at room temperature. Adapted from W. E. Pickett, [arXiv:2204.05930](https://arxiv.org/abs/2204.05930)."
    image_position="right"
    copy_col="col-lg-8 col-xl-7"
    media_col="col-lg-4 col-xl-5"
%}

{% capture physics_body %}
In a conventional superconductor, electrons pair up through vibrations of the crystal lattice (phonons), and the pairs move through the material without scattering. Light atoms vibrate fast, and fast vibrations help the pairs survive to higher temperatures. Hydrogen, the lightest element, is the obvious candidate. Neil Ashcroft argued in 1968 that metallic hydrogen should superconduct near room temperature, but squeezing hydrogen into a metal takes pressures that experiments can still barely reach.

Hydrogen-rich compounds offer a shortcut. At high pressure, chemistry plays by different rules: compounds like H₃S and LaH₁₀, which cannot exist at ambient conditions, become stable, and in LaH₁₀ the hydrogen atoms form cage-like networks around each lanthanum atom. These *superhydrides* hold the records for conventional superconductivity, at about 200 K for H₃S and 250 K for LaH₁₀. Both were predicted by calculations before anyone made them in the lab, one of the clearest cases of theory leading experiment in materials science. Both also need more than a million atmospheres, the kind of pressure found deep inside the Earth.
{% endcapture %}

{% include blocks/text-section.html
    title="Why Hydrogen?"
    body=physics_body
%}

{% capture challenge_body %}
So the question is whether we can keep the high critical temperature and bring the pressure down. One promising route is to add a third element. In a ternary hydride, the extra atoms can donate electrons to the hydrogen network and hold it together from the inside, doing part of the work that external pressure does in a binary hydride. This idea is known as *chemical precompression*.

The catch is the size of the search. Every choice of elements, composition and crystal structure is a new candidate, and an accurate superconductivity calculation for a single one can take hundreds of CPU hours. There are far too many candidates to compute them all, so the search has to be guided.
{% endcapture %}

{% include blocks/text-section.html
    title="The Challenge: Designing Ternary Hydrides"
    body=challenge_body
%}

{% capture scientist_body %}
We are building AI scientists to run this search. Given a goal in plain language, our AI scientist reads the literature, decides which chemical families look promising, and chooses what to compute next.

Its decisions are grounded in high-fidelity calculation results. The AI scientist runs rigorous first-principles simulations itself, from crystal structure prediction and stability checks to electron–phonon calculations of the critical temperature, with direct access to high-performance computing clusters. Each result shapes what it tries next. Human scientists stay in the loop to check its reasoning and steer the campaign.
{% endcapture %}

{% include blocks/text-section.html
    title="AI Scientists for Superconductor Discovery"
    body=scientist_body
%}

{% capture lodestar_body %}
Project Huron is part of **Mission Lodestar**, led by the University of Michigan with Los Alamos National Laboratory and Argonne National Laboratory, and supported by OpenAI's contribution to the U.S. Department of Energy's [Genesis Mission](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/). The mission is a bet that one focused, large-scale effort pairing frontier AI with leadership-class computing can find things that many smaller projects would miss.

Superconductors are the first target. Given a different goal, the same AI scientist could search for battery materials, catalysts or other functional materials.
{% endcapture %}

{% capture lodestar_children %}
{% include blocks/cta-group.html
    class="justify-content-center"
    buttons=page.hero_ctas
%}
{% endcapture %}

{% include blocks/text-section.html
    title="Part of Mission Lodestar"
    body=lodestar_body
    children=lodestar_children
%}
