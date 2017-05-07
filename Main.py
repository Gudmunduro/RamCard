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
    """Main Class"""

    @staticmethod
    def main():
        """Main Function"""
        player_count = intinput("Sláðu inn hversu margir leikmenn eru", 1, 12) + 1
        players = []
        card_splitter = CardSplitter(player_count)
        card_count = 0
        for i in range(player_count - 1):
            name = input("Sláðu inn nafn leikmanns " + str(i + 1) + ": ")
            cards = card_splitter.get_random_cards()
            card_count += len(cards)
            players.append(Player(name, cards))
        ai_cards = card_splitter.get_random_cards()
        card_count += len(ai_cards)
        players.append(Player("Tölva", ai_cards))
        players[len(players) - 1].ai = True

        game = Game(players)
        game.card_count = card_count
        while True:
            game.loop()
            if game.restart_game:
                debug("restarting")
                return


if __name__ == '__main__':
    while True:
        Main.main()
