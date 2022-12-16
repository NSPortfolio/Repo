from Engine.CapuletEngine import CapuletEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        result = CapuletEngine('70000', '500')
        self.assertTrue(result)
        result = CapuletEngine('40000', '30000')
        self.assertFalse(result)

if __name__ -- '__main__':
    unittest.main()