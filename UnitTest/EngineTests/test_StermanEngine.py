from Engine.StermanEngine import StermanEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        result = StermanEngine(warning_light_on = True)
        self.assertTrue(result)
        result = StermanEngine(warning_light_on = False)
        self.assertFalse(result)

if __name__ -- '__main__':
    unittest.main()