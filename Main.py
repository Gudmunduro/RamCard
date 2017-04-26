"""
Guðmundur
main class
24/4/2017
"""
from Functions import *


class Main:

    @staticmethod
    def main():
        Main.player_count = intinput("Sláðu inn hversu margir leikmenn eru", 1, 12)


if __name__ == '__main__':
    Main.main()
