# Gianni, Anthony, Sebastian, Jack, and Rishabh's scrum baby
import sqlite3
import os
import lib.checkStrUtils as checkStrUtils
from lib.User import User
from lib.Job import Job
from lib.Setting import Setting
from lib.Friend import Friend
from lib.screens.ProfileScreen import ProfileScreen
from lib.screens.JobScreen import jobScreen
from lib.screens.MessagingScreen import MessagingScreen
from lib.Message import Message

def postJobScreen(loggedInUser):
    clearConsole()
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT COUNT() FROM jobs")
    jobCount = res.fetchone()[0]
    print("Number of jobs: " + str(jobCount))
    if (jobCount >= 10):
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
    jobScreenList(loggedInUser)


def jobScreenList(loggedInUser):
    clearConsole()
    jobscreen = jobScreen(loggedInUser)
    job = Job()
    userId = loggedInUser.getUserId()
    print("\n\tFind or post A Job\n")
    print("press \"1\" to search for a Job or internship.")
    print("press \"2\" to post a job")
    print("press \"3\" to view save later list")
    print("press \"4\" to delete a job posting")
    print("press \"5\" to return to the options screen")
    if job.checkStatus(userId) == True:
        print("1 or more jobs you have applied for have been deleted")
    selection = int(input())
    if selection == 1:
        jobsList = job.findAll()
        jobscreen.jobTitleList(jobsList)
        jobScreenList(loggedInUser)
    elif selection == 2:
        postJobScreen(loggedInUser)
    elif selection == 3:
        jobSavedList = job.findAllInterested(userId)
        jobscreen.jobInterestedScreen(jobSavedList)
        jobScreenList(loggedInUser)
    elif selection == 4:
        deleteJob(loggedInUser)
    elif selection == 5:
        optionsScreen(loggedInUser)


def deleteJob(loggedInUser):
    clearConsole()
    jobs = Job()
    # getting all jobs posted by logged in user
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT job_id, job_title FROM jobs WHERE job_user_id = ? ",
                      (loggedInUser.getUserId(),))
    i = 1
    jobList = res.fetchall()

    if len(jobList) == 0:  # if no jobs are found in joblist return to job screen
        print("\nNo Jobs Found\n")
        input("\tPress any key to return to the Job Screen\n")
        jobScreenList(loggedInUser)

    for job in jobList:  # for every job in joblist, print the job title
        print("[" + str(i) + "] ", job[1])
        i += 1
    selection = int(input("Select a job to delete:"))
    jobToDelete = jobList[selection - 1]
    # lets all the users who have applied know that the job is not avaiable anymore
    jobs.updateStatus(jobToDelete[0])
    jobs.removeJob(jobToDelete[0])
    print("\nthingy deleted\n")
    jobScreenList(loggedInUser)


def findSomeoneScreen(loggedInUser):
    clearConsole()
    print("\n\tFind Someone you Know\n")
    print("\n\tSearch By:\n")
    print("\t1: Last name")
    print("\t2: University")
    print("\t3: Major")
    selection = int(input("\t4: Return to options screen\n"))
    if (selection == 1):
        findSomeoneByLastNameScreen(loggedInUser)
    elif (selection == 2):
        findSomeoneByUniversityScreen(loggedInUser)
    elif (selection == 3):
        findSomeoneByMajorScreen(loggedInUser)
    elif (selection == 4):
        if (not loggedInUser):
            clearConsole()
            main()
        else:
            optionsScreen(loggedInUser)


def findSomeoneByLastNameScreen(loggedInUser: User):
    print("\n\tFind Someone By Last Name Screen")
    lastname = input(
        "Enter the last name of the person you are searching for: ")
    users = loggedInUser.findManyByLastname(lastname)
    if not loggedInUser.isLoggedIn():
        if len(users) == 0:
            print("No users found")
        for user in users:
            print(user[1], user[2])
        input("\tPress any key to return to find someone screen\n")
        findSomeoneScreen(loggedInUser)
    else:
        sendFriendInviteScreen(loggedInUser, users)


def findSomeoneByUniversityScreen(loggedInUser: User):
    print("\n\tFind Someone By University Screen")
    university = input(
        "Enter the university of the person you are searching for: ")
    users = loggedInUser.findManyByUniversity(university)
    if not loggedInUser.isLoggedIn():
        if len(users) == 0:
            print("No users found")
        for user in users:
            print(user[1], user[2])
        input("\tPress any key to return to find someone screen\n")
        findSomeoneScreen(loggedInUser)
    else:
        sendFriendInviteScreen(loggedInUser, users)


def findSomeoneByMajorScreen(loggedInUser: User):
    print("\n\Find Someone By Major Screen")
    major = input(
        "Enter the Major of the person you are searching for: ")
    users = loggedInUser.findManyByMajor(major)
    if not loggedInUser.isLoggedIn():
        if len(users) == 0:
            print("No users found")
        for user in users:
            print(user[1], user[2])
        input("\tPress any key to return to find someone screen\n")
        findSomeoneScreen(loggedInUser)
    else:
        sendFriendInviteScreen(loggedInUser, users)


def sendFriendInviteScreen(loggedInUser: User, users):
    if len(users) == 0:
        print("No users found")
        input("\tPress any key to return to find someone screen\n")
        findSomeoneScreen(loggedInUser)
    i = 1
    for user in users:
        print(str(i) + ": ", user[1], user[2])
        i += 1
    print("0: return to find someone screen\n")
    selection = int(input("Select a user to add as a friend or 0 to cancel: "))
    if selection == 0:
        findSomeoneScreen(loggedInUser)
    else:
        # users[selection - 1] since we start with i = 1
        userToAdd = users[selection - 1]
        userToAddId = userToAdd[0]
        friend = Friend(loggedInUser.getUserId())
        friend.sendInvite(userToAddId)
        print("invite sent!")
        input("\tPress any key to return to find someone screen\n")
        findSomeoneScreen(loggedInUser)


def showMyNetworkScreen(loggedInUser: User):
    print("\n\tShow My Network Screen")
    friend = Friend(loggedInUser.getUserId())
    friendsList = friend.getFriends()
    if not friendsList: 
        print("There is no one in your network...\n")
        input("\tPress any key to return to options screen\n")
        optionsScreen(loggedInUser)
    else:
        i = 1
        for myFriend in friendsList:
            # Prevents displaying of self
            if(myFriend[1] == loggedInUser.getUserId()):
                continue
            print(str(i), ":", myFriend[2], myFriend[3])
            i += 1
    friendToDecide = int(input("Select a friend or 0 to return to options\n"))
    if friendToDecide == 0:
        optionsScreen(loggedInUser)
    print("Press 1 to remove")
    friendUserId = friend.getFriendsUserID(friendsList[friendToDecide-1][0])
    friendHasProfile = friend.hasProfile(friendUserId)
    if friendHasProfile:
        print("Press 2 to view friend profile")
    print("Press 0 to go back")
    selection = input("")
    if selection == "1":
        print("Are you sure you want to remove this friend?")
        print("1: Yes")
        print("2: No")
        answer = input()
        if answer == "1":
            friendId = friendsList[friendToDecide-1][0]
            friend.removeFriend(friendId)
            optionsScreen(loggedInUser)
        else:
            optionsScreen(loggedInUser)
    elif selection == "2" and friendHasProfile: 
        #profile
        profileScreen = ProfileScreen(loggedInUser)
        profileScreen.view(friendUserId)
        input("Press any key to return to view my network screen...")
        showMyNetworkScreen(loggedInUser)
    else:
        showMyNetworkScreen(loggedInUser)

def underConstructionScreen():
    input("\n\t~ Under Construction ~ \n\tPress any key to restart")
    main()


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


def optionsScreen(loggedInUser: User):
    clearConsole()
    print("\n\tOptions Screen")
    print("Select an option:")
    print("\t1: Search for a Job")
    print("\t2: Find someone you know")
    print("\t3: Send a message to someone")
    print("\t4: Learn a new skill")
    print("\t5: for Useful Links.")
    print("\t6: for InCollege Important Links.")
    print("\t7: Show my network")
    friend = Friend(loggedInUser.getUserId())
    friendInvites = friend.getInvites()
    print("\t8: You have", len(friendInvites), "new friend invites")
    print("\t9: View my profile")
    message = Message(loggedInUser.getUserId())
    messageList = message.getMessages()
    print("\t10: You have", len(messageList), "new messages!")
    selection = int(input("\t0: Log out\n"))
    clearConsole()
    if selection == 1:
        jobScreenList(loggedInUser)
    elif selection == 2:
        findSomeoneScreen(loggedInUser)
    elif selection==3:
        messagingScreen=MessagingScreen(loggedInUser.getUserId())
        messagingScreen.messageList()
        optionsScreen(loggedInUser)
    elif selection == 4:
        skillsScreen(loggedInUser)
    elif selection == 5:
        usefulLinks(loggedInUser)
    elif selection == 6:
        InCollegeImportantLinks(loggedInUser)
    elif selection == 7:
        showMyNetworkScreen(loggedInUser)
    elif selection == 8:
        acceptInvitesScreen(loggedInUser)
    elif selection == 9:
        profileScreen = ProfileScreen(loggedInUser)
        profileScreen.render()
        optionsScreen(loggedInUser)
    elif selection ==10:
        messagingScreen=MessagingScreen(loggedInUser.getUserId())
        messagingScreen.viewIncomingMessages(messageList)
        optionsScreen(loggedInUser)
    elif selection == 0:
        main()


def acceptInvitesScreen(loggedInUser: User):
    print("\n\tAccept Invites Screen")
    friend = Friend(loggedInUser.getUserId())
    friendInvites = friend.getInvites()
    if len(friendInvites) == 0:
        print("You have no pending invites")
        input("Press any key to return to the options screen")
        optionsScreen(loggedInUser)
        return

    i = 1
    for friendInvite in friendInvites:
        print(str(i) + ":", friendInvite[2], friendInvite[3])
        i += 1
    print("0: return to options screen\n")
    selection = int(
        input("Select a user to accept/reject their invite or 0 to cancel: "))
    if selection == 0:
        optionsScreen(loggedInUser)
    else:
        # TO-DO
        print(friendInvites[selection-1][2], friendInvites[selection-1][3])
        print("1: Accept")
        print("2: Reject")
        print("0: Cancel")
        friendId = friendInvites[selection-1][0]
        decision = int(
            input(""))
        if decision == 1:
            clearConsole()
            print("Accepted\n")
            friend.addFriend(friendId)
            acceptInvitesScreen(loggedInUser)
        elif decision == 2:
            clearConsole()
            print("Rejected\n")
            friend.rejectInvite(friendId)
            acceptInvitesScreen(loggedInUser)
        elif decision == 0:
            acceptInvitesScreen(loggedInUser)
        return


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
    userType=int(input("Press 1 for a free standard account\nPress 2 for a ($10/month) Premium account: "))
    print(userType )
    print(type(userType))
    while(userType < 1 or userType > 2):
        userType=int(input("Press 1 for a free standard account\nPress 2 for a ($10/month) Premium account: "))

    newUser = User(None)
    newUser.create(username, password, firstname, lastname,userType)
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
        findSomeoneScreen(User(None))
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
