from game import Game

if __name__ == '__main__':
    
    game = Game()

    game.deal(52)

    game.show_state()

    game.reset()

    game.show_state()