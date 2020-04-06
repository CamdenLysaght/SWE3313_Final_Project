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
EMPTY_FOUNDATION = PhotoImage(file='cards\\foundation.png')
EMPTY_TABLEAU = PhotoImage(file='cards\\tableau.png')


# Frame for the top tableaus
TOP_TABLEAUS = LabelFrame(ROOT)
TOP_TABLEAUS.config(borderwidth=0)
TOP_TABLEAUS.grid(row=0, column=0)

# Buttons for the top tableaus
TOP_TABLEAU1 = Label(TOP_TABLEAUS, relief=GROOVE)
TOP_TABLEAU1.config(image=EMPTY_TABLEAU)
TOP_TABLEAU1.grid(row=0, column=0, padx=5*X_PADDING, pady=Y_PADDING)

TOP_TABLEAU2 = Label(TOP_TABLEAUS)
TOP_TABLEAU2.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU2.grid(row=0, column=1, padx=X_PADDING, pady=Y_PADDING)

TOP_TABLEAU3 = Label(TOP_TABLEAUS)
TOP_TABLEAU3.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU3.grid(row=0, column=2, padx=X_PADDING, pady=Y_PADDING)

TOP_TABLEAU4 = Label(TOP_TABLEAUS)
TOP_TABLEAU4.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU4.grid(row=0, column=3, padx=X_PADDING, pady=Y_PADDING)

TOP_TABLEAU5 = Label(TOP_TABLEAUS)
TOP_TABLEAU5.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU5.grid(row=0, column=4, padx=X_PADDING, pady=Y_PADDING)

TOP_TABLEAU6 = Label(TOP_TABLEAUS)
TOP_TABLEAU6.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU6.grid(row=0, column=5, padx=X_PADDING, pady=Y_PADDING)

TOP_TABLEAU7 = Label(TOP_TABLEAUS)
TOP_TABLEAU7.config(image=EMPTY_TABLEAU, relief=GROOVE)
TOP_TABLEAU7.grid(row=0, column=6, padx=X_PADDING, pady=Y_PADDING)

# Frame for the foundations
FOUNDATIONS = LabelFrame(ROOT)
FOUNDATIONS.config(pady=Y_PADDING, borderwidth=0)
FOUNDATIONS.grid(row=0, column=1, rowspan=3, padx=50)

# Labels for the foundations
FOUNDATION1 = Label(FOUNDATIONS)
FOUNDATION1.config(image=EMPTY_FOUNDATION, relief=GROOVE)
FOUNDATION1.grid(row=0, column=0, padx=X_PADDING, pady=Y_PADDING)

FOUNDATION2 = Label(FOUNDATIONS)
FOUNDATION2.config(image=EMPTY_FOUNDATION, relief=GROOVE)
FOUNDATION2.grid(row=1, column=0, padx=X_PADDING, pady=Y_PADDING)

FOUNDATION3 = Label(FOUNDATIONS)
FOUNDATION3.config(image=EMPTY_FOUNDATION, relief=GROOVE)
FOUNDATION3.grid(row=2, column=0, padx=X_PADDING, pady=Y_PADDING)

FOUNDATION4 = Label(FOUNDATIONS)
FOUNDATION4.config(image=EMPTY_FOUNDATION, relief=GROOVE)
FOUNDATION4.grid(row=3, column=0, padx=X_PADDING, pady=Y_PADDING)

# Frame for the bottom tableaus
BOTTOM_TABLEAUS = LabelFrame(ROOT)
BOTTOM_TABLEAUS.config(borderwidth=0)
BOTTOM_TABLEAUS.grid(row=2, column=0)

# Labels for the bottom tableaus
BOTTOM_TABLEAU1 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU1.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU1.grid(row=0, column=0, padx=X_PADDING, pady=Y_PADDING)

BOTTOM_TABLEAU2 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU2.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU2.grid(row=0, column=1, padx=X_PADDING, pady=Y_PADDING)

BOTTOM_TABLEAU3 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU3.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU3.grid(row=0, column=2, padx=X_PADDING, pady=Y_PADDING)

BOTTOM_TABLEAU4 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU4.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU4.grid(row=0, column=3, padx=X_PADDING, pady=Y_PADDING)

BOTTOM_TABLEAU5 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU5.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU5.grid(row=0, column=4, padx=X_PADDING, pady=Y_PADDING)

BOTTOM_TABLEAU6 = Label(BOTTOM_TABLEAUS)
BOTTOM_TABLEAU6.config(image=EMPTY_TABLEAU, relief=GROOVE)
BOTTOM_TABLEAU6.grid(row=0, column=5, padx=X_PADDING, pady=Y_PADDING)

ROOT.mainloop()