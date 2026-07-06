# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic CV website (etiennechassaing.com) built with Hugo and the Hugo Blox Builder "Academic CV" theme. Deployed to GitHub Pages via `.github/workflows/publish.yaml` on every push to `main` (a `netlify.toml` also exists but GitHub Pages is the active deployment, per `CNAME`).

## Commands

Requires Hugo **extended** v0.126.3 (the version pinned in the workflow and netlify.toml) and Go (theme is pulled in as Hugo modules via `go.mod`).

```bash
hugo server            # local dev server with live reload
hugo --minify          # production build into public/
```

There are no tests or linters. `public/` and `resources/` are gitignored build output — never edit them.

## Architecture

- **Theme via Hugo modules** (`config/_default/module.yaml` / `go.mod`): `blox-tailwind`, `blox-plugin-netlify`, and a personal fork `github.com/cetiennec/hugo-blox-language_block` (custom language block). No vendored theme code; run `hugo mod` commands to update.
- **Bilingual site** (`config/_default/languages.yaml`): English content in `content/en/`, French in `content/fr/`. The two trees are not mirrors — French has extra sections (`formations/`, `enseignements/`, `projets/`, `projets-recherche/`) with their own names. Menus are per-language: `menus.yaml` (en) and `menus.fr.yaml`. `content/mock_posts/` sits outside both content dirs and is not published.
- **Homepage** (`content/{en,fr}/_index.md`): a `type: landing` page composed of Hugo Blox `sections:` blocks (resume-biography-3, markdown, collections, etc.). Most site-wide settings live in `config/_default/params.yaml`.
- **Publications pipeline**: `.github/workflows/import-publications.yml` runs when `publications.bib` changes; it converts BibTeX to Markdown with the `academic` CLI and opens a PR. Note it imports into `content/publication/` (repo root), while the live pages are under `content/en/publication/` and `content/fr/publication/` — imported entries need to be moved/translated into the language dirs.
- **Jupyter Book at `/book/`**: `static/book/` is a committed, prebuilt Jupyter Book (Sphinx HTML) of control-engineering case studies (drone_delayed_control, fishing_boat, heat_pipe_control). Its source is **not in this repo** — to update it, rebuild the book elsewhere and copy the HTML output into `static/book/` (see "Update Jupyter Book build" commits). Don't hand-edit these files.
- **Custom layout overrides** are minimal: only `layouts/partials/hooks/head-end/github-button.html`.
