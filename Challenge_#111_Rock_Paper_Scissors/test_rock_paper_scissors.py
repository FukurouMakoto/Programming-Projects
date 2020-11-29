import unittest
import rock_paper_scissors

class TestRockPaperScissors(unittest.TestCase):
    def test_collect_input(self):
        self.assertEqual(rock_paper_scissors.collect_input('Rock'), 'Rock')
        




if __name__ == '__main__':
    unittest.main()