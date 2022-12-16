from Tires.Carrigan import Carrigan
import unittest

class TestCarrigan(unittest.TestCase):
    def test_needs_service(self):
        result = Carrigan([0, .1, .9, .8])
        self.assertTrue(result.needs_service())
        result = Carrigan([0, .1, .9, .9])
        self.assertTrue(result.needs_service())
        result = Carrigan([0, .1, .9, .9])
        self.assertFalse(result.needs_service())

if __name__ -- '__main__':
    unittest.main()