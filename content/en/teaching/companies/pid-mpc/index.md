---
title: PID and MPC control training
summary: Training software teams in the control of dynamic systems, from PID to the basics of MPC, delivered at Nehemis
date: 2025-02-01
type: docs
math: true
tags:
  - 'Control/PID/MPC'
image:
  caption: 'Principle of Model Predictive Control'
---

![Principle of MPC](featured.png)
*Principle of Model Predictive Control*

Training delivered in **February 2025 at [Nehemis](https://nehemis.com)** for its
**software teams**. The goal: give developers who are not control engineers what they need
to understand, tune and debug a control loop, then position Model Predictive Control
relative to a PID: when it brings something extra, and at what cost.

The program below is the one that was delivered; it can be adapted to your system and
the time available.

## Part 1: Understanding a Dynamic System

- Open-loop and closed-loop systems: what feedback changes.
- Modeling a simple process, transfer functions, poles and stability.
- Reading a step response: static gain, time constant, overshoot, settling time.
- Experimental identification of a process from real measurements.

## Part 2: The PID Controller in Practice

- The role of each term (proportional, integral, derivative) and what each one costs.
- Steady-state error, disturbance rejection, stability margin.
- Tuning methods: empirical approach, Ziegler-Nichols, model-based tuning.
- The implementation pitfalls that make a PID that is correct on paper fail in practice:
  integrator windup (*anti-windup*), actuator saturation, noise amplified by the
  derivative term and how to filter it.
- Discretization: sampling period, recursive form of the controller, effects of
  computation time and delays.

## Part 3: Introduction to Model Predictive Control

- Principle: optimize a sequence of control inputs over a receding horizon rather than
  reacting to the instantaneous error.
- Formulating the optimization problem: prediction model, cost function, prediction and
  control horizons.
- What MPC can do that PID cannot: **explicit constraints** on inputs and states,
  **multivariable** (MIMO) systems, anticipating a setpoint known in advance.
- The price to pay: a model is required, computational cost, sensitivity to modeling
  errors.
- Selection criteria: when a well-tuned PID is still the right answer.

## Part 4: Applications

- Hands-on work on a system representative of the participants' field.
- PID vs. MPC comparison on the same process: performance, constraint satisfaction,
  robustness.
- Discussion of internal use cases and possible next steps.

This training is offered in French or English, on site or remotely, and runs from one to
three days depending on how deep you want to go into MPC.
