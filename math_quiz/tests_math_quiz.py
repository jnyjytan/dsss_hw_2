import unittest
from math_quiz import get_random_integer, get_random_math_symbol, plus_minus_multiplication


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_math_symbol(self):
        # TODO there is something to be done
        self.assertIsInstance(get_random_math_symbol(),str)

        #pass

    def test_plus_minus_multiplication(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 2, '-', '3 - 2', 1 ),
                (5, 2, '*', '5 * 2', 10)
                #''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:

                    printed, result = plus_minus_multiplication(num1,num2,operator)
                    self.assertEqual(expected_problem, printed)
                    self.assertEqual(result, expected_answer)

        

if __name__ == "__main__":
    unittest.main()