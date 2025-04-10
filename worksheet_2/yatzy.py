import random

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5
        self.locked = [False] * 5
        self.roll()  # Roll all dice on instantiation

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = False

    def Ones(self): return sum(d for d in self.dice if d == 1)
    def Twos(self): return sum(d for d in self.dice if d == 2)
    def Threes(self): return sum(d for d in self.dice if d == 3)
    def Fours(self): return sum(d for d in self.dice if d == 4)
    def Fives(self): return sum(d for d in self.dice if d == 5)
    def Sixes(self): return sum(d for d in self.dice if d == 6)

    def OnePair(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        for i in range(5, -1, -1):
            if counts[i] >= 2:
                return (i + 1) * 2
        return 0

    def TwoPairs(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        pairs = [(i + 1) * 2 for i, c in enumerate(counts) if c >= 2]
        return sum(pairs[:2]) if len(pairs) >= 2 else 0

    def ThreeAlike(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def FourAlike(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def Small(self):
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def Large(self):
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def FullCourse(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        has_three = 3 in counts
        has_two = 2 in counts
        return sum(self.dice) if has_three and has_two else 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        return 50 if all(d == self.dice[0] for d in self.dice) else 0

    def get_dice(self):
        return self.dice