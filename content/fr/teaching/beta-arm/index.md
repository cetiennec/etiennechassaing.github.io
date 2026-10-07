---
title: "Bras trieur — bêta"
summary: "Aperçu non listé de la bannière animée proposée pour la page Cours."
type: docs
math: true
noindex: true
_build:
  list: never
  render: always
---

## Aperçu bêta

Cette page n'est liée nulle part et reste hors des moteurs de recherche : elle existe pour
regarder la bannière dans le vrai site, avec le vrai thème, les vrais logos et le bouton
mode sombre de la navbar. Rien n'a changé sur la page Cours en ligne.

### Option 1 — les trois écoles

{{< sorting-arm bins="CENTRALE/RL|ECE/SYS. BOUCLÉS|ALBERT/MATHS" >}}

La bannière telle qu'elle se placerait en haut de [Cours](../), au-dessus des trois
cartes :

<div class="school-cards">

<a class="school-card" href="../centralesupelec/">
  <div class="school-logo"><img src="../assets/logo-centralesupelec.png" alt="CentraleSupélec"></div>
  <div class="school-card-name">CentraleSupélec</div>
  <div class="school-card-desc">Apprentissage par renforcement</div>
</a>

<a class="school-card" href="../ece/">
  <div class="school-logo"><img src="../assets/logo-ece.webp" alt="ECE Paris"></div>
  <div class="school-card-name">ECE Paris</div>
  <div class="school-card-desc">Systèmes Bouclés</div>
</a>

<a class="school-card" href="../albertschool/">
  <div class="school-logo"><img src="../assets/logo-albertschool.png" alt="AlbertSchool"></div>
  <div class="school-card-name">AlbertSchool</div>
  <div class="school-card-desc">Mathematics Foundations</div>
</a>

</div>

### Option 2 — une école, trois séances

La même machine triant trois exemplaires du logo ECE vers les trois blocs du cours de
régulation numérique, pour la [page ECE](../ece/) plutôt que pour la page Cours.

{{< sorting-arm logos="../assets/logo-ece.webp|../assets/logo-ece.webp|../assets/logo-ece.webp" bins="TRANSFORMÉE Z/SÉANCE 5|PID ÉCH./SÉANCE 7|KALMAN/SÉANCE 9" >}}

### Notes

Tout est simulé plutôt qu'interpolé : cinématique inverse à deux bras en forme close
(branche coude en haut), chaque articulation suivie par une loi PD à $k_p = 70$,
$k_d = 13{,}5$ — soit $\omega_n \approx 8{,}4$ rad/s et $\zeta \approx 0{,}81$. Le léger
dépassement à l'arrivée de la pince, c'est le correcteur qui converge. Un poignet à
parallélogramme garde la tête droite, la pince s'ouvre au-dessus du bac et le logo tombe
en chute libre, et les yeux anticipent le mouvement vers la cible suivante.

La bannière se met en pause hors écran, respecte `prefers-reduced-motion` (une image fixe
composée et un bouton lecture) et porte un bouton pause en bas à droite.
