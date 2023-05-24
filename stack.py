import random

class Stack(list):
    """
    This class represents any stack of cards in the game, e.g. a player's hand, the main deck
    a discard pile or cards not in the game.
    """
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠', '♡', '♢', '♣']
    main = None

    def __init__(self) -> None:
        self.cards = []

        # Make a stack with all cards if the main stack hasn't been initialised
        if Stack.main == None:
            Stack.main = self

            for suit in Stack.suits:
                for rank in Stack.ranks:
                    self.cards.append(suit + rank)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def move(self, card : str, other_stack) -> None:
        """Move a card from one stack to another."""
        other_stack.cards.append(self.cards.pop(self.cards.index(card)))

    def pick(self, other_stack, index : int = None) -> None:
        """Pick a card from a stack (at index if provided)."""
        if index:
            card = other_stack.cards[index]
        else:
            card = random.choice(other_stack.cards)

        other_stack.move(card, self)

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def remove_pair(self, pile) -> bool:
        """Remove a pair from the player's hand to the pile. Return True if successful."""
        success = False

        # Check for each rank if there is more than one card in the player's hand.
        for rank in Stack.ranks:
            pair = []

            for card in self.cards:
                if card[1:] == rank:
                    pair += card

                # Move the pair to the pile
                if len(pair) >= 2:
                    self.move(pair[0], pile)
                    self.move(pair[0], pile)
                    success = True

        return success





