
## 1. System Description

The system consists of a 300m circular pipe through which water flows continuously. A heater is connected at the entrance ($x = 0$) 
of the pipe, providing a constant power input $P$ to the water. The water flows with constant velocity $u$, losing heat 
to the environment due to convection. At the outlet, the water returns to the heater, creating a closed loop.

![heat loop](images/simple_diagram.png)

The goal is to perform a bacteria decontamination of the loop, requiring a temperature of at least 85°C through the loop
with a 2°C/min ascent and without creating steam in the pipe.

***How to ensure $T_{outlet}$>85°C and $T_{inlet}$<95°C ? Can we control the heating speed precisely to 2°C/min?***

### First findings, why is it tricky?

Following plot shows what happens when the system is heated at a constant 30kW power which is barely the maximum power :

![heat loop](images/step_response.jpg)

From this we observe :
- Stair-like behavior due to the recirculation of water
- An inlet temperature that can go close to 100°C despite an outlet temperature that is barely above 85°C
- A significant delay (~12 min)
- A coupling and an intrication between inlet and outlet temperature

**How to model and simulate these stairs?**

### Naive model

[//]: # (The PDE equation can be naively discretized as follows:)

[//]: # (- The pipe is divided in N discrete segments)

[//]: # (- For each segment, its temperature is obtained by averaging its temperature with the neighbors and with the surrounding )

[//]: # (environment,subject to the heat loss coefficient.)

[//]: # (- Each temperature value is transferred to the next segment)

Following simulation divides the pipe into small segments to model heat transfer step by step. At each time step, every segment’s 
temperature is updated based on its neighbors and the environment (using a heat loss coefficient), while the temperature at the pipe’s end is "pushed forward" 
to the start—like a wave of heat moving through. The heater at one end injects warmth, and the animation reveals how heat spreads, 
stabilizes, and flows through the system.

![heat loop](images/pipe_simulation.gif)

This gives a first approximation and intuition on the system to explain the stairs and the impact of losses on the heating curve.

Detailed plots in Appendix show the impact of heat loss coefficient and external temperature on the curves.

## Physical model equations:

The system schematic is shown below:

![heat loop](images/heat_loop.png)

The evolution of the temperature in the pipe is governed by the following partial differential equation (PDE) obtained by 
writing the energy balance equation of a pipe infinitesimal segment:

$$
\frac{\partial T}{\partial t} + u \frac{\partial T}{\partial x} = -\frac{h P_{\text{pipe}}}{\rho S c_p} \left[ T(x, t) - T_{\text{ext}} \right]
$$

All notations are detailed in Appendix.

To include the heater power in the equations, we can write the energy balance of the heater using 
$ \Theta_{\text{inlet}}(t) = T_{\text{inlet}} - T_{\text{ext}} $ and $\Theta_{\text{outlet}}(t) = T_{\text{outlet}} - T_{\text{ext}}$.
This allows to write the following Delayed Equations in which $\tau$ is the time of travel, $P$ the power of the heater, and $K<1$ the loss coefficient:

$$
\Theta_{\text{inlet}}(t) = \frac{P}{\dot{m}c_p} + K \Theta_{\text{inlet}}(t - \tau),
\Theta_{\text{outlet}}(t) = K \left( \frac{P}{\dot{m} c_p} +  \Theta_{\text{outlet}}(t - \tau) \right).
$$

What these equations say :
- A pipe segment always sees the water from one turn past, which temperature is modulated by the losses
- From an energy point of view, the system adds to the loop the amount of energy contained by the water inside the heater 
- Effect of the power is inversely scaled by the flow $\dot{m}$ which directly affects system properties

