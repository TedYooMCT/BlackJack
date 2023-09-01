class Player(object):
    """
    Basic player class that will expand for each player that will use this class
    """
    def __init__(self, name, print_plays=False, save_plays=False):
        self.mode = "None player"
        self.prize = 0
        self.current_hand_value = 0
        self.cards = []
        self.ace_to_use = 0
        self.ace_to_use_split = 0
        self.name = name
        self.double = 1
        self.double_split = 1
        self.current_split = 0
        self.play_split = False
        self.cards_split = []
        self.print_plays = print_plays
        if save_plays:
            self.save_plays = True
            self.REWARD_HARD_TABLE = {
                '2': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '3': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '4': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '5': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '6': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '7': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '8': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '9': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '10': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                       [0, 0, 0]],
                'A': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]]}
            self.REWARD_SOFT_TABLE = {
                '2': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '3': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '4': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '5': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '6': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '7': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '8': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '9': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '10': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]],
                'A': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]]}
            self.REWARD_SPLIT_TABLE = {
                '2': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '3': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '4': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '5': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '6': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '7': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '8': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '9': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]],
                '10': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]],
                'A': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                      [0, 0, 0]]}
            self.memory = []
        else:
            self.save_plays = False

    def card_drawn(self, new_card):
        self.cards.append(new_card)
        self.current_hand_value += value(new_card)
        if new_card == 'A':
            self.ace_to_use += 1
        if self.current_hand_value > 21 and self.ace_to_use > 0:
            self.current_hand_value -= 10
            self.ace_to_use -= 1
        if self.print_plays:
            print(self.name + " -  Card drawn: " + new_card)

    def card_drawn_split(self, new_card):
        self.cards_split.append(new_card)
        self.current_split += value(new_card)
        if new_card == 'A':
            self.ace_to_use_split += 1
        if self.current_split > 21 and self.ace_to_use_split > 0:
            self.current_split -= 10
            self.ace_to_use_split -= 1
        if self.print_plays:
            print(self.name + " - Card drawn for second: " + new_card)

    def reset(self):
        self.current_hand_value = 0
        self.cards = []
        self.ace_to_use = 0
        self.ace_to_use_split = 0
        self.double = 1
        self.double_split = 1
        self.current_split = 0
        self.play_split = False
        self.cards_split = []
        self.memory = []

    def choose(self, dealer_card):
        raise NotImplementedError("None player can't choose action")

    def reward(self, reward, split_reward):
        self.prize += reward + split_reward
        if self.save_plays:
            # wtl is the key for the list order, win = 0, tie = 1, lose = 2
            if reward + split_reward > 0:
                wtl = 0
            elif reward + split_reward == 0:
                wtl = 1
            else:
                wtl = 2
            prev_current = -1
            for choice in self.memory:
                # choice is made of [table_num, dealer_card, self.current_hand_value, self.current_split]
                # table numbers: 1 - split, 2 - soft, 3 - hard, 4 - ace split (for splitting from splitting 6s)
                # Reward table is a dictionary with dealer_card as keys and list as values
                # the lists are ordered by the current value possible for each table
                # each list is a list of 3 elements by the order of 'wtl'
                if choice[0] == 1:
                    self.REWARD_SPLIT_TABLE[choice[1]][choice[2] // 2 - 2][wtl] += 1
                if choice[0] == 4:
                    self.REWARD_SPLIT_TABLE[choice[1]][9][wtl] += 1
                # if the current value didn't change then we are on the split plays

                elif choice[2] != prev_current and choice[2] < 21:
                    if choice[0] == 2:
                        self.REWARD_SOFT_TABLE[choice[1]][choice[2] - 12][wtl] += 1
                    if choice[0] == 3:
                        self.REWARD_HARD_TABLE[choice[1]][choice[2] - 4][wtl] += 1
                elif choice[3] < 21:
                    if choice[0] == 2:
                        self.REWARD_SOFT_TABLE[choice[1]][choice[3] - 12][wtl] += 1
                    if choice[0] == 3:
                        self.REWARD_HARD_TABLE[choice[1]][choice[3] - 4][wtl] += 1
                prev_current = choice[2]
        if self.print_plays:
            print(
                "\u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9        " + self.name + "'s reward is: " + str(
                    reward + split_reward) + " Total prize: " + str(
                    self.prize) + "   \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9")


def value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 11
    return int(card)
