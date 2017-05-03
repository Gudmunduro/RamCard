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
        scores = {}
        for p in players:
            scores[p.name] = p.get_top_card()
        print('--- Sigurvegari ---')
        print(winner)
        print("--- Stig ---")
        for i in scores:
            print(i, Functions.get_attr(i, attribute, scores))
