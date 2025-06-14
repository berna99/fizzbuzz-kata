import unittest
from fizz_buzz import FizzBuzz  


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(FizzBuzz.find_string_to_print(3), "Fizz")
    
    def test_buzz(self):
        self.assertEqual(FizzBuzz.find_string_to_print(5), "Buzz")
    
    def test_fizzbuzz(self):
        self.assertEqual(FizzBuzz.find_string_to_print(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()


    