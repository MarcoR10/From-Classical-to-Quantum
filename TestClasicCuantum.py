import unittest
import ClasicCuantum as cc


class MyTestCase(unittest.TestCase):
    def test_canicas(self):
        self.assertEqual(cc.canicas(
            [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0],
             [1, 0, 0, 0, 0, 0]], [6, 0, 3, 5, 3, 8], 99), [0, 11, 8, 3, 3, 0])

    def test_probabilistico(self):
        self.assertEqual(cc.propabilistico([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 3], [2 / 3, 1 / 3, 0]], [1, 0, 0], 0), [0.0, 0.3333333333333333, 0.6666666666666666])

    def test_cuantico(self):
        self.assertEqual(cc.cuantico([[(0, 1), (1, 0)], [(0, 1), (1, 0)]], [(1, 0), (1, 1)], 0), [(1, 2), (1, 2)])


if __name__ == '__main__':
    unittest.main()
