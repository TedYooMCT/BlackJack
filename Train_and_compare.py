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
q_learn_one_step1 = QLearningOneStepPlayer(lr=0.1, name="OneStep0.1")
q_learn_one_step01 = QLearningOneStepPlayer(lr=0.01, name="OneStep0.01")
q_learn_one_step2 = QLearningOneStepPlayer(lr=0.2, name="OneStep0.2")
q_learn_one_step05 = QLearningOneStepPlayer(lr=0.05, name="OneStep0.05")
q_learn_decay = QLearningDecayStepPlayer(lr=0.01, gamma=0.95)
# Define who joins the game
players = [base, ex, q_learn_one_step1, q_learn_one_step01, q_learn_one_step2, q_learn_one_step05, q_learn_decay]

# train X times and then compare the results for a 1000 games
with open("compare/compare_before_training - learning rate.txt", 'w') as f:
    for i in range(10000):
        # Init a single game
        game = Game(players)
        f.write("Game n." + str(i) + " " + "".join(
            [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")

train_amount = [pow(10, 3), pow(10, 4), pow(10, 5), pow(10, 6), pow(10, 7)]
for amount in train_amount:
    q_learn_decay.train(amount)
    q_learn_one_step1.train(amount)
    q_learn_one_step01.train(amount)
    q_learn_one_step2.train(amount)
    q_learn_one_step05.train(amount)

    game.reset_prize()
    with open("compare/compare_" + str(amount) + "_training - learning rate.txt", 'w') as f:
        for i in range(10000):
            # Init a single game
            game = Game(players)
            f.write("Game n." + str(i) + " " + "".join(
                [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")
