#!/usr/bin/env python
"""Calculate Euclidean distance between all 123 homotopic region pairs of
246-region Brainnetome atlas.
"""
import numpy as np
from nipype.algorithms.metrics import Distance
import os
import pandas as pd


ATLAS_DIR = '/data/mridata/jbrown/brains/brainnetome_suit_comb'

regions = np.arange(1,247,2)                    # (1,3,5,7,...,243,245)
homotopic_regions = np.arange(2,247,2)          # (2,4,6,8,...,244,246)
homotopic_pairs = ['{}-{}'.format(r,hr) for r,hr in zip(regions, homotopic_regions)] # 1-2, 3-4, 5-6,...243-244, 245-246

euc_distances = []

for r,hr in zip(regions, homotopic_regions):
    euc = Distance()
    euc.inputs.volume1 = os.path.join(ATLAS_DIR, 'vol_{}.nii'.format(r))
    euc.inputs.volume2 = os.path.join(ATLAS_DIR, 'vol_{}.nii'.format(hr))
    euc.inputs.method = 'eucl_cog_jd'
    out = euc.run()
    euc_distances.append(out.outputs.distance)

euc_distances = np.array(euc_distances).reshape(1,-1)

# Save to a spreadsheet
writer = pd.ExcelWriter('/data/mridata/jdeng/tools/asymmetry/data/246node_euclidean_distances.xlsx')
df = pd.DataFrame(euc_distances, columns=homotopic_pairs)
df.to_excel(writer, index=False)
writer.save()
