SUITS = ["Club", "Diamond", "Heart", "Spade"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, suit, rank):
        """ Constructor for cards. Each card may have:
            -- Suit: Spade, Heart, Club, or Diamond
            -- Rank: 2 - 10, Jack, Queen, King, or Ace
            -- Draggable: Whether the card can be drug by the mouse """
        self.suit = suit
        self.rank = rank
        self.draggable = True
        self.image_path = 'assets\\' + self.rank + self.suit + '.png'

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