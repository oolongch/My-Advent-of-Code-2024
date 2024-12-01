import unittest

import dayone_one as do


class ID_test_case(unittest.TestCase):
    def test_sum_differences(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]
        self.assertEqual(do.sum_total_difference(list_one, list_two), 11)


if __name__ == "__main__":
    unittest.main()
