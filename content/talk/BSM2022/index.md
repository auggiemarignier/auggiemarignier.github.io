---
title: "Proximal MCMC: Towards Building a Sparse Earth Model"

event: "British Seismology Meeting 2022"
event_url: "https://wserv4.esc.cam.ac.uk/bsm/#"

location:  "Downing College"
address: 
  street:  ""
  city:  "Cambridge"
  region:  ""
  postcode:  ""
  country:  ""

summary: ""
abstract: "Probabilistic sampling methods such as Markov chain Monte Carlo (MCMC) are a popular
way to sample the posterior probability density function of an inverse problem. They are
common in seismic tomography on local and regional scales, however they struggle on global
scales where the dimensionality of the problem is typically much higher. The appeal of these
methods for tomography is twofold: they allow for full uncertainty quantification and can
solve non-linear inverse problems. Solutions to high-dimensional problems include the
Hamiltonian Monte Carlo (HMC) method, which uses the gradient of the posterior to guide
the sampling search. Unfortunately, this prohibits using non-smooth priors such as the
Laplace distribution which promotes sparsity. Sparse image reconstructions have been shown
to be able to recover both sharp and smooth features, even in underdetermined systems or
when data are poorly distributed, the latter of which is a common scenario in seismic
tomography. In this work we use a recent proximal MCMC algorithm to build 2D global
fundamental mode Rayleigh wave phase velocity maps. Proximal MCMC leverages proximal
calculus to allow non-differentiable priors in a high-dimensional inversion. As such, we adopt
a sparsity-promoting prior, promoting sparsity in an axisymmetric spherical wavelet basis.
We perform synthetic experiments and real data inversions as an illustrative example of this
method. Finally, we introduce a new parameterisation of the 3D sphere using Fourier-Laguerre wavelets to impose sparsity in both the azimuthal and radial directions. This
parameterisation is used to invert the Rayleigh wave phase velocity maps for a 3D shear
velocity in the upper mantle."

date: "2022-09-12"
all_day: true

authors: []
tags: []

featured: false

links:
- name: Poster
  url: poster.pdf
  icon_pack: fas
  icon: scroll
- name: Code
  url: https://github.com/auggiemarignier/pxmcmc
  icon_pack: fab
  icon: github
---
