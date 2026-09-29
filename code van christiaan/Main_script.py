import pandas as pd
import numpy as np
import Lookup_incorp
import Lookup_imp_val

Volt = 3.8

e = Lookup_imp_val.Interp_volt_imp(Volt)
f = Lookup_imp_val.Interp_volt_imp(Volt)
g = Lookup_imp_val.Interp_volt_imp(Volt)
h = Lookup_imp_val.Interp_volt_imp(Volt)
j = Lookup_imp_val.Interp_volt_imp(Volt)
            
print(e)

Par_Voltage = e
Par_A = f
Par_B = g
Par_C = h
Par_D = j
