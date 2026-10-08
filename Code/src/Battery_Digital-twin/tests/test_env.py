import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from envs.battery_env import battery_env
from utils.plotter import BatteryPlotter


def test_with_visualization():
    env = battery_env()
    plotter = BatteryPlotter()

    obs, info = env.reset()

    print("Simulatie starten met logging...")
    for step in range(1, 60):

        action = [0.8]
        current = float(action[0])

        obs, reward, terminated, truncated, info = env.step(action)
        
        actual_current = float(action[0]) * 50.0
        plotter.log_step(step=step, current=actual_current, obs=obs, reward=reward)

        if terminated or truncated:
            print(f"Episode beëindigd bij stap {step}")
            break


    plotter.plot_episode(save_path="simulation_plot.png")


if __name__ == "__main__":
    test_with_visualization()