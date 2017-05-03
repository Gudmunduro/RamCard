"""
Guðmundur
game main class
26/4/2017
"""
from Reference import *
from Player import Player
from UI import UI


class Game:
    """Aðal klasinn fyrir leikinn sjálfan"""

    def __init__(self, players):
        self.players = players
        self.current_player_id = 0
        self.state = 0
        self.extra_card_players = []
        self.leftover_cards = []

    def current_player(self):
        """Skilar núverandi spilanda"""
        return self.players[self.current_player_id]

    def set_current_player_to_next_player(self):
        """Setur current_player_id í spilandann sem á að gera næst"""
        if len(self.players) >= self.current_player_id:
            self.current_player_id = 0
        else:
            self.current_player_id += 1

    def values_for_category(self, category):
        """Skilar lista af einkun fyrir tiltekin eiginleika fyrir alla spilendur"""
        values = []
        for i in range(len(self.players)):
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
        """Skilar spilenda með hæstu einkunn af eiginleika"""
        values = self.values_for_category(category)
        return self.players[values.index(max(values))]

    def two_players_with_same_value(self, category):
        """Skilar true eða false eftir því hvort tveir spilendur séu með sömu tölu eða ekki"""
        values = self.values_for_category(category)
        return values.count(max(values)) > 1

    def get_players_with_same_value(self, category):
        """Skilar lista af spilendum sem eru með hæstu einkunnina af eiginleika"""
        values = self.values_for_category(category)
        players = []
        for i in range(len(values)):
            if values[i] == max(values):
                players.append(self.players[i])
        return players

    def do_winner_stuff(self, category):
        """Þetta function þarf "betra" nafn"""
        player = self.find_player_with_highest_of(category)
        cards = []
        for p in self.players:
            if p != player:
                cards.append(player.remove_top_card())
        player.add_cards(cards)
        UI.print_score_board(self.players, category)
        self.set_current_player_to_next_player()

    # - state 2 -

    def state2_current_player(self):
        pass

    def state2_do_winner_stuff(self):
        pass

    def state2_values_for_category(self, category):
        """Skilar lista af einkun fyrir tiltekin eiginleika fyrir alla spilendur"""
        values = []
        for i in range(len(self.extra_card_players)):
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
        """Skilar true eða false eftir því hvort tveir spilendur séu með sömu tölu eða ekki"""
        values = self.values_for_category(category)
        return values.count(max(values)) > 1

    def state2_get_players_with_same_value(self, category):
        """Skilar lista af spilendum sem eru með hæstu einkunnina af eiginleika"""
        values = self.state2_values_for_category(category)
        players = []
        for i in range(len(values)):
            if values[i] == max(values):
                players.append(self.players[i])
        return players

    def state2(self):
        print("--- " + self.state2_current_player().name + " ---")
        category = self.state2_current_player().choose_category()
        if self.state2_two_players_with_same_value(category):
            players = self.state2_get_players_with_same_value(category)
            """Þessi partur er ekki tilbúinn"""
            print("Það fengu fleiri en einn hæðstu töluna")
            self.extra_card_players = players
            self.leftover_cards = self.values_for_category(category)
            self.state = 1
        else:
            self.do_winner_stuff(category)


    # -         -

    def loop(self):
        """Aðal loopan í leiknum"""
        if self.state == 1:
            self.state2()
        print("--- " + self.current_player().name + " ---")
        category = self.current_player().choose_category()
        if self.two_players_with_same_value(category):
            players = self.get_players_with_same_value(category)
            """Þessi partur er ekki tilbúinn"""
            print("Það fengu fleiri en einn hæðstu töluna")
            self.extra_card_players = players
            self.leftover_cards = self.values_for_category(category)
            self.state = 1
        else:
            self.do_winner_stuff(category)
