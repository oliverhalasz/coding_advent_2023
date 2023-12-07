from day7 import Hand, CARDS, BIDS
from time import time


class JokerHand(Hand):

    order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T",  "Q",
             "K", "A"]

    def __init__(self, cards, bid):
        super().__init__(cards, bid)
        self.jacks = self.count_jacks()
        self.value = self.re_eval()

    def count_jacks(self):
        j = 0
        for card in self.cards:
            if card == "J":
                j += 1
        return j

    def re_eval(self):
        ertek = self.eval()
        if self.jacks == 0:
            return ertek

        if ertek >= 5:
            return 7
        if ertek == 4:
            return 6
        if ertek == 3:
            if self.jacks == 1:
                return 5
            else:
                return 6
        if ertek == 2:
            return 4
        else:
            return 2


start = time()
HANDS = [JokerHand(card, bid) for card, bid in zip(CARDS, BIDS)]
HANDS = sorted(HANDS, reverse=False)

s = 0
for i, hand in enumerate(HANDS, start=1):
    s += i * hand.bid
print(s)
print(time()-start)
