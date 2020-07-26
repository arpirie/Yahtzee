import unittest

from Die import Die


class Yahtzee:
    def __init__(self):
        self.chosen = ()
        self.d1 = Die(6)
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]

    def score(self, numbers):
        return 50
        # figure out if numbers which is a list of 5 numbers between 1 and 6
        # if they are all the same and return 50 if that is the case
        # if not, return the sum of all the numbers

    def roll(self):
        if len(self.chosen) == 0:
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:
            for v in self.chosen:
                self.cup_of_dice[v].active = False
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def choose(self, choice):
        self.chosen = choice


class MyTestCase(unittest.TestCase):
    def test_yahtzee(self):
        self.game = Yahtzee()
        self.assertTrue(self.game != None)

    def test_roll(self):
        self.game = Yahtzee()
        values = self.game.roll()
        self.assertEqual(5, len(values))

    def test_die(self):
        d = Die(6)
        v = d.roll()
        self.assertGreater(v, 0)
        self.assertLess(v, 7)

    def test_choose(self):
        self.game = Yahtzee()
        values = self.game.roll()
        print(values)
        self.game.choose((0, 1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEqual(values[0], new_values[0])
        self.assertEqual(values[1], new_values[1])

    def test_score(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertTrue(self.game.score(values) == 50)
        values = [1, 2, 3, 4, 5]
        self.assertTrue(self.game.score(values) == 15)


if __name__ == '__main__':
    unittest.main()
