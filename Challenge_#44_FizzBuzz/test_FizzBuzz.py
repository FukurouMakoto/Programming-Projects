import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3),'Fizz')
        self.assertEqual(FizzBuzz.FizzBuzz(5),'Buzz')
        self.assertEqual(FizzBuzz.FizzBuzz(15),'FizzBuzz')
        self.assertEqual(FizzBuzz.FizzBuzz(6),'Fizz')
        self.assertEqual(FizzBuzz.FizzBuzz(20),'Buzz')
        self.assertEqual(FizzBuzz.FizzBuzz(30),'FizzBuzz')
        self.assertEqual(FizzBuzz.FizzBuzz(9),'Fizz')
        self.assertEqual(FizzBuzz.FizzBuzz(25),'Buzz')
        self.assertEqual(FizzBuzz.FizzBuzz(45),'FizzBuzz')
        self.assertEqual(FizzBuzz.FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz.FizzBuzz(4), 4)
        self.assertEqual(FizzBuzz.FizzBuzz(44), 44)
        self.assertEqual(FizzBuzz.FizzBuzz(258),'Fizz')
        self.assertEqual(FizzBuzz.FizzBuzz(325),'Buzz')
        self.assertEqual(FizzBuzz.FizzBuzz(15555),'FizzBuzz')
        self.assertEqual(FizzBuzz.FizzBuzz(426),'Fizz')
        self.assertEqual(FizzBuzz.FizzBuzz(380),'Buzz')
        self.assertEqual(FizzBuzz.FizzBuzz(735),'FizzBuzz')
        self.assertEqual(FizzBuzz.FizzBuzz(86), 86)
        self.assertEqual(FizzBuzz.FizzBuzz(1246), 1246)
        self.assertEqual(FizzBuzz.FizzBuzz(75182), 75182)
        self.assertEqual(FizzBuzz.FizzBuzz(795824), 795824)
        self.assertEqual(FizzBuzz.FizzBuzz(7958114), 7958114)
    
    def test_improve_FizzBuzz(self):
        self.assertEqual(FizzBuzz.improve_FizzBuzz(3),'Fizz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(5),'Buzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(15),'FizzBuzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(6),'Fizz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(20),'Buzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(30),'FizzBuzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(9),'Fizz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(25),'Buzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(45),'FizzBuzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(4), 4)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(44), 44)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(258),'Fizz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(325),'Buzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(15555),'FizzBuzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(426),'Fizz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(380),'Buzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(735),'FizzBuzz')
        self.assertEqual(FizzBuzz.improve_FizzBuzz(86), 86)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(1246), 1246)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(75182), 75182)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(795824), 795824)
        self.assertEqual(FizzBuzz.improve_FizzBuzz(7958114), 7958114)
    
    def test_even_better_FizzBuzz(self):
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(3),'Fizz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(5),'Buzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(15),'FizzBuzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(6),'Fizz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(20),'Buzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(30),'FizzBuzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(9),'Fizz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(25),'Buzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(45),'FizzBuzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(4), 4)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(44), 44)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(258),'Fizz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(325),'Buzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(15555),'FizzBuzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(426),'Fizz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(380),'Buzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(735),'FizzBuzz')
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(86), 86)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(1246), 1246)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(75182), 75182)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(795824), 795824)
        self.assertEqual(FizzBuzz.even_better_FizzBuzz(7958114), 7958114)


if __name__ == '__main__':
    unittest.main()