from Game.Game import Game
from Players.RLPlayers.QLearningDecayStep import QLearningDecayStepPlayer
from Players.RLPlayers.QLearningOneStep import QLearningOneStepPlayer
from Players.TablesPlayers.BasicPlayer import BasicPlayer
from Players.TablesPlayers.ExpectancyPlayer import ExpectancyPlayer

# Define the players (True or False for printing the computer moves)
# me = HumanPlayer("Bar")
# rand = RandomPlayer(False, save_plays=True)
base = BasicPlayer(print_plays=False, save_plays=True)
ex = ExpectancyPlayer(False, save_plays=True)
q_learn_one = QLearningOneStepPlayer(lr=0.008)
q_learn_decay90 = QLearningDecayStepPlayer(lr=0.01, gamma=0.9, name="90")
q_learn_decay95 = QLearningDecayStepPlayer(lr=0.01, gamma=0.95, name="95")
q_learn_decay99 = QLearningDecayStepPlayer(lr=0.01, gamma=0.99, name="99")
q_learn_decay85 = QLearningDecayStepPlayer(lr=0.01, gamma=0.85, name="85")
q_learn_decay80 = QLearningDecayStepPlayer(lr=0.01, gamma=0.80, name="80")
# Define who joins the game
players = [base, ex, q_learn_one, q_learn_decay90, q_learn_decay95, q_learn_decay99, q_learn_decay80, q_learn_decay85]

# train X times and then compare the results for 1000 games
with open("compare/compare_before_training - learning rate.txt", 'w') as f:
    for i in range(10000):
        # Init a single game
        game = Game(players)
        f.write("Game n." + str(i) + " " + "".join(
            [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")

train_amount = [pow(10, 3), pow(10, 4), pow(10, 5), pow(10, 6), pow(10, 7)]
for amount in train_amount:
    for player in players[2:]:
        player.train(amount)
    game.reset_prize()
    with open("compare/compare_" + str(amount) + "_training - learning rate.txt", 'w') as f:
        for i in range(10000):
            # Init a single game
            game = Game(players)
            f.write("Game n." + str(i) + " " + "".join(
                [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")
