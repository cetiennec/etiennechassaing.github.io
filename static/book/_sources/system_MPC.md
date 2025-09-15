
### 2) Optimal control via MPC, SIMO control fashion

Since we have access to a model, we can explore optimal control via Model Predictive Control (MPC). 
MPC leverages the model to find the best input to the system based on a horizon prediction ($N_p$).
It strength is to be able to consider both states for a single input to the system.
To do so, MPC uses weights to formulate the control objective and respect constraints in the optimization process.
MPC formulation of the problem is as follows:

$$
u^*(k) = \min_{u(0), \dots, u(N_p-1)}
\sum_{i=0}^{N_p-1} \left( y_i - (T_{set,i} - d_i) \right)^T Q \left( y_i - (T_{set,i} - d_i) \right) + u_i^T R u_i + \Delta u_i^T S \Delta u_i,
$$
$$
\text{subject to:}
\begin{align*}
&\mathbf{x}(0) = \mathbf{x}_0\\
&\mathbf{x}_{i+1} = A \mathbf{x}_i + B u_i,~y_i = C \mathbf{x}_i \quad i = 0, \dots, N_p-1, \\
&0 \leq x_i=T_{inlet,i},T_{outlet,i} \leq 95, \quad i = 1, \dots, N_p, \\
&0 \leq u_i=P_i \leq 33, \quad i = 0, \dots, N_p-1, \\
&Q \succ 0, \, R \succ 0.
\end{align*}
$$

[//]: # (&\Delta u_i = u&#40;i&#41; - u&#40;i-1&#41;, \quad i = 1, \dots, N_p-1, \\)

where:
- $x = (T_{inlet},T_{outlet} )$ is the state
- $N_p$ is the prediction horizon.
- $T_{set,i}$ is the moving reference at time $i$.
- $d_i$ is the moving disturbance ($T_{ext}$) at time $i$.
- $Q \succ 0$ and $R \succ 0$ are weighting matrices for output tracking and input usage, respectively.

**Is MPC tractable on this problem?** Think about the problem size ...

This approach can be solved using Quadratic Programming (QP) formulation. 
However, to employ this technique, difficulty lies in the fact that :
1) The model is high order, $x$ is (1,30) for a  30 segment pipe discretization.
2) Horizon to control $T_{outlet}$ should be 600, which implies dealing with huge matrices.

For each issue :
- 1 $N$ is set to 20 to lighten the simulation, and could be tackled by using simplified models for $T_{inlet}$ and $T_{outlet}$ respectively
- 2 is tackled by setting the controller frequency to 0.1Hz, meaning one step is 10s
