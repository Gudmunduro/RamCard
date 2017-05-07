"""
Guðmundur
game main class
26/4/2017
"""
from Reference import *
from Player import Player
from UI import UI
from Functions import *


class Game:
    """main class for the game"""

    def __init__(self, players):
        self.players = players
        self.current_player_id = 0
        self.state = 0
        self.extra_card_players = []
        self.leftover_cards = []
        self.state2_current_player_id = 0
        self.card_count = 0
        self.restart_game = False

    def current_player(self):
        """retunes the current player"""
        return self.players[self.current_player_id]

    def set_current_player_to_next_player(self):
        """sets current player id to the id of next player"""
        if len(self.players) - 1 <= self.current_player_id:
            self.current_player_id = 0
        else:
            self.current_player_id += 1

    def get_top_cards(self):
        """returns the top card for all players"""
        cards = []
        for p in self.players:
            if not p.out:
                cards.append(p.get_top_card())
        return cards

    def remove_top_cards(self):
        """removes the top card for all players"""
        for p in self.players:
            if not p.out:
                p.remove_top_card()

    def values_for_category(self, category):
        """returns a list of the values for category of the top card for all players"""
        values = []
        for i in range(len(self.players)):
            if self.players[i].out or len(self.players[i].cards) == 0:
                self.players[i].out = True
                continue
            if category == CATEGORY.WEIGHT:
                values.append(self.players[i].get_top_card().weight)
            elif category == CATEGORY.MILK:
                values.append(self.players[i].get_top_card().milk)
            elif category == CATEGORY.WOOL:
                values.append(self.players[i].get_top_card().wool)
            elif category == CATEGORY.CHILDS:
                values.append(self.players[i].get_top_card().childs)
            elif category == CATEGORY.HIND_LEGS:
                values.append(self.players[i].get_top_card().hind_legs)
            elif category == CATEGORY.FERTILITY:
                values.append(self.players[i].get_top_card().fertility)
            elif category == CATEGORY.MEAT:
                values.append(self.players[i].get_top_card().meat)
            elif category == CATEGORY.ASS:
                values.append(self.players[i].get_top_card().ass)
        return values

    def find_player_with_highest_of(self, category):
        """Returns player with higest value in a category"""
        values = self.values_for_category(category)
        return self.players[values.index(max(values))]

    def all_players_out_except_one(self):
        """returns true or false based on if there is only one player remaining or not"""
        count = 0
        for p in self.players:
            if p.out:
                count += 1
        return count > 1


    def check_for_game_winner(self):
        """checks of if any player has won the game"""
        for p in self.players:
            if len(p.cards) == self.card_count or self.all_players_out_except_one():
                UI.print_game_winner(p)
                if question("Villtu spila leikinn aftur"):
                    self.restart_game = True
                    return
                else:
                    exit()

    def check_for_zero_cards(self):
        """checks if any player has zero cards ands sets out to True on those players"""
        for p in self.players:
            if len(p.cards) == 0:
                p.out = True


    def two_players_with_same_value(self, category):
        """returns true or false based on if 2 players have same value"""
        values = self.values_for_category(category)
        return int(values.count(max(values))) > int(1)

    def get_players_with_same_value(self, category):
        """returns list of players which have highest of category"""
        values = self.values_for_category(category)
        players = []
        for i in range(len(values)):
            if values[i] == max(values):
                players.append(self.players[i])
        return players

    def do_winner_stuff(self, category):
        """the function that needs a better name"""
        player = self.find_player_with_highest_of(category)
        cards = []
        for p in self.players:
            if p != player:
                if p.out or len(p.cards) == 0:
                    p.out = True
                    continue
                else:
                    cards.append(p.remove_top_card())
        player.add_cards(cards)
        player.move_top_card_to_bottom()
        UI.print_score_board(self.players, category, player)
        self.set_current_player_to_next_player()

    # -------- state 2 --------
    """
        State 2 is when two or more players have the highest value
    """

    def state2_current_player(self):
        """returns the current player(in state 2)"""
        return self.extra_card_players[self.state2_current_player_id]

    def state2_set_current_player_to_next_player(self):
        """Setur current_player_id í spilandann sem á að gera næst(in state 2)"""
        if len(self.extra_card_players) >= self.state2_current_player_id:
            self.state2_current_player_id = 0
        else:
            self.state2_current_player_id += 1

    def state2_find_player_with_highest_of(self, category):
        """Returns player with highest value in a category(in state 2)"""
        values = self.state2_values_for_category(category)
        return self.extra_card_players[values.index(max(values))]

    def state2_get_top_cards(self):
        """returns the top card for all players(in state 2)"""
        cards = []
        for p in self.extra_card_players:
            if not p.out:
                cards.append(p.get_top_card())
        return cards

    def state2_remove_top_cards(self):
        """removes the top card for all players(in state 2)"""
        for p in self.extra_card_players:
            if not p.out:
                p.remove_top_card()

    def state2_do_winner_stuff(self, category):
        """Called when player wins a round(in state 2)"""
        self.state = 0
        player = self.state2_find_player_with_highest_of(category)
        cards = []
        for p in self.extra_card_players:
            if p != player:
                if p.out or len(p.cards) == 0:
                    p.out = True
                    continue
                else:
                    cards.append(p.remove_top_card())
        player.add_cards(self.leftover_cards)
        player.add_cards(cards)
        player.move_top_card_to_bottom()
        UI.print_score_board(self.extra_card_players, category, player)

    def state2_values_for_category(self, category):
        """returns a list of the values for category of the top card for all players(in state 2)"""
        values = []
        for i in range(len(self.extra_card_players)):
            if self.extra_card_players[i].out or len(self.extra_card_players[i].cards) == 0:
                self.extra_card_players[i].out = True
                continue
            if category == CATEGORY.WEIGHT:
                values.append(self.extra_card_players[i].get_top_card().weight)
            elif category == CATEGORY.MILK:
                values.append(self.extra_card_players[i].get_top_card().milk)
            elif category == CATEGORY.WOOL:
                values.append(self.extra_card_players[i].get_top_card().wool)
            elif category == CATEGORY.CHILDS:
                values.append(self.extra_card_players[i].get_top_card().childs)
            elif category == CATEGORY.HIND_LEGS:
                values.append(self.extra_card_players[i].get_top_card().hind_legs)
            elif category == CATEGORY.FERTILITY:
                values.append(self.extra_card_players[i].get_top_card().fertility)
            elif category == CATEGORY.MEAT:
                values.append(self.extra_card_players[i].get_top_card().meat)
            elif category == CATEGORY.ASS:
                values.append(self.extra_card_players[i].get_top_card().ass)
        return values

    def state2_two_players_with_same_value(self, category):
        """ returns true or falce based on if 2 players have same value(in state 2)"""
        values = self.state2_values_for_category(category)
        return int(values.count(max(values))) > int(1)

    def state2_get_players_with_same_value(self, category):
        """returnes list of players which have higest of category(in state 2)"""
        values = self.state2_values_for_category(category)
        players = []
        for i in range(len(values)):
            if values[i] == max(values):
                players.append(self.extra_card_players[i])
        return players

    def state2(self):
        """The main loop in state 2"""
        self.check_for_game_winner()
        if self.state2_current_player().out:
            self.state2_set_current_player_to_next_player()
            return
        print("--- " + self.state2_current_player().name + " ---")
        category = self.state2_current_player().choose_category()
        if self.state2_two_players_with_same_value(category):
            players = self.state2_get_players_with_same_value(category)
            print("Það fengu fleiri en einn hæðstu töluna aftur")
            self.extra_card_players = players
            self.leftover_cards = self.leftover_cards + self.state2_get_top_cards()
            self.state2_remove_top_cards()
        else:
            self.state2_do_winner_stuff(category)

    ######################################################################

    def loop(self):
        """main game loop"""
        self.check_for_game_winner()
        if self.restart_game:
            return
        self.check_for_zero_cards()
        if self.state == 1:
            self.state2()
        if self.current_player().out:
            self.set_current_player_to_next_player()
            return
        print("--- " + self.current_player().name + " ---")
        category = self.current_player().choose_category()
        if self.two_players_with_same_value(category):
            players = self.get_players_with_same_value(category)
            print("Það fengu fleiri en einn hæðstu töluna")
            self.extra_card_players = players
            self.leftover_cards = self.get_top_cards()
            self.remove_top_cards()
            self.state = 1
        else:
            self.do_winner_stuff(category)
