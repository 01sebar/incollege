from os import system
from traceback import print_tb
from lib.User import User
from lib.Profile import Profile

class ProfileScreen:

    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser
    
    def render(self):
        system('clear')
        profile = Profile(self.loggedInUser)
        if profile.exists():
            self.view()
        else:
            self.doesNotExist()
    
    def view(self):
        # TO-DO: IN-60
        print("print out profile info")
        print("Press \"1\" to edit")
        print("Press \"2\" to go back")
        selection = input("Select an option: ")
        if selection == "1":
            self.createOrUpdate()
        elif selection == "2":
            # return None returns control flow to wherever ProfileScreen was called from (likely main)
            return None


    def doesNotExist(self):
        print("You do not have a profile, would you like to create one?")
        print("Press \"1\" for Yes")
        print("Press \"2\" for No")
        selection = input("Select an option: ")
        if selection == "1":
            self.createOrUpdate()
        else:
            return None
            
    def createOrUpdate(self):
        system('clear')
        print("Update profile")
        profile = Profile(self.loggedInUser)
        if(not profile.exists()):
            profile.create()
        print("Press \"1\" to set Title")
        print("Press \"2\" to set Major")
        print("Press \"3\" to set University")
        print("Press \"4\" to set Description")
        print("Press \"5\" to set Experience")
        print("Press \"6\" to set Education")
        print("Press \"7\" to view profile")
        select = input("Select an option: ")
        if select == "1":
            title = input("Set Title: ")
            profile.setTitle(title)
        elif select == "2":
            major = input("Set Major: ")
            profile.setMajor(major)
        elif select == "3":
            university = input("Set University: ")
            profile.setUniversity(university)
        elif select == "4":
            description = input("Set Description: ")
            profile.setDescription(description)
        elif select == "5":
            print("experience")
        elif select == "6":
            print("education")
        elif select == "7":
            return self.view()
        self.createOrUpdate()
