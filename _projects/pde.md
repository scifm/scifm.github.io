---
title: Foundations Models for PDEs
layout: project
card-title: Partial Differential Equations
card-content: Creating surrogate physics models by finetuning a foundation model trained on multiple PDEs.
people:
- amalss
- bharath
card-image: /assets/img/pde_fig1.png
---

<section class="container my-5">
    	<div class="row align-items-start mb-4">
    		<div class="col-12">
			<h1 class="display-6 fw-bold">Foundation Models for PDEs</h1>
			<p>Score-based diffusion models offer a unified, probabilistic framework for solving forward and inverse problems in scientific computing.</p>

			<p>The team demonstrates their effectiveness for robust uncertainty quantification (UQ) in two key applications: field reconstruction and large-scale weather forecasting. The benefits of utilizing generative models for scientific computing can be summarized as follows:</p>

			<ul>
				<li>High-frequency details</li>
				<li>Ensemble sampling</li>
				<li>Unbiased uncertainty quantification</li>
				<li>Robustness to Noise</li>
			</ul>
		</div>


	</div>

	<hr />

	<section class="mb-5">
		<h3 class="h5"><strong>Forward - LaDCast</strong></h3>

		<div class="text-center mt-3">
			<img class="figure-full" src="{{ '/assets/img/pde_fig1.png' | relative_url }}" alt="PDE foundation model overview" style="width:92%; max-width:900px; object-fit:contain;" />
            <p class="mt-2" style="text-align:left; max-width:900px; margin-left:auto; margin-right:auto;">For forward problems, we introduce <strong>LaDCast</strong>, the first latent diffusion model for global weather forecasting. Trained on the ERA5 reanalysis dataset (1979–2017, 121×240 grid), LaDCast employs a deep compression autoencoder (DC-AE) with modified CNN kernels to efficiently encode large-scale atmospheric data. The model achieves performance comparable to the state-of-the-art probabilistic numerical weather prediction system (IFS-ENS) without requiring perturbed initial conditions and demonstrates superior skill in precipitation prediction.</p>
		</div>

		<div class="text-center mt-3">
			<img class="figure-full" src="{{ '/assets/img/pde_fig2.png' | relative_url }}" alt="LaDCast architecture" style="width:92%; max-width:900px; object-fit:contain;" />
			<p class="mt-2" style="text-align:left; max-width:900px; margin-left:auto; margin-right:auto;">A 15-day forecast can be generated in under one minute on a single H100 GPU, with multiple ensemble members produced in parallel. This enables computationally efficient, scalable, and low-bias uncertainty quantification for autoregressive predictions.</p>
		</div>

		<div class="text-center mt-4">
			<img class="figure-full" src="{{ '/assets/img/pde_fig3.png' | relative_url }}" alt="LaDCast performance" style="width:92%; max-width:900px; object-fit:contain;" />		
		</div>
	</section>

	<section class="mb-5">
		<h3 class="h5"><strong>Inverse - DiffusionReconstruct</strong></h3>

		<div class="text-center mt-3">
			<img class="figure-full" src="{{ '/assets/img/pde_fig4.png' | relative_url }}" alt="DiffusionReconstruct schematic" style="width:92%; max-width:900px; object-fit:contain;" />
			<p class="mt-2" style="text-align:left; max-width:900px; margin-left:auto; margin-right:auto;">The model reconstructs global fields from sparse data by generating an ensemble of plausible realizations. Our work presents a diffusion-based framework for reconstructing spatial and spatio-temporal fields from sparse and noisy sensor observations. Unlike traditional deterministic reconstruction methods, this probabilistic formulation enables the model to capture the underlying uncertainty and variability inherent in sparsely observed systems.</p>
		</div>

		<div class="text-center mt-4">
			<img class="figure-full" src="{{ '/assets/img/pde_fig5.png' | relative_url }}" alt="DiffusionReconstruct results" style="width:92%; max-width:900px; object-fit:contain;" />
			<p class="mt-2" style="text-align:left; max-width:900px; margin-left:auto; margin-right:auto;">Built upon a UNet backbone with cross-attention, the model effectively integrates spatial context from sparse measurements to infer full-field structures. This design allows the network to represent multiple plausible realizations rather than memorizing specific patterns, providing robustness against noise and incomplete observations.</p>
		</div>
	</section>

	<!-- Read more / CTA -->
	<section class="container my-4">
		<div class="row">
			<div class="col-12 text-center">
				<div class="md-ctas mt-4">
					<a class="btn btn-paper me-3" href="https://arxiv.org/abs/2506.09193" target="_blank" rel="noopener noreferrer">LaDCast</a>
					<a class="btn btn-code" href="https://doi.org/10.1016/j.cma.2024.117623" target="_blank" rel="noopener noreferrer">DiffusionReconstruct</a>
				</div>
			</div>
		</div>
	</section>

</section>