import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt

class Spline:
    '''A spline object contains the function that are needed to evaluate an open B-spline.
        There are only two necessary inputs:
        Control points - these define the structure you want to recreate
        Grid - this is a vector of the u:s
    '''
        
    def __init__(self, grid, control_points):
        self.grid = grid;
        self.control_points = control_points
            
    def __call__(self, u):
        '''Calculates the spline value for the grid point u'''
        return self._blossom(u)

    def _find_control_points(self, u):
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

    def _alpha(self, u, i1, i2):
        #Knots corresponds to the u:s inside a blossom pair
        #d[u; uI-1; uI] = alpha(u)d[uI-2; uI-1; uI] + (1 (u))d[uI-1; uI; uI+1]
        I = self._find_interval(u)
        u_right_most_knot = self.grid[I + i2]
        u_left_most_knot = self.grid[I + i1]
        alpha = (u_right_most_knot - u)/(u_right_most_knot - u_left_most_knot)
        return alpha

    def _blossom(self, u):
        if(u >= self.grid[-3] or u <= self.grid[2]): # check input
            raise ValueError("Invalid input. The spline is only defined on [u_2 u_k-2]")
        d = np.transpose(self._find_control_points(u)).tolist()
        index_order = [(-2, 1), (-1, 2), (0, 3), (-1, 1), (0, 2), (0, 1)]
        index_counter = 0
        while len(d) > 1:
            d2 = []
            for i in range(len(d) - 1):
                i1 = index_order[index_counter][0]
                i2 = index_order[index_counter][1]
                index_counter += 1
                merge_x = self._alpha(u, i1, i2)*d[i][0] + (1 - self._alpha(u, i1, i2))*d[i + 1][0]
                merge_y = self._alpha(u, i1, i2)*d[i][1] + (1 - self._alpha(u, i1, i2))*d[i + 1][1]
                d2.append([merge_x, merge_y])
            d = d2
        return d
        
    def plot(self, nbr_of_points = 100):
        '''Plots the open spline.'''
        u = np.linspace(self.grid[2], self.grid[-3], nbr_of_points) # u2:uK-2
        u = u[1:-1] # remove end-points
        s = np.zeros((nbr_of_points-2,2))
        for j in range(nbr_of_points-2):
            s[j,0] = self(u[j])[0][0]
            s[j,1] = self(u[j])[0][1] 
        plt.plot(self.control_points[0,:], self.control_points[1,:], 
                 color = 'r', 
                 ls = '--', 
                 marker = "o")    
        plt.plot(s[:,0],s[:,1], 'blue')        
        plt.axis([min(self.grid), max(self.grid), 
                  min(self.control_points[1][:]), max(self.control_points[1][:])])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    def _div(self, num, denom):
        if num == 0  and denom == 0:
            return 0
        else:
            return num/denom 
 

    def _N_base(self, u, i, k = 3):
        if k == 0:
            if u >= self.grid[i - 1] and u < self.grid[i]:
                return 1
            else:
                return 0
        a = self._N_base(u, i, k - 1)*self._div((u - self.grid[i - 1]),(self.grid[i + k - 1] - self.grid[i - 1]))
        b = self._N_base(u, i + 1, k - 1)*self._div((self.grid[i + k] - u),(self.grid[i + k] - self.grid[i]))
        return a + b

    def N(self, i, k = 3):
        def N(self,u):
            return self._N_base(u,i,k)
        return N
        
    def __repr__(self):
        return 'Class object: Spline'
    
               



'''
def eval_basis(grid, j):
    if j >  len(grid)-3:
        print("Invalid input")
        raise SystemExit
    control_points = np.zeros((len(grid)-2,2))
    control_points[j]= 1
    control_points = control_points.T
    s_temp = Spline(grid,control_points)
    print(s_temp.control_points)
    print(s_temp.grid)
    s_temp.plot(100)
'''
