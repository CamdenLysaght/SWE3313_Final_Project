from random import random

from src.Cards import *
from src.Tableaus import Tableau


class Board:

    def __init__(self, mainwindow):
        self.cards = []
        self.tableaus = []
        self.Foundations = []
        self.mainwindow = mainwindow

        self.restart()
        self.shuffle_cards()

    def shuffle_cards(self):
        """ --Shuffles all cards
            --Places 4 cards in each tableau
            --Moves kings to the back of every tableau """
        for card in range(0, 52):
            rand = int(52 * random())
            temp = self.cards[card]
            self.cards[card] = self.cards[rand]
            self.cards[rand] = temp

        for tableau in self.tableaus:
            for x in range(0, 4):
                tableau.add_card(self.cards.pop())

        for tableau in self.tableaus:
            for x in range(0, tableau.get_contents().__len__()):
                current_card = tableau.stack[x].get_rank()
                if current_card == "King":
                    temp = tableau.stack.pop(x)
                    tableau.stack.insert(0, temp)

    def restart(self):
        """ Starts a new game """
        self.cards = []
        for x in range(0, 13):
            self.tableaus.append(Tableau(self.mainwindow))
        # TODO: Initialize all 4 foundations
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(self.mainwindow, suit, rank))


if __name__ == "__main__":
    board1 = Board()
    print("Hold here")
