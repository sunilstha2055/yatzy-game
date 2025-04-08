import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.game = Yatzy()
        self.game.dice = [1, 2, 3, 4, 5]  # For consistent testing

    def test_ones(self):
        self.assertEqual(self.game.Ones(), 1)

    def test_twos(self):
        self.assertEqual(self.game.Twos(), 2)

    def test_one_pair(self):
        self.game.dice = [3, 3, 4, 5, 6]
        self.assertEqual(self.game.OnePair(), 6)

    def test_two_pairs(self):
        self.game.dice = [2, 2, 4, 4, 6]
        self.assertEqual(self.game.TwoPairs(), 12)

    def test_three_alike(self):
        self.game.dice = [3, 3, 3, 4, 5]
        self.assertEqual(self.game.ThreeAlike(), 9)

    def test_four_alike(self):
        self.game.dice = [4, 4, 4, 4, 5]
        self.assertEqual(self.game.FourAlike(), 16)

    def test_small(self):
        self.assertEqual(self.game.Small(), 15)

    def test_large(self):
        self.game.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.game.Large(), 20)

    def test_full_course(self):
        self.game.dice = [2, 2, 2, 3, 3]
        self.assertEqual(self.game.FullCourse(), 12)

    def test_chance(self):
        self.assertEqual(self.game.Chance(), 15)

    def test_yatzy(self):
        self.game.dice = [5, 5, 5, 5, 5]
        self.assertEqual(self.game.Yatzy(), 50)

if __name__ == '__main__':
    unittest.main()