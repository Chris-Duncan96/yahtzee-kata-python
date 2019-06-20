from yahtzee import Yahtzee
from unittest import TestCase


class YahtzeeTest(TestCase):

    def test_chance_scores_sum_of_all_dice(self):
        expected = 15
        actual = Yahtzee.chance(2, 3, 4, 5, 1)
        self.assertEqual(expected, actual)
        self.assertEqual(16, Yahtzee.chance(3, 3, 4, 5, 1))

    def test_yahtzee_scores_50(self):
        expected = 50
        actual = Yahtzee.yahtzee([4, 4, 4, 4, 4])
        self.assertEqual(expected, actual)
        self.assertEqual(50, Yahtzee.yahtzee([6, 6, 6, 6, 6]))
        self.assertEqual(0, Yahtzee.yahtzee([6, 6, 6, 6, 3]))

    def test_ones(self):
        self.assertEqual(1, Yahtzee.ones(1, 2, 3, 4, 5))
        self.assertEqual(2, Yahtzee.ones(1, 2, 1, 4, 5))
        self.assertEqual(0, Yahtzee.ones(6, 2, 2, 4, 5))
        self.assertEqual(4, Yahtzee.ones(1, 2, 1, 1, 1))

    def test_twos(self):
        self.assertEqual(4, Yahtzee.twos(1, 2, 3, 2, 6))
        self.assertEqual(10, Yahtzee.twos(2, 2, 2, 2, 2))

    def test_threes(self):
        self.assertEqual(6, Yahtzee.threes(1, 2, 3, 2, 3))
        self.assertEqual(12, Yahtzee.threes(2, 3, 3, 3, 3))

    def test_fours(self):
        self.assertEqual(12, Yahtzee.fours(4, 4, 4, 5, 5))
        self.assertEqual(8, Yahtzee.fours(4, 4, 5, 5, 5))
        self.assertEqual(4, Yahtzee.fours(4, 5, 5, 5, 5))

    def test_fives(self):
        self.assertEqual(10, Yahtzee.fives(4, 4, 4, 5, 5))
        self.assertEqual(15, Yahtzee.fives(4, 4, 5, 5, 5))
        self.assertEqual(20, Yahtzee.fives(4, 5, 5, 5, 5))

    def test_sixes(self):
        self.assertEqual(0, Yahtzee.sixes(4, 4, 4, 5, 5))
        self.assertEqual(6, Yahtzee.sixes(4, 4, 6, 5, 5))
        self.assertEqual(18, Yahtzee.sixes(6, 5, 6, 6, 5))

    def test_one_pair(self):
        self.assertEqual(6, Yahtzee.score_pair(3, 4, 3, 5, 6))
        self.assertEqual(10, Yahtzee.score_pair(5, 3, 3, 3, 5))
        self.assertEqual(12, Yahtzee.score_pair(5, 3, 6, 6, 5))

    def test_two_Pair(self):
        self.assertEqual(16, Yahtzee.two_pair(3, 3, 5, 4, 5))
        self.assertEqual(0, Yahtzee.two_pair(3, 3, 5, 5, 5))

    def test_three_of_a_kind(self):
        self.assertEqual(9, Yahtzee.three_of_a_kind(3, 3, 3, 4, 5))
        self.assertEqual(15, Yahtzee.three_of_a_kind(5, 3, 5, 4, 5))
        self.assertEqual(0, Yahtzee.three_of_a_kind(3, 3, 3, 3, 5))

    def test_four_of_a_knd(self):
        self.assertEqual(12, Yahtzee.four_of_a_kind(3, 3, 3, 3, 5))
        self.assertEqual(20, Yahtzee.four_of_a_kind(5, 5, 5, 4, 5))
        self.assertEqual(0, Yahtzee.three_of_a_kind(3, 3, 3, 3, 3))

    def test_smallStraight(self):
        self.assertEqual(15, Yahtzee.smallStraight(1, 2, 3, 4, 5))
        self.assertEqual(15, Yahtzee.smallStraight(2, 3, 4, 5, 1))
        self.assertEqual(0, Yahtzee.smallStraight(1, 2, 2, 4, 5))

    def test_largeStraight(self):
        self.assertEqual(20, Yahtzee.largeStraight(6, 2, 3, 4, 5))
        self.assertEqual(20, Yahtzee.largeStraight(2, 3, 4, 5, 6))
        self.assertEqual(0, Yahtzee.largeStraight(1, 2, 2, 4, 5))

    def test_fullHouse(self):
        self.assertEqual(18, Yahtzee.fullHouse(6, 2, 2, 2, 6))
        self.assertEqual(0, Yahtzee.fullHouse(2, 3, 4, 5, 6))
