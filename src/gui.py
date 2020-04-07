from tkinter import Tk, Label, LabelFrame, PhotoImage, GROOVE

# Define constants for padding
X_PADDING = 5
Y_PADDING = 5

# Set up frame and window
ROOT = Tk()
ROOT.config(pady=Y_PADDING)
ROOT.title("Baker's Dozen")
ROOT.geometry("1050x725")

# Define images for components
EMPTY_FOUNDATION = PhotoImage(file='assets\\foundation.png')
EMPTY_TABLEAU = PhotoImage(file='assets\\tableau.png')

# Frame for the top tableaus
TOP_FRAME = LabelFrame(ROOT)
TOP_FRAME.config(borderwidth=0)
TOP_FRAME.grid(row=0, column=0, padx=5*X_PADDING)

# Frame for the foundations
RIGHT_FRAME = LabelFrame(ROOT)
RIGHT_FRAME.config(pady=Y_PADDING, borderwidth=0)
RIGHT_FRAME.grid(row=0, column=1, rowspan=3, padx=50)

# Frame for the bottom tableaus
BOTTOM_FRAME = LabelFrame(ROOT)
BOTTOM_FRAME.config(borderwidth=0)
BOTTOM_FRAME.grid(row=2, column=0)

# Labels for the top tableaus
top_tableaus = []
for x in range(0, 7):
    top_tableaus.append(Label(TOP_FRAME, image=EMPTY_TABLEAU, relief=GROOVE))
    top_tableaus[x].grid(row=0, column=x, padx=X_PADDING, pady=Y_PADDING)

# Labels for the foundations
foundations = []
for x in range(0, 4):
    foundations.append(Label(RIGHT_FRAME, image=EMPTY_FOUNDATION, relief=GROOVE))
    foundations[x].grid(row=x, column=0, padx=X_PADDING, pady=Y_PADDING)

# Labels for the bottom tableaus
bottom_tableaus = []
for x in range(0, 6):
    bottom_tableaus.append(Label(BOTTOM_FRAME, image=EMPTY_TABLEAU, relief=GROOVE))
    bottom_tableaus[x].grid(row=0, column=x, padx=X_PADDING, pady=Y_PADDING)

ROOT.mainloop()