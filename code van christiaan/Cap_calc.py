import pandas as pd
import numpy as np

#Formula to calculate the SOC

Start_cap = 4627
i = 0

try:
    df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Time-rate.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

Sec_1 = df['Time'].loc[df.index[163]]
Sec_2 = df['Time'].loc[df.index[163+1]]
Rate = df['C rate'].loc[df.index[163]]
Time_int = Sec_2-Sec_1
Cap_updated = Start_cap + (Time_int * ((Start_cap / 3600) * Rate))

print(Cap_updated)

#print(value)

#print(value)

