---
title: "Final exam — Altitude control of a drone"
summary: "A running case study: modelling, closed-loop control, discretisation and filtering of an observation drone. Final exam of the Sampled Control Systems course (ECE Paris, 2025-2026)."
date: 2026-06-11
math: true
toc: false
tags:
  - 'Control/Systèmes Bouclés'
  - PID
  - Kalman
  - ECE Paris
image:
  caption: "Agricultural observation drone"
---

## Context

This is the final exam of the **Sampled Control Systems** course I taught at ECE Paris
to the full year group (500 students) from April to June 2026. Rather than a set of
disconnected questions, it is built as a **single running case study**: all four parts
work on the same system — the altitude control of an agricultural observation drone —
and each part picks up where the previous one left off.

Duration: **1h30** — calculator and documents not allowed. 20 points, plus 2 bonus points.

![Agricultural observation drone](drone_obs.jpg)
*The system under study: an observation drone holding a constant altitude over a field*

## What the paper covers

**Warm-up — quiz and two exercises.** Five multiple-choice questions on PID gain effects,
the mapping between the Laplace plane and the $z$-plane, first-order dynamics and discrete
stability; then an inverse Laplace transform by partial fractions, and the discretisation
of a first-order plant behind a zero-order hold.

**Part 1 — Modelling.** From Newton's second law on the vertical axis to the transfer
functions of the drone: four brushless motors, fluid friction, and gravity treated as a
constant disturbance. The motor itself is identified graphically from a measured step
response ($K_m$, $\tau$), then the open-loop transfer function is factorised and its poles
and zeros placed in the Laplace plane.

**Part 2 — Closed-loop control.** Black's formula on the closed loop, then the final-value
theorem applied by superposition to both the setpoint and the gravity disturbance — which
exposes the steady-state error a proportional controller cannot remove. The part closes on
integral action, a feedforward alternative (bonus), and the risk derivative action creates
when the drone flies in gusty wind.

**Part 3 — Discretisation and implementation.** The controller moves onto an ESP32 behind
a zero-order hold: backward-Euler substitution, the recurrence equations for the P, I and D
terms, the low-pass filter the derivative branch needs in practice, a Python implementation
to complete, and a comparison of continuous versus sampled step responses.

**Part 4 — Filtering.** Anti-aliasing ahead of the accelerometer's ADC, then sensor fusion:
which filter merges a 10 Hz GPS with a 100 Hz accelerometer, at what rate it runs, and how
the two sensors' standard deviations drive the trade-off between short-term dynamics and
long-term drift.

## The paper

The exam is written in French, as the course is taught in French. A **full transcription
with all figures and formulas** is available on the French side of this site:

📄 **[Read the full transcription (French)](/fr/classes/ece/examen-final/)**

Solutions are not published.

<div style="position:relative;padding-top:129%;margin:1.5rem 0;border:1px solid #d4d4d8;border-radius:6px;overflow:hidden;">
  <iframe
    src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    title="Final exam — Sampled Control Systems (PDF)"></iframe>
</div>

**Related documents:**
[exam paper](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf) ·
[answer sheet](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final_feuille_reponse.pdf) ·
[all course material](../)
