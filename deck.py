import random

class Deck:
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    def __init__(self) -> None:
        self.cards = []

        # Initialise a deck with all cards
        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.cards.append((rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

d = Deck()
d.shuffle()

