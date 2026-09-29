import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe B#

try:
    chAf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Charging_imp/Ch_Imp_A.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_chA = np.array(chAf, dtype=float)

# === Step 2: Extract x, y, z ===
x_chA = chAf.index.to_numpy(dtype=float)          # X values from index
y_chA = chAf.columns.to_numpy(dtype=float)        # Y values from header
z_chA = chAf.to_numpy(dtype=float)              # Z grid values

xy_chA = np.array(list(product(x_chA, y_chA)))

chA2 = np.concatenate(z_chA)
#print(B2)

interpolator_chA = CloughTocher2DInterpolator(xy_chA, chA2)
print(interpolator_chA(3.8, 0.8))

def Calculate_chA(a,b):
    aa = interpolator_chA(a, b)
    print(interpolator_chA(a, b))
    return aa