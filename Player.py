"""
Guðmundur
Player class
24/4/2017
"""


class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def get_top_card(self):
        return self.cards[len(self.cards) - 1]

    def remove_top_card(self):
        self.cards.pop(len(self.cards) - 1)
