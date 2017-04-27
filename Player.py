"""
Guðmundur
Player class
24/4/2017
"""
from UI import UI
from random import randint
from Functions import intinput


class Player:

    def __init__(self, name, cards, ai=False):
        self.name = name
        self.cards = cards
        self.ai = ai

    def get_top_card(self):
        return self.cards[len(self.cards) - 1]

    def cardDown(self):
        if (not self.ai):
            UI.display_card(self.get_top_card())
            return intinput("Hvaða flokk villtu velja", 1, 8)
        else:
            return randint(1, 8)

    def remove_top_card(self):
        self.cards.pop()
