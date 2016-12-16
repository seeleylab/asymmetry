import nibabel as nib
import numpy as np


def pathread(paths_file):
    with open(paths_file, 'r') as fin:
        img_paths = [path.strip() for path in fin.readlines()]
        return img_paths

def imgmean(infile_list, outfile):
    presumed_img_dims = nib.load(infile_list[0]).shape
    sum_img_data = np.zeros(presumed_img_dims)
    
    for path in infile_list:
        img_data = nib.load(path).get_data()
        try:
            sum_img_data += img_data
        except ValueError:
            print 'Your input images cannot be averaged because they have '
            'different dimensions!'
            
    mean_img_data = sum_img_data / len(infile_list)
    mean_img_path = outfile
    mean_img_affine = nib.load(path).affine
    img = nib.Nifti1Image(mean_img_data, mean_img_affine)
    img.to_filename(mean_img_path)
