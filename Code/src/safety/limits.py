from pathlib import Path
from hardware.relay import turnOff, turnOn
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] /"config.yaml"

config = yaml.safe_load(open(CONFIG_PATH, encoding="utf-8"))


def applyLimits(voltage, wasCharging, batteryType):
    # Retrieve voltage limits from the config.yaml
    limits = config["chemistries"][batteryType]
    cutoff_v = limits["cutoff_v"]
    resume_v = limits["resume_v"]

    # compaire the voltage to the maximun voltage, so the battery can never explode
    if (voltage >= cutoff_v):
        turnOff()
        return False
    if (voltage < resume_v):
        turnOn()
        return True
    if (voltage >= resume_v) and (voltage < cutoff_v) and (wasCharging == True):
        return True
    if (voltage >= resume_v) and (voltage < cutoff_v) and (wasCharging == False):
        return False

    # If it goes past all if statements it raises an error
    turnOff()
    raise ValueError(f"Variable Failure: {voltage} {wasCharging} {batteryType}")