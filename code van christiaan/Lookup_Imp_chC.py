import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

# Import dataframe B#

try:
    chCf = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Charging_imp/Ch_Imp_C.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

array_chC = np.array(chCf, dtype=float)

# === Step 2: Extract x, y, z ===
x_chC = chCf.index.to_numpy(dtype=float)          # X values from index
y_chC = chCf.columns.to_numpy(dtype=float)        # Y values from header
z_chC = chCf.to_numpy(dtype=float)              # Z grid values

xy_chC = np.array(list(product(x_chC, y_chC)))

chC2 = np.concatenate(z_chC)
#print(B2)

interpolator_chC = CloughTocher2DInterpolator(xy_chC, chC2)
print(interpolator_chC(3.8, 0.8))

def Calculate_chC(a,b):
    cc = interpolator_chC(a, b)
    print(interpolator_chC(a, b))
    return cc