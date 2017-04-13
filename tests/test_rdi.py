import unittest
import numpy.testing as npt
import asymmetry.rdi as rdi
import numpy as np


TEST_MAT = np.array([[1,2,3,4,5],
                     [2,1,2,3,4],
                     [3,2,1,2,3],
                     [4,3,2,1,2],
                     [5,4,3,2,1]])          

class Test_RDI(unittest.TestCase):

    def test_one_index(self):
        one_indexed_mat = rdi.one_index(TEST_MAT)
        
        npt.assert_array_equal(one_indexed_mat,
                               np.array([[0,0,0,0,0,0],
                                         [0,1,2,3,4,5],
                                         [0,2,1,2,3,4],
                                         [0,3,2,1,2,3],
                                         [0,4,3,2,1,2],
                                         [0,5,4,3,2,1]]))
        
    def test_LL(self):
        LL_value = rdi.LL(1, TEST_MAT)
        self.assertEqual(LL_value, 8)
        
    def test_LR(self):
        LR_value = rdi.LR(1, TEST_MAT)
        self.assertEqual(LR_value, 4)
    
    def test_RR(self):
        RR_value = rdi.RR(2, TEST_MAT)
        self.assertEqual(RR_value, 3)
    
    def test_RL(self):
        RL_value = rdi.RL(2, TEST_MAT)
        self.assertEqual(RL_value, 6)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    