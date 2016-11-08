import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np
import math
import copy
from numpy import linalg as LA
# -------------Matrix Related Functions----------------------------
def egiens(matrix_):
    '''docstring for eigens''' 
    matrix = np.zeros((len(matrix_),len(matrix_)), int)
    for i, line in enumerate(matrix_):
        for j, item in enumerate(line):
           matrix[i][j] = item; 
    w, v = LA.eig(matrix)
    print "egiens:" 
    print w
    return w


def angle_vector(x, y):
    '''docstring for angle_vector''' 
    t = math.degrees(math.atan2(y,x))
    return t
# -------------------------------------------------------------------



def discrete_differential(y_list):
    '''docstring for discrete_differential''' 
    t = copy.deepcopy(y_list)
    for i,elem in enumerate(y_list[1:len(y_list)]):
        y_list[i+1] -= t[i]
    y_list[0] = 0
    return y_list


def previous_sum(vals):
    '''docstring for revious_sum''' 
    for i,elem in enumerate(vals[1:len(vals)]):
        vals[i+1] += vals[i]
    return vals


