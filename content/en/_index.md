---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  spacing: "4rem"

# Homepage: home-hero and home-sections blocks (layouts/partials/blox/)
sections:
  - block: home-hero
    content:
      username: admin
      pitch: "I build controllers and learning systems for robots and drones, and I teach them."
      # Show the long bio (the author page body) over the photo instead of the pitch
      bio: true
      buttons:
        - text: Resume
          url: /experience/
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
          filename: test.jpeg
          filters:
            brightness: 0.4
          size: cover
          position: center
          parallax: false

  - block: home-sections
    content:
      # One-sentence statement between the hero and "What I do"
      statement:
        title: "At the intersection of control and AI,"
        text: "I am interested in methods that formally guarantee the learning of robust controllers on physical systems."
      what:
        title: What I do
        items:
          - icon: 🤗
            title: ML Engineer at Hugging Face
            text: "LeRobot on humanoid robots, and the Hugging Face robotics course."
            url: https://huggingface.co/cetiennec
            link: My Hugging Face profile
          - icon: 🎓
            title: Teaching
            text: "Courses at CentraleSupélec, ECE Paris and AlbertSchool, with all the material freely available."
            url: /teaching/
            link: See the courses
          - icon: 🛠️
            title: Missions and research
            text: "13 projects: drones, reinforcement learning, robotics, thermal systems."
            url: /fr/projects/
            link: See the portfolio (in French)
      side:
        title: Side projects
        text: "Alongside this, I build two side projects."
        items:
          - title: Cragdiary
            text: "A multi-pitch climbing logbook to tell your outings your way, with no performance tracking."
            url: https://cragdiary.com
            icon: /media/cragdiary-icon.png
          - title: The Future With AI
            text: "Write down your bets on how AI will shape the future, and revisit them years later."
            url: https://thefuturewithai.org
            icon: /media/tfwai-icon.svg
      selected:
        title: Selected work
        items:
          - page: /publication/chassaing-thermoxels-2025
            kind: Paper
          - url: /book/case-studies/drone_delayed_control/case_study.html
            title: Precision landing of a Parrot drone
            text: "Landing a Parrot Anafi AI on a QR-code target despite remote control, delays, wind and packet losses, step by step with code."
            image: /fr/projets/drone-precision-landing/featured.jpg
            kind: Case study
          - page: /teaching/centralesupelec/reinforcement-learning
            kind: Course
      logos:
        title: They trusted me
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
---
