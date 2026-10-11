---
title: "Études de cas"
date: 2025-06-01
type: landing

design:
  spacing: "2rem"
# Cards linking into the Jupyter Book at /book/case-studies/ (layouts/partials/blox/case-studies.html)
sections:
  - block: case-studies
    content:
      title: "Études de cas"
      text: "Cette page propose plusieurs des projets que j'ai réalisés sous format d'étude de cas, la modélisation, la résolution et la qualité des résultats sont présentés pour chaque projet."
      result_label: "Résultat clé"
      read_label: "Lire l'étude"
      items:
        - title: "Atterrissage de précision d'un drone Parrot"
          image: /book/case-studies/_images/drone_real-min.jpg
          tags: [Drones, Contrôle PID, Vision, Systèmes à retard]
          problem: "Faire atterrir un drone de 30 cm dans une zone de 60 cm repérée par QR code, alors que tout le calcul tourne sur un PC déporté."
          result: "Un bon réglage ne suffit pas : retards, bruit et pertes de paquets dégradent la stabilité, et la période de commande est le paramètre le plus influent."
          url: /book/case-studies/drone_delayed_control/case_study.html
          mission: /fr/projets/drone-precision-landing/
          mission_label: "Voir la mission"
        - title: "Contrôle d'un tuyau chauffé de 450 m"
          image: /book/case-studies/_images/PI_results.png
          fit: contain
          tags: [Thermique, PI, MPC, Reinforcement Learning]
          problem: "Réguler la température de sortie d'une boucle de 450 m proche de l'ébullition, avec un fort retard de transport."
          result: "PI, MPC et RL comparés : si le modèle est excellent, un PI bien réglé remplit les besoins dans la très large majorité des cas."
          url: /book/case-studies/heat_pipe_control/system_tutorial.html
          mission: /fr/projets/optimisation_thermique/
          mission_label: "Voir la mission"
        - title: "Environnement RL de bateaux de pêche"
          image: /book/case-studies/_images/example.gif
          tags: [Reinforcement Learning, Données AIS, Détection d'anomalies]
          problem: "Simuler le comportement de navires de pêche dans la ZEE de Dakar pour générer des exemples synthétiques de pêche illégale, rares dans les données réelles."
          result: "Un environnement fondé sur de vraies cartes et trajectoires AIS, où des agents apprennent des comportements de pêche ou d'évitement, réutilisables pour la détection d'anomalies."
          url: /book/case-studies/fishing_boat/case_study.html
          mission: /fr/projets/marl/
          mission_label: "Voir la mission"
---
