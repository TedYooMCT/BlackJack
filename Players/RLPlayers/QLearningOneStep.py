import os
import pickle
import random

import numpy as np

from Game import Game
from Player import Player
from utility.Tables import plot_heatmap_based_on_values

translate = 'HSDP'


class QLearningOneStepPlayer(Player):
    def __init__(self, print_plays=False, save_plays=False, name="QLearning1Step", mode="QLearning1Step"):
        super(QLearningOneStepPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode
        self.memory = []
        self.lr = 0.1
        self.exp_rate = 0.2
        self.update_rate = 1 / 10000
        self.train_mode = False
        try:
            fr = open(os.path.abspath(
                "C:/Users/baral/PycharmProjects/ReinforcementLearning/BlackJack/" +
                "Players/RLPlayers/QLearningOneStep_policy"),
                'rb')
            self.Q_Values = pickle.load(fr)
            fr.close()
            print(name + " policy loaded")

        except FileNotFoundError:
            self.Q_Values = {}
            print(name + " policy not found")

    def choose(self, dealer_card):
        """
        :param: dealer_card:
        state is a tuple of (dealer_card, current_value, ace_to_use, split_possible)
        :return: action to play
        """
        if dealer_card in ['J', 'Q', 'K']:
            dealer_card = '10'
        if len(self.cards) == 2 and self.current_split == 0 and self.cards[0] == self.cards[1]:
            state = (dealer_card, self.current_hand_value, self.ace_to_use, True)
            if state in self.Q_Values.keys():
                if np.random.uniform(0, 1) <= self.exp_rate and self.train_mode:
                    action = random.choice([0, 1, 2, 3])  # represent H, S, D, P

                else:
                    v = -100000000
                    for i, a in enumerate(self.Q_Values[state]):
                        if self.Q_Values[state][i] > v:
                            action = i
                            v = self.Q_Values[state][i]
            else:
                self.Q_Values[state] = [0, 0, 0, 0]  # represent H, S, D, P
                action = random.choice([0, 1, 2, 3])  # represent H, S, D, P
        else:
            if not self.play_split:
                state = (dealer_card, self.current_hand_value, self.ace_to_use, False)
            else:
                state = (dealer_card, self.current_split, self.ace_to_use_split, False)
            if state in self.Q_Values.keys():
                if np.random.uniform(0, 1) <= self.exp_rate and self.train_mode:
                    action = random.choice([0, 1, 2])  # represent H, S, D
                else:
                    v = -100000000
                    for i, a in enumerate(self.Q_Values[state]):
                        if self.Q_Values[state][i] > v:
                            action = i
                            v = self.Q_Values[state][i]
            else:
                self.Q_Values[state] = [0, 0, 0]  # represent H, S, D
                action = random.choice([0, 1, 2])  # represent H, S, D

        if self.print_plays:
            print(self.name + " action is: " + translate[action])
        self.memory.append((state, action))
        return translate[action]

    def reward(self, reward, split_reward):
        self.prize += reward + split_reward
        total_reward = reward + split_reward
        reward_array = [reward, split_reward]
        split = False
        if len(self.memory) > 0 and self.memory[0][1] == 3:
            split = True
            split_turn = 0
        for i, (state, action) in enumerate(self.memory):
            if split:
                if action == 3:
                    self.Q_Values[state][action] = (1 - self.lr) * self.Q_Values[state][action] + self.lr * total_reward
                else:
                    if i + 1 > len(self.cards) - int(self.current_hand_value >= 21):
                        split_turn = 1
                    self.Q_Values[state][action] = (1 - self.lr) * self.Q_Values[state][action] + self.lr * \
                                                   reward_array[split_turn]
            else:
                self.Q_Values[state][action] = (1 - self.lr) * self.Q_Values[state][action] + self.lr * total_reward
        if np.random.uniform(0, 1) <= self.update_rate:
            self.update_file()

        if self.print_plays:
            print(
                "\u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9        " + self.name + "'s reward is: " + str(
                    reward + split_reward) + " Total prize: " + str(
                    self.prize) + "   \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9 \u03A9")

    def update_file(self):
        fr = open(os.path.abspath(
            "C:/Users/baral/PycharmProjects/ReinforcementLearning/BlackJack/Players/RLPlayers/QLearningOneStep_policy"),
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
    q_learn = QLearningOneStepPlayer()
    q_learn.print_table()
