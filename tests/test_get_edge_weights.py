import unittest
import numpy as np
import numpy.testing as npt
from asymmetry.get_edge_weights import *

class TestData(unittest.TestCase):
    """Test input data.
    """

    def test_index_shift_of_matrix_from_zero_to_one_worked(self):
        npt.assert_equal(mx[1, 1], 0)
        npt.assert_almost_equal(mx[1, 2], 0.864082903664975)
        npt.assert_almost_equal(mx[27, 11], 0.572212758580463)

class TestGetIpsiEdgeWeights(unittest.TestCase):
    """Test get_ipsi_edge_weights function.
    """

    def test_get_ipsi_edge_weights_for_a_left_sided_node(self):
        node_1_ipsi_ew = get_ipsi_edge_weights(1)
        npt.assert_equal(len(node_1_ipsi_ew), 122)
        node_1_first_five_ipsi_ew = node_1_ipsi_ew[:5]
        npt.assert_almost_equal(node_1_first_five_ipsi_ew,
                                [0.709158648139153,
                                 0.662617932805789,
                                 0.643417301317752,
                                 0.69170960723321,
                                 0.774093362758112])
        node_1_last_five_ipsi_ew = node_1_ipsi_ew[-5:]
        npt.assert_almost_equal(node_1_last_five_ipsi_ew,
                                [0.439794368875201,
                                 0.462043371739233,
                                 0.445909896902388,
                                 0.392428981228604,
                                 0.444323775262963])

    def test_get_ipsi_edge_weights_for_a_right_sided_node(self):
        node_88_ipsi_ew = get_ipsi_edge_weights(88)
        npt.assert_equal(len(node_88_ipsi_ew), 122)
        node_88_first_five_ipsi_ew = node_88_ipsi_ew[:5]
        npt.assert_almost_equal(node_88_first_five_ipsi_ew,
                                [0.505350664074651,
                                 0.470174057253487,
                                 0.557578085174955,
                                 0.429655965028972,
                                 0.517850187631153])
        node_88_last_five_ipsi_ew = node_88_ipsi_ew[-5:]
        npt.assert_almost_equal(node_88_last_five_ipsi_ew,
                                [0.173511738247224,
                                 0.356209208364548,
                                 0.259733170697977,
                                 0.19841319103098,
                                 0.211100380701962])

class TestGetContraEdgeWeights(unittest.TestCase):
    """Test get_contra_edge_weights function.
    """
    
    def test_get_contra_edge_weights_for_a_left_sided_node(self):
        node_233_contra_ew = get_contra_edge_weights(233)
        npt.assert_equal(len(node_233_contra_ew), 123)
        node_233_first_five_contra_ew = node_233_contra_ew[:5]
        npt.assert_almost_equal(node_233_first_five_contra_ew,
                                [0.381856803921492,
                                 0.284843610294808,
                                 0.247648329015974,
                                 0.289485874642011,
                                 0.290504947776768])
        node_233_last_five_contra_ew = node_233_contra_ew[-5:]
        npt.assert_almost_equal(node_233_last_five_contra_ew,
                                [0.472340151892052,
                                 0.468716361109088,
                                 0.362880932421908,
                                 0.300590978355714,
                                 0.606897363291253])
    
    def test_get_contra_edge_weights_for_a_right_sided_node(self):
        node_180_contra_ew = get_contra_edge_weights(180)
        npt.assert_equal(len(node_180_contra_ew), 123)
        node_180_first_five_contra_ew = node_180_contra_ew[:5]
        npt.assert_almost_equal(node_180_first_five_contra_ew,
                                [0.63850418086549,
                                 0.494321729162706,
                                 0.449049432629588,
                                 0.45249119924731,
                                 0.524850129619764])
        node_180_last_five_contra_ew = node_180_contra_ew[-5:]
        npt.assert_almost_equal(node_180_last_five_contra_ew,
                                [0.418871089939136,
                                 0.48028854293471,
                                 0.430336391376886,
                                 0.356544093862028,
                                 0.513800557356093])

class TestGetNodePairs(unittest.TestCase):
    """Test get_ipsi_node_pairs and get_contra_node_pairs functions.
    """
    
    def test_get_ipsi_node_pairs(self):
        node_1_ipsi_node_pairs = get_ipsi_node_pairs(1)
        npt.assert_equal(len(node_1_ipsi_node_pairs), 122)
        node_1_first_and_last_five_ipsi_node_pairs = node_1_ipsi_node_pairs[:5] + \
                                                    node_1_ipsi_node_pairs[-5:]
        npt.assert_equal(node_1_first_and_last_five_ipsi_node_pairs,
                                ['1-3', '1-5', '1-7', '1-9', '1-11',
                                 '1-237', '1-239', '1-241', '1-243', '1-245'])
        
    def test_get_contra_node_pairs(self):
        node_13_contra_node_pairs = get_contra_node_pairs(13)
        npt.assert_equal(len(node_13_contra_node_pairs), 123)
        node_13_first_and_last_five_contra_node_pairs = node_13_contra_node_pairs[:5] + \
                                                        node_13_contra_node_pairs[-5:]
        npt.assert_equal(node_13_first_and_last_five_contra_node_pairs,
                         ['13-2', '13-4', '13-6', '13-8', '13-10',
                          '13-238', '13-240', '13-242', '13-244', '13-246'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
