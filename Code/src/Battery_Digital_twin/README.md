# Li-ion Battery Digital Twin

A high-performance, modular Python framework for simulating Lithium-ion battery dynamics. Designed for seamless integration into `gymnasium` Reinforcement Learning (RL) environments, this Digital Twin decouples data management from mathematical execution to optimize step-time performance.

---

## Architecture Overview
The Digital Twin models non-linear battery dynamics across varying operating conditions by integrating physical sub-models with Reinforcement Learning execution into a unified framework:
1. **Data Loader** (data_loader.py): Fetches dynamic parameter lookup tables and baseline specifications from a database upon environment initialization, caching data in-memory via Pandas DataFrames and NumPy arrays to eliminate disk or network I/O overhead during simulation loops.
2. **Capacity Model** (capacity_model.py): Computes temperature- and C-rate-dependent available capacity via 1D linear polynomial interpolation. 
3. **Voltage Model** (voltage_model.py): Evaluates 2-RC Equivalent Circuit Model (ECM) parameters ($R_0, R_1, C_1, R_2, C_2, OCV$) using fast 2D regular grid interpolation over State of Charge (SOC) and Temperature.Digital 
4. **Twin Core** (twin.py): Serves as the central physical state engine, unifying the Capacity and Voltage models to calculate realtime battery responses under dynamic current loads.
5. **Gymnasium Environment** (battery_env.py): Encapsulates the DigitalTwin inside a standard Gymnasium interface, mapping Discrete(3) actions to current inputs ($-50\text{A}, 0\text{A}, +50\text{A}$), monitoring safety limits, and passing state observations ($SOC, V_{terminal}, Temp$) and rewards to the agent.
6. **RL Execution** (train.py / deploy_twin.py): Handles model optimization using Stable-Baselines3 DQN during training, and executes real-time inference on the active Digital Twin setup during deployment.


## Digital Twin Structure:
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
|   |── __init__,py 
|   └── test_env.py             # Script to test the gymnasium environment
├── main.py                     # Entry point for execution/testing
├── README.md                   # Module documentation
└── requirements.txt            # Python dependencies
```
## The Architecture
```

+-----------------------------------------------------------+
|                     Database / DB                         |
+-----------------------------------------------------------+
                              |
                              | (On init: loads tables)
                              v
+-----------------------------------------------------------+
|                      data_loader.py                       |
+-----------------------------------------------------------+
                              |
                              | (provides parameters)
                              v
+-----------------------------------------------------------+
|                         twin.py                           |
|      (combines capacity_model.py & voltage_model.py)      |
+-----------------------------------------------------------+
                              |
                              | (calculates SOC, Volt, Temp)
                              v
+-----------------------------------------------------------+
|                      battery_env.py                       |
|  (Gymnasium wrapper: maps actions & calculates rewards)   |
+-----------------------------------------------------------+
                              |
               +--------------+--------------+
               |                             |
               v                             v
+-----------------------------+-------+---------------------+
|          train.py           |       |     evaluate.py     |
|        (trains DQN)         |       |    (tests agent)    |
+--------------+--------------+-------+----------+----------+
               |                                 |
               | (saves model)                   | (loads model)
               v                                 |
+-------------------------------------+          |
|        dqn_battery_model.zip        |<---------+
+----------------------+--------------+
                       |
                       | (loads model)
                       v
+-----------------------------------------------------------+
|                      deploy_twin.py                       |
|              (Live control & Digital Twin)                |
+-----------------------------------------------------------+