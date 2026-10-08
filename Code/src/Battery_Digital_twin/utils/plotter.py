import matplotlib.pyplot as plt
import numpy as np

class BatteryPlotter:
    def __init__(self):
        self.soc_history = []
        self.voltage_history = []
        self.temp_history = []
        self.current_history = []
        self.reward_history = []
        self.steps = []

    def log_step(self, step: int, current: float, obs: np.ndarray, reward: float):
        """Slaat de gegevens van 1 simulatiestap op."""
        self.steps.append(step)
        self.current_history.append(current)
        self.soc_history.append(obs[0] * 100.0)  
        self.voltage_history.append(obs[1])
        self.temp_history.append(obs[2])
        self.reward_history.append(reward)

    def plot_episode(self, save_path: str = None):
        """Genereert een overzichtelijke 4-in-1 grafiek van de episode."""
        fig, axs = plt.subplots(4, 1, figsize=(10, 10), sharex=True)
        fig.suptitle("Battery Digital Twin Simulation Results", fontsize=14)

        # 1.(Action)
        axs[0].plot(self.steps, self.current_history, color="tab:blue", linewidth=1.5)
        axs[0].set_ylabel("Stroom (A)")
        axs[0].grid(True)

        # 2. SOC (%)
        axs[1].plot(self.steps, self.soc_history, color="tab:green", linewidth=1.5)
        axs[1].set_ylabel("SOC (%)")
        axs[1].set_ylim(-5, 105)
        axs[1].grid(True)

        # 3.(V)
        axs[2].plot(self.steps, self.voltage_history, color="tab:red", linewidth=1.5)
        axs[2].axhline(y=2.8, color="r", linestyle="--", alpha=0.6, label="V_min (2.8V)")
        axs[2].axhline(y=4.2, color="r", linestyle="--", alpha=0.6, label="V_max (4.2V)")
        axs[2].set_ylabel("Spanning (V)")
        axs[2].legend(loc="upper right")
        axs[2].grid(True)

        # 4.(°C)
        axs[3].plot(self.steps, self.temp_history, color="tab:orange", linewidth=1.5)
        axs[3].axhline(y=60.0, color="r", linestyle="--", alpha=0.6, label="T_max (60°C)")
        axs[3].set_ylabel("Temp (°C)")
        axs[3].set_xlabel("Stap (dt = 1s)")
        axs[3].legend(loc="upper right")
        axs[3].grid(True)
        min_temp = min(self.temp_history) - 0.5
        max_temp = max(self.temp_history) + 1.0
        axs[3].set_ylim(min_temp, max(max_temp, 30.0))

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
            print(f"Grafiek opgeslagen als: {save_path}")
        else:
            plt.show()

    def clear(self):
        """Wist de historie voor een nieuwe episode."""
        self.__init__()