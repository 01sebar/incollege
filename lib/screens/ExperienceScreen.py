
from os import system
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
            self.addExperience()
        elif selection == "2":
            self.removeExperience()
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

    def removeExperience(self):
        print("Select an experience to delete")
        experience = Experience(self.profileId)
        if(experience.getCount() == 0):
            print("You do not have any experiences added profile and can therefore not delete any")
            input("Press any key to continue...")
            return self.render()
        experiences = experience.getMany()
        i = 1
        for experienceElem in experiences:
            print("[" + str(i) + "]", experienceElem[1], "@", experienceElem[2])
            i += 1
        print("Press 0 to go back")
        selection = int(input("Make a selection: "))
        if selection != 0:
            experienceIdToDelete = experiences[selection - 1][0]
            print("experienceIdToDelete: ", experienceIdToDelete)
            experience.removeOne(experienceIdToDelete)
        self.render()
            