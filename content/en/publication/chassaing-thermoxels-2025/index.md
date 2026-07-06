---
title: 'Thermoxels: A Voxel-Based Method to Generate Simulation-Ready 3D Thermal
  Models'
authors:
- Etienne Chassaing
- Florent Forest
- Olga Fink
- Malcolm Mielle
date: '2025-04-06'
publishDate: '2026-07-06T00:00:00.000000Z'
publication_types:
- paper-conference
publication: '*Journal of Physics: Conference Series* (CISBAT 2025), vol. 3140,
  042003'
doi: 10.1088/1742-6596/3140/4/042003
abstract: In the European Union, buildings account for 42% of energy use and 35%
  of greenhouse gas emissions. Since most existing buildings will still be in use
  by 2050, retrofitting is crucial for emissions reduction. However, current building
  assessment methods rely mainly on qualitative thermal imaging, which limits data-driven
  decisions for energy savings. On the other hand, quantitative assessments using
  finite element analysis (FEA) offer precise insights but require manual CAD design,
  which is tedious and error-prone. Recent advances in 3D reconstruction, such as
  Neural Radiance Fields (NeRF) and Gaussian Splatting, enable precise 3D modeling
  from sparse images but lack clearly defined volumes and the interfaces between
  them needed for FEA. We propose Thermoxels, a novel voxel-based method able to
  generate FEA-compatible models, including both geometry and temperature, from a
  sparse set of RGB and thermal images. Using pairs of RGB and thermal images as
  input, Thermoxels represents a scene's geometry as a set of voxels comprising color
  and temperature information. After optimization, a simple process is used to transform
  Thermoxels' models into tetrahedral meshes compatible with FEA. We demonstrate
  Thermoxels' capability to generate RGB+Thermal meshes of 3D scenes, surpassing
  other state-of-the-art methods. To showcase the practical applications of Thermoxels'
  models, we conduct a simple heat conduction simulation using FEA, achieving convergence
  from an initial state defined by Thermoxels' thermal reconstruction. Additionally,
  we compare Thermoxels' image synthesis abilities with current state-of-the-art
  methods, showing competitive results, and discuss the limitations of existing
  metrics in assessing mesh quality.
tags:
- Computer Science - Computer Vision and Pattern Recognition
- Electrical Engineering and Systems Science - Image and Video Processing
image:
  caption: 'Thermoxels pipeline: from RGB + thermal images to a simulation-ready 3D mesh'
links:
- name: URL
  url: https://arxiv.org/abs/2504.04448
- name: Code
  url: https://github.com/Schindler-EPFL-Lab/thermoxels
---
