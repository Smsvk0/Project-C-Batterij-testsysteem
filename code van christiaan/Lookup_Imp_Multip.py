import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

#Import dataframe A#

try:
    Af = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_A.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_A = np.array(Af, dtype=float)

# === Step 2: Extract x, y, z ===
x_A = Af.index.to_numpy(dtype=float)          # X values from index
y_A = Af.columns.to_numpy(dtype=float)        # Y values from header
z_A = Af.to_numpy(dtype=float)              # Z grid values

xy_A = np.array(list(product(x_A, y_A)))

A2 = np.concatenate(z_A)
print(A2)

interpolator_A = CloughTocher2DInterpolator(xy_A, A2)

# Import dataframe B#

try:
    Bf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance/Imp_B.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_B = np.array(Bf, dtype=float)

# === Step 2: Extract x, y, z ===
x_B = Bf.index.to_numpy(dtype=float)          # X values from index
y_B = Bf.columns.to_numpy(dtype=float)        # Y values from header
z_B = Bf.to_numpy(dtype=float)              # Z grid values

xy_B = np.array(list(product(x_B, y_B)))

B2 = np.concatenate(z_B)
print(B2)

interpolator_A = CloughTocher2DInterpolator(xy_A, A2)

def Calculate_A(a,b):
    c = interpolator_A(a, b)
    print(interpolator_A(a, b))
    return c

