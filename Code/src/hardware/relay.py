from gpiozero import OutputDevice
from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] /"config.yaml"
config = yaml.safe_load(open(CONFIG_PATH, encoding="utf-8"))
relay = OutputDevice(config["hardware"]["relay_pin"]) # add in active_high=False, initial_value=False if its inverted

def turnOff():
    relay.off()
def turnOn():
    relay.on()