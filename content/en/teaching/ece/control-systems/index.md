---
title: Sampled Control Systems
summary: "Digital control: six lecture decks, the midterm quiz and the final exam."
type: docs
sidebar:
  sections: true
weight: 1
math: true
---

A digital-control course taught to the full year group (500 students) from April to
June 2026: $z$-transform, discretisation, sampled PID, filtering and Kalman estimation.

**I taught the second half of the course** (sessions 5 to 9, digital control proper)
along with its assessments. The first half, on continuous-time systems, was taught by
another lecturer.

The documents below are the ones actually handed out to students. The course is taught
in French, so the material is in French.

### Lecture slides

| # | Session | Topic | Pages |
| - | ------- | ----- | ----- |
| 5 | [Continuous and discrete systems](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/05-transformee-z/diffusion/05-transformee-z.pdf) | Laplace and $\mathcal{Z}$ transforms | 32 |
| 5 bis | [Partial fractions](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/05-bis-elements-simples/diffusion/05-bis-elements-simples.pdf) | Decomposition of rational fractions, general case | 10 |
| 6 | [Sampled systems](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/06-systemes-echantillonnes/diffusion/06-systemes-echantillonnes.pdf) | Sampling, zero-order hold, digital control | 38 |
| 7 | [Digital PID controller](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/07-pid-echantillonnes/diffusion/07-pid-echantillonnes.pdf) | From the model to the real implementation | 39 |
| 8 | [Filtering and the Kalman filter](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/08-filtrage-kalman/diffusion/08-filtrage-kalman.pdf) | From a noisy signal to optimal state estimation | 26 |
| 9 | [Applications and revision](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/cours/09-applications-revisions/diffusion/09-applications-revisions-etudiant.pdf) | Data-based approaches, inverted-pendulum case study *(student version)* | 19 |

### Midterm quiz

A one-page, 20-minute quiz on sampled systems and filtering. Every student gets an
**individualised paper**: papers are generated with
[auto-multiple-choice](https://www.auto-multiple-choice.net/) with a different random
draw per group, then marked by optical recognition.

- [Sample paper (PDF)](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/qcm-final/diffusion/qcm_midterm_exemple.pdf)

### Final exam

Rather than a set of disconnected questions, the exam is a **single running case study**:
all four parts work on the same system, the altitude control of an agricultural
observation drone, and each part picks up where the previous one left off. The paper is in
French, as the course is taught in French.

- **Warm-up:** five multiple-choice questions, an inverse Laplace transform, and the
  discretisation of a first-order plant behind a zero-order hold
- **Part 1, modelling:** from Newton's second law to the drone's transfer functions, with
  the motor identified from a measured step response
- **Part 2, closed-loop control:** steady-state error under gravity, integral action,
  and the risk of derivative action in gusty wind
- **Part 3, discretisation and implementation:** the controller on an ESP32, recurrence
  equations for P, I and D, and a Python implementation to complete
- **Part 4, filtering:** anti-aliasing, and fusing a 10 Hz GPS with a 100 Hz accelerometer

Duration: **1h30**, calculator and documents not allowed. 20 points, plus 2 bonus points.
Solutions are not published.

<div style="position:relative;padding-top:129%;margin:1.5rem 0;border:1px solid #d4d4d8;border-radius:6px;overflow:hidden;">
  <iframe
    src="https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    title="Final exam: Sampled Control Systems (PDF)"></iframe>
</div>

Other documents: [answer sheet (PDF)](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final_feuille_reponse.pdf) · [exam paper, full screen](https://cdn.jsdelivr.net/gh/cetiennec/cours-pdf@main/ece/systemes-boucles/evaluations/2025-2026/examen-final/diffusion/examen_final.pdf)
