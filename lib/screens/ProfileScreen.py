from traceback import print_tb
from lib.User import User
from lib.Profile import Profile

class ProfileScreen:

    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser
    
    def render(self):
        profile = Profile(self.loggedInUser)
        if profile.exists():
            print("EXISTS")
        else:
            self.doesNotExist()

    def doesNotExist(self):
        print("You do not have a profile, would you like to create one?")
        print("Press \"1\" for Yes")
        print("Press \"2\" for No")
        selection = input()
        if selection == "1":
            self.create()
        else:
            return None
            
    def create(self):
        print("create profile")
        input("")

