---
title: Formations et enseignements
summary: Mes expériences d'enseignements
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true

sections:
  - block: collection
    id: Enseignements
    content:
      title: Enseignements
      filters:
        folders:
          - enseignements
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: Formations
    content:
      title: Formations
      filters:
        folders:
          - formations
    design:
      view: article-grid
      columns: 2
---
