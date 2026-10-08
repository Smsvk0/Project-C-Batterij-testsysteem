import numpy as np
import pandas as pd
from scipy.interpolate import RegularGridInterpolator

def create_impedance_interpolator(df_matrix: pd.DataFrame) -> RegularGridInterpolator:
    """
    Build a fast 2D regular grid interpolator from a parameter matrix.

    Parameters:
        df_matrix (pd.DataFrame): Matrix with SOC as index (0.0 - 1.0) and
                                  Temperature (°C) as columns.

    Returns:
        RegularGridInterpolator: Pre-compiled 2D interpolator object.
    """
    x_coords = df_matrix.index.to_numpy(dtype=float)
    y_coords = df_matrix.columns.to_numpy(dtype=float)
    z_values = df_matrix.to_numpy

    return RegularGridInterpolator(
        (x_coords, y_coords),
        z_values,
        method="linear",
        bounds_error=False,
        fill_value=None
    )

def create_all_interpolators(matrices: dict[str, pd.DataFrame]) -> dict[str, RegularGridInterpolator]:
    """
    Convert a dictionary of parameter DataFrames (e.g. loaded from SQL)
    into a dictionary of 2D RegularGridInterpolators.

    Parameters:
        matrices (dict[str, pd.DataFrame]): Dictionary containing DataFrames for 
                                            R0, R1, C1, R2, C2, and OCV.

    Returns:
        dict[str, RegularGridInterpolator]: Dictionary of pre-compiled 2D interpolators.
    """
    return {
        param_name: create_impedance_interpolator
        for param_name, df in matrices.items()
    }