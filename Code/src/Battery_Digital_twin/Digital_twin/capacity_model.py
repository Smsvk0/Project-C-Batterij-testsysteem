import numpy as np
import pandas as pd
from scipy.interpolate import interp1d


def Capacity_calc(Temp: float, Ch_rate: float, df_temp_cap: pd.DataFrame) -> float:
    """
    Calculate available battery capacity based on temperature, C-rate, and lookup table data.

    Parameters:
        temp (float): Temperature in degrees Celsius.
        ch_rate (float): Charge/discharge C-rate.
        df_temp_cap (pd.DataFrame): DataFrame containing 'Temperature', 'A', 'B', and 'C' columns.

    Returns:
        float: Interpolated battery capacity.
    """
    if ch_rate <= 0:
        ch_rate = 0.01


    known_x = df_temp_cap['Temperature']
    known_A = df_temp_cap['A']
    known_B = df_temp_cap['B']
    known_C = df_temp_cap['C']

    Val_constA = interp1d(known_x, known_A, kind='linear', bounds_error=False)
    Val_constB = interp1d(known_x, known_B, kind='linear', bounds_error=False)
    Val_constC = interp1d(known_x, known_C, kind='linear', bounds_error=False)


    A = float(Val_constA(Temp))
    B = float(Val_constB(Temp))
    C = float(Val_constC(Temp))

    cap_interp = (A * ( 1/ Ch_rate)**2) + (B *(1 / Ch_rate)) + C

    return float(cap_interp)



