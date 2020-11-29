import unittest
import Highest_Prime_Factor

class TestFizzBuzz(unittest.TestCase):

    def test_highest_prime_factor(self):
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(52), 13)
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(96), 3)
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(115), 23)
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(150), 5)
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(2255), 41)
        '''
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        self.assertEqual(Highest_Prime_Factor.highest_prime_factor(), )
        '''    
    


if __name__ == '__main__':
    unittest.main()