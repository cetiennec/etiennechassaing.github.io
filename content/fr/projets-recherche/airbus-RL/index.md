---
title: "Contrôle multi-drones par Apprentissage par Renforcement (RL)" 
summary: "Simulateur et contrôle multi-drones par Reinforcement Learning, validé en hardware-in-the-loop sur drones DJI."
domain: drones
client: "Airbus Group"
duration: "6 mois"
date: 2022-07-09
type: docs
tags:
  - Reinforcement-Learning
  - Contrôle
  - IA
  - Multi-agents
  - Drones
image:
  caption: 'Source : databasecamp'
---

## Contexte du projet

Stage de recherche de 6 mois chez Airbus Group, sur le contrôle multi-agents de drones par apprentissage par renforcement (Reinforcement Learning, RL). L'objectif était de concevoir un algorithme capable de coordonner des équipes de drones sur une tâche collaborative complexe, avec de meilleures performances que les techniques de contrôle existantes.

### Approche

J'ai développé un simulateur basé sur *OpenAI Gym* et utilisé *Stable Baselines3* pour entraîner les drones sur une tâche multi-agents. En comparant l'état de l'art du contrôle multi-agents, j'ai identifié les situations où le RL surpasse les méthodes traditionnelles, notamment en adaptabilité et en efficacité dans des scénarios complexes et dynamiques.

### Contributions

- Développement d'un simulateur pour l'entraînement et la validation d'algorithmes de contrôle.
- Conception d'un algorithme de contrôle multi-agents basé sur le RL.
- Identification des briques techniques où le RL fait mieux que les méthodes classiques sur des tâches multi-agents.
- Validation en conditions réelles sur des drones DJI, en Hardware in the Loop (HWIL), pour tester la robustesse et la performance des algorithmes dans un environnement quasi réel.

### Outils

- *Reinforcement Learning* avec *OpenAI Gym* et *Stable Baselines3*.
- Simulation multi-agents en boucle matérielle (HWIL).

### Résultats

Les algorithmes développés ont montré de meilleures performances et des stratégies nouvelles par rapport aux techniques existantes, en particulier dans des environnements dynamiques et incertains. Les essais sur drones DJI ont confirmé la faisabilité et la robustesse du contrôle multi-agents par RL pour des applications industrielles.
