---
title: 'Experience'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: cta-button-list
    content:
      # Need a custom icon?
      # Add an SVG image to the `assets/media/icons/` folder and reference it in the `icon` field below
      buttons:
        - text: Téléchargez mon CV
          icon: custom/download
          url: https://drive.google.com/file/d/1MMlh1rtOdCdeIpU9QKK-XQv2tei8wmIu/view?usp=share_link
  - block: resume-skills
    content:
      title: Compétences 
      id: 1
      username: admin_fr
    design:
      columns: '1'

  - block: resume-experience
    content:
      username: admin_fr
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: false
  - block: resume-awards
    content:
      title: Récompenses
      username: admin_fr
  - block: 'github.cetiennec.language_block'
    content:
      title: Langues
      text: Langues
    
  - block: features
    content:
      title: Activités sportives
      subtitle: Mes activités sportives
      items:
        - name: 🧗🏻‍♂️ Escalade sportive 
          description: Falaise et grandes voies
        - name: 🏔️ Randonnée et trekking
          description: GR 20, GR70 et treks en autonomie 
      design:
        columns: '2'




---
