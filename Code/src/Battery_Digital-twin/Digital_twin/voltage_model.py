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
