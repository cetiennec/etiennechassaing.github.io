---
title: 'CV'
date: 2023-10-24
type: landing

design:
  spacing: '3rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  # Name, role, links and PDF download (layouts/partials/blox/cv-header.html)
  - block: cv-header
    content:
      username: admin_fr
      pdf: https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/personnel/cv/diffusion/CV_etienne_chassaing_juillet_2026.pdf

  - block: resume-experience
    content:
      username: admin_fr
    design:
      # Hugo date format
      date_format: 'Jan 2006'
      # Education or Experience section first?
      is_education_first: false
  - block: resume-awards
    content:
      title: Récompenses
      username: admin_fr

  - block: resume-skills
    content:
      title: Compétences et loisirs
      id: 1
      username: admin_fr
    design:
      columns: '1'
---
