def menu():
    active = True #defines if program is running
    menuItems = ["New Password", "See your Passwords", "Delete Passwords", "Exit"] #menu items -> easier to add a new one, just add here and it will add it when ran
    while active:
        validChoice = False #checks if choice is valid
        i = 1
        for item in menuItems: #prints the main menu
            print(i, " - ", item)
            i += 1
        while not validChoice: #gets the user option
            selection = input("Your option: ")
            if not(int(selection) > len(menuItems) or int(selection) < 1):
                validChoice = True
            else:
                print("Enter a value between 1-",len(menuItems),"!")
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
    f = open("data.txt", "a")
    location = input("What website/program are you saving? ")
    username = input("Please enter your username: ")
    userPassword = input("Please enter your password: ")
    print("Saved your username ", username, " with the password ", userPassword, " for ", location)
    f.write(location + "|" + username + "|" + userPassword + "\n")
    f.close()
def seePassMenu():
    toSearch = input("Enter the website/program you want to search fo (type '_' if you want to list all of them): ")
    try:
        f = open("data.txt", 'r')
    except:
        print('You haven\'t saved any passwords yet.')
    else:
        hadOcurrence = False
        print()
        for a in f:
            s = a.split("|") #splits line into 3 different strings
            if(s[0] == toSearch or toSearch == '_'):
                hadOcurrence = True
                print("Website/Application: " + s[0])
                print("Username: " + s[1])
                print("Password: " + s[2])
        if not hadOcurrence:
            print("Failed! No ocurrences found. Did you add that password before?")
        f.close()
        print()

def deletePassMenu():
    toSearch = input("Enter the website/program name you wish to delete: ")
    try:
        f = open("data.txt", 'r')
    except:
        print('You haven\'t saved any passwords yet.')
    else:
        locations = []
        i = -1
        helper = f.read().split("\n") #splits at each paragraph
        f.close()
        done = False
        if len(helper) == 0: #file is empty -> exit function
            print("You haven't saved any password yet.")
        else:
            for b in helper:
                i += 1
                a = b.split('|')
                if a[0] == toSearch:
                    locations.append(i)
                    print("[", i, "] - ", a[0], " - ", a[1], " - ", a[2])
            if len(locations) == 0:
                print("No ocurrences found! Check if you typed it correctly or if you've got a password in that program/website.")
            else:
                if len(locations) == 1: #eliminates the only option
                    helper[locations[0]] = ""
                else:
                    while not done:
                        choice = input("Please enter the line you wish to remove: ")
                        if int(choice) not in locations: #checks the valid option
                            print("Enter a valid position!")
                        else:
                            helper[int(choice)] = ""
                            done = True
                x = 0
                f = open("data.txt", 'w')
                for c in helper: #rewrites information except the info to be removed
                    if c != "":
                        f.write(helper[x]+"\n")
                    x += 1
                f.close()

menu()
