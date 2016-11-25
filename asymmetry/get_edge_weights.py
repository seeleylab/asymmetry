import os
import numpy as np
import csv
from itertools import izip_longest

mx_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data',
'mean_brainnetome_matrix_165hc_246regions.txt'))
mx = np.loadtxt(mx_path)
empty_array_of_246 = np.zeros((246))
mx = np.vstack((empty_array_of_246, mx))
empty_array_of_247 = np.zeros((247, 1))
mx = np.hstack((empty_array_of_247, mx))

left_side_nodes = np.arange(1, 247, 2)     # 1, 3, 5, 7, ..., 245
right_side_nodes = np.arange(2, 247, 2)    # 2, 4, 6, 8, ..., 246

def get_ipsi_edge_weights(node_number):
    if node_number % 2 != 0:
        # if node_number is odd (left-sided)
        ipsi_nodes = left_side_nodes
    else:
        # if node_number is even (right-sided)
        ipsi_nodes = right_side_nodes

    ipsi_nodes_without_self = set(ipsi_nodes) - {node_number}
    ipsi_nodes_without_self = np.array(list(ipsi_nodes_without_self))
    ipsi_edge_weights = [mx[node_number, ipsi_node_number] for
                         ipsi_node_number in ipsi_nodes_without_self]
    return ipsi_edge_weights

def get_contra_edge_weights(node_number):
    if node_number % 2 != 0:
        # if node_number is odd (left-sided)
        contra_nodes = right_side_nodes
    else:
        # if node_number is even (right-sided)
        contra_nodes = left_side_nodes
        
    contra_edge_weights = [mx[node_number, contra_node_number] for
                           contra_node_number in contra_nodes]
    return contra_edge_weights

def get_ipsi_node_pairs(node_number):
    if node_number % 2 != 0:
        # if node_number is odd (left-sided)
        ipsi_nodes = left_side_nodes
    else:
        # if node_number is even (right-sided)
        ipsi_nodes = right_side_nodes

    ipsi_nodes_without_self = set(ipsi_nodes) - {node_number}
    ipsi_nodes_without_self = np.array(list(ipsi_nodes_without_self))
    ipsi_node_pairs = ['%s-%s' % (node_number, ipsi_node_number) for
                       ipsi_node_number in ipsi_nodes_without_self]
    return ipsi_node_pairs

def get_contra_node_pairs(node_number):
    if node_number % 2 != 0:
        # if node_number is odd (left-sided)
        contra_nodes = right_side_nodes
    else:
        # if node_number is even (right-sided)
        contra_nodes = left_side_nodes
        
    contra_node_pairs = ['%s-%s' % (node_number, contra_node_number) for
                         contra_node_number in contra_nodes]
    return contra_node_pairs


if __name__ == '__main__':
    results = []
    
    for i in np.arange(1,247):
        results.append(get_ipsi_node_pairs(i))
        results.append(get_ipsi_edge_weights(i))
        results.append(get_contra_node_pairs(i))
        results.append(get_contra_edge_weights(i))
        
    with open('/data/mridata/ejkim/EJ/AN_Project/FC/test.csv', 'a') as fout:
        writer = csv.writer(fout)
        for values in izip_longest(*results):
            writer.writerow(values)
