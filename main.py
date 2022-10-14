# 5 unique student accounts
#Gianni, Anthony, Sebastian, Jack, and Rishabh's scrum baby
import sqlite3
import os
import lib.checkStrUtils as checkStrUtils
from lib.User import User
from lib.Job import Job
from lib.Setting import Setting


def postJobScreen(loggedInUser):
    clearConsole()
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT COUNT() FROM jobs")
    userCount = res.fetchone()[0]
    print("Number of jobs: " + str(userCount))
    if (userCount >= 5):
        print("\tReached limit on jobs posted.\n \tPlease come back later.\n")
        return None
    title = input("Enter the Title of the position you are posting: ")

    description = input("Enter the description of the position: ")

    employer = input("Enter name of employer: ")

    location = input("Enter location of employer: ")
    salary = input("Enter salary for the position: ")

    job = Job()
    job.create(title, description, employer, location, salary,
               loggedInUser.getUserId())
    jobScreen(loggedInUser)


def jobScreen(loggedInUser):
    clearConsole()
    print("\n\tFind or post A Job\n")
    print("press \"1\" to search for a Job or internship.")
    print("press \"2\" to post a job")
    print("press \"3\" to return to the options screen")
    selection = int(input())
    if selection == 1:
        underConstructionScreen()
    elif selection == 2:
        postJobScreen(loggedInUser)
    elif selection == 3:
        optionsScreen(loggedInUser)


def findSomeoneScreen(loggedInUser):
    clearConsole()
    print("\n\tFind Someone you Know\n")
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    firstname = input(
        "Enter the first name of the person you are searching for: \n")
    firstname = firstname.lower()
    lastname = input(
        "Enter the last name of the person you are searching for: \n")
    lastname = lastname.lower()
    res = cur.execute(
        "SELECT user_firstname, user_lastname FROM users WHERE user_firstname = ? AND user_lastname = ? LIMIT 1",
        (firstname, lastname))
    user = res.fetchone()
    if (user == None):
        print("They are not yet part of the InCollege system yet.")
    else:
        print("\nThey are a part of the InCollege System.")
        if (not loggedInUser):
            print("\tWant to become a part of InCollege?")
            print("\tLog-in or Sign-up to join your friends!\n")
            print("Press \"0\" to return to home screen.")
            print("Press \"1\" to log in using an existing account.")
            loginI = int(input("Press \"2\" to create a new account.\n"))
            if loginI == 1:
                login()
            elif loginI == 2:
                signup()
            elif loginI == 0:
                clearConsole()
                main()
            else:
                print("invalid input")


def underConstructionScreen():
    print("\n\t~ Under Construction ~")


def clearConsole():
    os.system('clear')


def skillsScreen(loggedInUser):
    clearConsole()
    print("\n\tSkills Screen")
    print("Select a skill to learn: ")
    print(
        "\t1. Python\n\t2. SQL Databases\n\t3. PyTest\n\t4. Command Line Interface\n\t5. Machine Learning\n\t6. Return to Options\n"
    )
    selection = int(input(""))
    clearConsole()
    if selection == 6:
        optionsScreen(loggedInUser)
    underConstructionScreen()


def optionsScreen(loggedInUser):
    clearConsole()
    print("\n\tOptions Screen")
    print("Select an option:")
    print("\t1: Search for a Job")
    print("\t2: Find someone you know")
    print("\t3: Learn a new skill")
    print("\t4: for Useful Links.")
    print("\t5: for InCollege Important Links.")
    selection = int(input("\t6: Log out\n"))
    clearConsole()
    if selection == 1:
        jobScreen(loggedInUser)
    elif selection == 2:
        findSomeoneScreen(loggedInUser)
    elif selection == 3:
        skillsScreen(loggedInUser)
    elif selection == 4:
        usefulLinks(loggedInUser)
    elif selection == 5:
        InCollegeImportantLinks(loggedInUser)
    elif selection == 6:
        main()


def checkIfUsernameIsUniqueInDB(username):
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute(
        "SELECT user_username FROM users WHERE user_username = ? LIMIT 1",
        (username, ))
    user = res.fetchone()
    return user == None


# 8-12 characters
# at least 1 cap letter
# at least 1 digit
# at least 1 special character
def checkPassword(password):
    if not checkStrUtils.checkIfStrIsCorrectLength(password, 8, 12):
        print("\tPassword must be 8-12 characters in length ")
        return False

    if not checkStrUtils.checkIfStrContainsUpperChar(password):
        print("\tPassword must contain at least 1 uppercase character ")
        return False

    if not checkStrUtils.checkIfStrContainsDigit(password):
        print("\tPassword must contain at least 1 digit ")
        return False

    if not checkStrUtils.checkIfStrContainsSpecialChar(password):
        print("\tPassword must contain at least 1 special character ")
        return False

    return True


def login():
    clearConsole()
    print("\n\tLogin Screen")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = User(None)
    user = tempUser.findOneByUsername(username)
    if (user == None or user[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()
    else:
        print("\tYou have successfully logged in\n")
        clearConsole()
        loggedInUser = User(user[0])
        optionsScreen(loggedInUser)


def checkUsername(username):
    if (not checkStrUtils.checkIfStrIsCorrectLength(username, 1, 32)):
        print(
            "\tUsername must be between 1 and 32 characters!\n\tPlease try again.\n"
        )
        return False
    if (not checkIfUsernameIsUniqueInDB(username)):
        print("\tUsername must be unique!\n\tPlease try again.\n")
        return False
    return True


def signup():
    clearConsole()
    print("\tSignup Screen")
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT COUNT() FROM users")
    userCount = res.fetchone()[0]
    print("Number of Users: " + str(userCount))
    if (userCount >= 5):
        print(
            "\tAll permitted accounts have been created.\n \tPlease come back later.\n"
        )
        return None
    username = input("Enter Username: ")
    while (not checkUsername(username)):
        username = input("Enter Username: ")
    password = input("Enter Password:")
    while (not checkPassword(password)):
        password = input("Enter Password: ")
    firstname = input("Enter First Name:")
    while (firstname == None):
        firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name:")
    while (lastname == None):
        lastname = input("Enter Last Name: ")

    newUser = User(None)
    newUser.create(username, password, firstname, lastname)
    newUser.createDefaultSettings()
    print("\tAccount Created!\n")
    main()


def videoScreen():
    print("\n\tVideo is now playing\n")
    print("Press 1 to return to home screen.")
    print("Press 2 to replay video.")

    choice = int(input())

    if choice == 1:
        clearConsole()
        main()
    else:
        videoScreen()


# Function for General Links
def general(loggedInUser):
    clearConsole()
    print("General\n")
    print("Press \"1\" for Sign Up.")
    print("Press \"2\" for Help Center.")
    print("Press \"3\" for About.")
    print("Press \"4\" for Press.")
    print("Press \"5\" for Blog.")
    print("Press \"6\" for Careers.")
    print("Press \"7\" for Developers.")
    print("Press \"8\" to return to Useful Links.")
    userSelect = int(input())

    if userSelect == 1:
        signup()
    elif userSelect == 2:
        clearConsole()
        print("We're here to help")
        print("Press \"1\" to return to General.")
        userSelect = int(input())
        if userSelect == 1:
            general(loggedInUser)
    elif userSelect == 3:
        clearConsole()
        print(
            "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.\n"
        )
        print("Press \"1\" to return to General.")
        userSelect = int(input())
        if userSelect == 1:
            general(loggedInUser)
    elif userSelect == 4:
        clearConsole()
        print(
            "In College Pressroom: Stay on top of the latest news, updates, and reports"
        )
        print("Press \"1\" to return to General.")
        userSelect = int(input())
        if userSelect == 1:
            general(loggedInUser)
    elif userSelect == 5:
        underConstructionScreen()
    elif userSelect == 6:
        underConstructionScreen()
    elif userSelect == 7:
        underConstructionScreen()
    elif userSelect == 8:
        usefulLinks(loggedInUser)


def userSettings(loggedInUser):
    clearConsole()
    print("Guest Controls\n")
    if not loggedInUser:
        print("You must be logged in to access this section")
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)

    setting = Setting()
    emailValue = setting.getValue("email", loggedInUser.userId)
    print("emailValue:", emailValue)
    smsValue = setting.getValue("sms", loggedInUser.userId)
    print("smsValue:", smsValue)
    targetedAdvertisingValue = setting.getValue("targetedAdvertising",
                                                loggedInUser.userId)
    print("targetedAdvertisingValue:", targetedAdvertisingValue)

    print("Press \"1\" to disable InCollege Email (current status: ",
          "enabled" if emailValue == "true" else "disabled",
          ")",
          sep="")
    print("Press \"2\" to disable InCollege SMS (current status: ",
          "enabled" if smsValue == "true" else "disabled",
          ")",
          sep="")
    print(
        "Press \"3\" to disable InCollege Targeted Advertising (current status: ",
        "enabled" if targetedAdvertisingValue == "true" else "disabled",
        ")",
        sep="")
    print("Press \"4\" to return to InCollege Important Links.")
    userSelect = int(input())

    clearConsole()
    if userSelect == 1:
        setting.update("email", "false", loggedInUser.userId)
        userSettings(loggedInUser)
    elif userSelect == 2:
        setting.update("sms", "false", loggedInUser.userId)
        userSettings(loggedInUser)
    elif userSelect == 3:
        setting.update("targetedAdvertising", "false", loggedInUser.userId)
        userSettings(loggedInUser)
    elif userSelect == 4:
        InCollegeImportantLinks(loggedInUser)


def languages(loggedInUser):
    clearConsole()
    print("Languages\n")
    if not loggedInUser:
        print("You must be logged in to access this section")
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)

    setting = Setting()
    languageValue = setting.getValue("language", loggedInUser.userId)
    print("Press \"1\" to toggle language between English",
          (" (current) " if languageValue == "english" else " "),
          "and Spanish",
          " (current)" if languageValue == "spanish" else "",
          sep="")
    print("Press \"2\" to return to InCollege Important Links.")
    userSelect = int(input(""))

    if userSelect == 1:
        if (languageValue == "english"):
            setting.update("language", "spanish", loggedInUser.userId)
        else:
            setting.update("language", "english", loggedInUser.userId)
        languages(loggedInUser)
    elif userSelect == 2:
        InCollegeImportantLinks(loggedInUser)


def usefulLinks(loggedInUser):
    clearConsole()
    print("Useful Links\n")
    print("Press \"1\" for General.")
    print("Press \"2\" for Browse InCollege.")
    print("Press \"3\" for Business Solutions.")
    print("Press \"4\" for Directories.")
    print("Press \"5\" to Go Back.")
    userSelect = int(input())
    clearConsole()
    if userSelect == 1:
        general(loggedInUser)
    elif userSelect == 2:
        underConstructionScreen()
    elif userSelect == 3:
        underConstructionScreen()
    elif userSelect == 4:
        underConstructionScreen()
    elif userSelect == 5:
        if not loggedInUser:
            main()
        else:
            optionsScreen(loggedInUser)


def InCollegeImportantLinks(loggedInUser):
    clearConsole()
    print("InCollege Important Links\n")
    print("Press \"1\" for A Copyright Notice.")
    print("Press \"2\" for About.")
    print("Press \"3\" for Accessibility.")
    print("Press \"4\" for User Agreement.")
    print("Press \"5\" for Privacy Policy.")
    print("Press \"6\" for Cookie Policy.")
    print("Press \"7\" for Copyright Policy.")
    print("Press \"8\" for Brand Policy.")
    print("Press \"9\" for Guest Controls.")
    print("Press \"10\" for Languages.")
    print("Press \"11\" to Go Back.")
    userSelect = int(input(""))

    if userSelect == 1:
        clearConsole()
        print("© 2022 InCollege")
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 2:
        clearConsole()
        print(
            "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"
        )
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 3:
        clearConsole()
        print("Accessibility\n")
        print("Please refer to Guest Settings for Language options")
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 4:
        clearConsole()
        print(
            "When using InCollege services you agree to InCollege and Associates to use information provided to us by you, the user."
        )
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 5:
        clearConsole()
        print("We value your data here, aint no way we finna sell it")
        print("Press \"1\" for Guest Controls.")
        print("Press \"2\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            userSettings(loggedInUser)
        elif userSelect == 2:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 6:
        clearConsole()
        print(
            "We use your cookies, guess you should have left them in the jar..."
        )
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 7:
        clearConsole()
        print("All rights reserved, don't steal our product...")
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 8:
        clearConsole()
        print(
            "We will pursue legal action if we see misuse of the InCollege brand or other InCollege product."
        )
        print("Press \"1\" to return to InCollege Important Links.")
        userSelect = int(input(""))
        if userSelect == 1:
            InCollegeImportantLinks(loggedInUser)
    elif userSelect == 9:
        userSettings(loggedInUser)
    elif userSelect == 10:
        languages(loggedInUser)
    elif userSelect == 11:
        if not loggedInUser:
            main()
        else:
            optionsScreen(loggedInUser)


def main():
    clearConsole()
    print("\tHome Screen")
    print(
        "\n\tJames was a student at the University of South Florida.\n\t He used InCollege to connect with employers and explore job opportunities.\n\t Through InCollege's internship programs, James earned an internship with Google which eventually turned into a full time employment opportunity for James.\n\t He now works as a senior software developer for Google.\n\t Watch our Video to learn more about how InCollege can help you find an internship or career opportunity!\n"
    )

    print(
        "Press \"1\" to learn more about how InCollege can help you find a career."
    )
    print("Press \"2\" to connect with an InCollege user.")
    print("Press \"3\" to log in using an existing account.")
    print("Press \"4\" to create a new account.")
    print("Press \"5\" for Useful Links.")
    print("Press \"6\" for InCollege Important Links.")
    loginI = int(input())
    clearConsole()
    if loginI == 1:
        videoScreen()
    elif loginI == 2:
        findSomeoneScreen(0)
    elif loginI == 3:
        login()
    elif loginI == 4:
        signup()
    elif loginI == 5:
        usefulLinks(0)
    elif loginI == 6:
        InCollegeImportantLinks(0)
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
