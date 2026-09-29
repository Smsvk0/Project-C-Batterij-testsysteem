import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe D#

try:
    V2f = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_volt2.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_V = np.array(V2f, dtype=float)

# === Step 2: Extract x, y, z ===
x_V2 = V2f.index.to_numpy(dtype=float)          # X values from index
y_V2 = V2f.columns.to_numpy(dtype=float)        # Y values from header
z_V2 = V2f.to_numpy(dtype=float)              # Z grid values

xy_V2 = np.array(list(product(x_V2, y_V2)))

V22 = np.concatenate(z_V2)
print(V22)

interpolator_V2 = CloughTocher2DInterpolator(xy_V2, V22)

def Calculate_V2(a,b):
    q = interpolator_V2(a, b)
    print(interpolator_V2(a, b))
    return q