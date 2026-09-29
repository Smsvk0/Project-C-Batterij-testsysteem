import numpy as np
import scipy.interpolate as interp
import pandas as pd
from itertools import product

x = np.array([-0.5, 0, 0.5])
y = np.array([0, 10, 20, 30.0, 40])
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#X, Y = np.meshgrid(x, y, indexing='ij')

#df3 = np.concatenate([x,y])

#print(df3)
print(list(product(x, y)))

interpolator = interp.CloughTocher2DInterpolator(list(product(x,y)), z)

print(interpolator(0, 21))
