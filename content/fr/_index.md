---
# Leave the homepage title empty to use the site title
title: ""
date: 2024-10-04
type: landing

design:
  spacing: "4rem"

# Homepage: home-hero and home-sections blocks (layouts/partials/blox/)
sections:
  - block: home-hero
    content:
      username: admin_fr
      pitch: "Je conçois des contrôleurs et des systèmes d'apprentissage pour des robots et des drones, et je les enseigne."
      # Show the long bio (the author page body) over the photo instead of the pitch
      bio: true
      buttons:
        - text: Mon CV
          url: /fr/experience/
          primary: true
        - text: Portfolio
          url: /fr/projects/
        - text: Contact
          url: mailto:contact@etiennechassaing.com
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: mountain-cover.jpg
          filters:
            brightness: 0.45
          size: cover
          position: center
          parallax: false

  - block: home-sections
    content:
      # One-sentence statement between the hero and "What I do"
      statement:
        title: "Au croisement du contrôle et de l'IA,"
        text: "je m'intéresse aux méthodes permettant de garantir de façon formelle l'apprentissage de contrôleurs robustes sur des systèmes physiques."
      what:
        title: Ce que je fais
        items:
          - icon: 🤗
            title: ML Engineer chez Hugging Face
            text: "LeRobot sur des humanoïdes et le cours de robotique de Hugging Face."
            url: https://huggingface.co/cetiennec
            link: Mon profil Hugging Face
          - icon: 🎓
            title: Enseignement
            text: "Cours à CentraleSupélec, ECE Paris et AlbertSchool, avec tous les supports en accès libre."
            url: /fr/teaching/
            link: Voir les cours
          - icon: 🛠️
            title: Missions et recherche
            text: "13 projets : drones, Reinforcement Learning, robotique, thermique."
            url: /fr/projects/
            link: Voir le portfolio
      selected:
        title: Travaux choisis
        items:
          - page: /publication/chassaing-thermoxels-2025
            kind: Publication
          - page: /projets/drone-precision-landing
            kind: Étude de cas
          - page: /teaching/centralesupelec/reinforcement-learning
            kind: Cours
      logos:
        title: Ils m'ont fait confiance
        items:
          - name: Hugging Face
            img: /fr/assets/huggingface.png
            url: https://huggingface.co
          - name: Airbus Group
            img: /fr/assets/airbus-group.png
            url: /fr/projets-recherche/airbus-rl/
          - name: Schindler
            img: /fr/assets/schindler.png
            url: /fr/projets-recherche/insulated/
          - name: Stryx
            img: /fr/assets/stryx.jpeg
            url: /fr/projets/stryx-ai-drone-interception/
          - name: Eurofins
            img: /fr/assets/logo-eurofins.jpg
          - name: Geomatys
            img: /fr/assets/geomatys.jpeg
            url: /fr/projets/marl/
          - name: phospho
            img: /fr/assets/phospho.svg
            url: /fr/projets/phospho/
          - name: Neode Systems
            img: /fr/assets/neodesystems_logo.jpeg
            url: /fr/projets/dev_ia_drones/
          - name: Nehemis
            img: /fr/assets/nehemis.png
          - name: Junior CentraleSupélec
            img: /fr/assets/JCS.png
          - name: Software République
            img: /fr/assets/software-republique.webp
      side:
        title: Projets personnels
        items:
          - title: Cragdiary
            text: "Un carnet de grande voie pour raconter vos sorties, sans suivi de performance."
            url: https://cragdiary.com
            icon: /media/cragdiary-icon.png
          - title: The Future With AI
            text: "Écrivez vos paris sur le futur de l'IA et relisez-les dans quelques années."
            url: https://thefuturewithai.org
            icon: /media/tfwai-icon.svg
---
