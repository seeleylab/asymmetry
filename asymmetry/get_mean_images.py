import nibabel as nib
import numpy as np


syndromes = ['AD', 'bvFTD', 'CBS', 'PCA', 'svPPA', 'naPPA', 'lvPPA', 'PSP', 'GRNP', 'GRNS']

for s in syndromes:
    smwc1_path_file = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps_raw/%s_smwc1_paths.txt' % s
    
    with open(smwc1_path_file, 'r') as fin:
        smwc1_paths = [path.strip() for path in fin.readlines()]

    sum_img_data = np.zeros((121, 145, 121))
    
    for path in smwc1_paths:
        smwc1_img_data = nib.load(path).get_data()
        sum_img_data += smwc1_img_data
        
    mean_img_data = sum_img_data / len(smwc1_paths)
    
    mean_img_path = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps_raw/%s_raw_mean.nii' % s
    mean_img_affine = nib.load(path).affine
    img = nib.Nifti1Image(mean_img_data, mean_img_affine)
    img.to_filename(mean_img_path)
    print s