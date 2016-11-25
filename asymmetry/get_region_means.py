import numpy as np
import nibabel as nib

atlas_path = '/data/mridata/ejkim/BrainnetomeALL_v1_Beta_20160106 2/Atlas/subregion/all_subregions_15mm.nii'
atlas_data = nib.load(atlas_path).get_data()
atlas_data_1d = atlas_data.flatten()

region_indices = {i: np.where(atlas_data_1d == i)[0] for i in range(1, 247)}


def get_region_means_from_merged_mean_images(syndrome):

    outfile_path = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps/%s_merged_mean_region_means.txt' % syndrome

    mean_atrophy_map_path = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps/%s_merged_mean.nii' % syndrome
    mean_atrophy_map_data = nib.load(mean_atrophy_map_path).get_data()
    mean_atrophy_map_data_1d = mean_atrophy_map_data.flatten()

    for i in range(1, 247):
        indices = region_indices[i]
        region_values = mean_atrophy_map_data_1d[indices]
        region_mean = region_values.mean()
        region_mean_value = region_mean.tolist()

        with open(outfile_path, 'a') as fout:
            fout.write(str(round(region_mean_value, 2)))
            fout.write('\n')

def get_region_means_from_merged_sum_images(syndrome):

    outfile_path = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps/%s_merged_sum_region_means.txt' % syndrome

    mean_atrophy_map_path = '/data/mridata/ejkim/EJ/AN_Project/VBM/unionmaps/%s_merged_sum.nii' % syndrome
    mean_atrophy_map_data = nib.load(mean_atrophy_map_path).get_data()
    mean_atrophy_map_data_1d = mean_atrophy_map_data.flatten()

    for i in range(1, 247):
        indices = region_indices[i]
        region_values = mean_atrophy_map_data_1d[indices]
        region_mean = region_values.mean()
        region_mean_value = region_mean.tolist()

        with open(outfile_path, 'a') as fout:
            fout.write(str(round(region_mean_value, 2)))
            fout.write('\n')

syndromes = ['AD', 'bvFTD', 'CBS', 'GRNS', 'lvPPA', 'naPPA', 'PCA', 'PSPS', 'svPPA', 'WG']

if __name__ == '__main__':
    for s in syndromes:
        get_region_means_from_merged_mean_images(s)
        get_region_means_from_merged_sum_images(s)
