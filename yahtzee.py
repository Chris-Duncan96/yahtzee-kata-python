class Yahtzee:

    @staticmethod
    def chance(*args):
        return sum(args)

    @staticmethod
    def score_singles(number_match, *dice):
        points = 0
        for die in dice:
            if die == number_match:
                points += number_match
        return points

    @staticmethod
    def ones(*dice):
        return Yahtzee.score_singles(1, *dice)

    @staticmethod
    def twos(*dice):
        return Yahtzee.score_singles(2, *dice)

    @staticmethod
    def threes(*dice):
        return Yahtzee.score_singles(3, *dice)

    @staticmethod
    def fours(*dice):
        return Yahtzee.score_singles(4, *dice)

    @staticmethod
    def fives(*dice):
        return Yahtzee.score_singles(5, *dice)

    @staticmethod
    def sixes(*dice):
        return Yahtzee.score_singles(6, *dice)

    @staticmethod
    def score_pair(*dice):
        tallies = Yahtzee.get_tallies(*dice)
        for i in range(6):
            if (tallies[5 - i] == 2):
                return (6 - i) * 2
        return 0

    @staticmethod
    def get_tallies(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        return tallies

    @staticmethod
    def two_pair(*dice):
        tallies = Yahtzee.get_tallies(*dice)
        pair_count = 0
        score = 0
        for i in range(6):
            if (tallies[5 - i] == 2):
                pair_count = pair_count + 1
                score += (6 - i)

        if (pair_count == 2):
            return score * 2
        return 0

    @staticmethod
    def find_dice_which_repeats_times(times, *dice):
        tallies = Yahtzee.get_tallies(*dice)
        for i in range(6):
            if (tallies[i] == times):
                return i + 1
        return 0


    @staticmethod
    def four_of_a_kind(*dice):
        quartet = Yahtzee.find_dice_which_repeats_times(4, *dice)
        if quartet:
            return quartet * 4
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        triplet = Yahtzee.find_dice_which_repeats_times(3, *dice)
        if triplet:
            return triplet * 3
        return 0

    @staticmethod
    def smallStraight(*dice):
        tallies = Yahtzee.get_tallies(*dice)
        tallies_for_1_to_4 = tallies[0:4]
        if all(tallies == 1 for tallies in tallies_for_1_to_4):
            return 15
        return 0

    @staticmethod
    def largeStraight(*dice):
        tallies = Yahtzee.get_tallies(*dice)
        tallies_for_2_to_5 = tallies[1:5]
        if all(tallies == 1 for tallies in tallies_for_2_to_5):
            return 20
        return 0

    @staticmethod
    def fullHouse(*dice):
        pair_score = Yahtzee.score_pair(*dice)
        triplet_score = Yahtzee.three_of_a_kind(*dice)

        if pair_score and triplet_score:
            return pair_score + triplet_score
        else:
            return 0

    @staticmethod
    def yahtzee(dice):
        tallies = Yahtzee.get_tallies(*dice)
        for count in tallies:
            if count == 5:
                return 50
        return 0
