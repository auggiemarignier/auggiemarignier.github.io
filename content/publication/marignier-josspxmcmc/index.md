---
title: "PxMCMC: A Python package for proximal Markov Chain Monte Carlo"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- A. Marignier

# Author notes (optional)
author_notes: []

date: "26 July 2023"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*JOSS*"
publication_short: "*Journal of Open Source Software*"

abstract: Markov Chain Monte Carlo (MCMC) methods form the dominant set of algorithms for Bayesian inference.
The appeal of MCMC in the physical sciences is that it produces a set of samples from the posterior distribution of model parameters given the available data, integrating any prior information one may have about the parameters and providing a fully flexible way to quantify uncertainty.
However, it is well known that in high dimensions (many model parameters) standard MCMC struggles to converge to a solution due the exponentially large space to be sampled.
This led to the development of gradient-based MCMC algorithms, which use the gradient of the posterior distribution to efficiently navigate the parameter space.
While this allows MCMC to scale to high dimensions, it restricts the form of the posterior to be continuously differentiable.
Certain forms of prior information used in imaging problems, such as sparsity, use a non-smooth prior distribution, thus gradient-based MCMC cannot be used for these inference problems.
Proximal MCMC leverages the proximity mapping operator (Moreau, 1962), a form of generalised gradient, used in convex optimisation problems to efficiently navigate non-smooth parameter spaces.

tags: []

# Custom links (uncomment lines below)
links:
- name: URL
  url: https://joss.theoj.org/papers/10.21105/joss.05582
  icon_pack: fas
  icon: globe
- name: DOI
  url: https://doi.org/10.21105/joss.05582.
  icon_pack: ai
  icon: doi
- name: Code
  url: https://github.com/auggiemarignier/pxmcmc/releases/tag/v1.0.0
  icon_pack: fab
  icon: github
---