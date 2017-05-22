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
            newPassMenu()
        elif selection == '2':
            seePassMenu()
        elif selection == '3':
            deletePassMenu()
        elif selection == '4':
            active = False
        if active == False:
            return 0

def newPassMenu():
    location = input("What website/program are you saving? ")
    username = input("Please enter your username: ")
    userPassword = input("Please enter your password: ")
    print("Saved your username ", username, " with the password ", userPassword, " for ", location)

def seePassMenu():
    toSearch = input("Enter the website/program you want to search for: ")

def deletePassMenu():
    toSearch = input("Enter the website/program name you wish to delete: ")

menu()
