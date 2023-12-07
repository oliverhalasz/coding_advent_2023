from time import time

with open("C:/Users/Oliver/Documents/coding_advent2023/day7.txt") as f:
    lines = f.read().split("\n")

lines_ = [line.split() for line in lines]
CARDS = [line[0] for line in lines_]
BIDS = [*map(lambda x: int(x[1]), lines_)]


class Hand:

    order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q",
             "K", "A"]

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.value = self.eval()

    def __str__(self) -> str:
        return self.cards

    def __repr__(self) -> str:
        return f"Cards: {self.cards}, Value: {self.value}, Bid: {self.bid}\n"

    def eval(self):
        chars = {}
        for character in self.cards:
            if character in chars:
                chars[character] += 1
            else:
                chars[character] = 1

        if 5 in chars.values():  # 5 of a kind
            return 7
        elif 4 in chars.values():  # 4 of a kind
            return 6
        elif 3 in chars.values() and 2 in chars.values():  # Full house
            return 5
        elif 3 in chars.values():  # 3 of a kind
            return 4
        elif 2 in chars.values() and len(chars.values()) == 3:  # 2 pairs
            return 3
        elif 2 in chars.values():  # 1 pair
            return 2
        else:  # High card
            return 1

    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        for self_card, other_card in zip(self.cards, other.cards):
            if self.order.index(self_card) > self.order.index(other_card):
                return True
            if self.order.index(self_card) < self.order.index(other_card):
                return False
        return True


start = time()
HANDS = [Hand(card, bid) for card, bid in zip(CARDS, BIDS)]
HANDS = sorted(HANDS)

s = 0
for i, hand in enumerate(HANDS, start=1):
    s += i * hand.bid
print(s)
print(time()-start)
