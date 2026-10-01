import numpy as np
import pandas as pd 
from scipy.interpolate import RegularGridInterpolator

def build_2d_interpolator(df_matrix: pd.DataFrame) -> RegularGridInterpolator:
    """
    Construct a fast 2D regular grid interpolator from a lookup matix.

    Parameters:
        df_matrix (pd.DataFrame): Matrix where index is X (e.g. SOC),
                                  columns are Y (e.g., Temperature),
                                  and values are Z (parameter values).
    
    Returns:
        RegularGridInterpolator: Compiled 2D interpolation object.
    """

    x_coords = df_matrix.index.to_numpy(dtype=float)
    y_coords = df_matrix.columns.to_numpy(dtype=float)
    z_values = df_matrix.to_numpy(dtype=float)

    interpolator = RegularGridInterpolator(
        (x_coords, y_coords),
        z_values,
        method= "linear",
        bounds_error=False,
        fill_value=None
    )
    return interpolator

def evaluate_parameter(soc: float, temp: float, interpolator: RegularGridInterpolator) -> float:
    """
    Evaluate a single battery parameter at given SOC and Temperature coordinates.

    Parameters:
        soc (float): Current State of Charge (0.0 to 1.0).
        temp (float): Current Temperature in degrees Celsius.
        interpolator (RegularGridInterpolator): Pre-built 2D interpolator.

    Returns:
        float: Interpolated parameter value.
    """
    point = np.array([[soc, temp]])
    return float(interpolator(point)[0])

def calculate_rc_parameters(soc: float, temp: float, interpolator: dict) -> dict:
    """
    Evaluate all 2-RC ECM parameters (OCV, R0, R1, C1, R2, C2) simultaneously.

    Parameters:
        soc (float): Current State of Charge.
        temp (float): Current Temperature.
        interpolators (dict): Dictionary mapping parameter names to RegularGridInterpolator objects.

    Returns:
        dict: Interpolated parameter values for the current battery state.
    """  
    return {
        param_name: evaluate_parameter(soc, temp, interpolator)
        for param_name, interpolator in interpolator.items()
    }

def update_rc_voltage(
    v_rc1: float,
    v_rc2: float,
    current: float,
    r1: float,
    c1: float,
    r2: float,
    c2: float,
    dt: float = 1.0
) -> tuple[float, float]:
    """
    Update the dynamic voltages across the RC networks using discrete-time integration.

    Parameters:
        v_rc1 (float): Voltage drop across RC1 branch at step k-1 (V).
        v_rc2 (float): Voltage drop across RC2 branch at step k-1 (V).
        current (float): Load current in Amperes (positive = discharge, negative = charge).
        r1 (float): Resistance of RC1 network (Ohm).
        c1 (float): Capacitance of RC1 network (Farad).
        r2 (float): Resistance of RC2 network (Ohm).
        c2 (float): Capacitance of RC2 network (Farad).
        dt (float): Time step duration in seconds (default: 1.0s).

    Returns:
        tuple[float, float]: Updated (v_rc1, v_rc2) voltages for step k.
    """

    tau1 = r1 * c1 if (r1 * c1) > 0 else 1e-6
    tau2 = r2 * c2 if (r2 * c2) > 0 else 1e-6

    v_rc1_next = v_rc1 * np.exp(-dt / tau1) + r1 * (1.0 - np.exp(-dt / tau1)) * current
    v_rc2_next = v_rc2 * np.exp(-dt / tau2) + r2 * (1.0 - np.exp(-dt / tau2)) * current

    return float(v_rc1_next), float(v_rc2_next)
    
    