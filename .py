import random #gives us random thingys

class Card:#:#make card 
    def __init__(self, suit, number):#store an empty list of cards
        self.suit = suit #the empty list of suit
        self.number = number# the numbers

    def __repr__(self): #creates a string using placeholder values
        return f"{self.number} of {self.suit}"

    @property #the value of self._suit stored within the my_card
    def suit(self):
        return self._suit

    @suit.setter# checks if data is a real suit
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            raise ValueError("That's not a valid suit!")

class Deck:# makes deck for us to use
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):#makes deck have cards
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(suit, number) for suit in suits for number in numbers]

    def shuffleDeck(self):#use random module to randomize card
        random.shuffle(self._cards)

    def showTopCards(self, count=3):#shows top card on deck by selecting first 3 card in cards
        return self._cards[:count] 

 

    def highestCard(self, cards):
        order = {str(n): n for n in range(2, 11)}
        order.update({"J": 11, "Q": 12, "K": 13, "A": 14})
        return max(cards, key=lambda card: order[card.number])

def describeProject():
    print("Project: our sigma aplha card")
    print(" makes a 52-card deck")


