import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)


if __name__ == '__main__':
    unittest.main()
