from os import system
import sys
from lib.User import User
from lib.Experience import Experience

class ExperienceScreen:

    def __init__(self, profileId: int):
        self.profileId = profileId

    def render(self):
        system('clear')
        print("Experiences")
        print("Press \"1\" to add an experience")
        print("Press \"2\" to remove an experience")
        print("Press \"3\" to go back")
        selection = input("Make a selection:")
        if selection == "1":
            print("add experience")
            self.addExperience()
        elif selection == "2":
            print("remove experience")
        else:
            # return None returns control flow to wherever ExperienceScreen.render() was called from
            return None

    def addExperience(self):
        system('clear')
        print("Add an experience")
        experience = Experience(self.profileId)
        # Check limit of 3 experiences per profile
        if(experience.getCount() >= 3):
            print("You have reach the limit (3) of experiences you can add to your profile")
            print("Please remove an experience and try again")
            input("Press any key to continue...")
            return self.render()

        title = input("Title: ")
        employer = input("Employer: ")
        dateStarted = input("Date started: ")
        dateEnded = input("Date ended: ")
        location = input("Location: ")
        description = input("Description: ")
        experience.create(title, employer, dateStarted, dateEnded, location, description)
        self.render()

