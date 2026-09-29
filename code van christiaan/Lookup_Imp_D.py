import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe D#

try:
    Df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_C.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_D = np.array(Df, dtype=float)

# === Step 2: Extract x, y, z ===
x_D = Df.index.to_numpy(dtype=float)          # X values from index
y_D = Df.columns.to_numpy(dtype=float)        # Y values from header
z_D = Df.to_numpy(dtype=float)              # Z grid values

xy_D = np.array(list(product(x_D, y_D)))

D2 = np.concatenate(z_D)
print(D2)

interpolator_D = CloughTocher2DInterpolator(xy_D, D2)

def Calculate_D(a,b):
    j = interpolator_D(a, b)
    print(interpolator_D(a, b))
    return j