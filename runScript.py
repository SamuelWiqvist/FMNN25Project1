import numpy as np
import scipy.linalg as sl
from spline import Spline

#%%
grid = np.linspace(0,10,10) # K = 9
control_points = np.array([[3,4.5,5,6,7,8,8.6],[4,5,6,8,4,6,7.2]])# L = K - 2 = 7
#%%
s = Spline(grid, control_points) # initialize the spline 
#%%
u = 3.5
s(u) # run __call__   
#%%
points = np.linspace(0,10,100).tolist()
plot(s,points) #plot spline
#%%
u = np.linspace(0,10,10).tolist() #knot sequence
j = 5 # index
eval_basis(u, j)  #evaluate j:th B-spline basis


#%%
i = 2
col1 = [control_points[0][i-2], control_points[0][i-1], control_points[0][i], control_points[0][i+1]]
col2 = [control_points[1][i-2], control_points[1][i-1], control_points[1][i], control_points[1][i+1]]
#%%
t = np.array([col1, col2])
#%%
s._find_interval(3.5)
#%%
t = s._find_controlPoints(3.5)
#%%
s._alpha(3.5)
#%%
s._blossom(3.5)
