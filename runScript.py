import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt

from spline import Spline
#from spline import eval_basis
#runfile('./spline.py')
#%%
grid = np.linspace(0,10,10) # K = 9
#control_points = np.array([[3,4.5,5,6,7,8,8.6,9],[4,5,6,8,4,6,7.2,6]])# L = K - 2 = 7
control_points = np.array([[2.3,2.1,4,6,7,8,5.5,6.3],[7,5.5,4.3,4.5,4,5.56,7.2,6]])# L = K - 2 = 7
#%%
s = Spline(grid, control_points) # initialize the spline 
#%%
s._find_interval(3)
#%%
t = s._find_control_points(7) #Fungerar inte för 7 som bör vara med i domain(s)
#%%
#s._alpha(3.5)
#%%
s._blossom(3.5)
#%%
#t = eval_basis(s.grid, 3)
#%%
s.plot(100)
#%%
control_points = np.zeros((7,2))
control_points[5] = 1
#%%
#s(2)  # this is not an valid input since 2 in [u_1 u_2] 
#%%
#s(7) # this is a valid input since t in [u_k-3 u_k-2]
#%%
#t = s.plot(100)
#%%
#basis_0 = _setup_basis(grid)
#%%
#t = _basis_recursion(grid,3.5, 4, basis_0)
#%%
x = np.linspace(min(grid),max(grid),100)
plt.plot(x,t[0])        
#%%
utest = np.linspace(0,10,1000)
Ntest = s.N(3)
Narray = []
for j in range(len(utest)):
    Narray.append(Ntest(s,utest[j]))
plt.plot(utest,Narray)
