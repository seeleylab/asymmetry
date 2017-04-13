import numpy as np


def one_index(matrix):
    x = matrix.shape[0]
    y = matrix.shape[1]
    one_indexed_matrix = np.zeros((x+1,y+1))
    one_indexed_matrix[1:,1:] = matrix
    return one_indexed_matrix

def LL(node, matrix):
    matrix = one_index(matrix)
    all_ipsi = np.arange(1, matrix.shape[0], 2)
    all_ipsi_except_self = all_ipsi[all_ipsi != node]
    return matrix[node, all_ipsi_except_self].sum()
    
def LR(node, matrix):
    matrix = one_index(matrix)
    all_contra = np.arange(2, matrix.shape[0], 2)
    all_contra_except_homotopic = all_contra[all_contra != node+1]
    return matrix[node, all_contra_except_homotopic].sum()
    
def RR(node, matrix):
    matrix = one_index(matrix)
    all_ipsi = np.arange(2, matrix.shape[0], 2)
    all_ipsi_except_self = all_ipsi[all_ipsi != node]
    return matrix[node, all_ipsi_except_self].sum()
    
def RL(node, matrix):
    matrix = one_index(matrix)
    all_contra = np.arange(1, matrix.shape[0], 2)
    all_contra_except_homotopic = all_contra[all_contra != node-1]
    return matrix[node, all_contra_except_homotopic].sum()
    