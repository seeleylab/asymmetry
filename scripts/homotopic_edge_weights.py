#!/usr/bin/env python
import numpy as np
import os
import pandas as pd


# Calculate homotopic edge weights
with open('/data/mridata/jdeng/tools/asymmetry/data/165_wmap_FC_HC_paths.txt', 'r') as fin:
    hcs = [path.strip() for path in fin.readlines()]
    
regions = np.arange(1,247,2) - 1                    # (1,3,5,7,...,243,245) - 1
homotopic_regions = np.arange(2,247,2) - 1          # (2,4,6,8,...,244,246) - 1
homotopic_pairs = ['{}-{}'.format(r+1,hr+1) for r,hr in zip(regions, homotopic_regions)] # 1-2, 3-4, 5-6,...243-244, 245-246
homotopic_edge_weights_mat = np.zeros((165,123))

for row_no,hc in enumerate(hcs):
    matrix_246 = np.loadtxt(os.path.join(hc, 'processedfmri_TRCNnSFmDI/matrix/fc_mat_246.txt'))
    homotopic_edge_weights = []
    
    for r,hr in zip(regions, homotopic_regions):
        homotopic_edge_weights.append(matrix_246[r,hr])
    
    homotopic_edge_weights_mat[row_no,:] = homotopic_edge_weights

# Save to a spreadsheet
writer = pd.ExcelWriter('/data/mridata/jdeng/tools/asymmetry/data/165hc_246node_homotopic_edge_weights.xlsx')
df = pd.DataFrame(homotopic_edge_weights_mat, index=hcs, columns=homotopic_pairs)
df.to_excel(writer)
writer.save()
