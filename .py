class Card:#make card 
    def __init__(self, suit, number):#store an empty list of cards
        self.suit = suit#the suit
        self.number = number# the numbers

    def __repr__(self): #creates a string using placeholder values
        return f"{self.number} of {self.suit}"

    @property #the value of self._suit stored within the my_card
    def suit(self):
        return self._suit

    @suit.setter # checks if data is a real suit
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            raise ValueError("That's not a valid suit!")

class Deck:# makes deck for us to use
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self): #makes deck have cards
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(suit, number) for suit in suits for number in numbers]

def test(): #tests if works
    print("Creating a new deck...")
    deck = Deck()

    print("\nTotal cards in deck:", len(deck._cards))
    print("\nFirst five cards in the deck:")
    for card in deck._cards[:5]:
        print(card)

    print("\nLast five cards in the deck:")
    for card in deck._cards[-5:]:
        print(card)

test()
