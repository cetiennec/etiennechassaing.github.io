[//]: # (# Heated Pipe System with Heat Loss)

[//]: # ()
[//]: # (This tutorial describes the process of controlling the outlet temperature of a 300 meters heat pipe close to the )

[//]: # (boiling temperature.)

[//]: # ()
[//]: # (The main goal is to describe the process of solving rather than the details of the equations.)

[//]: # ()
[//]: # (---)

## 1. System Description

The system consists of a circular pipe through which water flows continuously. A heater is connected at the entrance ($x = 0$) 
of the pipe, providing a constant power input $P$ to the water. The water flows with constant velocity $u$, losing heat 
to the environment due to convection. At the outlet, the water returns to the heater, creating a closed loop.

![heat loop](simple_diagram.png)


### Schematic of the system:

![heat loop](heat_loop.png)


### Step response and first findings:

![heat loop](step_response.jpg)

From this we observe :
- Stair-like behavior due to the recirculation
- An inlet temperature that can go close to 100°C despite an outlet temperature that is barely above 85°C
- A significant delay (~12 min)
- A coupling and an intrication between inlet and outlet temperature

**How to model and simulate these stairs?**


## Physical model equations:


The evolution of the temperature in the pipe is governed by the following partial differential equation (PDE):

$$
\frac{\partial T}{\partial t} + u \frac{\partial T}{\partial x} = -\frac{h P_{\text{pipe}}}{\rho S c_p} \left[ T(x, t) - T_{\text{ext}} \right]
$$

All notations are detailed in Appendix.

Using $ \Theta_{\text{inlet}}(t) = T_{\text{inlet}} - T_{\text{ext}} $ and $\Theta_{\text{outlet}}(t) = T_{\text{outlet}} - T_{\text{ext}}$

We can write delayed equations in which $\tau$ is the time of travel and $P$ the power f the heater:

$$
\Theta_{\text{inlet}}(t) = \frac{P}{\dot{m}c_p} + K \Theta_{\text{inlet}}(t - \tau),
\Theta_{\text{outlet}}(t) = K \left( \frac{P}{D c_p} +  \Theta_{\text{outlet}}(t - \tau) \right).
$$

### Naive model

The PDE equation can be naively discretized as follows:
- The pipe is divided in N discrete segments
- For each segment, its temperature is obtained by averaging its temperature with the neighbors and with the surrounding 
environment,subject to the heat loss coefficient.
- Each temperature value is transferred to the next segment

![heat loop](pipe_simulation.gif)

This simulation divides a pipe into small segments to model heat transfer step by step. At each time step, every segment’s 
temperature is updated based on its neighbors and the environment, while the temperature at the pipe’s end is "pushed forward" 
to the start—like a wave of heat moving through. The heater at one end injects warmth, and the animation reveals how heat spreads, 
stabilizes, and flows through the system. 

![heat loop](param_comparison.png)

## 2. System Simulation
