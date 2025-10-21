import random  # gives us random thingys

class Card:  # make card
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self): #creates a string using placeholder values
        return f"{self.number} of {self.suit}"

    @property #the value of self._suit stored within the my_card
    def suit(self):
        return self._suit

    @suit.setter#makes sure the suits are the right one although i doubt we need it 
    def suit(self, suit):#ts is where it looks
        if suit in ["hearts", "clubs", "diamonds", "spades"]:#what the suits should be
            self._suit = suit
        else:
            raise ValueError("That's not a valid suit!")

class Deck:  # makes deck for us to use
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self): #make the cards pretty easy to tell what it is by looking
        suits = ["hearts", "clubs", "diamonds", "spades"]#tuff suits
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]# there is numbers and face cards 
        self._cards = [Card(suit, number) for suit in suits for number in numbers]

    def shuffleDeck(self):#uses that random to shuffle 
        random.shuffle(self._cards)

    def dealOne(self):#ts is 90% your code charlie you should know what it is 
        if self._cards:#use if to make sure there aare cards
            top_card = self._cards.pop()#remove and return the last item from the self.cards list
            print(f"Dealt card: {top_card}")
            print(f"Remaining cards in deck: {len(self._cards)}")
        else:
            print("No cards left to deal :( use reset funtion.")

    def resetDeck(self):#idk bro ts was easy then i thought
        self.populate()#legit just running this function
        print("Deck reset! you can keep playing!!!!!")


deck = Deck()#i forgot to make deck for way too long so here it is

def describeProject():#you dont need me to tell you what print does
    print("Project: our super useful card deck")
    print("Makes a 52 card deck, shuffles, deals, and resets so unbeliveably useful.")

def aboutTeam():#you know what print is
    print("We are Charlie and Elijah and we like are humans in like this insane class")
    print("And like they like forced me to like make this I know crazy!!!!!!!")

def menu():#menu funtion you did this
    stop = False
    while not stop:
        print("\nMenu: Please choose a number:")
        print("1: About/Team")
        print("2: Shuffle Deck")
        print("3: Deal One Card")
        print("4: Reset Deck")
        print("5: Describe Project")
        print("6: Close Program")
        try:
            menu_number = int(input("Please select a number: "))
        except ValueError:
            print("That is not a number. I request you put a number.")
            continue

        if menu_number == 1:
            aboutTeam()
        elif menu_number == 2:
            deck.shuffleDeck()
            print("Deck shuffled!")
        elif menu_number == 3:
            deck.dealOne()
        elif menu_number == 4:
            deck.resetDeck()
        elif menu_number == 5:
            describeProject()
        elif menu_number == 6:
            print("Exiting code")
            stop = True
        else:
            print("Invalid input!")

menu()
