import nipype.interfaces.fsl as fsl


DEFAULTS = {
    'mask': False
}

def fslxmean(images, output, mask=DEFAULTS['mask']):
    # fslmerge
    fsl.Merge(inputs=images, dimension='t', output_type='NIFTI_GZ', merged_file='')
    # fslmaths -Tmean
    
    if mask:
        # fslmaths -mas
