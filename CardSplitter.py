"""
Guðmundur
Card splitter class
24/4/2017
"""
import Reference
from random import randint
from Sort_info import Sort
from Functions import debug


class CardSplitter:
    """Class witch splits cards between players"""

    def __init__(self, player_count):
        sort = Sort()
        sort.main()
        self.player_count = player_count
        self.remaining_cards = sort.card_list

    def get_random_cards(self):
        """Returns random cards for player in a list."""
        rnd_card_list = []
        card_count = int(52 / self.player_count)
        for i in range(card_count):
            rnd_number = randint(0, len(self.remaining_cards) - 1)
            rnd_card_list.append(self.remaining_cards[rnd_number])
            self.remaining_cards.pop(rnd_number)
        debug(rnd_card_list)
        return rnd_card_list
