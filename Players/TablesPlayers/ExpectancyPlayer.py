from pandas import DataFrame

import Game
import Utility
from .TableOperations import choose_from_table

EXPECT_FINAL_HARD_TABLE = {
    '2': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '3': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '4': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '5': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '6': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '7': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'],
    '8': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S'],
    '9': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S'],
    '10': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S']}

HARD_INDEX = list(range(4, 22))
EXPECT_FINAL_HARD_TABLE = DataFrame(EXPECT_FINAL_HARD_TABLE, index=HARD_INDEX)

EXPECT_FINAL_SOFT_TABLE = {'2': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                           '3': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                           '4': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'S', 'S', 'S'],
                           '5': ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S'],
                           '6': ['H', 'H', 'H', 'D', 'D', 'D', 'D', 'S', 'S', 'S'],
                           '7': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                           '8': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
                           '9': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
                           '10': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
                           'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S']}

SOFT_INDEX = list(range(12, 22))
EXPECT_FINAL_SOFT_TABLE = DataFrame(EXPECT_FINAL_SOFT_TABLE, index=SOFT_INDEX)

EXPECT_FINAL_SPLIT_TABLE = {'2': ['H', 'H', 'H', 'D', 'S', 'S', 'P', 'S', 'S', 'P'],
                            '3': ['H', 'H', 'H', 'D', 'S', 'S', 'P', 'P', 'S', 'P'],
                            '4': ['H', 'H', 'H', 'D', 'P', 'S', 'P', 'P', 'S', 'P'],
                            '5': ['H', 'H', 'H', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                            '6': ['P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                            '7': ['H', 'H', 'H', 'D', 'H', 'H', 'P', 'S', 'S', 'P'],
                            '8': ['H', 'H', 'H', 'D', 'H', 'H', 'P', 'P', 'S', 'P'],
                            '9': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'P'],
                            '10': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'P'],
                            'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'P']}

SPLIT_INDEX = ['2/2', '3/3', '4/4', '5/5', '6/6', '7/7', '8/8', '9/9', '10/10', 'A/A']
EXPECT_FINAL_SPLIT_TABLE = DataFrame(EXPECT_FINAL_SPLIT_TABLE, index=SPLIT_INDEX)

cal_prob_stick_dict = {}
cal_prob_hit_dict = {}


def cal_prob_stick(dealer_current, dealer_ace, player_ace, current):
    """
    Calculate the probability for win if you chose stick
    :param dealer_current: current_hand_value dealer score
    :param dealer_ace: -1 is there no ace in the dealer's deck, 0 if ace is used, 1 if there is ace to use
    :param player_ace: -1 is there no ace in the player's deck, 0 if ace is used, 1 if there is ace to use
    :param current: current_hand_value player score
    :return: the probability of player's win by stick
    """
    if current > 21 and player_ace != 1:
        cal_prob_hit_dict[dealer_current, dealer_ace == 1, player_ace, current] = 0
        return 0
    if current > 21 and player_ace == 1:
        current -= 10
        player_ace = 0
    if dealer_current > 21 and dealer_ace == 1:
        dealer_current -= 10
        dealer_ace = 0
    if (dealer_current, dealer_ace == 1, current) in cal_prob_stick_dict.keys():
        return cal_prob_stick_dict[dealer_current, dealer_ace == 1, current]
    # Dealer sticks on a soft 17
    if dealer_current >= 17:
        if current > dealer_current or dealer_current > 21:
            cal_prob_stick_dict[dealer_current, dealer_ace == 1, current] = 1
            return 1
        else:
            cal_prob_stick_dict[dealer_current, dealer_ace == 1, current] = 0
            return 0
    else:
        prob = 0
        # Calculate and add the probability for each drawing for the dealer
        for card in Game.card_of_each_value[1:]:
            prob += cal_prob_stick(dealer_current + card, dealer_ace, player_ace, current) / 13
        # consider also soft/hard hand for ace drawing
        if dealer_ace == -1:
            prob += cal_prob_stick(dealer_current + 11, 1, player_ace, current) / 13
        else:
            prob += cal_prob_stick(dealer_current + 1, dealer_ace, player_ace, current) / 13
        # save to dict to save computing time later
        cal_prob_stick_dict[dealer_current, dealer_ace == 1, current] = prob
        return prob


def cal_prob_hit(dealer_current, dealer_ace, player_ace, current):
    """
    Calculate the probability for win if you chose hit
    :param dealer_current: current_hand_value dealer score
    :param dealer_ace: -1 is there no ace in the dealer's deck, 0 if ace is used, 1 if there is ace to use
    :param player_ace: -1 is there no ace in the player's deck, 0 if ace is used, 1 if there is ace to use
    :param current: current_hand_value player score
    :return: the probability of player's win by hit
    """
    if current > 21 and player_ace != 1:
        cal_prob_hit_dict[dealer_current, dealer_ace == 1, player_ace == 1, current] = 0
        return 0
    if current > 21 and player_ace == 1:
        current -= 10
        player_ace = 0
    if (dealer_current, dealer_ace == 1, player_ace == 1, current) in cal_prob_hit_dict.keys():
        return cal_prob_hit_dict[dealer_current, dealer_ace == 1, player_ace == 1, current]
    prob = 0
    # Calculate and add the probability for each drawing for the player
    for card in Game.card_of_each_value[1:]:
        prob += max(cal_prob_stick(dealer_current, dealer_ace, player_ace, current + card),
                    cal_prob_hit(dealer_current, dealer_ace, player_ace, current + card)) / 13
    # consider also soft/hard hand for ace drawing
    if player_ace == -1 and current + 11 < 22:
        prob += max(cal_prob_stick(dealer_current, dealer_ace, 1, current + 11),
                    cal_prob_hit(dealer_current, dealer_ace, 1, current + 11)) / 13
    else:
        prob += max(cal_prob_stick(dealer_current, dealer_ace, player_ace, current + 1),
                    cal_prob_hit(dealer_current, dealer_ace, player_ace, current + 1)) / 13
    # save to dict to save computing time later
    cal_prob_hit_dict[dealer_current, dealer_ace == 1, player_ace == 1, current] = prob
    return prob


def cal_prob_double(dealer_current, dealer_ace, player_ace, current):
    """
    Calculate the probability for win if you chose double
    :param dealer_current: current_hand_value dealer score
    :param dealer_ace: -1 is there no ace in the dealer's deck, 0 if ace is used, 1 if there is ace to use
    :param player_ace: -1 is there no ace in the player's deck, 0 if ace is used, 1 if there is ace to use
    :param current: current_hand_value player score
    :return: the probability of player's win by double
    """
    if current > 21 and player_ace != 1:
        return 0
    if current > 21 and player_ace == 1:
        current -= 10
        player_ace = 0
    prob = 0
    # Calculate and add the probability for each drawing for the player
    for card in Game.card_of_each_value[1:]:
        prob += cal_prob_stick(dealer_current, dealer_ace, player_ace, current + card) / 13
    # consider also soft/hard hand for ace drawing
    if player_ace == -1:
        prob += cal_prob_stick(dealer_current, dealer_ace, player_ace, current + 11) / 13
    else:
        prob += cal_prob_stick(dealer_current, dealer_ace, player_ace, current + 1) / 13
    return prob


def train_expectancyPlayer():
    """
    Calculate the probabilities for each move (stick, hit, double, split(if possible))
    save them to image with the following logic: hit - purple, stick - yellow, double - blue, split - green.
    :return:
    """
    EXPECTANCY_HARD_TABLE = {'2': [],
                             '3': [],
                             '4': [],
                             '5': [],
                             '6': [],
                             '7': [],
                             '8': [],
                             '9': [],
                             '10': [],
                             'A': []}
    EXPECTANCY_SOFT_TABLE = {'2': [],
                             '3': [],
                             '4': [],
                             '5': [],
                             '6': [],
                             '7': [],
                             '8': [],
                             '9': [],
                             '10': [],
                             'A': []}
    EXPECTANCY_SPLIT_TABLE = {'2': [],
                              '3': [],
                              '4': [],
                              '5': [],
                              '6': [],
                              '7': [],
                              '8': [],
                              '9': [],
                              '10': [],
                              'A': []}
    for dealer_card in list(EXPECTANCY_HARD_TABLE.keys()).__reversed__():
        if dealer_card == 'A':
            dealer_ace = 1
        else:
            dealer_ace = -1
        for current in HARD_INDEX:
            # Stick calculation
            stick = cal_prob_stick(Game.value(dealer_card), dealer_ace, 0, current)
            # Hard hand hit
            hard = cal_prob_hit(Game.value(dealer_card), dealer_ace, -1, current)
            double_hard = cal_prob_double(Game.value(dealer_card), dealer_ace, -1, current)
            # Change probability to expectancy
            stick = round(2 * stick - 1, 2)
            hard = round(2 * hard - 1, 2)
            double_hard = round(2 * double_hard - 2 * (1 - double_hard), 2)
            EXPECTANCY_HARD_TABLE[dealer_card].append((stick, hard, double_hard))
            # Soft hand hit
            if current >= 12:
                soft = cal_prob_hit(Game.value(dealer_card), dealer_ace, 1, current)
                double_soft = cal_prob_double(Game.value(dealer_card), dealer_ace, 1, current)
                # Change probability to expectancy
                soft = round(2 * soft - 1, 2)
                double_soft = round(2 * double_soft - 2 * (1 - double_soft), 2)
                EXPECTANCY_SOFT_TABLE[dealer_card].append((stick, soft, double_soft))
        # Split calculation for two till ten
        for pair in range(2, 11):
            split_win = cal_prob_hit(Game.value(dealer_card), dealer_ace, -1, pair)
            win = split_win ** 2
            tie = 2 * split_win * (1 - split_win)
            hit = cal_prob_hit(Game.value(dealer_card), dealer_ace, -1, pair * 2)
            stick = cal_prob_stick(Game.value(dealer_card), dealer_ace, -1, pair * 2)
            double = cal_prob_double(Game.value(dealer_card), dealer_ace, -1, pair * 2)
            # Change probability to expectancy
            hit = round(2 * hit - 1, 2)
            stick = round(2 * stick - 1, 2)
            double = round(2 * double - 2 * (1 - double), 2)
            split = round(2 * win + 0 * tie - 2 * (1 - win - tie), 2)
            EXPECTANCY_SPLIT_TABLE[dealer_card].append((stick, hit, double, split))
        # Split calculation for two ACEs
        split_win = cal_prob_hit(Game.value(dealer_card), dealer_ace, 1, 11)
        win = split_win ** 2
        tie = 2 * split_win * (1 - split_win)
        hit = cal_prob_hit(Game.value(dealer_card), dealer_ace, 1, 12)
        stick = cal_prob_stick(Game.value(dealer_card), dealer_ace, 1, 12)
        double = cal_prob_double(Game.value(dealer_card), dealer_ace, 1, 12)
        # Change probability to expectancy
        hit = round(2 * hit - 1, 2)
        stick = round(2 * stick - 1, 2)
        double = round(2 * double - 2 * (1 - double), 2)
        split = round(2 * win + 0 * tie - 2 * (1 - win - tie), 2)
        EXPECTANCY_SPLIT_TABLE[dealer_card].append((stick, hit, double, split))

    return EXPECTANCY_HARD_TABLE, EXPECTANCY_SOFT_TABLE, EXPECTANCY_SPLIT_TABLE


if __name__ == '__main__':
    EXPECTANCY_HARD_TABLE, EXPECTANCY_SOFT_TABLE, EXPECTANCY_SPLIT_TABLE = train_expectancyPlayer()
    Utility.plot_heatmap_based_on_values("Expectancy", EXPECTANCY_HARD_TABLE, EXPECTANCY_SOFT_TABLE, EXPECTANCY_SPLIT_TABLE)


class ExpectancyPlayer(Game.Player):
    def __init__(self, print_plays=False, save_plays=False, name="Expectancy", mode="Expectancy"):
        super(ExpectancyPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode

    def choose(self, dealer_card):
        return choose_from_table(self, dealer_card, EXPECT_FINAL_SPLIT_TABLE, EXPECT_FINAL_HARD_TABLE,
                                 EXPECT_FINAL_SOFT_TABLE)
