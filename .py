#This project maskes a card deck 
#The goal is to implement functions like shuffleDeck(), dealOne(), and resetDeck() there have been no real challenges so far
#i did the new functions and charlie did the new menu

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

def shuffleDeck():
    print("shuffleDeck(): Coming soon!")
def dealOne():
    print("dealOne(): Coming soon!")
def resetDeck():
    print("resetDeck(): Coming soon!")
def describeProject():
    print("describeProject(): Coming soon!")
def menu():

        print("\nMenu: Please choose a number:")
        print("1: About/Team")
        print("2: Shuffle Deck")
        print("3: Deal One Card")
        print("4: Reset Deck")
        print("5: Close Program")
        menu_number = int(input("Please select a number: "))

        if menu_number == 1:
            describeProject()
        elif menu_number == 2:
            shuffleDeck()
        elif menu_number == 3:
            dealOne()
        elif menu_number == 4:
            resetDeck()
        elif menu_number == 5:
            print("Exiting code")
            stop = True
        else:
            print("Invalid input!")
menu()
            
                    
    
#Add function stubs for all planned features. 
#Implement one working function: describeProject() (8–12 lines describing goals, next steps, challenges, and learning). This should include  your about page from Task 1. 
#How will you do it 
#Create functions like shuffleDeck(), dealOne(), dealNth(), showTopCard(), resetDeck(), etc. 
#Inside their def, have them all print “Coming soon!” 
#Fully implement and link describeProject() in the menu. 
#How will you test it 
#Select each menu option. Functions should all print a response. You might wish to change the message to be unique for each function. 
#describeProject() prints a full, formatted paragraph. 
#Evidence to submit 
#Screenshot of menu showing new options. 
#Screenshot of code with functions and placeholder text. 
#Screenshot of describeProject() output with the build log for this task. 

