# Battery AI

Machine learning extension for the **Project C battery test system**.
The system charges a battery from a solar panel; the ML part decides **when and how much** to charge/discharge.

**Goal:** optimize charge/discharge and keep improving **while deployed** —
online/streaming learning only, no stop-and-retrain cycles, the system never stops running.

## Hard constraints

- Main code is written in **Python**.
- Every dependency that we do not build ourselves must be **open source and free** (no commercial licenses).
- Runs on a **Raspberry Pi 4B** (4 or 8 GB); the server runs on a separate Pi.

## Three layers (bottom up)

1. **Safety — fixed, never learned.**
   Pure function `apply_limits(measured_voltage, requested_current, config) -> allowed_current`.
   - Limits live in a **per-chemistry config**, not in the logic.
   - Cutoff slightly **below 4.2 V**, resume with **hysteresis**.
   - Missing, stale, NaN, or implausible voltage → **stop charging**.
   - The same clamp runs in the twin and on the hardware; triggering it costs a reward penalty in RL.
   - A hardware protection backstop exists because the Pi can hang.
2. **Learning — online models** (River / recursive least squares): solar forecast, SoC drift, battery response.
3. **Decision** — starts as a simple rule-based baseline, replaced by **RL (SAC/PPO)** once it beats the baseline.

New model versions run in **shadow mode** first: they log their decisions while the baseline stays in control, and only take over when they demonstrably beat the baseline.

## Hardware & existing system

- Sensors: current/voltage meter on the solar panel, weather station (humidity, rain, light, temperature).
- Existing codebase (`batterij_test_systeem`): FastAPI backend, Angular frontend, **InfluxDB OSS** for sensor time series, **PostgreSQL** for users/devices.

## Batteries

- **Now:** lithium-ion — 4.2 V max, 2.85 V empty (capacity to be confirmed), charged from solar.
- **Later:** redox flow battery — gets its own twin and its own config, retrained model, but plugs into the **same `Battery` interface** (`read() -> Measurement`, `apply(current)`).

Tests run on a **digital twin first**, then deploy to the real system.

## Build plan (each step has a "done when")

| # | Step | Done when |
|---|------|-----------|
| 1 | Config + `apply_limits` + tests | limit, just below, and NaN cases behave correctly |
| 2 | InfluxDB loader → resampled DataFrame (1 min) | a full day of solar/weather data plots |
| 3 | Li-ion twin: coulomb counting + equivalent circuit (R0/R1/C1, OCV curve fitted from logs) | predicted voltage matches held-out data |
| 4 | Gymnasium env wrapping the twin, replays logged solar/weather, all actions through `apply_limits`, twin params randomized | agent can train on the twin |
| 5 | Baseline controller (e.g. charge when solar high and SoC below threshold) | its score is recorded |
| 6 | Online solar forecast with River, prequential evaluation | beats "same as 15 min ago" |
| 7 | RL agent trained in the twin | beats the baseline across randomized twin parameters |
| 8 | Runtime loop on the Pi: read → sanity check → model → `apply_limits` → apply → log | runs in shadow mode |
| 9 | Flow battery: new twin + config, same interface, retrained | steps 3–8 repeated for the flow battery |

## Tech stack

Python · FastAPI · InfluxDB OSS (MIT) · PyYAML · NumPy/SciPy/pandas (BSD) · River (Apache-2.0) · Gymnasium + Stable-Baselines3 (MIT) · pytest

## Open questions

- What exactly should the system optimize? Solar self-consumption, battery lifetime, keeping a reserve for a load — or a combination?
- Exact capacity of the current test battery.
