from Game import Game
from Players.HumanPlayer import HumanPlayer
from Players.RLPlayers.QLearningDecayStep import QLearningDecayStepPlayer
from Players.RLPlayers.QLearningOneStep import QLearningOneStepPlayer
from Players.RandomPlayer import RandomPlayer
from Players.TablesPlayers.BasicPlayer import BasicPlayer
from Players.TablesPlayers.ExpectancyPlayer import ExpectancyPlayer

# Define the players (True or False for printing the computer moves)
me = HumanPlayer("Bar")
rand = RandomPlayer(False, save_plays=True)
base = BasicPlayer(print_plays=False, save_plays=True)
ex = ExpectancyPlayer(False, save_plays=True)
q_learn_one_step = QLearningOneStepPlayer()
q_learn_decay = QLearningDecayStepPlayer()
# Define who joins the game
players = [rand, base, ex, q_learn_one_step, q_learn_decay]
# players = [rand, me]
with open("compare/compare_before_training.txt", 'w') as f:
    for i in range(10000):
        # Init a single game
        game = Game(players)
        f.write("Game n." + str(i) + " " + "".join(
            [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")

train_amount = [pow(10, 3), pow(10, 4), pow(10, 5), pow(10, 6), pow(10, 7), pow(10, 8), pow(10, 9)]
for amount in train_amount:
    q_learn_decay.train(amount)
    q_learn_one_step.train(amount)

    game.reset_prize()
    with open("compare_" + str(amount) + "_training.txt", 'w') as f:
        for i in range(10000):
            # Init a single game
            game = Game(players)
            f.write("Game n." + str(i) + " " + "".join(
                [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")
