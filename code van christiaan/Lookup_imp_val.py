import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
from itertools import product
import math
import Lookup_Imp_Volt1
import Lookup_Imp_Volt2
import Lookup_Imp_A
import Lookup_Imp_B
import Lookup_Imp_C
import Lookup_Imp_D


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

#print(Val_Volt_calc(3.70), Val_A(3.70), Val_B(3.70), Val_C(3.70), Val_D(3.70))

def Interp_volt_imp(d):
    e = Val_Volt_calc(d)
    return e
    
def Interp_A_imp(d):
    f = Val_A(d)
    return f
    
def Interp_B_imp(d):
    g = Val_B(d)
    return g

def Interp_C_imp(d):
    h = Val_C(d)
    return h

def Interp_D_imp(d):
    j = Val_D(d)
    return j

def Interp_factors(Volt, Charge):
    print('Ok dude')
    e = Lookup_Imp_Volt1.Calculate_V1(Volt, Charge)
    f = Lookup_Imp_A.Calculate_A(Volt, Charge)
    g = Lookup_Imp_B.Calculate_B(Volt, Charge)
    h = Lookup_Imp_C.Calculate_C(Volt, Charge)
    j = Lookup_Imp_D.Calculate_D(Volt, Charge)
    q = Lookup_Imp_Volt2.Calculate_V2(Volt, Charge)
    
    return e
    return f
    return g
    return h
    return j
    return q
    
def Calc_volt_imp(k, l, m, n, o, p, r):
    
    c = (l + (m * (1 - math.exp(-(k / n))))) + (r + (o * (1 - math.exp(-(k / p)))))
    
    return c

def Calc_volt_charge_imp(s, t, u, v):
    
    c = t * (1 / (s**v)) + u
    
    return c


