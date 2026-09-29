import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
from itertools import product

try:
    Imp = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Impedance.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

#Define the arrays from the dataframe

Imp_array = np.array(Imp, dtype=float)

#print(Imp_array)

known_x = Imp['Voltage']
known_Volt_calc = Imp['Volt_calc']
known_A = Imp['A']
known_B = Imp['B']
known_C = Imp['C']
known_D = Imp['D']

#print(known_x, known_Volt_calc, known_A, known_B, known_C, known_D)

#Interpolate for the values of the impedance factors

Val_Volt_calc = interp1d(known_x, known_Volt_calc, kind='linear', bounds_error=False)
Val_A = interp1d(known_x, known_A, kind='linear', bounds_error=False)
Val_B = interp1d(known_x, known_B, kind='linear', bounds_error=False)
Val_C = interp1d(known_x, known_C, kind='linear', bounds_error=False)
Val_D = interp1d(known_x, known_D, kind='linear', bounds_error=False)

print(Val_Volt_calc(3.70), Val_A(3.70), Val_B(3.70), Val_C(3.70), Val_D(3.70))