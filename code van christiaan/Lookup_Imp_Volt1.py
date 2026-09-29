import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe D#

try:
    V1f = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_volt1.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_V = np.array(V1f, dtype=float)

# === Step 2: Extract x, y, z ===
x_V1 = V1f.index.to_numpy(dtype=float)          # X values from index
y_V1 = V1f.columns.to_numpy(dtype=float)        # Y values from header
z_V1 = V1f.to_numpy(dtype=float)              # Z grid values

xy_V1 = np.array(list(product(x_V1, y_V1)))

V21 = np.concatenate(z_V1)
print(V21)

interpolator_V1 = CloughTocher2DInterpolator(xy_V1, V21)

def Calculate_V1(a,b):
    e = interpolator_V1(a, b)
    print(interpolator_V1(a, b))
    return e