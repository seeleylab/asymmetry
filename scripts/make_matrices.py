import os
import numpy as np


# Make 165 HC 246 node mean matrix
with open('/data/mridata/jdeng/tools/asymmetry/data/165_wmap_FC_HC_paths.txt', 'r') as fin:
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

#####################################################################################################
import os
import numpy as np


# Make individual 246 node matrices for all 165 HCs
with open('/data/mridata/jdeng/tools/asymmetry/data/165_wmap_FC_HC_paths.txt', 'r') as fin:
    hc_165 = [path.strip() for path in fin.readlines()]
    
for path in hc_165:
    matrix_273regions_path = os.path.join(path, 'processedfmri_TRCNnSFmDI/matrix/fc_mat_273.txt')
    matrix_273regions_data = np.loadtxt(matrix_273regions_path)
    matrix_246regions_data = matrix_273regions_data[:246,:246]
    np.savetxt(os.path.join(path, 'processedfmri_TRCNnSFmDI/matrix/fc_mat_246.txt'), matrix_246regions_data)
    print 'Matrix created for {}'.format(path)
    