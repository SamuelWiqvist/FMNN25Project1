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
<<<<<<< HEAD
'''
    def _alpha_(u):
=======
        
>>>>>>> 650e32db03c7f751becfbdf764a04ca00a6ce809
        
'''     
    def _find_interval_(self, u):
'''                     
        
'''            
    def _blossom(self, u):
        
    def plot(s, points):
<<<<<<< HEAD
'''

def eval_basis(u, j): # just something I came up with, I dont know if it is correct / Samuel
    control_points = [(0,0)]
    for i in range(1, len(u)-3):
        control_points.append((0,0))
    control_points[j] = (1,1) 
    s_temp = Spline(u,control_points)
    points = np.linspace(min(u),max(u),100).tolist()     
    plot(s_temp, points)

=======
"""
    def eval_basis(u, j): # just something I came up with, I dont know if it is correct / Samuel
        control_points = [(0,0)]
        for i in range(1, len(u)-3):
            control_points.append((0,0))
        control_points[j] = (1,1) 
        s_temp = Spline(u,control_points)
        points = np.linspace(min(u),max(u),100).tolist()     
        plot(s_temp, points)

    def _alpha_(u):
        '''Knots corresponds to the u:s inside a blossom pair'''
        d[u; uI-1; uI] = alpha(u)d[uI-2; uI-1; uI] + (1 (u))d[uI-1; uI; uI+1]
        I = self._find_interval(u)
        u_right_most_knot = u[I+1]
        u_left_most_knot = u[I-2]
        alpha = (u_right_most_knot - u)/(u_right_most_knot - u_left_most_knot)
        return alpha

    def _find_interval_(self, u):
        return np.argmax(self.grid > u)
        
        
        
        
        
        
        
        
>>>>>>> 650e32db03c7f751becfbdf764a04ca00a6ce809