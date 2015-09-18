import numpy as np
import scipy.linalg as sl

class Spline:
    def __init__(self, grid, control_points):
        self.grid = grid;
        self.control_points = control_points
    

    def __call__(self, u):
        pass
        
    def _alpha_(u):
        pass
        
    def _find_interval_(self, u):
        pass
    
    def _find_controlPoint_(self, u):
        pass
        
    def _blossom(self, u):
        d = _find_controlPoint_(self, u).toList()
        while len(d) > 1:
            d2 = []
            for i in range(len(d) - 1):
                merge_x = _alpha(self, u)*d[i][0] + (1 - alpha(self, u))*d[i + 1][0]
                merge_y = _alpha(self, u)*d[i][1] + (1 - alpha(self, u))*d[i + 1][1]
                d2.append([merge_x, merge_y])
            d = d2
        return d
        
    def plot(self, points = 10**5):
        u_plot = np.linspace(grid[2], grid[-3], points)
        # not finished..

def eval_basis(u, j): # just something I came up with, I dont know if it is correct / Samuel
    control_points = [(0,0)]
    for i in range(1, len(u)-3):
        control_points.append((0,0))
    control_points[j] = (1,1) 
    s_temp = Spline(u,control_points)
    points = np.linspace(min(u),max(u),100).tolist()     
    plot(s_temp, points)



