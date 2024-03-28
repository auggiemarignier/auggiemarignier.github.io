---
title: "Fast emulation of anisotropies induced in the cosmic microwave background by cosmic strings"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- M. A. Price
- M. Mars
- M. M. Docherty
- A. Spurio Mancini
- A. Marignier
- J. D. McEwen

# Author notes (optional)
author_notes: []

date: "06 Oct 2023"

# Publication type.
# https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Open Journal of Astrophysics*"
publication_short: "*OJA*"

abstract: Cosmic strings are linear topological defects that may have been produced during symmetry-breaking phase transitions in the very early Universe. In an expanding Universe the existence of causally separate regions prevents such symmetries from being broken uniformly, with a network of cosmic string inevitably forming as a result. To faithfully generate observables of such processes requires computationally expensive numerical simulations, which prohibits many types of analyses. We propose a technique to instead rapidly emulate observables, thus circumventing simulation. Emulation is a form of generative modelling, often built upon a machine learning backbone. End-to-end emulation often fails due to high dimensionality and insufficient training data. Consequently, it is common to instead emulate a latent representation from which observables may readily be synthesised. Wavelet phase harmonics are an excellent latent representations for cosmological fields, both as a summary statistic and for emulation, since they do not require training and are highly sensitive to non-Gaussian information. Leveraging wavelet phase harmonics as a latent representation, we develop techniques to emulate string induced CMB anisotropies over a 7.2 degree field of view, with sub-arcminute resolution, in under a minute on a single GPU. Beyond generating high fidelity emulations, we provide a technique to ensure these observables are distributed correctly, providing a more representative ensemble of samples. The statistics of our emulations are commensurate with those calculated on comprehensive Nambu-Goto simulations. Our findings indicate these fast emulation approaches may be suitable for wide use in, e.g., simulation based inference pipelines. We make our code available to the community so that researchers may rapidly emulate cosmic string induced CMB anisotropies for their own analysis.

tags: []

# Custom links (uncomment lines below)
links:
- name: URL
  url: https://astro.theoj.org/article/88524-fast-emulation-of-anisotropies-induced-in-the-cosmic-microwave-background-by-cosmic-strings
  icon_pack: fas
  icon: globe
- name: DOI
  url: https://doi.org/10.21105/astro.2307.04798
  icon_pack: ai
  icon: doi
- name: Code
  url: https://github.com/astro-informatics/stringgen
  icon_pack: fab
  icon: github
---