from Engine.CapuletEngine import CapuletEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        result = CapuletEngine('70000', '500')
        self.assertTrue(result.needs_service())
        result = CapuletEngine('40000', '30000')
        self.assertFalse(result.needs_service())

if __name__ -- '__main__':
    unittest.main()
