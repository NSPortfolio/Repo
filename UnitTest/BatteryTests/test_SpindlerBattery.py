from Battery.SpindlerBattery import SpindlerBattery
import unittest

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        result = SpindlerBattery('2022-12-16', '2018-12-16')
        self.assertTrue(result)
        result = SpindlerBattery('2022-12-16', '2021-12-16')
        self.assertFalse(result)

if __name__ -- '__main__':
    unittest.main()