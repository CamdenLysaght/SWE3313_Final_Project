class Tableau:

    def __init__(self):
        self.stack = []

    def add_card(self, card):
        self.stack.append(card)

    def get_contents(self):
        return self.stack
