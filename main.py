from Game import Game
from Players.HumanPlayer import HumanPlayer
from Players.RLPlayers.QLearningOneStep import QLearningOneStepPlayer
from Players.RandomPlayer import RandomPlayer
from Players.TablesPlayers.BasicPlayer import BasicPlayer
from Players.TablesPlayers.ExpectancyPlayer import ExpectancyPlayer

# Define the players (True or False for printing the computer moves)
user_name = input("Enter your name: ")
print("Hey " + user_name + "! welcome to Bar's Blackjack game")
user_input = input("Choose your Rivals (enter the initial only/T for start playing) - Random | Basic | Expectancy | "
                   "Qlearning: ")
players = [HumanPlayer(user_name)]
while user_input != "T":
    if user_input == "R":
        players.append(RandomPlayer(False, save_plays=True))
    elif user_input == "B":
        players.append(BasicPlayer(print_plays=False, save_plays=True))
    elif user_input == "E":
        players.append(ExpectancyPlayer(False, save_plays=True))
    elif user_input == "Q":
        players.append(QLearningOneStepPlayer())
    else:
        print("Invalid choice")
    user_input = input(
        "Choose your Rivals (enter the initial only/T for start playing) - Random | Basic | Expectancy | "
        "Qlearning: ")
i = 0
while True:
    # Init a single game
    game = Game(players)
    i = i + 1
    print("Game n." + str(i) + " " + "".join(
        [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")