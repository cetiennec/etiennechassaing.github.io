---
title: Formations
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
      count: 0
      filters:
        folders:
          - enseignements
    design:
      view: article-grid
      columns: 3

  - block: collection
    id: Formations
    content:
      title: Formations
      count: 0
      filters:
        folders:
          - formations
    design:
      view: article-grid
      columns: 3
---
