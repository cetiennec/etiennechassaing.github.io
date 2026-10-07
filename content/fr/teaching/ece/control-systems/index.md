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

### Diaporamas de cours

| # | Séance | Contenu | Pages |
| - | ------ | ------- | ----- |
| 5 | [Systèmes continus et discrets](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/05-transformee-z/diffusion/05-transformee-z.pdf) | Transformées de Laplace et en $\mathcal{Z}$ | 32 |
| 5 bis | [Éléments simples](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/05-bis-elements-simples/diffusion/05-bis-elements-simples.pdf) | Décomposition des fractions rationnelles, cas général | 10 |
| 6 | [Systèmes échantillonnés](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/06-systemes-echantillonnes/diffusion/06-systemes-echantillonnes.pdf) | Échantillonnage, bloqueur d'ordre zéro, régulation numérique | 38 |
| 7 | [Correcteur PID numérique](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/07-pid-echantillonnes/diffusion/07-pid-echantillonnes.pdf) | Du modèle à l'implantation réelle | 39 |
| 8 | [Filtrage et filtre de Kalman](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/08-filtrage-kalman/diffusion/08-filtrage-kalman.pdf) | Du signal bruité à l'estimation optimale d'état | 26 |
| 9 | [Applications et révisions](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/09-applications-revisions/diffusion/09-applications-revisions-etudiant.pdf) | Approches data-based, étude de cas du pendule inversé *(version étudiant)* | 19 |

### QCM de mi-parcours

QCM d'une page sur les systèmes échantillonnés et le filtrage, en 20 minutes. Chaque
étudiant reçoit un **sujet individualisé** : les sujets sont générés avec
[auto-multiple-choice](https://www.auto-multiple-choice.net/) avec un tirage aléatoire
différent par groupe, puis corrigés par lecture optique.

- [Exemple de sujet (PDF)](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/qcm-final/diffusion/qcm_midterm_exemple.pdf)

### Examen final

Un sujet construit comme une **étude de cas filée** : les quatre parties traitent
successivement la modélisation, l'asservissement continu, la discrétisation et
l'implémentation embarquée, puis le filtrage et la fusion de capteurs, sur un seul et même
système, le contrôle en altitude d'un drone d'observation agricole.

Durée : **1h30**, calculatrice et documents interdits. 20 points, plus 2 points de bonus.
Le corrigé n'est pas diffusé.

<div style="position:relative;padding-top:129%;margin:1.5rem 0;border:1px solid #d4d4d8;border-radius:6px;overflow:hidden;">
  <iframe
    src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    title="Examen final : Systèmes bouclés (PDF)"></iframe>
</div>

Autres documents : [feuille réponse (PDF)](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final_feuille_reponse.pdf) · [sujet en plein écran](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf)
