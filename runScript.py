import numpy as np
import scipy.linalg as sl

#%%
grid = np.linspace(0,10,10).tolist() # K = 9
control_points = [(3.2,4),(4.5,5),(5,6),(6,8),(7,4), (8,6),(8.6,7)] # L = K - 2 = 7
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


