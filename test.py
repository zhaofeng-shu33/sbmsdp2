import unittest
from sbmsdp import sbm2, sdp2
from utility import get_ground_truth, compare

class TestGenerator(unittest.TestCase):
    def test_sbm(self):
        with self.assertRaises(ValueError):
            sbm2(50, 16, 4)
        with self.assertRaises(ValueError):
            sbm2(100, 3, 4)
        with self.assertRaises(ValueError):
            sbm2(101, 16, 4)

class TestSDP(unittest.TestCase):
    def test_sdp2(self):
        G = sbm2(100, 16, 4)
        results = sdp2(G)
        print(results)
        labels_true = get_ground_truth(G)
        self.assertAlmostEqual(compare(results, labels_true), 1.0)        


if __name__ == '__main__':
    unittest.main()