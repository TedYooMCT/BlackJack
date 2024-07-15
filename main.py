import Game
import Players as P


# Define the players (True or False for printing the computer moves)
user_name = input("Enter your name: ")
print("Hey " + user_name + "! welcome to Bar's Blackjack game")
user_input = input("Choose your Rivals (enter the initial only/T for start playing) - Random | Basic | Expectancy | "
                   "Qlearning: ")
players = [P.Human(user_name)]
while user_input != "T":
    if user_input == "R":
        players.append(P.Random(False, save_plays=True))
    elif user_input == "B":
        players.append(P.Basic(print_plays=False, save_plays=True))
    elif user_input == "E":
        players.append(P.Expectancy(False, save_plays=True))
    elif user_input == "Q":
        players.append(P.QLOneStep())
    else:
        print("Invalid choice")
    user_input = input(
        "Choose your Rivals (enter the initial only/T for start playing) - Random | Basic | Expectancy | "
        "Qlearning: ")


i = 0
while i < 5:
    # Init a single game
    game = Game.Game(players)
    i = i + 1
    print("Game n." + str(i) + " " + "".join(
        [player.name + " prize is : " + str(player.prize) + " , " for player in players]) + "\n")