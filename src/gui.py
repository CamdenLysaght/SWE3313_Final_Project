from tkinter import Tk, Label, PhotoImage, GROOVE
from src.Board import Board

# Define constants for placement
FOUNDATIONS_X_CORNER = 934
FOUNDATION_Y_CORNERS = [17, 193, 369, 545]
TOP_TABLEAU_Y_CORNER = 72
TOP_TABLEAU_X_CORNERS = [48, 166, 284, 402, 520, 638, 756]
BOTTOM_TABLEAU_X_CORNERS = [120, 238, 356, 474, 592, 710]
BOTTOM_TABLEAU_Y_CORNER = 489

# Set up frame and window
ROOT = Tk()
ROOT.config(pady=5)
ROOT.title("Baker's Dozen")
ROOT.geometry("1050x725")

# Create game board
mainboard = Board()

# Create arrays for placeholder objects
foundations = []
top_tableaus = []
bottom_tableaus = []

# Define images for components
EMPTY_FOUNDATION = PhotoImage(file='assets\\foundation.png')
EMPTY_TABLEAU = PhotoImage(file='assets\\tableau.png')


def place_placeholders():
    # Labels for the foundations
    for x in range(0, 4):
        foundations.append(Label(ROOT, image=EMPTY_FOUNDATION, relief=GROOVE))
        foundations[x].place(x=FOUNDATIONS_X_CORNER, y=FOUNDATION_Y_CORNERS[x])

    # Labels for the top tableaus
    for x in range(0, 7):
        top_tableaus.append(Label(ROOT, image=EMPTY_TABLEAU, relief=GROOVE))
        top_tableaus[x].place(x=TOP_TABLEAU_X_CORNERS[x], y=TOP_TABLEAU_Y_CORNER)

    # Labels for the bottom tableaus
    for x in range(0, 6):
        bottom_tableaus.append(Label(ROOT, image=EMPTY_TABLEAU, relief=GROOVE))
        bottom_tableaus[x].place(x=BOTTOM_TABLEAU_X_CORNERS[x], y=BOTTOM_TABLEAU_Y_CORNER)


place_placeholders()
ROOT.mainloop()
