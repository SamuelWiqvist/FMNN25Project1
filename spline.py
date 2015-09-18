import numpy as np
import scipy.linalg as sl

class Spline:
    def __init__(self, grid, control_points):
        self.grid = grid;
        self.control_points = control_points
    def _find_controlPoints_(self, u, i):
        # returns an array with four first control points
        cp = self.control_points
        col1 = [cp[0][i-2], cp[0][i-1], cp[0][i], cp[0][i+1]]
        col2 = [cp[1][i-2], cp[1][i-1], cp[1][i], cp[1][i+1]] 
        cp_first = np.array([col1, col2])
        return cp_first
'''
    def __call__(self, u):
'''
    def _alpha_(u):
        
'''     
    def _find_interval_(self, u):
'''                     
        
'''            
    def _blossom(self, u):
        
    def plot(s, points):
'''

def eval_basis(u, j): # just something I came up with, I dont know if it is correct / Samuel
    control_points = [(0,0)]
    for i in range(1, len(u)-3):
        control_points.append((0,0))
    control_points[j] = (1,1) 
    s_temp = Spline(u,control_points)
    points = np.linspace(min(u),max(u),100).tolist()     
    plot(s_temp, points)

