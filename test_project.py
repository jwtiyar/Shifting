import unittest

import self

from project import fri_Remove, day_inWeek

# FILE: test_project.py

class TestProjectFunctions(unittest.TestCase):


    def test_fri_Remove(self):
        # Test for a known Friday
        self.assertTrue(fri_Remove(2023, 10, 6))  # October 6, 2023 is a Friday
        # Test for a known non-Friday
        self.assertFalse(fri_Remove(2023, 10, 5))  # October 5, 2023 is a Thursday
        # Test for an invalid date
        self.assertFalse(fri_Remove(2023, 2, 30))  # February 30, 2023 is an invalid date

    def test_day_inWeek(self):
        cells = ["code", 10, 2023] + [0] * 31
        # Test for fingerprint 2 on a Monday
        result = day_inWeek(2023, 10, 2, 2, cells.copy())  # October 2, 2023 is a Monday
        self.assertEqual(result[4], "x")
        # Test for fingerprint 3 on a Tuesday
        result = day_inWeek(2023, 10, 3, 3, cells.copy())  # October 3, 2023 is a Tuesday
        self.assertEqual(result[5], "x")
        # Test for fingerprint 2 on a Friday
        result = day_inWeek(2023, 10, 6, 2, cells.copy())  # October 6, 2023 is a Friday
        self.assertEqual(result[8], "x")
        # Test for fingerprint 3 on a Friday
        result = day_inWeek(2023, 10, 6, 3, cells.copy())  # October 6, 2023 is a Friday
        self.assertEqual(result[8], "x")

if __name__ == '__main__':
    unittest.main()
