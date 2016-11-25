import os
import numpy as np

# Get mean matrix
with open('/data/mridata/jdeng/tools/asymmetry/165_wmap_FC_HC_paths.txt', 'r') as fin:
    hc_165 = [path.strip() for path in fin.readlines()]

sum_brainnetome_matrix_165hc_273regions = np.zeros((273, 273))

for p in hc_165:
    matrix_273regions_path = os.path.join(p, 'processedfmri_TRCNnSFmDI/matrix/fc_mat_273.txt')
    matrix_273regions_data = np.loadtxt(matrix_273regions_path)
    sum_brainnetome_matrix_165hc_273regions += matrix_273regions_data

mean_brainnetome_matrix_165hc_273regions = sum_brainnetome_matrix_165hc_273regions / 165.0

# Trim mean matrix
mean_brainnetome_matrix_165hc_246regions = mean_brainnetome_matrix_165hc_273regions[:246, :246]

np.savetxt('/data/mridata/ejkim/EJ/AN_Project/FC/mean_brainnetome_matrix_165hc_246regions.txt',
           mean_brainnetome_matrix_165hc_246regions)
