
import sys
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = MODEL_DIR.parent
TWIN_DIR = PROJECT_ROOT / "Battery_Digital_twin"

if str(TWIN_DIR) not in sys.path:
    sys.path.insert(0, str(TWIN_DIR))

from stable_baselines3 import DQN  
from envs.battery_env import battery_env

def train():
    env = battery_env()

    
    model = DQN(
        policy="MlpPolicy",
        env=env,
        learning_rate=1e-3,
        buffer_size=50_000,
        learning_starts=1000,
        batch_size=32,
        gamma=0.99,
        exploration_fraction=0.1,
        exploration_final_eps=0.02,
        verbose=1
    )

    print("Starten met trainen van DQN agent...")
    model.learn(total_timesteps=50_000)

    save_path = MODEL_DIR / "dqn_battery_model"
    model.save(save_path)
    print(f"DQN model opgeslagen op: {save_path}.zip")

if __name__ == "__main__":
    train()