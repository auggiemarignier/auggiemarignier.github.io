---
title: "Proximal Markov chain Monte Carlo: Towards building a sparse Earth model"

event: "SSA Virtual Tomography Sessions"
event_url: "https://www.seismosoc.org/tomography/past-tomography/"

location: "Online"
address: 
  street:  ""
  city:  ""
  region:  ""
  postcode:  ""
  country:  ""

summary: ""
abstract: "Probabilistic sampling methods such as Markov chain Monte Carlo (MCMC) are a popular way to sample the posterior probability density function of an inverse problem. They are common in seismic tomography on local and regional scales, however they struggle on global scales where the dimensionality of the problem is typically much higher. The appeal of these methods for tomography is twofold: they allow for full uncertainty quantification and can solve non-linear inverse problems. Solutions to high-dimensional problems include the Hamiltonian Monte Carlo (HMC) method, which uses the gradient of the posterior to guide the sampling search. Unfortunately, this prohibits using non-smooth priors such as the Laplace distribution which promotes sparsity. Sparse image reconstructions have been shown to be able to recover both sharp and smooth features, even in underdetermined systems or when data are poorly distributed, the latter of which is a common scenario in seismic tomography.  

In this work we use a recent proximal MCMC algorithm to build global fundamental mode Rayleigh wave phase velocity maps. Proximal MCMC leverages proximal calculus to allow non-differentiable priors in a high-dimensional inversion. As such, we adopt a sparsity-promoting prior, promoting sparsity in a spherical wavelet basis. We perform synthetic experiments and compare our results to those of a typical linear least-squares inversion. Finally, we discuss the future possibilities of building a 3D Earth model with uncertainties using a similar wavelet parameterised proximal MCMC approach."

date: "2021-02-02"
all_day: true

authors: []
tags: []

featured: false

links:
- name: Slides
  url: main.pdf
  icon_pack: fas
  icon: chalkboard-teacher
- name: Code
  url: https://github.com/auggiemarignier/pxmcmc
  icon_pack: fab
  icon: github
---
