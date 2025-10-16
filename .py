import random #gives us random thingys

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f"{self.number} of {self.suit}"

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            raise ValueError("That's not a valid suit!")

class Deck:
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(suit, number) for suit in suits for number in numbers]

    def shuffleDeck(self):
        random.shuffle(self._cards)

    def showTopCards(self, count=3):
        return self._cards[:count]

    def dealCards(self, count=5):
        if count > len(self._cards):
            raise ValueError("Not enough cards left to deal!")
        dealt = self._cards[:count]
        self._cards = self._cards[count:]
        return dealt

    def resetDeck(self):
        self.populate()

    def count(self):
        return len(self._cards)

    def highestCard(self, cards):
        order = {str(n): n for n in range(2, 11)}
        order.update({"J": 11, "Q": 12, "K": 13, "A": 14})
        return max(cards, key=lambda card: order[card.number])

def describeProject():
    print("Project: Enhanced Deck Class")
    print("Features:")
    print("- Builds a 52-card deck")
    print("- Shuffles and shows top 3 cards")
    print("- Deals 5 cards and reports highest")
    print("- Resets deck and confirms count = 52")
    print("- Validates input when dealing")

def test():
    describeProject()
    deck = Deck()
    print("\nInitial deck count:", deck.count())

    deck.shuffleDeck()
    print("\nTop 3 cards after shuffle:")
    for card in deck.showTopCards():
        print(card)

    print("\nDealing 5 cards...")
    hand = deck.dealCards()
    for card in hand:
        print(card)

    print("\nHighest card in hand:", deck.highestCard(hand))

    print("\nDeck count after dealing:", deck.count())

    print("\nResetting deck...")
    deck.resetDeck()
    print("Deck count after reset:", deck.count())

    print("\nTrying to deal 60 cards (should fail):")
    try:
        deck.dealCards(60)
    except ValueError as e:
        print("Error:", e)

test()
