from Tires.Octoprime import Octoprime
import unittest

class TestOctoprime(unittest.TestCase):
    def test_needs_service(self):
        result = Octoprime([0, 1, 1, 1])
        self.assertTrue(result.needs_service())
        result = Octoprime([0, .1, .9, .9])
        self.assertFalse(result.needs_service())

if __name__ -- '__main__':
    unittest.main()