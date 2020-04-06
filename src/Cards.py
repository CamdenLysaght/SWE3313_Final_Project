class Card:
    def __init__(self, suit, rank):
        """ Constructor for cards. Each card may have:
            -- Suit: Spade, Heart, Club, or Diamond
            -- Rank: 2 - 10, Jack, Queen, Kind, or Ace
            -- Draggable: Whether the card can be drug by the mouse """
        self.suit = suit
        self.rank = rank
        self.draggable = True

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