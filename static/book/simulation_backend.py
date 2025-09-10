import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# System Parameters
params = {
    "c_p": 4186,  # Specific heat capacity of water (J/kg·K)
    "h": 2.7,  # Convective heat transfer coefficient (W/m²·K)
    "D": 22.2e-3,  # Pipe diameter (m)
    "rho": 1000,  # Density of water (kg/m³)
    "L": 450,  # Length of pipe (m)
    "u": 0.8,  # Fluid velocity (m/s)
    "N": 20,  # Number of pipe segments
}

params["A"] = np.pi * (params["D"] / 2) ** 2  # Cross-sectional area of pipe (m²)
params["m_dot"] = params["rho"] * params["u"] * params["A"]  # Water flow (kg/s)
params["Delta_x"] = params["L"] / params["N"]  # Length of each segment (m)
params["alpha"] = (params["h"] * np.pi * params["D"]) / (
    params["rho"] * params["A"] * params["c_p"]
)  # Heat loss coefficient (1/s)

# Fixed simulation parameters
T_ext = 20  # Constant ambient temperature (°C)
Tinlet = 25  # Inlet temperature (°C)
Toutlet = 25  # Outlet temperature (°C)
simulation_time = np.linspace(0, 3600, 1000)  # 1 hour simulation, 1000 points


# Initial condition: linear temperature profile along the pipe
def get_Tinit(Tinlet, Toutlet, params):
    return Tinlet + (Toutlet - Tinlet) * np.cumsum(np.ones(params["N"])) / params["N"]


# ODE function for the pipe-heater system
def pipe_heater_odes(x, t, params, P, T_ext):
    dxdt = np.zeros(params["N"])
    # if x[1]>=95 :
    #     overshoot = True
    # elif overshoot:
    #     P=0.0
    T0 = x[-1] + P / (
        params["m_dot"] * params["c_p"]
    )  # Temperature at the start of the pipe

    # ODE for the first segment
    dxdt[0] = -(params["u"] / params["Delta_x"]) * (x[0] - T0) - params["alpha"] * (
        x[0] - T_ext
    )

    # ODEs for segments 2 to N
    for i in range(1, params["N"]):
        dxdt[i] = -(params["u"] / params["Delta_x"]) * (x[i] - x[i - 1]) - params[
            "alpha"
        ] * (x[i] - T_ext)

    return dxdt


# Simulation and plotting function
def simulate_and_plot(P):
    P = P * 1e3
    overshoot = False

    Tinit = get_Tinit(Tinlet, Toutlet, params)
    T = odeint(pipe_heater_odes, Tinit, simulation_time, args=(params, P, T_ext))
    T1 = T[:, 0]  # Temperature at the first segment (inlet)
    T_end = T[:, -1]  # Temperature at the last segment (outlet)

    plt.figure(figsize=(10, 6))
    plt.plot(simulation_time / 3600, T1, label="Simulated Inlet Temperature (°C)")
    plt.plot(simulation_time / 3600, T_end, label="Simulated Outlet Temperature (°C)")
    plt.xlabel("Time (hours)")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Pipe-Heater System Simulation (P = {P/1e3:.1f} kW)")
    plt.legend()
    plt.grid(True)
    plt.ylim(15, 100)  # Adjust as needed
    plt.show()
