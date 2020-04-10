from tkinter import Tk, Label, PhotoImage, GROOVE
from src.Board import Board

# Define constants for placement
from src.Cards import Card

FOUNDATIONS_X_CORNER = 934
FOUNDATION_Y_CORNERS = [17, 193, 369, 545]
TOP_TABLEAU_Y_CORNER = 72
TOP_TABLEAU_X_CORNERS = [48, 166, 284, 402, 520, 638, 756]
BOTTOM_TABLEAU_X_CORNERS = [120, 238, 356, 474, 592, 710]
BOTTOM_TABLEAU_Y_CORNER = 489

# Create arrays for placeholder objects
foundations = []



class Mainwindow():

    def __init__(self):

        # Set up frame and window
        self.ROOT = Tk()
        self.EMPTY_FOUNDATION = PhotoImage(file='assets\\foundation.png')
        self.ROOT.config(pady=5)
        self.ROOT.title("Baker's Dozen")
        self.ROOT.geometry("1050x725")

        # Create game board
        self.mainboard = Board(self.ROOT)

        # Place placeholders
        self.place_placeholders()

        # Start the main window loop
        self.ROOT.mainloop()

    def place_placeholders(self):

        # Labels for the foundations
        for x in range(0, 4):
            foundations.append(Label(self.ROOT, image=self.EMPTY_FOUNDATION, relief=GROOVE))
            foundations[x].place(x=FOUNDATIONS_X_CORNER, y=FOUNDATION_Y_CORNERS[x])

        # Labels for the top tableaus
        for x in range(0, 7):
            self.mainboard.tableaus[x].place(x=TOP_TABLEAU_X_CORNERS[x], y=TOP_TABLEAU_Y_CORNER)

        # Labels for the bottom tableaus
        for x in range(7, 13):
            self.mainboard.tableaus[x].place(x=BOTTOM_TABLEAU_X_CORNERS[x - 7], y=BOTTOM_TABLEAU_Y_CORNER)
