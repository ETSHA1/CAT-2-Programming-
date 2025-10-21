#This project maskes a card deck 
#The goal is to implement functions like shuffleDeck(), dealOne(), and resetDeck() there have been no real challenges so far
#i did the new functions and charlie did the new menu
def aboutTeam():
    print("aboutTeam(): Coming soon!")
def shuffleDeck():
    print("shuffleDeck(): Coming soon!")
def dealOne():
    print("dealOne(): Coming soon!")
def resetDeck():
    print("resetDeck(): Coming soon!")
def describeProject():
    print("describeProject(): This project is designed to be a fun card game that anyone can learn easily and relax with!")
def menu():
    #these just define terms and saves us time and makes the code cleaner
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

