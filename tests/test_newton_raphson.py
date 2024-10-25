# test_newton_raphson.py

import unittest
from src.newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):

    def test_square_root(self):
        f = lambda x: x**2 - 9
        f_prime = lambda x: 2 * x
        root = newton_raphson(f, f_prime, x0=3)
        self.assertAlmostEqual(root, 3, places=5)

    def test_zero_derivative(self):
        f = lambda x: x**3 - 2 * x + 2
        f_prime = lambda x: 3 * x**2 - 2
        with self.assertRaises(ValueError):
            newton_raphson(f, f_prime, x0=0)

if __name__ == "__main__":
    unittest.main()
