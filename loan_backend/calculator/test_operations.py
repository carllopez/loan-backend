from django.test import TestCase

from .operations import addition, subtract, multiplication, division, square_root, random_string


class TestOperations(TestCase):
    def test_addition(self):
        a = 90
        b = 10

        res = addition(a, b)
        self.assertEqual(res, 100)

        b = "wrong"

        res = addition(a, b)
        self.assertEqual(type(res), tuple)
        self.assertIsNone(res[0])

    def test_subtract(self):
        a = 90
        b = 10

        res = subtract(a, b)
        self.assertEqual(res, 80)

        b = "wrong"

        res = subtract(a, b)
        self.assertEqual(type(res), tuple)
        self.assertIsNone(res[0])

    def test_multiplication(self):
        a = 10
        b = 10

        res = multiplication(a, b)
        self.assertEqual(res, 100)

        b = "wrong"

        res = multiplication(a, b)
        self.assertEqual(type(res), tuple)
        self.assertIsNone(res[0])

    def test_division(self):
        a = 90
        b = 10

        res = division(a, b)
        self.assertEqual(res, 9)

        b = "wrong"

        res = division(a, b)
        self.assertEqual(type(res), tuple)
        self.assertIsNone(res[0])

    def test_square_root(self):
        a = 81

        res = square_root(a)
        self.assertEqual(res, 9)

        a = "wrong"

        res = square_root(a)
        self.assertEqual(type(res), tuple)
        self.assertIsNone(res[0])

    def test_random_string(self):
        res = random_string()
        self.assertEqual(type(res), str)
