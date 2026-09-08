---
title: CentraleSupélec — Apprentissage par renforcement
summary: "Refonte du cours PARL : quatre cours et des TD écrits, des MDP au contrôle sans modèle."
type: docs
math: true
---

## Apprentissage par renforcement — CentraleSupélec

Refonte du cours PARL, structurée en **quatre séances de cours**, chacune suivie d'une
feuille de TD écrite qui reprend le sujet du cours précédent.

Les sources LaTeX vivent dans un dépôt privé ; les PDF diffusés sont publiés sur
[github.com/cetiennec/cours-pdf](https://github.com/cetiennec/cours-pdf) et servis
directement depuis GitHub — cliquez un titre pour un aperçu en ligne, ou « open » pour
le PDF en plein écran.

### Cours

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/cours/01-introduction-mdp/diffusion/01-introduction-mdp.pdf"
    title="1 — Introduction et MDP" >}}

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/cours/02-programmation-dynamique/diffusion/02-programmation-dynamique.pdf"
    title="2 — Programmation dynamique" >}}

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/cours/03-model-free-learning/diffusion/03-model-free-learning.pdf"
    title="3 — Prédiction sans modèle" >}}

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/cours/04-deep-rl-applications/diffusion/04-deep-rl-applications.pdf"
    title="4 — Contrôle sans modèle et deep RL" >}}

Séance 1 : processus de décision markoviens, retour, fonctions de valeur, équations de
Bellman. Séance 2 : évaluation de politique, itération sur la politique, itération sur
la valeur. Séance 3 : méthodes de Monte-Carlo, différences temporelles TD(0). Séance 4 :
Monte-Carlo control, SARSA, Q-Learning, et une ouverture sur le deep RL.

### TD écrits

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/TD-2026-2027/01-introduction-mdp/diffusion/exercises.pdf"
    title="TD — Introduction et MDP" >}}

{{< pdf src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/centralesupelec/reinforcement-learning/TD-2026-2027/02-programmation-dynamique/diffusion/exercises.pdf"
    title="TD — Programmation dynamique" >}}

> Les feuilles de TD des séances 3 et 4, ainsi que les notebooks, sont en préparation.

---

Voir aussi la [formation Deep Reinforcement Learning](/fr/formations/drl/) que je propose
en entreprise, sur les mêmes fondamentaux mais orientée mise en pratique avec
Stable-Baselines3 et Gym.
