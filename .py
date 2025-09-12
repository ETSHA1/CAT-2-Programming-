#looping not done
stop = False  #loop
while not stop:
    # print menu 
    print("Menu: Please choose a number:\n1: About/Team\n2: Our Next Feature:\n3: Close Program")
    menu_number = int(input("Please select a number."))
    if menu_number == 1:
        print("insert about us message")
    elif menu_number == 2:
        print("Coming Soon!")
    elif menu_number == 3:
        print("Exiting code")
        stop = True #ts is for exit 
    else:
        print("Invalid input!")
  
  



