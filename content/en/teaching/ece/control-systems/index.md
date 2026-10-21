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

### Course material

- Session 5: continuous and discrete systems, Laplace and $\mathcal{Z}$ transforms.
- Session 5 bis: partial fractions, decomposition of rational fractions in the general case.
- Session 6: sampled systems, sampling, zero-order hold, digital control.
- Session 7: the digital PID controller, from the model to the real implementation.
- Session 8: filtering and the Kalman filter, from a noisy signal to optimal state estimation.
- Session 9: applications and revision, data-based approaches, inverted-pendulum case study.

Slides of sessions 5 to 9 and the final exam paper:

{{< teaching-reader course="ece/sbe" title="Sampled Control Systems: course material" >}}

### Midterm quiz

A one-page, 20-minute quiz on sampled systems and filtering. Every student gets an
**individualised paper**: papers are generated with
[auto-multiple-choice](https://www.auto-multiple-choice.net/) with a different random
draw per group, then marked by optical recognition.

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
Solutions are not published. The exam paper is the last item of the
[course material](#course-material) above.
