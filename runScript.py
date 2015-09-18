import numpy as np
import scipy.linalg as sl
from spline import Spline

#%%
grid = np.linspace(0,10,10) # K = 9
control_points = np.array([[3,4.5,5,6,7,8,8.6],[4,5,6,8,4,6,7.2]])# L = K - 2 = 7
#%%
s = Spline(grid, control_points) # initialize the spline 
#%%
s._find_interval(3.5)
#%%
t = s._find_controlPoints(3.5)
#%%
s._alpha(3.5)
#%%
s._blossom(3.5)
#%%
t = eval_basis(s.grid, 3)