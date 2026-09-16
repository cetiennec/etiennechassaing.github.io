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
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/personnel/cv/diffusion/CV_etienne_chassaing_juillet_2026.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: test.jpeg
          filters:
            brightness: 0.4
          size: cover
          position: center
          parallax: false
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        This site gathers my CV, my classes and teaching material, my case studies, and my publications.

        <div style="display: flex; gap: 10px; margin-top: 10px;">
          <div style="flex: 1;">
            <ul style="list-style: none; padding: 0; margin: 0; font-size: 22px;">
              <li><a href="/book/classes/">📚 See my classes</a></li>
              <li><a href="/book/case-studies/">🛠️ See my case studies</a></li>
              <li><a href="/publication/">📄 See my publications</a></li>
              <li><a href="https://cragdiary.com" target="_blank" rel="noopener">🧗 CragDiary: your multi-pitch climbing logbook</a></li>
              <li><a href="https://thefuturewithai.org" target="_blank" rel="noopener">🔮 The Future With AI: share your bets on the future</a></li>
            </ul>
          </div>
        </div>
    design:
      columns: '1'
  # - block: collection
  #   id: papers
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     view: article-grid
  #     columns: 2
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

---
