from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random
#from Cap_calc_upd import model.Sec_1

x = [0]
y = [4627]
fig, ax = plt.subplots()
graph = ax.plot(x,y,color = 'g')[0]
plt.ylim(0,5000)
plt.ylim(0,3600)

Sec_1=0
SOC = 4627


# updates the data and graph
def update(frame):
    global graph

    # updating the data
    #x.append(x[-1] + 1)
    #y.append(random.randint(1,10))
    x.append(Sec_1)
    y.append(SOC)

    # creating a new graph or updating the graph
    graph.set_xdata(x)
    graph.set_ydata(y)
    #plt.xlim(x[0], x[-1])
    print('Updating plot')

anim = FuncAnimation(fig, update, frames = 2000)
plt.show()
