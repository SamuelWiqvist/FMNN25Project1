import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt

#from spline import Spline
runfile('./spline.py')
#%%
grid = np.linspace(0,10,10) # K = 9
control_points = np.array([[3,4.5,5,6,7,8,8.6,9],[4,5,6,8,4,6,7.2,6]])# L = K - 2 = 7
#%%
s = Spline(grid, control_points) # initialize the spline 
#%%
s._find_interval(7)
#%%
t = s._find_controlPoints(7.7) #Fungerar inte för 7 som bör vara med i domain(s)
#%%
s._alpha(3.5)
#%%
s._blossom(3.5)
#%%
t = eval_basis(s.grid, 3)
#%%
s.plot(50)
#%%
control_points = np.zeros((7,2))
control_points[5] = 1
#%%
s(2)  # this is not an valid input since 2 in [u_1 u_2] 
#%%
s(7) # this is a valid input since t in [u_k-3 u_k-2]
#%%
t = s.plot(50)
#%%
t = eval_basis(s.grid, 8)
#%%


