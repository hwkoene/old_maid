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
        """Deal the specified amount cards to players or until the pile is emtpy."""

        self.draw_deck.shuffle()

        for i in range(amount):
            for player in self.players:
                if self.draw_deck.is_empty():
                    break
                else:
                    player.pick(self.draw_deck)

    def reset(self) -> None:
        """Move all the cards to the draw deck."""
        for player in self.players:
            while not player.is_empty():
                self.draw_deck.pick(player)

    def show_state(self):
        """
        Show the hand of each player.
        Example:    Player 0: ♡K    ♣10     ♠Q      ♣6
                    Player 1: ♡10   ♢8      ♢K      ♢6      ♡8
        """
        for i, player in enumerate(self.players):
            print("Player %d: " % i, end='')
            for c in player.cards:
                print(c, end='\t')

            print()

    def game_ended(self) -> None:
        """Checks if the game is finished."""
        return sum([len(player.cards) for player in self.players]) == 1

    def run(self) -> None:
        """A round is started with the specified amount of players."""
        finished = False

        # Deal all the cards
        self.deal(52)

        # Every player discards their pairs
        for player in self.players:
            while player.discard_pair(self.discard_pile):
                continue
        
        print("Game started. Press enter to go to the next round.")
        
        while not finished:    
            # Simulate a round until the end state is reached where one player has a queen
            for i, player in enumerate(self.players):
                player.pick(self.players[i-1])

                self.show_state()

                player.discard_pair(self.discard_pile)

                # End state is reached
                if self.game_ended():
                    # Show final hands and terminate
                    print()
                    self.show_state()
                    print("Game ended.")
                    finished = True
                    break
                    
                input()

        self.reset()
