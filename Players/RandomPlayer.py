import random

import Game


class RandomPlayer(Game.Player):
    def __init__(self, print_plays=False, save_plays=False, name="Rand", mode="Random"):
        super(RandomPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode

    def choose(self, dealer_card):
        # check if we play split or not
        if len(self.cards) == 2 and self.current_split == 0 and self.cards[0] == self.cards[1]:
            choice = random.choice(['H', 'S', 'D', 'P'])
        else:
            choice = random.choice(['H', 'S', 'D'])
        if self.print_plays:
            print(self.name + " choice is: " + choice)

        return choice
