import numpy as np
import pandas as pd


### Create writer object ###
writer = pd.ExcelWriter('/data/mridata/jdeng/tools/asymmetry/data/brainnetome_regional_ai.xlsx')

# column names
with open('/data/mridata/ejkim/BrainnetomeALL_v1_Beta_20160106 2/Testatlas.txt', 'r') as fin:
    regions_246 = [item.split()[1] for item in fin.readlines()]
regions_123 = [regions_246[i].replace('_R_', '').replace('_L_', '') for i in range(1,246,2)]

# row names
with open('/data/mridata/jdeng/tools/asymmetry/asymmetry/subjs_439.txt', 'r') as fin:
    subjs = [line.strip() for line in fin.readlines()]

### AI spreadsheet ###
all_matrix = np.loadtxt('/data/mridata/jdeng/tools/asymmetry/data/brainnetome_regional_wscores.txt')
left_regions = np.arange(1,247,2) - 1
right_regions = np.arange(2,247,2) - 1
left_matrix = all_matrix[:,left_regions]
right_matrix = all_matrix[:,right_regions]

ai = np.abs( (left_matrix - right_matrix) / (left_matrix + right_matrix) )

df = pd.DataFrame(ai, index=subjs, columns=regions_123)
df.to_excel(writer, sheet_name='AI')

### wscore spreadsheet ###
wscores = np.loadtxt('/data/mridata/jdeng/tools/asymmetry/data/brainnetome_regional_wscores.txt')

df = pd.DataFrame(wscores, index=subjs, columns=regions_246[:-1])  # get rid of last label (Spheric_ROI)
df.to_excel(writer, sheet_name='wscores')

### Save spreadsheet ###
writer.save()
