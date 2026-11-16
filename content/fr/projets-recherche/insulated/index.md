---
title: "Projet Insulated : développement d'un modèle de reconstruction 3D multi-modal" 
summary: "Thermoxels : des modèles thermiques 3D de bâtiments à partir d'images RGB et thermiques."
domain: thermique
client: "EPFL et Schindler"
duration: "6 mois"
date: 2024-08-09
paper: /publication/chassaing-thermoxels-2025
code: https://github.com/Schindler-EPFL-Lab/thermoxels
type: docs
tags:
  - IA
  - Deep-Learning
  - Computer-Vision
---

<div class="pf-case-callout">
  <strong>📄 Thermoxels : article et code</strong>
  <span>La méthode est publiée à CISBAT 2025 (<em>Journal of Physics: Conference Series</em>), et son code est en accès libre.</span>
  <a href="/fr/publication/chassaing-thermoxels-2025/">Lire l'article →</a>
  <a href="https://github.com/Schindler-EPFL-Lab/thermoxels" target="_blank" rel="noopener">Voir le code sur GitHub →</a>
</div>

## Contexte du projet

Projet de recherche de 6 mois à l'EPFL, en partenariat avec Schindler, terminé en octobre 2024.

Les bâtiments représentent une part importante des émissions de CO2 en Europe, et la rénovation thermique est une solution clé pour réduire leur consommation énergétique. Elle est cruciale pour atteindre les objectifs climatiques fixés par l'Accord de Paris. Pourtant, il n'existe pas de méthode systématique et efficace pour modéliser les bâtiments en 3D tout en intégrant des données thermiques.

Le projet Insulated propose une méthode pour modéliser thermiquement des bâtiments en 3D. J'y ai développé *Thermoxels*, une approche qui utilise l'apprentissage automatique pour générer des modèles thermiques 3D précis, afin d'aider à prioriser les bâtiments à rénover et à identifier les zones à isoler.

### Objectifs

Automatiser la génération de Building Information Models (BIM) thermiques : à partir d'images RGB et thermiques, produire des modèles 3D géométriquement précis, avec une distribution correcte des températures, pour améliorer les simulations thermiques qui évaluent les besoins énergétiques et les résultats des rénovations.

### Méthode

Inspiré par les champs de radiance neuronaux (NeRF) et d'autres techniques de synthèse de vue, Thermoxels représente la scène par des voxels (cubes) qui portent à la fois la géométrie et la température, dans un format directement utilisable par les logiciels de simulation thermique (FEM, CFD). Cette approche contourne les limites des méthodes actuelles, qui demandent des capteurs coûteux ou un travail manuel laborieux.

### Résultats

- Une représentation explicite et indépendante des vues, intégrable directement dans les logiciels de simulation thermique.
- Des résultats prometteurs en précision thermique et géométrique.
- Une simulation de conduction thermique par éléments finis qui converge à partir de l'état initial reconstruit par Thermoxels.

### Suite

Le projet se poursuit avec des pistes d'amélioration, notamment l'apprentissage des résistances thermiques des matériaux pour des simulations plus précises.

## Encadrement

- Dr Malcolm Mielle
- Prof. Olga Fink
- Dr Florent Forest
