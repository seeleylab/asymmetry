import unittest
import os
import numpy as np
import nibabel as nib
import glob
import numpy.testing as npt
import asymmetry.get_mean_images as gmi

class TestPathread(unittest.TestCase):
    
    test_file = os.path.join(os.path.dirname(__file__), 'fake_paths.txt')
    
    def setUp(self):
        paths = ['/data5/patientNIC/1234/1234_20010101/rsfmri',
                     '  /data5/patientNIC/5678/5678_20020202/rsfmri',
                     '/data5/patientNIC/9101/9101_20030303/rsfmri  ']
        
        with open(TestPathread.test_file, 'w') as fout:
            for item in paths:
                fout.write(item)
                fout.write('\n')
    
    def tearDown(self):
        os.remove(TestPathread.test_file)
    
    def test_pathread(self):
        file_contents = gmi.pathread(TestPathread.test_file)
        self.assertEqual(file_contents, ['/data5/patientNIC/1234/1234_20010101/rsfmri',
                                         '/data5/patientNIC/5678/5678_20020202/rsfmri',
                                         '/data5/patientNIC/9101/9101_20030303/rsfmri'])
        
class TestImgMean(unittest.TestCase):
    
    def setUp(self):
        for i in range(1,4):
            fake_img = np.random.rand(10,10,10)
            fake_img_path = os.path.join(os.path.dirname(__file__), 'fake_image%d.nii' % i)
            fake_img_affine = np.array([[-1.5, 0., 0., 90.],
                                        [0., 1.5, 0., -126.],
                                        [0., 0., 1.5, -72.],
                                        [0., 0., 0., 1.]])
            img = nib.Nifti1Image(fake_img, fake_img_affine)
            img.to_filename(fake_img_path)
    
    def tearDown(self):
        outputs = glob.glob(os.path.join(os.path.dirname(__file__), 'fake_image*.nii'))
        for f in outputs:
            os.remove(f)
        
    def test_imgmean(self):
        fake_img_list = glob.glob(os.path.join(os.path.dirname(__file__), 'fake_image*.nii'))
        gmi.imgmean(fake_img_list, os.path.join(os.path.dirname(__file__), 'fake_image_mean.nii'))
        
        fake_image_mean = nib.load(os.path.join(os.path.dirname(__file__), 'fake_image_mean.nii')).get_data()
        fake_image1 = nib.load(os.path.join(os.path.dirname(__file__), 'fake_image1.nii')).get_data()
        fake_image2 = nib.load(os.path.join(os.path.dirname(__file__), 'fake_image2.nii')).get_data()
        fake_image3 = nib.load(os.path.join(os.path.dirname(__file__), 'fake_image3.nii')).get_data()
        for idx,mean_value in enumerate(fake_image_mean.flatten()):
            npt.assert_allclose(mean_value, (fake_image1.flatten()[idx] +
                                             fake_image2.flatten()[idx] +
                                             fake_image3.flatten()[idx]) / 3.)

if __name__ == '__main__':
    unittest.main(verbosity=2)