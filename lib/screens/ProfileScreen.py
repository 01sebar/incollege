from cmath import exp
from os import system
from traceback import print_tb
from lib.User import User
from lib.Profile import Profile
from lib.Education import Education
from lib.Experience import Experience
from lib.screens.ExperienceScreen import ExperienceScreen
from lib.screens.EducationScreen import EducationScreen

class ProfileScreen:

    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser
    
    def render(self):
        system('clear')
        profile = Profile(self.loggedInUser)
        if profile.exists():
            self.view(self.loggedInUser.getUserId())
            print("Press \"1\" to edit")
            print("Press \"2\" to go back")
            selection = input("Select an option: ")
            if selection == "1":
                self.createOrUpdate()
            elif selection == "2":
                # return None returns control flow to wherever ProfileScreen was called from (likely main)
                return None
        else:
            self.doesNotExist()

    def renderFriend(self, friendUserId):
        system('clear')
        self.view(friendUserId)
        selection = input("Press any key to return to friends list...")
        return None

    def view(self, userId):
        print("~~Profile~~\n")
        i = 1 #counter for education
        j = 1 #counter for workExperience 
        #getting User info for Major and University name
        tempU = User(None)
        user = tempU.findOne(userId)

        #getting Profile information 
        tempP = Profile(None)
        profile = tempP.findOne(userId)

        #getting Education information 
        tempEdu = Education(userId)
        profileEdu = tempEdu.getMany()

        #getting Previous Work Experience
        tempExp = Experience(userId)
        workExp = tempExp.getMany()

        if user[2]!= "":
            print("First name: ",user[2])
        
        if user[3]!= "":
            print("Last name: ",user[3])

        if profile[1] != None:
            print("Title:",profile[1])

        if user[5]!= "":
            print("Major: ",user[5])

        if user[4] != "":
            print("University Name: ",user[4])
    
        if profile[2] != None:
            print("About me: ",profile[2])

        if profileEdu:
            print("Previous Education:")
            for educationElem in profileEdu:
                print("\t[Institution #" + str(i) + "]  Name:", educationElem[1], ", Major:", educationElem[2],", Years Attended:", educationElem[3],"-",educationElem[4])
                i += 1
        if workExp:
            print("Previous Work Experience:")
            for job in workExp:
                print("\t[Job #" + str(j) + "]  Job:", job[1], ", Employer:", job[2],", Date Started:", job[3],", Date Ended:",job[4], ", Location:",job[5], ", Description:",job[6])
                j += 1


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
            ExperienceScreen(profile.getProfileId()).render()
        elif select == "6":
            EducationScreen(profile.getProfileId()).render()
        elif select == "7":
            return self.view(self.loggedInUser.getUserId())
        self.createOrUpdate()
