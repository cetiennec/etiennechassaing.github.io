---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin_fr
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: markdown
    content:
      title: 'Mon approche'
      subtitle: ''
      text: |-
        <div style="font-size: smaller;">
          En partant de votre problème métier, je vous accompagne dans votre projet d'explorer l'utilisation de l'IA, en particulier dans le domaine de l'ingéniérie. J'apporte une attention particulière à vous aider à formuler le problème de façon scientifique et générique.

          ![Image alt](ma_vision.svg)
          
          Voici un exemple type :

          - Un client identifie le besoin de détecter des pannes sur son parc machine
          - Le client peut avoir une idée de technologie pour mener ce projet
          - Nous formulons ensemble le problème comme un problème de détection d'anomalies, courant en Machine-Learning
          - Une fois le problème formulé, travaillons ensemble pour éclaircir ce domaine et la ou les technologies envisagés
          - J'établi une feuille de route pour identifier les technologies les moins risquées, par exemple une famille d'algorithme 
          - Je vous propose un plan pour réaliser une preuve de concept de la solution et former vos équipes sur cette technologie

          Vous pouvez retrouver des exemples de missions rélisées dans l'onglet "Conseil et Projets".

          Certifications:
          - Consultant agréé Crédit Impôt Innovation depuis le 3 octobre 2024
        </div>
    design:
      columns: 2


  - block: cta-card
    demo: false # Only display this section in the Hugo Blox Builder demo site
    content:
      title: 👉 Discutons de votre projet
      text: |- 
        Cliquez sur le lien ci-dessous pour réserver un créneau de 30 min et discuter de votre projet.

      button:
        text: Prendre rendez-vous
        url: https://calendly.com/etienne-chassaing-conseil/30min
    design:
      card:
        # Card background color (CSS class)
        css_class: "bg-primary-700"
        css_style: ""

  - block: collection
    id: papers
    content:
      title: Projets récents
      sort_by: 'Date'
      # Choose how many pages you would like to display (0 = all pages)
      count: 9 
      filters:
        folders:
          - project
          - publication
          - formations
        featured_only: false
    design:
      view: article-grid
      columns: 3
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     view: article-grid
  #     columns: 1
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: date-title-summary
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  - block: collection
    content:
      title: Publications
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation

---
