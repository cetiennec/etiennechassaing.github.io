
## 3. Control

### Control Objectives

### 1) Traditionnal SISO control technique, with tinkering

The standard equation of the PI controller is:

$$
u(t) = K_p \, e(t) + K_i \int_0^t e(\tau) \, d\tau,
$$

where:
- u(t) is the power of the heater,
- $K_p$ is the proportional gain,
- $K_i$ is the integral gain,
- e(t) is the error between the setpoint and the outlet temperature.


This is a Single Input - Single Output (SISO) controller
First simulation show the result with a P controller only. 
It exhibits the need to continuously add energy to the system to compensate for the losses, hence a nonzero $K_i$.





