---
title: "Sparse Bayesian mass-mapping using trans-dimensional MCMC"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- A. Marignier
- T. D. Kitching
- J. D. McEwen
- A. M. G. Ferreira

# Author notes (optional)
author_notes: []

date: "19 Jun 2023"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*Open Journal of Astrophysics*"
publication_short: "*OJA*"

abstract:     Uncertainty quantification is a crucial step of cosmological mass-mapping that is often ignored.
    Suggested methods are typically only approximate or make strong assumptions of Gaussianity of the shear field.
    Probabilistic sampling methods, such as Markov chain Monte Carlo (MCMC), draw samples form a probability distribution, allowing for full and flexible uncertainty quantification, however these methods are notoriously slow and struggle in the high-dimensional parameter spaces of imaging problems.
    In this work we use, for the first time, a trans-dimensional MCMC sampler for mass-mapping, promoting sparsity in a wavelet basis.
    This sampler gradually grows the parameter space as required by the data, exploiting the extremely sparse nature of mass maps in wavelet space.
    The wavelet coefficients are arranged in a tree-like structure, which adds finer scale detail as the parameter space grows.
    We demonstrate the trans-dimensional sampler on galaxy cluster-scale images where the planar modelling approximation is valid.
    In high-resolution experiments, this method produces naturally parsimonious solutions, requiring less than 1\% of the potential maximum number of wavelet coefficients and still producing a good fit to the observed data.
    In the presence of noisy data, trans-dimensional MCMC produces a better reconstruction of mass-maps than the standard smoothed Kaiser-Squires method, with the addition that uncertainties are fully quantified.
    This opens up the possibility for new mass maps and inferences about the nature of dark matter using the new high-resolution data from upcoming weak lensing surveys such as \emph{Euclid}.

tags: []

# Custom links (uncomment lines below)
links:
- name: URL
  url: https://astro.theoj.org/article/81253-sparse-bayesian-mass-mapping-using-trans-dimensional-mcmc
  icon_pack: fas
  icon: globe
- name: DOI
  url: https://doi.org/10.21105/astro.2211.13963
  icon_pack: ai
  icon: doi
- name: Code
  url: https://github.com/auggiemarignier/tdtmassmapping
  icon_pack: fab
  icon: github
---