# Heated Pipe System with Heat Loss

This tutorial presents the modeling and simulation of a heated pipe system with heat loss to the surroundings.  
We will derive the main equations, present a simplified simulation, and finally introduce ARX model identification.

---

## 1. System Description

We consider a system consisting of a circular pipe through which water flows continuously.  
A heater is connected at the entrance ($x = 0$) of the pipe, providing a constant power input $P$ to the water.  
The water flows with constant velocity $u$, losing heat to the environment due to convection.  
At the outlet, the water returns to the heater, creating a closed loop.

**Schematic of the system:**

![heat loop](heat_loop.png)


**Step response:**



**Physical model equations**


The evolution of the temperature in the pipe is governed by the following partial differential equation (PDE):
$$
    \frac{\partial T}{\partial t} + u \frac{\partial T}{\partial x} = -\frac{h P_{\text{pipe}}}{\rho S c_p} \left[ T(x, t) - T_{\text{ext}} \right]
    \label{eq:complete_equation}
$$
Where 

$ \Theta_{\text{inlet}}(t) = T_{\text{inlet}} - T_{\text{ext}} $ and $\Theta_{\text{outlet}}(t) = T_{\text{outlet}} - T_{\text{ext}}$

$$
\Theta_{\text{inlet}}(t) = \frac{P}{\dot{m}c_p} + K \Theta_{\text{inlet}}(t - \tau),
\label{eq:theta-eq}
$$

# Appendix

- $ x $: Position along the pipe $\si{\meter}$.
- $ t $: Time $[ \si{\second} ]$.
- $ T(x, t) $: Temperature of water at position $ x $ and time $ t $ $[ \si{\kelvin} ]$.
- $ u $: Fluid velocity $[ \si{\meter\per\second} ]$.
- $ \rho $: Density of water $[ \si{\kilogram\per\meter\cubed} ]$.
- $ c_p $: Specific heat capacity of water $[ \si{\joule\per\kilogram\kelvin} ]$.
- $ S $: Cross-sectional area of the pipe $[ \si{\meter\squared} ]$.
- $ P_{\text{pipe}} $: Perimeter of the pipe $[ \si{\meter} ]$.
- $ h $: Convective heat transfer coefficient $[ \si{\watt\per\meter\squared\kelvin} ]$.
- $ P $: Heater power input $[ \si{\watt} ]$.
- $K = e^{-\frac{\alpha \tau}{2}}$, a factor representing the effect of time delay and thermal losses,
- $\tau$ is the delay time,