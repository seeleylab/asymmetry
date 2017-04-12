import nibabel as nib
import os

syndromes = ['AD', 'bvFTD', 'CBS', 'GRNS', 'lvPPA', 'naPPA', 'PCA', 'PSPS', 'svPPA', 'WG']

for s in syndromes:
    LA_atrophy_map_path = os.path.join('/data/mridata/ejkim/EJ/AN_Project/VBM', s+'_LA', 'spmT_0001.nii')
    RA_atrophy_map_path = os.path.join('/data/mridata/ejkim/EJ/AN_Project/VBM', s+'_RA', 'spmT_0001.nii')
    SG_atrophy_map_path = os.path.join('/data/mridata/ejkim/EJ/AN_Project/VBM', s+'_SG', 'spmT_0001.nii')

    LA_atrophy_map_data = nib.load(LA_atrophy_map_path).get_data()
    RA_atrophy_map_data = nib.load(RA_atrophy_map_path).get_data()
    SG_atrophy_map_data = nib.load(SG_atrophy_map_path).get_data()

    sum_atrophy_map_path = os.path.join('/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps', s+'_merged_sum.nii')
    sum_atrophy_map_data = LA_atrophy_map_data + RA_atrophy_map_data + SG_atrophy_map_data
    sum_atrophy_map_affine = nib.load(LA_atrophy_map_path).affine
    img = nib.Nifti1Image(sum_atrophy_map_data, sum_atrophy_map_affine)
    img.to_filename(sum_atrophy_map_path)
