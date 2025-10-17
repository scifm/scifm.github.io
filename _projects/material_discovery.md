---
title: Material Discovery
layout: project
card-title: Material Discovery
weight: 10
card-content: |
    (Placeholder) Material discovery project — content to be added.

card-image: /assets/img/cloud_cover.png
people:
- 
---

<!-- Material Discovery — page scaffold / placeholders -->

<section class="container my-5">
    <!-- Fancy intro figure -->
    <div class="row align-items-start mb-4">
        <div class="col-lg-6 order-lg-2 text-center">
            <!-- Large hero image placeholder: make the image fill the box to remove white padding -->
            <div class="placeholder-hero" style="background:transparent; border-radius:12px; padding:0; height:520px; display:flex; align-items:center; justify-content:center; overflow:hidden;">
                <img src="{% link assets/img/cloud_bigpic.png %}" alt="Material discovery visual placeholder" style="width:100%; height:75%; object-fit:cover; display:block; border-radius:12px;">
            </div>
        </div>
        <div class="col-lg-6 order-lg-1">
            <h1 class="display-6 fw-bold" style="white-space:nowrap;">Scientific Foundation Model for Inorganic Crystals</h1>
            <p class="lead text-muted">Accelerating materials design with foundation models that know symmetry, physics, and crystal chemistry.</p>
            <p style="max-width:680px;">Materials science is standing at an inflection point. We know that the world’s next great battery, catalyst, or semiconductor hides somewhere in the endless space of possible crystals — but exploring that space atom by atom with density functional theory (DFT) or experiments is impossibly slow.
            What if we could give materials the same kind of foundation models that transformed natural language — models that learn the “grammar of crystals” and can generalize to new compounds, new conditions, and even new physics?</p>

            <p>That question led us to <strong>CLOUD</strong> (Crystal Language mOdel for Unified and Differentiable materials modeling) — a large-scale transformer built to understand the rules that nature writes in symmetry, composition, and structure. But to teach such a model, we first needed a new language for crystals themselves.</p>
        </div>
    </div>


    <!-- Three normal stacked sections: SCOPE / CLOUD / CLOUD-DEBYE -->

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>SCOPE</strong>: Symmetry-consistent String Representation for Crystals</h3>
            <p>
            The first roadblock we hit was representation. How do you show a neural network what a crystal is without drowning it in atomic coordinates?
            Coordinates are costly — every DFT calculation can take hours, and yet they only describe one snapshot of a structure. Worse, they hide the very thing that defines crystals: symmetry.</p>

            <p>So we asked a simple question — <em>what if we speak the language crystals actually use</em>?
            This led us to design <strong>SCOPE (Symmetry-Consistent Ordered Parameter Encoding)</strong> — a coordinate-free representation that encodes the <strong>space group’s generator strings</strong>, <strong>Wyckoff positions</strong>, and <strong>composition</strong>.
            Instead of feeding positions in 3D space, SCOPE captures the rules of repetition — the mathematical symmetries that define how a motif repeats infinitely in the crystal lattice.</p>

            <p>In essence, SCOPE tells the model <em>how the structure wants to be, not just where the atoms are</em>.
            That design choice made all the difference: CLOUD could now learn from over 6 million crystals at scale, discovering recurring symmetry–property patterns that no human could manually encode. The attention maps later confirmed what we hoped — the model was indeed “looking” where the physics lives: the symmetry tokens.
            </p>
        </div>

        <!-- Centered figure below the text. We avoid embedding the PDF; instead we show an img tag.
             For best results, replace '/assets/img/scope.pdf' with a cropped PNG (e.g. assets/img/scope.png).
             The src here points to the PDF as a fallback so authors can preview; browsers will generally show nothing for img->pdf, so consider rasterizing. -->
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/scope.png' | relative_url }}" alt="SCOPE figure (cropped)" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 2: Illustration of SCOPE representation. SCOPE consists of space group generator strings, Wyckoff position symbols, and material compositions.</div>
        </div>
    </section>

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>CLOUD</strong>: Crystal Foundation Model</h3>
            <p>Built on a <strong>BERT-style transformer</strong>, CLOUD is pre-trained on <strong>6.3 million</strong> crystals from the OPTIMADE database through masked language modeling, then fine-tuned for property prediction tasks.
            Across eight benchmark datasets (MatBench), CLOUD consistently outperforms prior coordinate-free and structure-based models. It even rivals graph neural networks (GNNs) that use full atomic coordinates — all while being far more efficient. When tested on out-of-distribution and defective structures (UnconvBench), CLOUD’s symmetry-centric design shines, capturing global patterns that traditional GNNs miss.</p>

            <p>
            Foundation models are known to follow predictable scaling laws — larger models trained on more data yield smoother improvements. CLOUD obeys the same rule.
            Its loss scales with model and data size following Hoffmann’s power law with exponents (a ≈ 0.45, b ≈ 0.55) — strikingly close to those found in large language models.
            This means the frontier of materials prediction can be pushed simply by scaling data and compute, just as GPT scaling advanced natural language understanding.
            </p>
        </div>  

        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/cloud_results.png' | relative_url }}" alt="CLOUD figure placeholder" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 3: Summary of fine-tuning results on benchmark datasets.</div>
        </div>
    </section>

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>CLOUD-DEBYE</strong>: Where SciFM Meets Physics</h3>
            <p>
            After building CLOUD, we faced a deeper question: could we move beyond predicting numbers and actually embed physics into learning itself?
            In most machine learning models, accuracy can come at the cost of physical meaning. For instance, a network might predict a correct heat capacity value at one temperature but fail entirely at another — violating the thermodynamic laws that govern matter.</p>

            <p>To fix this, we merged CLOUD with one of the simplest yet most powerful physical laws: the Debye model for heat capacity.
            In this hybrid framework — CLOUD-DEBYE — the neural network predicts the Debye temperature, and the Debye equation computes heat capacity and internal energy as a function of temperature. Because the entire pipeline is differentiable, CLOUD learns to align its predictions with the physics, not against it.</p>

            <p>This wasn’t just an academic experiment. It was our attempt to close the loop between data and theory, between prediction and understanding. The result was striking: CLOUD-DEBYE not only beat state-of-the-art graph models on accuracy but produced thermodynamically consistent curves across temperatures — even for materials it had never seen.</p>

            <p>It was the moment when the model stopped just learning from data and started reasoning with physics.
            </p>
        </div>

        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/cloud_debye.png' | relative_url }}" alt="CLOUD-DEBYE figure placeholder" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2" style="text-align:left; max-width:900px; margin-left:auto; margin-right:auto;">Figure 4: (a) Integration of physics laws with CLOUD model. The example exhibits the prediction for constant-volume heat capacity (C<sub>v</sub>) where CLOUD outputs the Debye temperature (&Theta;) and the Debye model predicts C<sub>v</sub> using &Theta; as input under different temperatures. (b) The violin plot of the prediction errors in C<sub>v</sub> by CGCNN, ALIGNN, CLOUD, and CLOUD-DEBYE. (c) C<sub>v</sub> predictions by CLOUD-DEBYE for Al<sub>2</sub>O<sub>3</sub>. Model predictions are compared against experimental and DFT-calculated results.</div>
        </div>
    </section>

    <!-- Perspective -->
    <div class="row mt-5">
        <div class="col-12">
            <h2 class="h4">Perspective</h2>
            <p> CLOUD began as an effort to make crystal modeling more scalable — and is now evolving into a framework for autonomous scientific reasoning. Building on the same philosophy that shaped SCOPE and CLOUD-DEBYE, we aim to develop foundation models that <em>understand</em> materials through physics, not just data. Our next direction is toward multi-modal models that integrate textual, structural, and thermodynamic information, alongside specialized variants for key physical phenomena. We are also beginning to leverage generative models to explore and propose new crystal candidates under different physical conditions. </p> <p> Beyond individual models, the broader vision is a <em>MaterialsGPT ecosystem</em> — uniting foundation models, reasoning agents, and knowledge graphs to generate, simulate, and interpret materials under arbitrary conditions. These models won’t just predict—they’ll design, test, and learn autonomously through closed-loop pipelines that connect learning, simulation, and experimentation. </p> <p> In short, CLOUD is not just a model — it is the first step toward a thinking framework for materials science: one that learns the structure of nature, obeys its laws, and scales with human curiosity. </p>
        </div>
    </div>

</section>

<!-- Call-to-action buttons -->
<section class="container my-5">
    <div class="row">
        <div class="col-12 text-center">
            <div class="md-ctas mt-4">
                <a class="btn btn-paper me-3" href="https://arxiv.org/abs/2506.17345" target="_blank" rel="noopener noreferrer">Read the Paper</a>
                <a class="btn btn-code" href="https://github.com/ChangwenXu98/CLOUD" target="_blank" rel="noopener noreferrer">Check the Code</a>
            </div>
        </div>
    </div>
</section>

