def menu():
    active = True
    menuItems = ["New Password", "See your Passwords", "Delete Passwords", "Exit"]
    while active:
        validChoice = False
        i = 1
        for item in menuItems:
            print(i, " - ", item)
            i += 1
        while not validChoice:
            selection = input("Your option: ")
            if not(int(selection) > 4 or int(selection) < 1):
                validChoice = True
            else:
                print("Enter a value between 1-4!")
        if selection == '1':
            print(1)
        elif selection == '2':
            print(2)
        elif selection == '3':
            print(3)
        elif selection == '4':
            active = False
        if active == False:
            return 0

menu()
