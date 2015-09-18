import numpy as np
import scipy.linalg as sl
#from spline import Spline
runfile('./spline.py')
#%%
grid = np.linspace(0,10,10) # K = 9
control_points = np.array([[3,4.5,5,6,7,8,8.6,9],[4,5,6,8,4,6,7.2,6]])# L = K - 2 = 7
#%%
s = Spline(grid, control_points) # initialize the spline 
#%%
s._find_interval(0.2)
#%%
t = s._find_controlPoints(5.58620689655) #Fungerar inte för sista intervallet, fungerar dock nu
#%%
s._alpha(3.5)
#%%
s._blossom(3.5)
#%%
t = eval_basis(s.grid, 3)
#%%
s.plot(np.linspace(min(s.grid),max(s.grid),100))
