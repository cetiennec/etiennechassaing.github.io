---
title: "Etude du don d'objet entre un robot et un humain" 
summary: "Mesurer la rigidité de la prise humaine pour savoir quand un robot peut lâcher un objet."
domain: robotique
client: "Stanford University"
duration: "6 mois"
date: 2022-02-09
paper: /publication/pacaud-identifying-2023
type: docs
tags:
  - Contrôle
  - Robotique
  - Modélisation
---

<div class="pf-case-callout">
  <strong>📄 Article</strong>
  <span>Ces travaux sont publiés à la IEEE World Haptics Conference 2023 : <em>Identifying Human Grasp Properties During Robot-to-Human Handovers</em>.</span>
  <a href="/fr/publication/pacaud-identifying-2023/">Lire l'article →</a>
</div>

## Contexte du projet

Ce projet explore la manière dont un robot peut juger de la sécurité d'une prise humaine lors du transfert d'un objet. C'est un enjeu clé des interactions physiques entre humains et robots (pHRI), notamment pour la manipulation collaborative d'objets. L'objectif était de mesurer la rigidité de la prise humaine et d'en déduire quand le robot peut relâcher l'objet en toute sécurité.

### Mon rôle

Responsable de la recherche initiale, j'ai :

- conçu le modèle physique de la prise ;
- mis au point les méthodes d'identification de la rigidité, d'abord avec mon propre capteur de force, puis avec les capteurs de mouvement et de force d'un robot ;
- développé le cadre théorique, fondé sur l'identification de systèmes (Sys ID), pour modéliser et mesurer la rigidité d'une prise humaine ;
- mis en place les expériences qui valident cette approche.

### Résultats

Les expériences montrent que la rigidité d'une prise humaine augmente de manière prévisible avec la force appliquée par le sujet. Le robot peut donc détecter le moment où il est sûr de relâcher l'objet, ce qui améliore la sécurité et la fluidité des transferts entre humains et robots.

### Suite

Ces travaux fournissent une méthode robuste pour mesurer en temps réel la rigidité de la prise humaine lors des transferts robot-humain, et ouvrent la voie à des interactions physiques plus sûres dans les applications industrielles et collaboratives.
