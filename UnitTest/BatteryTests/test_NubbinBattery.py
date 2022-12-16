from Battery.NubbinBattery import NubbinBattery
import unittest
from datetime import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2022-12-16")
        last_service_date = date.fromisoformat("2017-12-16")
        result = NubbinBattery(current_date, last_service_date)
        self.assertTrue(result.needs_service())
        current_date = date.fromisoformat("2022-12-16")
        last_service_date = date.fromisoformat("2020-12-16")
        result = NubbinBattery(current_date, last_service_date)
        self.assertFalse(result.needs_service())

if __name__ -- '__main__':
    unittest.main()
