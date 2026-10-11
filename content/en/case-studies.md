---
title: "Case Studies"
date: 2025-06-01
type: landing

design:
  spacing: "2rem"
# Cards linking into the Jupyter Book at /book/case-studies/ (layouts/partials/blox/case-studies.html)
sections:
  - block: case-studies
    content:
      title: "Case Studies"
      text: "This page presents several of my projects as case studies: for each one, the modelling, the solution and the quality of the results are laid out."
      result_label: "Key result"
      read_label: "Read the study"
      items:
        - title: "Precision landing of a Parrot drone"
          image: /book/case-studies/_images/drone_real-min.jpg
          tags: [Drones, PID control, Vision, Delayed systems]
          problem: "Land a 30 cm drone in a 60 cm area marked by a QR code, while all the computation runs on a remote PC."
          result: "Good tuning is not enough: delays, noise and packet losses erode stability, and the controller update rate matters most."
          url: /book/case-studies/drone_delayed_control/case_study.html
          mission: /fr/projets/drone-precision-landing/
          mission_label: "See the mission (in French)"
        - title: "Controlling a 450 m heated pipe"
          image: /book/case-studies/_images/PI_results.png
          fit: contain
          tags: [Thermal, PI, MPC, Reinforcement learning]
          problem: "Regulate the outlet temperature of a 450 m loop close to boiling point, with a long transport delay."
          result: "PI, MPC and RL compared: with an excellent model, a well-tuned PI meets the needs in the vast majority of cases."
          url: /book/case-studies/heat_pipe_control/system_tutorial.html
          mission: /fr/projets/optimisation_thermique/
          mission_label: "See the mission (in French)"
        - title: "Fishing-boat reinforcement learning environment"
          image: /book/case-studies/_images/example.gif
          tags: [Reinforcement learning, AIS data, Anomaly detection]
          problem: "Simulate fishing vessels in Dakar's exclusive economic zone to generate synthetic examples of illegal fishing, which are rare in real data."
          result: "An environment built on real maps and AIS trajectories, where agents learn fishing or evasive behaviours, reusable for anomaly detection."
          url: /book/case-studies/fishing_boat/case_study.html
          mission: /fr/projets/marl/
          mission_label: "See the mission (in French)"
---
