---
title: Systèmes Bouclés
summary: "Régulation numérique : six diaporamas, le QCM de mi-parcours et l'examen final."
type: docs
sidebar:
  sections: true
weight: 1
math: true
---

Cours de régulation numérique dispensé en promotion complète (500 élèves) d'avril à
juin 2026 : transformée en $z$, discrétisation, PID échantillonné, filtrage et Kalman.

**J'ai assuré la deuxième partie du cours** (les séances 5 à 9, la régulation numérique
proprement dite) ainsi que les évaluations qui s'y rapportent. La première partie, sur
les systèmes continus, était assurée par un autre intervenant.

Les documents ci-dessous sont ceux réellement distribués aux étudiants.

### Supports

- Séance 5 : systèmes continus et discrets, transformées de Laplace et en $\mathcal{Z}$.
- Séance 5 bis : éléments simples, décomposition des fractions rationnelles dans le cas général.
- Séance 6 : systèmes échantillonnés, échantillonnage, bloqueur d'ordre zéro, régulation numérique.
- Séance 7 : correcteur PID numérique, du modèle à l'implantation réelle.
- Séance 8 : filtrage et filtre de Kalman, du signal bruité à l'estimation optimale d'état.
- Séance 9 : applications et révisions, approches data-based, étude de cas du pendule inversé.

Diaporamas des séances 5 à 9 et sujet de l'examen final :

{{< teaching-reader course="ece/sbe" title="Systèmes bouclés échantillonnés : supports" >}}

### QCM de mi-parcours

QCM d'une page sur les systèmes échantillonnés et le filtrage, en 20 minutes. Chaque
étudiant reçoit un **sujet individualisé** : les sujets sont générés avec
[auto-multiple-choice](https://www.auto-multiple-choice.net/) avec un tirage aléatoire
différent par groupe, puis corrigés par lecture optique.

### Examen final

Un sujet construit comme une **étude de cas filée** : les quatre parties traitent
successivement la modélisation, l'asservissement continu, la discrétisation et
l'implémentation embarquée, puis le filtrage et la fusion de capteurs, sur un seul et même
système, le contrôle en altitude d'un drone d'observation agricole.

Durée : **1h30**, calculatrice et documents interdits. 20 points, plus 2 points de bonus.
Le corrigé n'est pas diffusé. Le sujet est le dernier document des
[supports](#supports) ci-dessus.
