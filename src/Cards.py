from tkinter import Label, PhotoImage, GROOVE

SUITS = ["Club", "Diamond", "Heart", "Spade"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card(Label):
    def __init__(self, mainwindow, suit, rank, **kw):
        """ Constructor for cards. Each card may have:
            -- Suit: Spade, Heart, Club, or Diamond
            -- Rank: 2 - 10, Jack, Queen, King, or Ace
            -- Draggable: Whether the card can be drug by the mouse """
        self.suit = suit
        self.rank = rank
        self.draggable = True
        self.image = PhotoImage(file='assets\\' + self.rank + self.suit + '.png')
        super().__init__(master=mainwindow, image=self.image, relief=GROOVE, **kw)

    def __str__(self):
        return "Card object: " + self.rank + " of " + self.suit + "s"

    def get_suit(self):
        """ Returns the suit of the card """
        return self.suit

    def get_rank(self):
        """ Returns the rank of the card """
        return self.rank

    def set_draggable(self, draggable):
        """ Sets the draggable property of the card """
        self.draggable = draggable

    def is_draggable(self):
        """ Returns whether the card is draggable or not """
        return self.draggable