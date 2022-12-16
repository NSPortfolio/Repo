from Engine.StermanEngine import StermanEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        result = StermanEngine(warning_light_on = True)
        self.assertTrue(result.needs_service())
        result = StermanEngine(warning_light_on = False)
        self.assertFalse(result.needs_service())

if __name__ -- '__main__':
    unittest.main()
