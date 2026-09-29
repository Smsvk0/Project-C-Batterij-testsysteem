import pandas as pd
import numpy as np
import Lookup_incorp
import Lookup_imp_val
import matplotlib.pyplot as plt
import time
import threading
import Temp_calc_add
import Lookup_Imp_Volt1
import Lookup_Imp_Volt2
import Lookup_Imp_A
import Lookup_Imp_B
import Lookup_Imp_C
import Lookup_Imp_D
import Lookup_Imp_chA
import Lookup_Imp_chB
import Lookup_Imp_chC

#Formula to calculate temperature dependent capacity#
Temperature = 1
Charging = 0.5

#Formula to calculate the SOC - filling in cap_calc can provide a starting capacity#
Cap_calc = Temp_calc_add.Capacity_calc(Temperature, Charging)
#Cap_calc = 3800
Init_cap = Cap_calc
start_time = 0

try:
    df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Time-rate-ext.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

Sec_1 = 0
#Init_cap = 4263
Voltage = 4.14

plt.ion()
class start_model():
    def model():
        i = 0
        while i < 490:
    
            if i == 0:
                Start_cap = Cap_calc
            else: 
                Start_cap = Cap
            global Sec_1
            Sec_1 = df['Time'].loc[df.index[i]]
            Sec_2 = df['Time'].loc[df.index[i+1]]
            Rate = df['C rate'].loc[df.index[i]]
            Rate_lookup = df['C rate'].loc[df.index[i-2]]
            Time_int = Sec_2-Sec_1
            Cap = Start_cap + (Time_int * ((5000 / 3600) * Rate))
            print(Cap)
            i += 1
            global SOC
            SOC = (Cap / Init_cap) * 100
            print(SOC)
    
            if not Rate == 0:
                c = Lookup_incorp.Calculate(SOC, Rate)
                print(c)
                Volt = c
                start_time = 0
                t = 0
        
    
            else:
                if t == 0 and Rate_lookup < 0:
                    Period = start_time + Time_int

                    e = Lookup_Imp_Volt1.Calculate_V1(Volt, Rate_lookup)
                    f = Lookup_Imp_A.Calculate_A(Volt, Rate_lookup)
                    g = Lookup_Imp_B.Calculate_B(Volt, Rate_lookup)
                    h = Lookup_Imp_C.Calculate_C(Volt, Rate_lookup)
                    j = Lookup_Imp_D.Calculate_D(Volt, Rate_lookup)
                    q = Lookup_Imp_Volt2.Calculate_V2(Volt, Rate_lookup)
                    
                    print(e,f,g,h,i,q)
            
                    Par_Voltage1 = e
                    Par_A = f
                    Par_B = g
                    Par_C = h
                    Par_D = j
                    Par_Voltage2 = q
            
                    c = Lookup_imp_val.Calc_volt_imp(Period, Par_Voltage1, Par_A, Par_B, Par_C, Par_D, Par_Voltage2)
                    t = 1
                    start_time = Period
                    Volt = c
                    #print(Volt, Period)
                
                if t == 0 and Rate_lookup > 0:
                    print('Charging impedence is chosen')
                    Period2 = start_time + Time_int
                    
                    aa = Lookup_Imp_chA.Calculate_chA(Volt, Rate_lookup)
                    bb = Lookup_Imp_chB.Calculate_chB(Volt, Rate_lookup)
                    cc = Lookup_Imp_chC.Calculate_chC(Volt, Rate_lookup)
                    
                    Par_AA = aa
                    Par_BB = bb
                    Par_CC = cc
                    
                    t = 2
        
                if t == 1:
                    Period = start_time + Time_int
                    c = Lookup_imp_val.Calc_volt_imp(Period, Par_Voltage1, Par_A, Par_B, Par_C, Par_D, Par_Voltage2)
                    print(c)
                    start_time = Period
                    Volt = c
                
                if t == 2:
                    Period = start_time + Time_int
                    c = Lookup_imp_val.Calc_volt_charge_imp(Period, Par_CC, Par_AA, Par_BB)
                    print(c)
                    start_time = Period
                    Volt = c
                    print('Charging parameter have been set')
                    
                
            global Voltage
            Voltage = Volt
            time.sleep(0.05)
                    #print('Voltage', Volt, 'Period', Period)
            
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    #max_x = 10
    max_x = 4400

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []
        for x in np.arange(0,414,1):
            xdata.append(Sec_1)
            #ydata.append(SOC)
            ydata.append(Voltage)
            self.on_running(xdata, ydata)
            time.sleep(0.01)
        
        #for x in np.arange(0,20,0.5):
            #xdata.append(x)
            #ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
            #self.on_running(xdata, ydata)
            #time.sleep(1)
        return xdata, ydata

t1 = threading.Thread(target=DynamicUpdate())
t2 = threading.Thread(target=start_model.model)
t1.start()
t2.start()
#starter()

    