from os import system
from lib.Education import Education
from lib.utils.Format import Format
class EducationScreen:

    def __init__(self, profileId: int):
        self.profileId = profileId

    def render(self):
        system('clear')
        print("Education ")
        print("Press \"1\" to add education")
        print("Press \"2\" to remove education")
        print("Press \"3\" to go back")
        selection = input("Make a selection:")
        if selection == "1":
            self.addEducation()
        elif selection == "2":
            self.removeEducation()
        else:
            # return None returns control flow to wherever EducationScreen.render() was called from
            return None

    def addEducation(self):
        system('clear')
        print("Add an Education")
        education = Education(self.profileId)
        schoolName = input("School Name: ")
        degree = input("Degree: ")
        startingYear = input("Year Started: ")
        endingYeear = input("Year finished: ")
        education.create(schoolName, degree, startingYear, endingYeear)
        self.render()

    def removeEducation(self):
        print("Select an Education to delete")
        education = Education(self.profileId)
        if(education.getCount() == 0):
            print("You do not have any Education history added to your profile and can therefore not delete any")
            input("Press any key to continue...")
            return self.render()
        educationList = education.getMany()
        i = 1
        for educationElem in educationList:
            print("[" + str(i) + "]", educationElem[1], ":", educationElem[2],"Years:", educationElem[3],",",educationElem[4])
            i += 1
        print("Press 0 to go back")
        selection = int(input("Make a selection: "))
        if selection != 0:
            educationIdToDelete = educationList[selection - 1][0]
            print("educationIdToDelete: ", educationIdToDelete)
            education.removeOne(educationIdToDelete)
        self.render()
            