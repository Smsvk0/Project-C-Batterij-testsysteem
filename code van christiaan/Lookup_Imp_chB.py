import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe B#

try:
    chBf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Charging_imp/Ch_Imp_B.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_chB = np.array(chBf, dtype=float)

# === Step 2: Extract x, y, z ===
x_chB = chBf.index.to_numpy(dtype=float)          # X values from index
y_chB = chBf.columns.to_numpy(dtype=float)        # Y values from header
z_chB = chBf.to_numpy(dtype=float)              # Z grid values

xy_chB = np.array(list(product(x_chB, y_chB)))

chB2 = np.concatenate(z_chB)
#print(B2)

interpolator_chB = CloughTocher2DInterpolator(xy_chB, chB2)
print(interpolator_chB(3.8, 0.8))

def Calculate_chB(a,b):
    bb = interpolator_chB(a, b)
    print(interpolator_chB(a, b))
    return bb