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
        This site gathers my CV, my courses and teaching material, my case studies, and my publications.

        <div style="display: flex; gap: 10px; margin-top: 10px;">
          <div style="flex: 1;">
            <ul style="list-style: none; padding: 0; margin: 0; font-size: 22px;">
              <li><a href="/teaching/">📚 See my teaching</a></li>
              <li><a href="/book/case-studies/">🛠️ See my case studies</a></li>
              <li><a href="/publication/">📄 See my publications</a></li>
              <li><a href="/experience/">📋 See my resume</a></li>
            </ul>
            <p style="margin: 14px 0 6px;">I also run and maintain the following two websites:</p>
            <ul style="list-style: none; padding: 0; margin: 0; font-size: 22px;">
              <li><a href="https://cragdiary.com" target="_blank" rel="noopener">🧗 Cragdiary: your multi-pitch climbing logbook</a></li>
              <li><a href="https://thefuturewithai.org" target="_blank" rel="noopener">🔮 The Future With AI: share your bets on the future</a></li>
            </ul>
            <a class="home-contact" href="mailto:contact@etiennechassaing.com">✉️ Get in touch: contact@etiennechassaing.com</a>
          </div>
        </div>

        <h3>They trusted me:</h3>
        <div class="trusted-companies">
          <a class="company-link" href="https://huggingface.co" title="Hugging Face" target="_blank" rel="noopener"><img src="/fr/assets/huggingface.png" alt="Hugging Face" class="company-logo-small"></a>
          <a class="company-link" href="/fr/projets/stryx-ai-drone-interception/" title="See the Stryx"><img src="/fr/assets/stryx.jpeg" alt="Stryx" class="company-logo-small"></a>
          <img src="/fr/assets/nehemis.png" alt="Nehemis" class="company-logo">
          <a class="company-link" href="/fr/projets/phospho/" title="See the Phospho"><img src="/fr/assets/phospho.svg" alt="Phospho" class="company-logo"></a>
          <a class="company-link" href="/fr/projets/dev_ia_drones/" title="See the Neodesystems"><img src="/fr/assets/neodesystems_logo.jpeg" alt="Neodesystems" class="company-logo"></a>
          <a class="company-link" href="/fr/projets/marl/" title="See the Geomatys"><img src="/fr/assets/geomatys.jpeg" alt="Geomatys" class="company-logo"></a>
          <img src="/fr/assets/logo-eurofins.jpg" alt="Eurofins" class="company-logo">
          <img src="/fr/assets/JCS.png" alt="JCS" class="company-logo">
          <a class="company-link" href="/fr/projets-recherche/insulated/" title="See the Schindler"><img src="/fr/assets/schindler.png" alt="Schindler" class="company-logo"></a>
          <a class="company-link" href="/fr/projets-recherche/airbus-rl/" title="See the Airbus Group"><img src="/fr/assets/airbus-group.png" alt="Airbus Group" class="company-logo"></a>
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
      count: 0
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
