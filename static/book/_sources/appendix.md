## Comparison and conclusion

### Performances

### Security

### Complexity


### Conclusion




# Appendix

### Parameters

- $x$: Position along the pipe in **meters (m)**.
- $t$: Time in **seconds (s)**.
- $T(x, t)$: Temperature of water at position $x$ and time $t$ in **kelvin (K)**.
- $u$: Fluid velocity in **meters per second (m/s)**.
- $\rho$: Density of water in **kilograms per cubic meter (kg/m³)**.
- $c_p$: Specific heat capacity of water in **joules per kilogram-kelvin (J/(kg·K))**.
- $S$: Cross-sectional area of the pipe in **square meters (m²)**.
- $P_{\text{pipe}}$: Perimeter of the pipe in **meters (m)**.
- $h$: Convective heat transfer coefficient in **watts per square meter-kelvin (W/(m²·K))**.
- $P$: Heater power input in **watts (W)**.
- $K = e^{-\frac{\alpha \tau}{2}}$: A factor representing the effect of time delay and thermal losses (dimensionless).
- $\tau$: Delay time in **seconds (s)**.
- $\alpha$: Heat loss coefficient in **per second (1/s)**.

## Simulation details : Impact of coefficients:

Following plots the impact of heat loss coefficient and external temperature on the curves.

![heat loop](images/param_comparison.png)

## PID details : Bode plots

## MPC details : System precision

MPC uses a simplified version of the model with 20 pipe segments and a 10s integration steps, this creates discrepancies 
in its prediction, the magnitude of the impact is show below on a 30kW input :

![heat loop](images/MPC_vs_full_model.png)

## RL details : 
