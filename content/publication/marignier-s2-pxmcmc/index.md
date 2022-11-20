---
title: "Posterior sampling for inverse imaging problems on the sphere in seismology and cosmology"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- A. Marignier
- J. D. McEwen
- A. M. G. Ferreira
- T. D. Kitching

# Author notes (optional)
author_notes: []

date: "14 Sep 2022"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "*Royal Astronomical Society Techniques and Instruments, under review*"
publication_short: "*RASTI, under review*"

abstract:     In this work, we describe a framework for solving spherical inverse imaging problems using posterior sampling for full uncertainty quantification.
    Inverse imaging problems defined on the sphere arise in many fields, including seismology and cosmology where images are defined on the globe and the cosmic sphere, and are generally high-dimensional and computationally expensive.
    As a result, sampling the posterior distribution of spherical imaging problems is a challenging task.
    Our framework leverages a proximal Markov chain Monte Carlo (MCMC) algorithm to efficiently sample the high-dimensional space of spherical images with a sparsity-promoting wavelet prior.
    We detail the modifications needed for the algorithm to be applied to spherical problems, and give special consideration to the crucial forward modelling step which contains computationally expensive spherical harmonic transforms.
    By sampling the posterior, our framework allows for full and flexible uncertainty quantification, something which is not possible with other methods based on, for example, convex optimisation.
    We demonstrate our framework in practice on full-sky cosmological mass-mapping and to the construction of phase velocity maps in global seismic tomography.
    We find that our approach is potentially useful at moderate resolutions, such as those of interest in seismology.
    However at high resolutions, such as those required for astrophysical applications, the poor scaling of the complexity of spherical harmonic transforms severely limits our method, which may be resolved with future GPU implementations.
    A new Python package, pxmcmc, containing the proximal MCMC sampler, measurement operators, wavelet transforms and sparse priors is made publicly available.

tags: []

# Custom links (uncomment lines below)
links:
- name: URL
  url: https://arxiv.org/abs/2107.06500
  icon_pack: fas
  icon: globe
- name: DOI
  url: https://doi.org/10.48550/arXiv.2107.06500
  icon_pack: ai
  icon: doi

---