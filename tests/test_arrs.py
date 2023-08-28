import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -1), None)
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 2), 3)
        self.assertRaises(IndexError, arrs.get, [], 0, "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertIsNot(test_array := [1, 2, 3], arrs.my_slice(test_array))
        self.assertIsInstance(arrs.my_slice([]), list)
        self.assertEqual(arrs.my_slice([1, 2, 3], -100), [1, 2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([], 1, 3), [])
        self.assertEqual(arrs.my_slice(test_array := [1, 2, 3], -len(test_array) + 1), [2, 3])


if __name__ == "__main__":
    unittest.main()
