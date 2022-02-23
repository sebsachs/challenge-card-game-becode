from card.py import Card
from card.py import Symbol

class Player():
    def __init__(self):
        self.number_of_cards = 0
        self.turn_count = 0
        self.cards = []
        self.history = []




    def play(self):
        variable = random.choice(cards)
        history.append(random.choice(cards))
        print(f"{self.name} played {card.value} {card.icon}")
        return variable
class Deck():
    def __init__(self):
        self.cards = []
    def fill_deck(self):
        for j in Card.value_options:
            self.cards.append(Card("red", '♥', j))
            self.cards.append(Card("red", ' ♦', j))
            self.cards.append(Card("black", '♣', j))
            self.cards.append(Card("black",  '♠', j))
    def shuffle(self):
        shuffle(self.cards)
    def distribute(self):


















