import random

from .Player import Player

num_of_deck = 6
card_of_each = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_of_each_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
one_deck = card_of_each * 4
full_deck = one_deck * num_of_deck


def draw_card():
    return random.choice(full_deck)


class Game:
    def __init__(self, players):
        assert len(players) > 0, "The dealer won't play with himself for fun"
        self.players = players

        for player in self.players:
            player.reset()
            if player.print_plays:
                self.print_plays = True
        if not hasattr(self, "print_plays"):
            self.print_plays = False

        if self.print_plays:
            print("-----------------------------NEW GAME-----------------------------")
        for player in self.players:
            player.card_drawn(draw_card())

        self.dealer_card = draw_card()
        self.dealer = Player("Dealer", print_plays=self.print_plays)
        self.dealer.card_drawn(self.dealer_card)

        for player in self.players:
            player.card_drawn(draw_card())

        self.play()

    def reset_prize(self):
        for player in self.players:
            player.prize = 0

    def play(self):
        rewarded = []
        for player in self.players:
            if player.current_hand_value == 21:
                player.reward(3 / 2, 0)
                rewarded.append(player)
            else:
                stay = False
                while player.current_hand_value < 21 and not stay:
                    if self.print_plays:
                        print(player.name + " turn, dealer first card: " + self.dealer_card)
                        print(player.name + " - Current value: " + str(
                            player.current_hand_value) + " | Total cards: " + str(player.cards))
                    action = player.choose(self.dealer_card)
                    if action == 'S':
                        stay = True
                    if action == 'H':
                        player.card_drawn(draw_card())
                    if action == 'D':
                        player.card_drawn(draw_card())
                        player.double = 2
                        stay = True
                    if action == 'P':
                        # continue playing on this hand until it finished and then play with split variables
                        if player.cards[0] == 'A':
                            player.current_hand_value = 11
                            player.ace_to_use = 1
                        else:
                            player.current_hand_value //= 2
                        player.current_split = player.current_hand_value
                        player.cards_split = [player.cards.pop()]
                        player.ace_to_use_split = player.ace_to_use
                        player.card_drawn(draw_card())
                        player.card_drawn_split(draw_card())
                stay = False
                while 0 < player.current_split < 21 and not stay:
                    player.play_split = True
                    if self.print_plays:
                        print(player.name + " turn, dealer first card: " + self.dealer_card)
                        print(player.name + " - Current value: " + str(
                            player.current_split) + " | Total cards: " + str(player.cards_split))
                    action = player.choose(self.dealer_card)
                    if action == 'S':
                        stay = True
                    if action == 'H':
                        player.card_drawn_split(draw_card())
                    if action == 'D':
                        player.card_drawn_split(draw_card())
                        player.double_split = 2
                        stay = True

        while self.dealer.current_hand_value < 17:
            self.dealer.card_drawn(draw_card())
            if self.print_plays:
                print("Dealer's current_hand_value value: " + str(
                    self.dealer.current_hand_value) + " Dealer's cards: " + str(
                    self.dealer.cards))

        for player in self.players:
            reward = 0
            split_reward = 0
            if player in rewarded:
                continue
            elif player.current_hand_value > 21:
                reward += -1 * player.double
            elif self.dealer.current_hand_value > 21 or player.current_hand_value > self.dealer.current_hand_value:
                reward += 1 * player.double
            elif player.current_hand_value < self.dealer.current_hand_value:
                reward += -1 * player.double

            if player.current_split > 21:
                split_reward = -1 * player.double_split
            elif player.current_split > 0 and (
                    self.dealer.current_hand_value > 21 or player.current_split > self.dealer.current_hand_value):
                split_reward = 1 * player.double_split
            elif 0 < player.current_split < self.dealer.current_hand_value:
                split_reward = -1 * player.double_split

            player.reward(reward, split_reward)

        if self.print_plays:
            print("-----------------------------END GAME-----------------------------")
