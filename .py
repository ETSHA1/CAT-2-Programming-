stop = False  
while not stop:
    print("Menu: Please choose a number:\n1: About/Team\n2: Our Next Feature:\n3: Close Program")
    menu_number = int(input("Please select a number."))
    if menu_number == 1:
        print("insert about us message")
    elif menu_number == 2:
        print("Coming Soon!")
    elif menu_number == 3:
        print("Exiting code")
        stop = True 
    else:
        print("Invalid input!")
def shuffleDeck():
    print("shuffleDeck(): Coming soon!")
def dealOne():
    print("dealOne(): Coming soon!")
def dealNth():
    print("dealNth(): Coming soon!")
def showTopCard():
    print("showTopCard(): Coming soon!")
def resetDeck():
    print("resetDeck(): Coming soon


Add function stubs for all planned features. 
Implement one working function: describeProject() (8–12 lines describing goals, next steps, challenges, and learning). This should include  your about page from Task 1. 
How will you do it 
Create functions like shuffleDeck(), dealOne(), dealNth(), showTopCard(), resetDeck(), etc. 
Inside their def, have them all print “Coming soon!” 
Fully implement and link describeProject() in the menu. 
How will you test it 
Select each menu option. Functions should all print a response. You might wish to change the message to be unique for each function. 
describeProject() prints a full, formatted paragraph. 
Evidence to submit 
Screenshot of menu showing new options. 
Screenshot of code with functions and placeholder text. 
Screenshot of describeProject() output with the build log for this task. 
