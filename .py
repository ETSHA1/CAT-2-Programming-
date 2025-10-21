stop = False  #loop
while not stop:
    # print menu
    print("Menu:\nWelcome to Elijah & Charlie’s card deck game. Please choose a number:\n1: About/Team\n2: Our Next Feature:\n3: Close Program")
    menu_number = int(input("Please select a number. "))
    if menu_number == 1:
        print("We are a small company that specialises in games based in Python!")
    elif menu_number == 2:
        print("Coming Soon!")
    elif menu_number == 3:
        print("Exiting code")
        stop = True 
    else:
        print("Invalid input!")
  
  



