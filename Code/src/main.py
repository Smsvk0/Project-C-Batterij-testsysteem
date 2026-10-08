import os
import threading
import time
from pathlib import Path

import uvicorn
import yaml

from api import receiver
from safety.limits import applyLimits

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yaml"
config = yaml.safe_load(open(CONFIG_PATH, encoding="utf-8"))

BATTERY_TYPE = "li-ion"
LOOP_INTERVAL = 0.1   # seconden tussen besturingsbeslissingen
STALE_AFTER = 3.0     # meetdata ouder dan dit is verouderd -> geen actie

def pinToCore(core: int):
    """Koppel deze thread aan een specifieke CPU-kern (alleen Pi/Linux)."""
    try:
        os.sched_setaffinity(0, {core})
    except (AttributeError, OSError):
        pass  # geen core-affinity mogelijk, OS plant gewoon in

def modelLoop():
    """Model/safety-loop: leest de laatste meting en past de limits toe.

    Draait op een eigen core, los van de FastAPI in de main loop.
    """
    pinToCore(config["runtime"].get("model_core", 1))
    wasCharging = False
    last_seen = None
    last_update = time.monotonic()
    waiting = False
    while True:
        data = receiver.latest_data
        if data is not None and data is not last_seen:
            last_seen = data
            last_update = time.monotonic()
        voltage = data.get("battery_voltage") if data is not None else None
        stale = voltage is None or not isinstance(voltage, (int, float)) \
            or isinstance(voltage, bool) or time.monotonic() - last_update > STALE_AFTER
        if stale:
            if not waiting:
                print("geen verse meetdata, wachten...")
                waiting = True
            time.sleep(1)
            continue
        waiting = False
        wasCharging = applyLimits(float(voltage), wasCharging, BATTERY_TYPE)
        time.sleep(LOOP_INTERVAL)

# ---------- main loop: FastAPI ----------

# Main-thread (FastAPI event loop) op zijn eigen core, anders dan de model-loop
pinToCore(config["runtime"].get("api_core", 0))

# Model-loop alvast op een eigen thread/core starten, dan blokkeert uvicorn hier
modelThread = threading.Thread(target=modelLoop, name="model-loop", daemon=True)
modelThread.start()
print(f"model-loop gestart, FastAPI luistert op 0.0.0.0:8000 (batterij: {BATTERY_TYPE})")

if __name__ == "__main__":
    uvicorn.run(receiver.app, host="0.0.0.0", port=8000, log_level="warning")
    