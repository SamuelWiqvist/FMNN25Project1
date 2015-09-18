import numpy as np
import scipy.linalg as sl

class Spline:
    def __init__(self, grid, control_points):
        self.grid = grid;
        self.control_points = control_points

    def __call__(self, u):
        return self._blossom(self, u)

    def _find_controlPoints(self, u):
        # returns an array with four first control points
        I = self._find_interval(u)
        cp = self.control_points
        col1 = [cp[0][I-2], cp[0][I-1], cp[0][I], cp[0][I+1]]
        col2 = [cp[1][I-2], cp[1][I-1], cp[1][I], cp[1][I+1]] 
        cp_first = np.array([col1, col2])
        return cp_first
    
    def _find_interval(self, u):
        return np.argmax(self.grid > u)


    def _alpha(self,u):
        #Knots corresponds to the u:s inside a blossom pair
        #d[u; uI-1; uI] = alpha(u)d[uI-2; uI-1; uI] + (1 (u))d[uI-1; uI; uI+1]
        I = self._find_interval(u)
        u_right_most_knot = self.grid[I+1]
        u_left_most_knot = self.grid[I-2]
        alpha = (u_right_most_knot - u)/(u_right_most_knot - u_left_most_knot)
        return alpha

    def _blossom(self, u):
        d = self._find_controlPoints(u).tolist()
        while len(d) > 1:
            d2 = []
            for i in range(len(d) - 1):
                merge_x = self._alpha(u)*d[i][0] + (1 - self._alpha(u))*d[i + 1][0]
                merge_y = self._alpha(u)*d[i][1] + (1 - self._alpha(u))*d[i + 1][1]
                d2.append([merge_x, merge_y])
            d = d2
        return d
        
    def plot(s, points):
        pass
    
    def __repr__(self):
        return 'Spline'

def eval_basis(u, j): # just something I came up with, I dont know if it is correct / Samuel
    control_points = [(0,0)]
    for i in range(1, len(u)-3):
        control_points.append((0,0))
    control_points[j] = (1,1) 
    s_temp = Spline(u,control_points)
    points = np.linspace(min(u),max(u),100).tolist()     
    plot(s_temp, points)
