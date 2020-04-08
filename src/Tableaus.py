from tkinter import Label, PhotoImage, GROOVE


class Tableau(Label):

    def __init__(self, mainwindow, **kw):
        self.image = PhotoImage(file='assets\\tableau.png')
        self.relief = GROOVE
        super().__init__(master=mainwindow, image=self.image, relief=self.relief, **kw)
        self.stack = []

    def __str__(self):
        return "Tableau object of type " + str(type(self))

    def add_card(self, card):
        self.stack.append(card)

    def get_contents(self):
        return self.stack
