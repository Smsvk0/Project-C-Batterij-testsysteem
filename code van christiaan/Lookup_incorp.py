import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import CloughTocher2DInterpolator
from itertools import product

try:
    df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/SOC-rate_2.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

data_array = np.array(df, dtype=float)

# === Step 2: Extract x, y, z ===
x = df.index.to_numpy(dtype=float)          # X values from index
y = df.columns.to_numpy(dtype=float)        # Y values from header
z = df.to_numpy(dtype=float)              # Z grid values

xy = np.array(list(product(x, y)))

z2 = np.concatenate(z)
print(z2)

interpolator = CloughTocher2DInterpolator(xy, z2)

def Calculate(a,b):
    c = interpolator(a, b)
    print(interpolator(a, b))
    return c

