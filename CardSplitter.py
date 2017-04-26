"""
Guðmundur
Card splitter class
24/4/2017
"""
import Reference
from random import randint


class CardSplitter:

    def __init__(self, player_count):
        self.player_count = player_count
        self.remaining_cards = Reference.CARD_LIST

    def get_random_cards(self):
        rnd_card_list = []
        card_count = 52 / self.player_count
        for i in range(card_count):
            rnd_number = randint(0, len(self.remaining_cards) - 1)
            rnd_card_list.append(self.remaining_cards[rnd_number])
            self.remaining_cards.pop(rnd_number)
        return rnd_card_list