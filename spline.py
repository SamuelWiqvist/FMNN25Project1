import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt

class Spline:
    def __init__(self, grid, control_points):
        self.grid = grid;
        self.control_points = control_points

    def __call__(self, u):
        if(u >= self.grid[-3] or u <= self.grid[2]): # check input
            print("Invalid input. The splin is only defined on [u_2 u_k-2]")
            raise SystemExit
        return self._blossom(u)

    def _find_controlPoints(self, u):
        # returns an array with the four first control points
        # for the blossom recursion 
        I = self._find_interval(u)
        cp = self.control_points
        row0 = [cp[0][I-2], cp[0][I-1], cp[0][I], cp[0][I+1]]
        row1 = [cp[1][I-2], cp[1][I-1], cp[1][I], cp[1][I+1]] 
        cp_first = np.array([row0, row1])
        return cp_first
        
    
    def _find_interval(self, u):
        return np.argmax(self.grid > u) -1

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
        
    def plot(self, points):
        u = np.linspace(self.grid[2], self.grid[-3], points) # u2:uK-2
        u = u[1:len(u)-2] # remove end-points
        s = np.zeros((points-3,2))
        for j in range(points-3):
            s[j,0] = self(u[j])[0][0]
            s[j,1] = self(u[j])[0][1] 
        #return s 
        plt.plot(self.control_points[0,:], self.control_points[1,:], 'ro',self.control_points[0,:], self.control_points[1,:], 'r', s[:,0],s[:,1])
        plt.axis([0, 10, 0, 10])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    def __repr__(self):
        return 'Spline'

def eval_basis(grid, j):
    control_points = np.zeros((len(grid)-3,2))
    control_points[j] = 1
    control_points.T
    s_temp = Spline(grid,control_points)
    s_temp.plot(100)
