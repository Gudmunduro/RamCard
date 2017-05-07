"""
Guðmundur
Class for ui
27/4/2017
"""

import Functions


class UI:

    @staticmethod
    def display_card(card):
        """Prints out card info"""
        print("--- " + card.name + " ---")
        print("1 Þyngd: " + str(card.weight))
        print("2 Mjólkurlangi dætra: " + str(card.milk))
        print("3 Einkunn ullar: " + str(card.wool))
        print("4 Fjöldi afkvæma: " + str(card.childs))
        print("5 Einkunn læris: " + str(card.hind_legs))
        print("6 Frjósemi: " + str(card.fertility))
        print("7 Þykkt bakvöðva: " + str(card.meat))
        print("8 Enkun fyrir malir: " + str(card.ass))
        print("---------")

    @staticmethod
    def print_score_board(players, attribute, winner):
        """Prints the score board (called after each round)"""
        scores = {}
        for p in players:
            if p.out or len(p.cards) == 0:
                print(p.name + " er úr leik")
                p.out = True
                continue
            scores[p.name] = p.get_top_card()
            print('---------')
            print(p.name)
            print(len(p.cards))
            for i in p.cards:
                print(i.name)
            print('---------')
        print('--- Sigurvegari ---')
        print(winner.name)
        print("--- Stig ---")
        for i in scores:
            print(i, Functions.get_attr(i, attribute, scores))

    @staticmethod
    def print_game_winner(player):
        """Prints the winner of the game"""
        print("------")
        print(player.name + " vann leikinn")
        print("------")

