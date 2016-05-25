import unittest
from zadanie import *


class TestClass(unittest.TestCase):
    def setUp(self):
        self.prime = Primary(5)
        self.pascal = Pascal_Triangle(5)
        self.monte = montecarlo()
        self.monte_use = monte_use()

    def test_prime_init(self):
        self.assertEqual(5, self.prime.number)

    def test_prime_is_prime(self):
        self.assertEqual(True, self.prime.isPrime(7))

    def test_prime_next(self):
        self.assertEqual(2, self.prime.__next__())

    def test_pascal_init(self):
        self.assertEqual(5, self.pascal.rows)

    def test_pascal_next(self):
        #ta funkcja jest celowo z bledem, tak sie dowiedzialem od kolegi
        self.assertEqual([1.0], self.test_pascal_next())

    def test_montecarlo(self):
        self.assertEqual(0.15804498821804103, self.monte.__next__())

    def test_monte_use(self):
        self.assertEqual(sin(0.3), self.monte_use.func(0.3))

if __name__ == '__main__':
    unittest.main()
