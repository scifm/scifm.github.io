---
title: DREAMS — Agentic DFT for Computational Science
layout: project
card-title: DREAMS: Agentic DFT
weight: 20
card-content: |
    Hierarchical LLM agents that plan, run, and fix high‑fidelity DFT workflows — approaching L3 automation for materials discovery.

card-image: assets/img/comp_sci_card.svg
people:
- venkvis
- janssen
- ziqi
- hongshuo
---

<!-- DREAMS — page following the style of material_discovery.md -->

<section class="container my-5">
    <!-- Intro row with hero image on the right (to mirror the style) -->
    <div class="row align-items-start mb-4">
        <div class="col-lg-6 order-lg-2 text-center">
            <!-- Large hero image: architecture overview (Fig. 1) -->
            <div class="placeholder-hero" style="background:transparent; border-radius:12px; padding:0; height:520px; display:flex; align-items:center; justify-content:center; overflow:hidden;">
                <img src="{% link assets/img/figure1.png %}" alt="DREAMS architecture overview" style="width:100%; height:75%; object-fit:cover; display:block; border-radius:12px;">
            </div>
        </div>
        <div class="col-lg-6 order-lg-1">
            <h1 class="display-6 fw-bold" style="white-space:nowrap;">DREAMS: DFT‑based Research Engine for Agentic Materials Simulation</h1>
            <p class="lead text-muted">A hierarchical, multi‑agent framework that couples LLM reasoning with robust DFT tools, HPC scheduling, and structured memory to deliver high‑fidelity, self‑correcting simulations.</p>
            <p style="max-width:680px;">High‑throughput, high‑fidelity simulations like DFT are accurate but labor‑intensive: they demand expert setup, systematic convergence testing, error triage, and careful uncertainty analysis. <strong>DREAMS</strong> addresses these pain points with a planning supervisor and specialized worker agents — a <em>DFT Agent</em> for structure and scripts, an <em>HPC Agent</em> for submission/monitoring, and a <em>Convergence Agent</em> for targeted fixes — all grounded by a shared <em>Canvas</em> for lossless, time‑invariant state.</p>
            <p>Validated on (i) the <strong>Sol27LC lattice‑constant</strong> benchmark (expert‑level accuracy, sub‑1% MAPE), (ii) the classic <strong>CO/Pt(111)</strong> adsorption site puzzle (recovering FCC preference and literature‑consistent ∆BE), and (iii) <strong>functional‑driven uncertainty</strong> via BEEF‑vdW ensembles, DREAMS approaches <strong>L3 automation</strong> — autonomous exploration within a defined design space.</p>
        </div>
    </div>

    <!-- Three stacked sections following the pattern (concept / result / physics insight) -->

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>Architecture</strong>: Planning, Specialized Agents, and a Shared Canvas</h3>
            <p>The <strong>Supervisor</strong> decomposes objectives into executable plans, assigns tasks, and revises dynamically from execution traces. The <strong>DFT Agent</strong> generates bulk/slab/adsorbate structures, performs systematic convergence tests, prepares QE inputs, and parses outputs. The <strong>HPC Agent</strong> chooses partitions/resources, submits jobs, tracks status, and retrieves results. The <strong>Convergence Agent</strong> provides targeted, <em>parameter‑level</em> remedies (e.g., <code>degauss</code>, <code>mixing_beta</code>, <code>local-TF</code>, <code>electron_maxstep</code>) to resolve difficult SCF cases. A shared <strong>Canvas</strong> stores paths, settings, pseudopotentials, and prior adjustments to prevent drift and repetition.</p>
        </div>
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/figure1.png' | relative_url }}" alt="DREAMS architecture" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 1: DREAMS components and dataflow — Supervisor, DFT/HPC/Convergence Agents, HPC cluster interface, and the Canvas.</div>
        </div>
    </section>

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>Benchmark I — Sol27LC</strong>: Expert‑Level Lattice Constants with Minimal Deviation</h3>
            <p>DREAMS automates a <strong>two‑stage convergence</strong> protocol (plane‑wave cutoff then k‑mesh) under a 1&nbsp;meV/atom threshold, then fits an EOS to extract <em>a<sub>eq</sub></em>. Across BCC/FCC/Diamond systems, the framework achieves <strong>&lt; 1% MAPE</strong> relative to human‑expert baselines and selects sensible <code>ecutwfc</code> and k‑point ranges for production.</p>
        </div>
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/figure3.png' | relative_url }}" alt="Convergence studies for Sol27LC" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 3: Representative convergence curves for <code>ecutwfc</code> and k‑spacing relative to a strict reference; 1&nbsp;meV/atom threshold shown.</div>
        </div>
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/table2.png' | relative_url }}" alt="Sol27LC summary table" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Table 2: Summary of correct structure generation, MAPE, and chosen parameters across Sol27LC systems.</div>
        </div>
    </section>

    <section class="mb-5">
        <div>
            <h3 class="h5"><strong>Benchmark II — CO/Pt(111)</strong>: Site Preference &amp; Uncertainty at GGA Level</h3>
            <p>For a p(2×2) overlayer (θ = 1/4 ML), DREAMS sets up ontop/FCC configurations, executes production with auto‑fixed SCF settings, and computes adsorption energies. The recovered <strong>∆BE = E<sub>ads,ontop</sub> − E<sub>ads,FCC</sub> &gt; 0</strong> matches expert/literature values under PBE/LDA, confirming <strong>FCC preference</strong> at the GGA level. Extending to <strong>BEEF‑vdW ensembles</strong> (N=2000) shows 0 eV lies &gt;10σ from the ∆BE distribution, reinforcing robustness.</p>
        </div>
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/figure4.png' | relative_url }}" alt="Workflow for CO/Pt(111) study" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 4: End‑to‑end workflow with dynamic replanning and convergence‑agent interventions to ensure fully converged production results.</div>
        </div>
        <div class="text-center mt-3">
            <img class="figure-full" src="{{ '/assets/img/figure5.png' | relative_url }}" alt="BEEF‑vdW ensemble distribution of ∆BE" style="width:92%; max-width:900px;" />
            <div class="figure-caption text-muted small mt-2">Figure 5: BEEF‑vdW ensemble analysis for ∆BE; both expert and DREAMS means favor FCC, with tight σ and strong separation from 0 eV.</div>
        </div>
    </section>

    <!-- Perspective, mirroring style of material_discovery.md -->
    <div class="row mt-5">
        <div class="col-12">
            <h2 class="h4">Perspective</h2>
            <p>Agentic workflows can extend beyond <em>running</em> calculations to <em>reasoning</em> about them. By constraining tools (ASE/QE wrappers, batch modifiers), retaining state in Canvas, and codifying expert heuristics in the Convergence Agent, DREAMS demonstrates a principled path to <strong>trustworthy autonomy</strong> in scientific computing. Next steps include multi‑fidelity coupling (MLIPs ↔ DFT), multi‑physics expansions, and closed‑loop design that integrates synthesis‑aware constraints.</p>
        </div>
    </div>
</section>

<!-- Call-to-action buttons, consistent with style -->
<section class="container my-5">
    <div class="row">
        <div class="col-12 text-center">
            <div class="md-ctas mt-4">
                <a class="btn btn-paper me-3" href="{{ '/DREAMS.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer">Read the Paper</a>
                <a class="btn btn-code" href="https://github.com/BattModels/material_agent" target="_blank" rel="noopener noreferrer">Check the Code</a>
            </div>
        </div>
    </div>
</section>

