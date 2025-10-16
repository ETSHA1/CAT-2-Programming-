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

def dealOne():
    print("dealOne(): Coming soon!")

def resetDeck():
    print("resetDeck(): Coming soon!")
    
def shuffleDeck(self):#use random module to randomize cards
        random.shuffle(self._cards)

def describeProject():
    print("Project: our sigma aplha card")
    print(" makes a 52-card deck")
    
def aboutTeam():
    print("we are charlie and elijah and we like are humans in like this insane class")
    print("and like they like forced me to like make this i know crazy")
          
   stop = False
    while not stop:
        print("\nMenu: Please choose a number:")
        print("1: About/Team")
        print("2: Shuffle Deck")
        print("3: Deal One Card")
        print("4: Reset Deck")
        print("5: Describe Project")
        print("6: Close Program")
        menu_number = int(input("Please select a number: "))

        if menu_number == 1:
            aboutTeam()
        elif menu_number == 2:
            shuffleDeck()
        elif menu_number == 3:
            dealOne()
        elif menu_number == 4:
            resetDeck()
        elif menu_number == 5:
            describeProject()
        elif menu_number == 6:
            print("Exiting code")
            stop = True
        else:
            print("Invalid input!")
menu()
