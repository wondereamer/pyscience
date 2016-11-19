import numpy as np
import math
from numpy import linalg as LA
from scipy.optimize import fsolve
# -------------Matrix Related Functions----------------------------
def egiens(matrix_):
    matrix = np.zeros((len(matrix_),len(matrix_)), int)
    for i, line in enumerate(matrix_):
        for j, item in enumerate(line):
           matrix[i][j] = item; 
    w, v = LA.eig(matrix)
    print "egiens:" 
    print w
    return w


def angle_vector(x, y):
    ''' Computing angle based on coordinate ''' 
    t = math.degrees(math.atan2(y,x))
    return t

# -------------Advanced Mathematics----------------------------------

def equation(r):
    x, y, z = tuple(r)
    return [
        (x+0.00966)**2 + (y-0.267892)**2 + (z-1.197412)**2 - 0.09**2,
        (x+0.08347)**2 + (y-0.406319)**2 + (z-1.04607)**2 - 0.10855**2,
        x + 0.00966
    ]

#result = fsolve(equation, [1.0, 1.0, 1.0])



# -------------Probability-------------------------------------------
