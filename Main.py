"""
Guðmundur
main class
24/4/2017
"""
from Functions import *
from Game import Game
from Player import Player
from CardSplitter import CardSplitter


class Main:
    """Aðal klasinn í verkefninu"""

    @staticmethod
    def main():
        """Aðal fallið í verkefninu"""
        player_count = intinput("Sláðu inn hversu margir leikmenn eru", 1, 12) + 1
        players = []
        card_splitter = CardSplitter(player_count)
        for i in range(player_count - 1):
            name = input("Sláðu inn nafn leikmanns " + str(i + 1) + ": ")
            cards = card_splitter.get_random_cards()
            players.append(Player(name, cards))
        ai_cards = card_splitter.get_random_cards()
        players.append(Player("Tölva", ai_cards))

        game = Game(players)
        while True:
            game.loop()


if __name__ == '__main__':
    while True:
        Main.main()
