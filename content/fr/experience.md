---
title: 'Experience'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: skills
    content:
      title: Compétences
      id: 1
      username: admin_fr
    design:
      columns: '1'
  - block: skills
    content:
      title: Activités sportives
      username: admin_fr
    design:
      columns: '1'
  - block: markdown
    id: section-1
    content:
      title: Langues
      
  - block: 'github.cetiennec.language-block'
    content:
      title: My title
      text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
    
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
  - block: resume-languages
    content:
      title: Langues
      text: ''
      # Choose a user to display skills from (a folder name within `content/authors/`)
      username: admin_fr
    design:
      columns: '1'
      show_percentage: false


---
