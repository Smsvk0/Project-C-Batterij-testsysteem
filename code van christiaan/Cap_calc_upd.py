import pandas as pd
import numpy as np
import Lookup_incorp
import Lookup_imp_val
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Figure

#Formula to calculate the SOC

Init_cap = 4627
i = 0
start_time = 0

try:
    df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Time-rate.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")



while i < 414:
    
    if i == 0:
        Start_cap = 4627
    else: 
        Start_cap = Cap
    
    Sec_1 = df['Time'].loc[df.index[i]]
    Sec_2 = df['Time'].loc[df.index[i+1]]
    Rate = df['C rate'].loc[df.index[i]]
    Time_int = Sec_2-Sec_1
    Cap = Start_cap + (Time_int * ((Start_cap / 3600) * Rate))
    print(Cap)
    i += 1
    SOC = (Cap / Init_cap) * 100
    print(SOC)
    
    if not Rate == 0:
        c = Lookup_incorp.Calculate(SOC, Rate)
        print(c)
        Volt = c
        start_time = 0
        t = 0
    
    else:
        if t == 0:
            Period = start_time + Time_int
            e = Lookup_imp_val.Interp_volt_imp(Volt)
            f = Lookup_imp_val.Interp_A_imp(Volt)
            g = Lookup_imp_val.Interp_B_imp(Volt)
            h = Lookup_imp_val.Interp_C_imp(Volt)
            j = Lookup_imp_val.Interp_D_imp(Volt)
            
            Par_Voltage = e
            Par_A = f
            Par_B = g
            Par_C = h
            Par_D = j
            
            c = Lookup_imp_val.Calc_volt_imp(Period, Par_Voltage, Par_A, Par_B, Par_C, Par_D)
            t = 1
            start_time = Period
            Volt = c
                #print(Volt, Period)
        
        else:
            Period = start_time + Time_int
            c = Lookup_imp_val.Calc_volt_imp(Period, Par_Voltage, Par_A, Par_B, Par_C, Par_D)
            print(c)
            start_time = Period
            Volt = c
                #print('Voltage', Volt, 'Period', Period)
    
    plot_update = Figure.demo(Sec_1, Volt)