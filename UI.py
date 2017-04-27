"""
Guðmundur
Classes for ui
27/4/2017
"""


class UI():

    @staticmethod
    def display_card(card):
        print("--- " + card.name + " ---")
        print("Þyngd: " + str(card.weight))
        print("Mjólkurlangi dætra: " + str(card.milk))
        print("Einkunn ullar: " + str(card.wool))
        print("Fjöldi afkvæma: " + str(card.childs))
        print("Einkunn læris: " + str(card.hind_legs))
        print("Frjósemi: " + str(card.fertility))
        print("Þykkt bakvöðva: " + str(card.meat))
        print("Enkun fyrir malir: " + str(card.ass))
        print("---------")
