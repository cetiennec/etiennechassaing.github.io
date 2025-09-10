
## 3. Control

### Control Objectives

### 1) Traditionnal control technique with tinkering

The standard equation of the PI controller is:

$$
u(t) = K_p \, e(t) + K_i \int_0^t e(\tau) \, d\tau,
$$

where:
- u(t) is the power of the heater,
- $K_p$ is the proportional gain,
- $K_i$ is the integral gain,
- e(t) is the error between the setpoint and the outlet temperature.


### 2) Optimal control via MPC


$$
u^*(k) = \min_{u(0), \dots, u(N_p-1)}
\sum_{i=0}^{N_p-1} \left( y_i - (r_i - d_i) \right)^T Q \left( y_i - (r_i - d_i) \right) + u_i^T R u_i + \Delta u_i^T S \Delta u_i,
$$
$$
\text{subject to:}
\begin{align*}
&\mathbf{x}(0) = \mathbf{x}_0, \\
&\mathbf{x}_{i+1} = A \mathbf{x}_i + B u_i, \quad i = 0, \dots, N_p-1, \\
&y_i = C \mathbf{x}_i, \quad i = 0, \dots, N_p-1, \\
&0 \leq \mathbf{x}_i \leq 95, \quad i = 1, \dots, N_p, \\
&0 \leq u_i \leq 33, \quad i = 0, \dots, N_p-1, \\
&\Delta u_i = u(i) - u(i-1), \quad i = 1, \dots, N_p-1, \\
&0 \leq \Delta{u}_i \leq \Delta{u}_{max}, \quad i = 0, \dots, N_p-1, \\
&Q \succ 0, \, R \succ 0.
\end{align*}
$$

where:
- $N_p$ is the prediction horizon.
- $r_i$ is the moving reference at time $i$.
- $d_i$ is the moving disturbance ($T_{ext}$) at time $i$.
- $Q \succ 0$ and $R \succ 0$ are weighting matrices for output tracking and input usage, respectively.


### 3) Reinforcement Learning

## Comparison and conclusion

### Performances

### Security

### Complexity


### Conclusion



# Appendix

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

