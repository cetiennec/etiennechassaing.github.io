---
title: "Atterrissage de précision d'un drone Parrot"
summary: "Faire atterrir un drone Parrot Anafi AI sur une cible repérée par QR code, malgré un contrôle déporté sujet aux retards, au vent et aux pertes de paquets."
domain: drones
duration: "4 mois"
case_study: /book/case-studies/drone_delayed_control/case_study.html
date: 2025-03-01
type: docs
tags:
  - Drones
  - Contrôle
  - Vision
image:
  caption: 'Drone Parrot Anafi AI en approche de la cible'
---

<div class="pf-case-callout">
  <strong>📘 Étude de cas</strong>
  <span>La détection de la cible, la commande PID et l'étude de l'impact du vent, des retards et des pertes de paquets sont détaillées pas à pas, avec le code, dans l'étude de cas.</span>
  <a href="/book/case-studies/drone_delayed_control/case_study.html">Lire l'étude de cas : Precision-landing of a Parrot drone →</a>
</div>

## Contexte de la Mission
Durée : **mars à juin 2025**

### Objectifs :

Faire atterrir de façon autonome un drone Parrot Anafi AI à l'intérieur d'une cible, avec une orientation correcte si possible. Toute la chaîne de calcul tourne sur un PC déporté : le système doit donc composer avec les retards de communication, à l'envoi des commandes comme à la réception de l'odométrie et du flux vidéo.

### Tâches effectuées :

- Repérage de la cible par QR code, plus rapide et plus robuste que la reconnaissance d'image initialement envisagée.
- Estimation de la pose relative du drone à partir de la caméra, l'odométrie interne étant bruitée près du sol.
- Modélisation du drone et conception d'une commande PID en vitesse, avec gestion du lacet.
- Réglage de la commande en présence de retard.
- Étude de robustesse en conditions réelles : vent, bruit capteur, pertes de paquets et retards variables.
- Analyse de stabilité du système bouclé.
