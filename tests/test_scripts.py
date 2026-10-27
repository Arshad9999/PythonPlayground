import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run_script(name, user_input=""):
    return subprocess.run(
        [sys.executable, str(ROOT / name)], input=user_input,
        text=True, capture_output=True, timeout=10, check=True,
    ).stdout


class ScriptTests(unittest.TestCase):
    def test_armstrong_numbers_through_500(self):
        output = run_script("ArmstrongNumber.py")
        self.assertEqual(output.strip(), "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407")

    def test_factorial_zero_and_five(self):
        self.assertIn("is :  1", run_script("FactorialFunction.py", "0\n"))
        self.assertIn("is :  120", run_script("FactorialFunction.py", "5\n"))

    def test_fibonacci_prefix(self):
        self.assertTrue(run_script("FibonacciSeries.py", "7\n").strip().endswith("0 1 1 2 3 5 8"))

    def test_prime_interval_excludes_zero_and_one(self):
        output = run_script("PrimeNumbers.py", "0\n3\n")
        self.assertIn("2  is a Prime Number", output)
        self.assertIn("3  is a Prime Number", output)
        self.assertNotIn("0  is a Prime Number", output)
        self.assertNotIn("1  is a Prime Number", output)


if __name__ == "__main__":
    unittest.main()
