import os.path
import pickle

import numpy as np

from Game import Game
from Player import Player
from utility.Tables import plot_heatmap_based_on_values

translate = 'HSDP'


class QLearningDecayStepPlayer(Player):
    def __init__(self, print_plays=False, save_plays=False, name="QLearningDecayStep", mode="QLearningDecayStep"):
        super(QLearningDecayStepPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode
        self.memory = []
        self.lr = 0.1
        self.exp_rate = 0.2
        self.gamma = 0.9
        self.train_mode = False
        self.update_rate = 1 / 10000
        try:
            fr = open(os.path.abspath(
                "C:/Users/baral/PycharmProjects/ReinforcementLearning/" +
                "BlackJack/Players/RLPlayers/QLearningDecayStep_policy"),
                'rb')
            self.Q_Values = pickle.load(fr)
            fr.close()
            print(name + " policy loaded")
        except FileNotFoundError:
            self.Q_Values = {}
            print(name + " policy not found")

    def reward(self, reward, split_reward):
        self.prize += reward + split_reward
        total_reward = reward + split_reward
        reward_array = [reward, split_reward]
        split = False
        if len(self.memory) > 0 and self.memory[0][1] == 3:
            split = True
            split_turn = 0
        steps = len(self.memory)
        for i, (state, action) in enumerate(self.memory):
            if split:
                if action == 3:
                    self.Q_Values[state][action] = (1 - self.lr) * self.Q_Values[state][
                        action] + self.lr * total_reward * self.gamma ** (steps - i - 1)
                else:
                    if i + 1 > len(self.cards) - int(self.current_hand_value >= 21):
                        split_turn = 1
                    self.Q_Values[state][action] = (1 - self.lr) * self.Q_Values[state][
                        action] + self.lr * reward_array[split_turn] * self.gamma ** (steps - i - 1)
        if np.random.uniform(0, 1) <= self.update_rate:
            self.update_file()
        if self.print_plays:
            print(
                "\u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9        " + self.name + "'s reward is: " + str(
                    reward + split_reward) + " Total prize: " + str(
                    self.prize) + "   \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9")

    def update_file(self):
        fr = open(os.path.abspath(
            "C:/Users/baral/PycharmProjects/ReinforcementLearning/" +
            "BlackJack/Players/RLPlayers/QLearningDecayStep_policy"),
            'wb')
        pickle.dump(self.Q_Values, fr)
        fr.close()
        print(self.name + " policy updated")

    def train(self, n):
        players = [self]
        self.train_mode = True
        for i in range(n):
            # Init a single game
            Game(players)
            print("played " + str(i) + " games so far")
        self.update_file()

    def print_table(self):
        """
        Take the q_values formatted as (dealer_card, current_value, ace_to_use, split_possible)
        put it inside the basic table and print it
        :return:
        """
        HARD_TABLE = {'2': [],
                      '3': [],
                      '4': [],
                      '5': [],
                      '6': [],
                      '7': [],
                      '8': [],
                      '9': [],
                      '10': [],
                      'A': []}
        HARD_INDEX = list(range(4, 21))
        for dealer_card in HARD_TABLE.keys():
            for i in HARD_INDEX:
                HARD_TABLE[dealer_card].append(np.round(self.Q_Values[dealer_card, i, 0, False], 3))
        SOFT_TABLE = {'2': [],
                      '3': [],
                      '4': [],
                      '5': [],
                      '6': [],
                      '7': [],
                      '8': [],
                      '9': [],
                      '10': [],
                      'A': []}
        SOFT_INDEX = list(range(12, 21))
        for dealer_card in SOFT_TABLE.keys():
            for i in SOFT_INDEX:
                SOFT_TABLE[dealer_card].append(np.round(self.Q_Values[dealer_card, i, 1, False], 3))
        SPLIT_TABLE = {'2': [],
                       '3': [],
                       '4': [],
                       '5': [],
                       '6': [],
                       '7': [],
                       '8': [],
                       '9': [],
                       '10': [],
                       'A': []}
        SPLIT_INDEX = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        for dealer_card in SPLIT_TABLE.keys():
            for i in SPLIT_INDEX:
                SPLIT_TABLE[dealer_card].append(np.round(self.Q_Values[dealer_card, i, 0, True], 3))
            SPLIT_TABLE[dealer_card].append(np.round(self.Q_Values[dealer_card, 12, 1, True], 3))
        plot_heatmap_based_on_values(self.name, HARD_TABLE, SOFT_TABLE, SPLIT_TABLE, rl=True)


if __name__ == '__main__':
    q_learn = QLearningDecayStepPlayer()
    q_learn.print_table()
