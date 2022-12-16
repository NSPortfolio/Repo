from Battery.NubbinBattery import NubbinBattery
import unittest

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        result = NubbinBattery('2022-12-16', '2017-12-16')
        self.assertTrue(result)
        result = NubbinBattery('2022-12-16', '2019-12-16')
        self.assertFalse(result)

if __name__ -- '__main__':
    unittest.main()