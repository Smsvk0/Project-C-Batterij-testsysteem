import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
from itertools import product
import math

#Step 1: Import the lookup table for relating the current when reaching V = 4.2 during charging to the SOC.

try:
    Curr = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Current_SOC.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

#Step 2: Set the columns for interpolation in the next step.

known_x = Curr['Current']
known_SOC = Curr['SOC']

#Step 3: Define the 1D interpolation fuction.

Val_SOC = interp1d(known_x, known_SOC, kind='linear', bounds_error=False)

#Step 4a: Provide an example current to test the code.

#Current = 4333

#print(Val_SOC(Current))