import gymnasium as gym 
from gymnasium import spaces
import numpy as np 

from Digital_twin.twin import DigitalTwin

class battery_env(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode

        self.action_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(1,),
            dtype=np.float32
        )

        low_obs = np.array([0.0, 2.5, -20.0], dtype=np.float32)
        high_obs = np.array([1.0, 4.5, 80.0], dtype=np.float32)
        self.observation_space = spaces.Box(
            low=low_obs,
            high=high_obs,
            dtype=np.float32
        )

        self.v_min = 2.8
        self.v_max = 4.2
        self.temp_max = 60.0

        self.twin = DigitalTwin(capacity_ah=100.0, initial_soc=1.0, initial_temp=25.0)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.twin = DigitalTwin(capacity_ah=100.0, initial_soc=1.0, initial_temp=25.0)
        obs = self._get_obs()
        info = {}

        return obs, info

    def step(self, action: np.ndarray):
        current_amps = float(action[0]) * 50.0
        dt = 1.0

        state = self.twin.step(current_amps=current_amps, dt=dt)

        obs = self._get_obs()

        terminated = False
        if state["v_terminal"] < self.v_min or state["v_terminal"] > self.v_max:
            terminated = True
        elif state["temp"] > self.temp_max:
            terminated = True
        elif state["soc"] <= 0.0:
            terminated = True

        truncated = False

        reward = self._calculate_reward(state, current_amps, terminated)

        info = {
            "v_terminal": state["v_terminal"],
            "soc": state["soc"],
            "temp": state["temp"]
        }

        return obs, reward, terminated, truncated, info

    def _get_obs(self) -> np.ndarray:
        return np.array([
            self.twin.soc, 
            self.twin.v_terminal if hasattr(self.twin, 'v_terminal') else 4.2,
            self.twin.temp
        ], dtype=np.float32)

    def _calculate_reward(self, state:dict, current: float, terminated: bool) -> float:
        if terminated:
            return -100.0

        reward = 1.0 - (abs(current) * 0.01)
        return float(reward)

