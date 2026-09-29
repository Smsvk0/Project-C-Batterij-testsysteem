import pandas as pd
import numpy as np
import Lookup_incorp
import Lookup_imp_val
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import time
#from matplotlib.animation import FuncAnimation
import threading


#Formula to calculate the SOC

Init_cap = 4110

start_time = 0

try:
    df = pd.read_csv("C:/Users/Gebruiker/Documents/Li-ion pack/Time-rate.csv", delimiter=";", index_col=0)  # First column is x, header row is y
except FileNotFoundError:
    raise SystemExit("Error: CSV file not found.")
except pd.errors.EmptyDataError:
    raise SystemExit("Error: CSV file is empty or invalid.")

Sec_1 = 0
Init_cap = 4263
Voltage = 4.1896

plt.ion()
class start_model():
    def model():
        i = 0
        while i < 414:
    
            if i == 0:
                Start_cap = 4263
            else: 
                Start_cap = Cap
            global Sec_1
            Sec_1 = df['Time'].loc[df.index[i]]
            Sec_2 = df['Time'].loc[df.index[i+1]]
            Rate = df['C rate'].loc[df.index[i]]
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
            global Voltage
            Voltage = Volt
            time.sleep(0.05)
                    #print('Voltage', Volt, 'Period', Period)
            
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    #max_x = 10
    max_x = 3600

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

    