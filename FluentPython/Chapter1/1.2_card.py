import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    for i in deck:
        print(spades_high(i))
    print(len(deck))
    print(deck[0])
    print(choice(deck))