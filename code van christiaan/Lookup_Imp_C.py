import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe C#

try:
    Cf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_C.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_C = np.array(Cf, dtype=float)

# === Step 2: Extract x, y, z ===
x_C = Cf.index.to_numpy(dtype=float)          # X values from index
y_C = Cf.columns.to_numpy(dtype=float)        # Y values from header
z_C = Cf.to_numpy(dtype=float)              # Z grid values

xy_C = np.array(list(product(x_C, y_C)))

C2 = np.concatenate(z_C)
print(C2)

interpolator_C = CloughTocher2DInterpolator(xy_C, C2)

def Calculate_C(a,b):
    h = interpolator_C(a, b)
    print(interpolator_C(a, b))
    return h