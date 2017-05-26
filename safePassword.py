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
        if selection == '1': #Here needs to be done manually, since it will change every time with no order and it won't matter because it won't have more menus
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
    f = open("data.txt", "a") #opens file data.txt in append mode (doesn't erase its content when written)
    location = input("What website/program are you saving? ")
    username = input("Please enter your username: ")
    userPassword = input("Please enter your password: ")
    print("Saved your username ", username, " with the password ", userPassword, " for ", location) #info for the user
    f.write(location + "|" + username + "|" + userPassword + "\n") #writes to file
    f.close() #closes file to avoid over usage of memory
def seePassMenu():
    toSearch = input("Enter the website/program you want to search fo (type '_' if you want to list all of them): ")
    f = open("data.txt", 'r') #opens file in read mode
    hadOcurrence = False #checks if had ocurrences of 'toSearch'
    print() #paragraph for a better visual in console
    for a in f: #for each line in file
        s = a.split("|") #splits line into 3 different strings
        if(s[0] == toSearch or toSearch == '_'):
            hadOcurrence = True #there was at least 1 ocurrence
            print("Website/Application: " + s[0])
            print("Username: " + s[1])
            print("Password: " + s[2])
    if not hadOcurrence:
        print("Failed! No ocurrences found. Did you add that password before?")
    f.close() #hadOcurrence isn't set to False because it will be removed from RAM, since the function will terminate
    print() #paragraph for a better visual in console

def deletePassMenu():
    toSearch = input("Enter the website/program name you wish to delete: ")
    f = open("data.txt", 'r') #opens file in read mode
    locations = [] #This array will store all the possible locations that have THAT website
    i = -1 #helper var to place stuff in 'locations'
    helper = f.read().split("\n") #splits at each paragraph
    f.close() #closes file in read mode -> will open later in write mode
    done = False
    if len(helper) == 0: #file is empty -> exit function
        print("You haven't saved any password yet")
    else:
        for b in helper: #searches for ocurrences in each line of the file for the specified password
            i += 1 #gives us the line index to remove
            a = b.split('|') #each line is of type website|username|password so we can split it in 3
            if a[0] == toSearch:
                locations.append(i) #appends the index to locations array
                print("[", i, "] - ", a[0], " - ", a[1], " - ", a[2]) #prints the user what can be eliminated
        if len(locations) == 0:
            print("No ocurrences found! Check if you typed it correctly or if you've got a password in that program/website") #0 ocurrences of user wanted -> ends function
        else:
            if len(locations) == 1: #automatically eliminates the only option
                helper[locations[0]] = ""
            else:
                while not done: #only changes to false when done = True and it is only done when user has entered a valid option
                    choice = input("Please enter the line you wish to remove: ")
                    if int(choice) not in locations: #checks the valid option
                        print("Enter a valid position!")
                    else:
                        helper[int(choice)] = ""
                        done = True
            x = 0 #will represent each line (I prefer not to use another variable not being used to avoid conflicts at the cost of 2 bytes)
            f = open("data.txt", 'w') #opens file in write mode so we can overwrite it
            for c in helper:
                if c != "": #avoids empty lines for future usage
                    f.write(helper[x]+"\n") #writes to file
                x += 1
            f.close() #closes file

menu()
