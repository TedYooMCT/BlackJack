import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

import Game
from .TableOperations import choose_from_table


BASE_HARD_TABLE = {'2': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                   '3': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                   '4': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                   '5': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                   '6': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                   '7': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'],
                   '8': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'],
                   '9': ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'],
                   '10': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'],
                   'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S']}
HARD_INDEX = list(range(4, 22))
BASE_HARD_TABLE = DataFrame(BASE_HARD_TABLE, index=HARD_INDEX)

BASE_SOFT_TABLE = {'2': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                   '3': ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'S', 'S', 'S'],
                   '4': ['H', 'H', 'H', 'D', 'D', 'D', 'D', 'S', 'S', 'S'],
                   '5': ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'S'],
                   '6': ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'S'],
                   '7': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                   '8': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
                   '9': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
                   '10': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
                   'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S']}
SOFT_INDEX = list(range(12, 22))
BASE_SOFT_TABLE = DataFrame(BASE_SOFT_TABLE, index=SOFT_INDEX)

BASE_SPLIT_TABLE = {'2': ['P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                    '3': ['P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                    '4': ['P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                    '5': ['P', 'P', 'P', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                    '6': ['P', 'P', 'P', 'D', 'P', 'P', 'P', 'P', 'S', 'P'],
                    '7': ['P', 'P', 'H', 'D', 'H', 'P', 'P', 'S', 'S', 'P'],
                    '8': ['H', 'H', 'H', 'D', 'H', 'H', 'P', 'P', 'S', 'P'],
                    '9': ['H', 'H', 'H', 'D', 'H', 'H', 'P', 'P', 'S', 'P'],
                    '10': ['H', 'H', 'H', 'H', 'H', 'H', 'P', 'S', 'S', 'P'],
                    'A': ['H', 'H', 'H', 'H', 'H', 'H', 'P', 'S', 'S', 'P']}
SPLIT_INDEX = ['2/2', '3/3', '4/4', '5/5', '6/6', '7/7', '8/8', '9/9', '10/10', 'A/A']
BASE_SPLIT_TABLE = DataFrame(BASE_SPLIT_TABLE, index=SPLIT_INDEX)

if __name__ == '__main__':
    # Show the heatmap table
    for table_name, df in [("Hard table", BASE_HARD_TABLE),
                           ("Soft table", BASE_SOFT_TABLE),
                           ("Split table", BASE_SPLIT_TABLE)]:
        origin = df.to_numpy()
        heat_dye = df.replace({'P': 0, 'H': -2, 'S': 1, 'D': -1})
        sns.heatmap(heat_dye, annot=origin, fmt="", cmap='viridis', cbar=False, vmin=-2, vmax=1)
        plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False,
                        labeltop=True)
        plt.title(table_name)
        plt.savefig("Heat map tables/Basic player " + table_name)
        plt.clf()


class BasicPlayer(Game.Player):
    def __init__(self, print_plays=False, save_plays=False, name="Basic", mode="Basic"):
        super(BasicPlayer, self).__init__(name, print_plays, save_plays)
        self.mode = mode

    def choose(self, dealer_card):
        return choose_from_table(self, dealer_card, BASE_SPLIT_TABLE, BASE_HARD_TABLE, BASE_SOFT_TABLE)
