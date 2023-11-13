import unittest
from math_quiz import rndmInt, rndmOperator, operation


class TestMathGame(unittest.TestCase):

    def test_rndmInt(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rndmInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rndmOperator(self):
        # Test if random operators are one of "+", "-" or "*"
        for _ in range(1000):
            operator = rndmOperator()
            self.assertIn(operator, ["+", "-", "*"])

    def test_operation(self):
        # Test if the merged operation, the operator and the solution of the calculation is correct
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 4, '-', '7 - 4', 3),
                (8, 3, '*', '8 * 3', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
