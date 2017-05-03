"""
Guðmundur
Player class
24/4/2017
"""
from UI import UI
from random import randint
from Functions import intinput
from Reference import *


class Player:
    """Class for player"""

    def __init__(self, name, cards, ai=False):
        self.name = name
        self.cards = cards
        self.ai = ai

    def get_top_card(self):
        """Returns top card"""
        return self.cards[-1]

    def choose_category(self):
        """Returns attribute witch player selected"""
        if not self.ai:
            UI.display_card(self.get_top_card())
            return CATEGORY(intinput("Hvaða flokk villtu velja", 1, 8))
        else:
            return randint(1, 8)

    def remove_top_card(self):
        """pops top card and returns it"""
        card = self.cards[len(self.cards) - 1]
        self.cards.pop()
        return card

    def add_cards(self, cards):
        """Add cards to list"""
        self.cards = cards + self.cards
