import Game


class HumanPlayer(Game.Player):
    def __init__(self, name, print_plays=True, save_plays=False, mode="Human"):
        super(HumanPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode

    def choose(self, dealer_card):
        if len(self.cards) == 2 and not self.play_split or len(self.cards_split) == 2 and self.play_split:
            if self.cards[0] == self.cards[1] and self.current_split == 0:
                user_input = input('Please enter a move by the capital letter (Hit, Stick, sPlit, Double): ')
                while user_input not in ['H', 'S', 'P', 'D']:
                    user_input = input('Please enter a move by the capital letter (Hit, Stick, sPlit, Double): ')
            else:
                user_input = input('Please enter a move by the capital letter (Hit, Stick, Double): ')
                while user_input not in ['H', 'S', 'D']:
                    user_input = input('Please enter a move by the capital letter (Hit, Stick, Double): ')
        else:
            user_input = input('Please enter a move by the capital letter (Hit, Stick): ')
            while user_input not in ['H', 'S']:
                user_input = input('Please enter a move by the capital letter (Hit, Stick): ')
        return user_input