# Li-ion Battery Digital Twin

A high-performance, modular Python framework for simulating Lithium-ion battery dynamics. Designed for seamless integration into `gymnasium` Reinforcement Learning (RL) environments, this Digital Twin decouples data management from mathematical execution to optimize step-time performance.

---

## Architecture Overview

The Digital Twin models non-linear battery dynamics across varying operating conditions:

1. **Capacity Model (`capacity_model.py`)**: Computes temperature- and C-rate-dependent available capacity via 1D linear polynomial interpolation.
2. **Voltage Model (`voltage_model.py`)**: Evaluates 2-RC Equivalent Circuit Model (ECM) parameters ($R_0, R_1, C_1, R_2, C_2, OCV$) using fast 2D regular grid interpolation over State of Charge (SOC) and Temperature.
3. **Data Loader (`data_loader.py`)**: Fetches lookup tables from a database upon environment initialization, caching data in-memory via Pandas DataFrames to eliminate disk I/O overhead during simulation loops.


**Digital Twin Structure:** 
```text
Battery_Digital_Twin/
├── Digital_twin/               # Core physical simulation models
│   ├── __init__.py             # Package initializer
│   ├── capacity_model.py      # 1D capacity estimation (Temp & C-rate)
│   ├── data_loader.py         # SQL database queries via .env credentials
│   ├── impedance_model.py     # 2D impedance parameter interpolation
│   ├── twin.py                # Core Digital Twin state manager
│   └── voltage_model.py       # 2D terminal voltage & 2-RC ECM math
│
├── envs/                       # Gymnasium RL environments
│   ├── __init__.py             # Gym environment registration
│   └── battery_env.py         # RL environment (step, reset, rewards)
│
├── tests/                      # Unit tests and validation scripts
├── main.py                     # Entry point for execution/testing
├── README.md                   # Module documentation
└── requirements.txt            # Python dependencies