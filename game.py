from stack import Stack


class Game:
    """
    Old Maid game class. The queen of clubs is removed. Amount of players is prompted.
    
    The player can choose a card to draw to simulate reality.
    """

    def __init__(self) -> None:
        self.draw_deck    = Stack()
        self.removed      = Stack()
        self.discard_pile = Stack()

        self.draw_deck.move('♣Q', self.removed)

        self.num_players = self.prompt_number("Enter the amount of players", 2, 12)
        self.players = [Stack() for i in range(self.num_players)]

    def prompt_number(self, text : str, lower : int, upper : int) -> int:
        """Ask the user to enter a valid number (lower <= number <= upper)."""
        response = lower-1

        # Keep asking while not in range or not a number
        while not lower <= response <= upper:
            response = input(text + " (%d-%d): " % (lower, upper))
            
            try:
                response = int(response)
            except:
                response = lower-1
                continue

        return response

    def deal(self, amount : int = None) -> None:
        """
        Deal the specified amount cards to players or until the pile is emtpy.
        """

        self.draw_deck.shuffle()

        for i in range(amount):
            for player in self.players:
                if self.draw_deck.is_empty():
                    break
                else:
                    player.pick(self.draw_deck)

    def reset(self):
        """Move all the cards to the draw deck."""
        for player in self.players:
            while not player.is_empty():
                self.draw_deck.pick(player)

    def show_state(self):
        """Show the hand of each player."""
        for i, player in enumerate(self.players):
            print("Player %d: " % i, end='')
            for c in player.cards:
                print(c, end='\t')

            print()


        