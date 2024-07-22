def choose_from_table(self, dealer_card, split_table, hard_table, soft_table):
    """
    :param self: The player class
    :param dealer_card:
    :param split_table: The split table for choosing from
    :param hard_table: The hard table for choosing from
    :param soft_table: The soft table for choosing from
    :return: the choice according to the tables provided
    """
    if dealer_card in ['J', 'Q', 'K']:
        dealer_card = '10'

    lead = self.cards[0] if self.cards[0] not in ['J', 'Q', 'K'] else '10'
    # check if double is possible
    if len(self.cards) == 2 and self.current_split == 0 and self.cards[0] == self.cards[1]:
        action = split_table[dealer_card][lead + '/' + lead]
        # if split aces make it for making a difference from splitting 6s
        table_num = 1 if lead != 'A' else 4
    # check if we play split or not
    elif not self.play_split:
        # check if the hand contains ACE to choose between soft and hard tables
        if self.ace_to_use > 0:
            action = soft_table[dealer_card][self.current_hand_value]
            table_num = 2
        else:
            action = hard_table[dealer_card][self.current_hand_value]
            table_num = 3
    else:
        if self.ace_to_use_split > 0:
            action = soft_table[dealer_card][self.current_split]
            table_num = 2
        else:
            action = hard_table[dealer_card][self.current_split]
            table_num = 3
    if self.print_plays:
        # print(self.table_name + " action is: " + action)
        print("action is: " + action)
    if self.save_plays:
        self.memory.append([table_num, dealer_card, self.current_hand_value, self.current_split])
    return action
