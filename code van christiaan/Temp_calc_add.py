import math

import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
from itertools import product
import math

try:
    Imp = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Temp_cap.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

#Define the arrays from the dataframe
#Temp = 10

Imp_array = np.array(Imp, dtype=float)

#print(Imp_array)

known_x = Imp['Temperature']
known_A = Imp['A']
known_B = Imp['B']
known_C = Imp['C']

Val_constA = interp1d(known_x, known_A, kind='linear', bounds_error=False)
Val_constB = interp1d(known_x, known_B, kind='linear', bounds_error=False)
Val_constC = interp1d(known_x, known_C, kind='linear', bounds_error=False)

#print(Val_constA(Temp), Val_constB(Temp), Val_constC(Temp))

def Capacity_calc(Temp, Ch_rate):
    A = Val_constA(Temp)
    B = Val_constB(Temp)
    C = Val_constC(Temp)

    #Ch_rate = 0.5

    ### Capacity calculation for 15 degC ###

    Cap_15 = (-0.2227 * (1/Ch_rate)**2) + (16.748 * (1/Ch_rate)) + 4364.7

    #Cap_0 = 16.747 * (1/Ch-rate) + 4069.4

    Cap_0 = (-0.5922 * (1/Ch_rate)**2) + (32.53 * (1/Ch_rate)) + 4023.1

    ### Capacity calculation for interpolated degC ###

    Cap_interp = (A * (1/Ch_rate)**2) + (B * (1/Ch_rate)) + C

    print(Cap_15, Cap_0, Cap_interp)

    return Cap_interp

    

