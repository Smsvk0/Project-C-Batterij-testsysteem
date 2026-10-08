import numpy as np
import sys
from gymnasium.utils.env_checker import check_env
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from envs.battery_env import battery_env


def test_battery_environment():
    print("1. Env Initialisation")
    env = battery_env()

    print("2. Gymnasium API test")
    try:
        check_env(env)
        print("Environment works")
    except Exception as e:
        print("Environment doesnt work")
        return

    print ("3. Reset test")
    obs, info = env.reset()
    print(f"Start observation: {obs}")

    print("4. Step Test")
    for step in range(5):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"Step {step+1} | Action: {action[0]:.2f}A | Obs: {obs} | Reward: {reward:.2f}")

        if terminated or truncated:
            print("Veiligheidsgrens bereikt, Resetten van de omgeving")
            obs, info = env.reset()

if __name__ == "__main__":
    test_battery_environment()