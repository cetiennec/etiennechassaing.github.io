---
title: Formations et enseignments
summary: My courses
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true

sections:
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

sections:
  - block: collection
    id: Enseingements
    content:
      title: Enseingements
      filters:
        folders:
          - enseignements
    design:
      view: article-grid
      columns: 2
---
