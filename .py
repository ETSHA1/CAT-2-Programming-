#looping not done
stop = False  #loop

while stop == False:
    # print menu 
    print("Menu please chode a number:")
    print("1: About/Team")
    print("2: Our Next Feature")
    print("3: Close Program")
    menu_number = int(input("Enter 1 for About/Team Enter 2 for our next feature Enter 3 for closing our program."))
    if menu_number == 1:
        print("insert about us message")
    elif menu_number == 2:
        print("Coming Soon!")
    elif menu_number == 3:
        print("Exiting code")
        stop is True #ts is for exit 
    else:
        print("Invalid input!")
  
  

'Create main.py with a variable called stop that is set to False.'
'Then, create a while stop == False loop. Inside the loop, the menu should  do the following:'
'Print "1: About/Team" 
'If the user types 1: the menu prints the about us message.' 
'Print "2: Our Next Feature" 
'If the user types 2: the menu prints "Coming Soon!" 
'Print "3: Close Program" 
'If the user types 3: The program sets stop to True'
