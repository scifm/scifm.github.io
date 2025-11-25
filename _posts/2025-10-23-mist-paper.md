---
layout: post
title: "Foundation Models for Discovery and Exploration in Chemical Space"
image: assets/img/mist_logo.png
readmore: true
---

A paper about our molecular foundation model work *MIST* is now on arXiv! MIST is a family of models that spans small molecules, organometallics, mixtures/formulations, and even isotopes, relying on our Smirk tokenizer to incorporate stereochemical, isotopic, and electronic information. Using MIST, we screen over 8 million candidate electrolyte solvents in eight hours, identifying 63 Pareto-optimal candidates, and achieve state-of-the-art accuracy for mixture properties across temperature and composition, surpassing our previous GNN-based DiffMix models.

MIST also performs strongly on olfactory perception prediction on a dataset curated by Alex Wiltschko and the Google DeepMind team, and its learned token embeddings align with chemical “meaning,” revealing clean clusters of d- and p-block elements, features related to Lipinski’s Rule of Five, aromaticity, and PAH condensation.

Read more about MIST in our pre-print [here](https://arxiv.org/abs/2510.18900) or and try out [Smirk](https://eeg.engin.umich.edu/smirk/).