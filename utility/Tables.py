import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import DataFrame

SPLIT_INDEX = ['2/2', '3/3', '4/4', '5/5', '6/6', '7/7', '8/8', '9/9', '10/10', 'A/A']
attribute_dict = {
    "hard": [13, list(range(4, 21))],
    "soft": [8, list(range(12, 21))],
    "split": [10, ['2/2', '3/3', '4/4', '5/5', '6/6', '7/7', '8/8', '9/9', '10/10', 'A/A']]
}


def numbers_to_percent(table):
    for dealer in table:
        for i, each in enumerate(table[dealer]):
            s = sum(each)
            if s != 0:
                for j, num in enumerate(each):
                    table[dealer][i][j] = round(num / s, 2)


def extract_type(name):
    if "hard" in name.lower():
        return "hard"
    if "split" in name.lower():
        return "split"
    if "soft" in name.lower():
        return "soft"


def plot_three_lines_table(table, name):
    table_type = extract_type(name)
    table_dye = {key: [] for key in table}
    for key in table.keys():
        for i, cell in enumerate(table[key]):
            table_dye[key].append(cell[0])
            if len(cell) == 3:
                table[key][i] = str(cell[0]) + "\n" + str(cell[1]) + "\n" + str(cell[2])
            else:
                table[key][i] = str(cell[0]) + "\n" + str(cell[1]) + "\n" + str(cell[2]) + "\n" + str(cell[3])

    # change type to dataframe to work with heatmap
    df_values = DataFrame(table, attribute_dict[table_type][1])
    df_dye = DataFrame(table_dye, attribute_dict[table_type][1])

    # Show the heatmap table
    plt.figure(figsize=(10, int(attribute_dict[table_type][0])))
    sns.heatmap(df_dye, annot=df_values, fmt="", cmap='Greens', linewidths=1, cbar=False)
    plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False,
                    labeltop=True)
    plt.title(name)
    plt.savefig(os.path.abspath(
        "C:/Users/baral/PycharmProjects/ReinforcementLearning/BlackJack/Players/RLPlayer/Heat map tables/" + name))
    plt.clf()


def dye(hard, soft, split):
    """
    Find the value for dying according to the expectancy max value per action
    :param hard:  dict with array for each key that each member of the array represent the expectancy by the order
                  (stick, hit, double) considering hard value
    :param soft:  dict with array for each key that each member of the array represent the expectancy by the order
                  (stick, hit, double) considering soft value
    :param split: dict with array for each key that each member of the array represent the expectancy by the order
                  (stick, hit, double, split)
    :return: final tables - tables with index that fit with {'P', 'H', 'S', 'D'}
             dye tables - tables with index that fit with {'P': 0, 'H': -2, 'S': 1, 'D': -1}
    """
    DYE_HARD = {'2': [],
                '3': [],
                '4': [],
                '5': [],
                '6': [],
                '7': [],
                '8': [],
                '9': [],
                '10': [],
                'A': []}
    DYE_SOFT = {'2': [],
                '3': [],
                '4': [],
                '5': [],
                '6': [],
                '7': [],
                '8': [],
                '9': [],
                '10': [],
                'A': []}
    DYE_SPLIT = {'2': [],
                 '3': [],
                 '4': [],
                 '5': [],
                 '6': [],
                 '7': [],
                 '8': [],
                 '9': [],
                 '10': [],
                 'A': []}
    FINAL_HARD = {'2': [],
                  '3': [],
                  '4': [],
                  '5': [],
                  '6': [],
                  '7': [],
                  '8': [],
                  '9': [],
                  '10': [],
                  'A': []}
    FINAL_SOFT = {'2': [],
                  '3': [],
                  '4': [],
                  '5': [],
                  '6': [],
                  '7': [],
                  '8': [],
                  '9': [],
                  '10': [],
                  'A': []}
    FINAL_SPLIT = {'2': [],
                   '3': [],
                   '4': [],
                   '5': [],
                   '6': [],
                   '7': [],
                   '8': [],
                   '9': [],
                   '10': [],
                   'A': []}
    dye_colors = [1, -2, -1, 0]
    final_actions = ['S', 'H', 'D', 'P']

    for dealer_card in hard.keys():
        # Hard dying
        for cell in hard[dealer_card]:
            DYE_HARD[dealer_card].append(dye_colors[np.argmax(cell)])
            FINAL_HARD[dealer_card].append(final_actions[np.argmax(cell)])
        # Soft dying
        for cell in soft[dealer_card]:
            DYE_SOFT[dealer_card].append(dye_colors[np.argmax(cell)])
            FINAL_SOFT[dealer_card].append(final_actions[np.argmax(cell)])
        # Split dying
        for cell in split[dealer_card]:
            DYE_SPLIT[dealer_card].append(dye_colors[np.argmax(cell)])
            FINAL_SPLIT[dealer_card].append(final_actions[np.argmax(cell)])

    return DYE_HARD, DYE_SOFT, DYE_SPLIT, FINAL_HARD, FINAL_SOFT, FINAL_SPLIT


def plot_heatmap_based_on_values(player_name, hard_table, soft_table, split_table, rl=False):
    if rl:
        HARD_INDEX = list(range(4, 21))
        SOFT_INDEX = list(range(12, 21))
    else:
        HARD_INDEX = list(range(4, 22))
        SOFT_INDEX = list(range(12, 22))
    DYE_HARD, DYE_SOFT, DYE_SPLIT, FINAL_HARD, FINAL_SOFT, FINAL_SPLIT = dye(hard_table,
                                                                             soft_table,
                                                                             split_table)
    # change the values to a line separate string instead of a tuple
    for table in hard_table, soft_table:
        for key in table.keys():
            for i, cell in enumerate(table[key]):
                table[key][i] = str(cell[0]) + "\n" + str(cell[1]) + "\n" + str(cell[2])
    for key in split_table.keys():
        for i, cell in enumerate(split_table[key]):
            split_table[key][i] = str(cell[0]) + "\n" + str(cell[1]) + "\n" + str(cell[2]) + "\n" + str(
                cell[3])
    # change type to dataframe to work with heatmap
    hard_table = DataFrame(hard_table, index=HARD_INDEX)
    soft_table = DataFrame(soft_table, index=SOFT_INDEX)
    split_table = DataFrame(split_table, index=SPLIT_INDEX)
    DYE_HARD = DataFrame(DYE_HARD, index=HARD_INDEX)
    DYE_SOFT = DataFrame(DYE_SOFT, index=SOFT_INDEX)
    DYE_SPLIT = DataFrame(DYE_SPLIT, index=SPLIT_INDEX)
    # Show the heatmap table
    for name, df, dye_table, height in [("Hard table", hard_table, DYE_HARD, 13),
                                        ("Soft table", soft_table, DYE_SOFT, 8),
                                        ("Split table", split_table, DYE_SPLIT, 10)]:
        plt.figure(figsize=(10, height))
        sns.heatmap(dye_table, annot=df, fmt="", cmap='viridis', linewidths=1, cbar=False, vmin=-2, vmax=1)
        plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False,
                        labeltop=True)
        plt.title(name)
        plt.savefig("Heat map tables/" + player_name + " " + name)
        plt.clf()
