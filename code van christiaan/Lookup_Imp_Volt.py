import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe D#

try:
    Vf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_volt.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_V = np.array(Vf, dtype=float)

# === Step 2: Extract x, y, z ===
x_V = Vf.index.to_numpy(dtype=float)          # X values from index
y_V = Vf.columns.to_numpy(dtype=float)        # Y values from header
z_V = Vf.to_numpy(dtype=float)              # Z grid values

xy_V = np.array(list(product(x_V, y_V)))

V2 = np.concatenate(z_V)
print(V2)

interpolator_V = CloughTocher2DInterpolator(xy_V, V2)

def Calculate_V(a,b):
    e = interpolator_V(a, b)
    print(interpolator_V(a, b))
    return e