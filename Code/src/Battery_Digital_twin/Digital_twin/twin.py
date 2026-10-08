class DigitalTwin:
    def __init__(self, capacity_ah: float = 100.0, initial_soc: float = 1.0, initial_temp: float = 25.0):
        self.capacity_ah = capacity_ah
        self.soc = initial_soc
        self.temp = initial_temp
        self.v_terminal = 4.2  
        

        self.r_internal = 0.01  
        self.thermal_capacity = 400.0  

    def step(self, current_amps: float, dt: float = 1.0) -> dict:

        delta_soc = (current_amps * (dt / 3600.0)) / self.capacity_ah
        self.soc = max(0.0, min(1.0, self.soc - delta_soc))
        
   
        self.v_terminal = 3.0 + (self.soc * 1.2) - (current_amps * self.r_internal)

        p_loss = (current_amps ** 2) * self.r_internal
        delta_temp = (p_loss * dt) / self.thermal_capacity
        self.temp += delta_temp

        return {
            "v_terminal": self.v_terminal,
            "soc": self.soc,
            "temp": self.temp
        }