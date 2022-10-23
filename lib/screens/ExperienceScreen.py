from os import system
from lib.User import User

class ExperienceScreen:

    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser

    def render():
        system('clear')
        print("Experiences")
    
    