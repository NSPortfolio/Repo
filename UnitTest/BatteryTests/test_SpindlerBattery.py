from Battery.SpindlerBattery import SpindlerBattery
import unittest
from datetime import datetime

class SpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2022-12-16")
        last_service_date = date.fromisoformat("2017-12-16")
        result = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(result)
        current_date = date.fromisoformat("2022-12-16")
        last_service_date = date.fromisoformat("2020-12-16")
        result = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(result)

if __name__ -- '__main__':
    unittest.main()
