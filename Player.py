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
    """Klasi fyrir spilanda"""

    def __init__(self, name, cards, ai=False):
        self.name = name
        self.cards = cards
        self.ai = ai

    def get_top_card(self):
        """Skilar efsta spilinu"""
        return self.cards[len(self.cards) - 1]

    def choose_category(self):
        """Skilar flokknum sem spílandinn valdi"""
        if not self.ai:
            UI.display_card(self.get_top_card())
            return CATEGORY(intinput("Hvaða flokk villtu velja", 1, 8))
        else:
            return randint(1, 8)

    def remove_top_card(self):
        """Tekur í burtu efsta spilið og skilar því"""
        card = self.cards[len(self.cards) - 1]
        self.cards.pop()
        return card

    def add_cards(self, cards):
        """Bætir lista af spilum"""
        self.cards = cards + self.cards
