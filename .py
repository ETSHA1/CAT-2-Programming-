#This project maskes a card deck 
#The goal is to implement functions like shuffleDeck(), dealOne(), and resetDeck() there have been no real challenges so far
#i did the new functions and charlie did the new menu
def shuffleDeck():
    print("shuffleDeck(): Coming soon!")
def dealOne():
    print("dealOne(): Coming soon!")
def resetDeck():
    print("resetDeck(): Coming soon!")
def describeProject():
    print("describeProject(): Coming soon!")
def menu():
    stop = False
    while not stop:
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

