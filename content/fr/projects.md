---
title: 'Portfolio'
date: 2024-05-19
type: landing

design:
  spacing: '3rem'

# Page sections
sections:
  # Projects grouped by their `domain` front matter (layouts/partials/blox/portfolio.html)
  - block: portfolio
    content:
      text: |-
        <h1 class="pf-title-page">Portfolio</h1>

        Les missions que j'ai réalisées pour des entreprises, de la startup au grand groupe, et mes projets de recherche, classés par domaine. Chaque carte mène au détail du projet.
      groups:
        - id: drones
          title: Drones et contrôle de vol
          text: Guidage, interception et contrôle de drones, du simulateur aux essais en vol.
        - id: rl
          title: Reinforcement Learning multi-agents
          text: Stratégies d'apprentissage par renforcement pour faire coopérer plusieurs agents.
        - id: robotique
          title: Robotique
          text: Bras robotiques, robot agricole, interaction humain-robot et veille technologique.
        - id: thermique
          title: Thermique et capteurs
          text: Modélisation et contrôle de systèmes thermiques, vision 3D thermique et capteurs connectés.
---
