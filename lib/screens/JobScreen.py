from os import system
#from pickle import FALSE, TRUE
from traceback import print_tb
import sqlite3
from lib.Job import Job
from lib.User import User

class jobScreen:
    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser
    

    def getTitleList(self, jobList):       #function to display list of jobs that user can pick from
        if len(jobList) == 0:           #if no jobs are found in joblist return to job screen
            print("No Jobs Found")
            input("\tPress any key to return to the Job Screen\n")
            return None
        
        job = Job()
        userId = self.loggedInUser.getUserId() 
        i = 1
        print("\nList of Jobs:")
        for jobPost in jobList:         #for every job in joblist, print the job title
            if job.hasApplied(jobPost[0],userId) == True: #checks if user has applied to job already
                print("\t"+ str(i) + "-", jobPost[1], "(has applied:)")
            else:
                print("\t"+ str(i) + "-", jobPost[1], "(has not applied:)")
            i += 1
        
        print("Select a job to learn more about it:")
        selection = int(input("Press '0' to return to the Options Screen\n"))         #user selects a job they want to learn more about
        
        if selection == 0:             #0 to return to job screen
            return None
        else: # need to add a checker so the selection is not out of range 
            pickedJob = jobList[selection - 1]          #if user selects a job from joblist, call printPickedJob function that displays job info
            self.printPickedJob(pickedJob)

        if job.hasApplied(pickedJob[0],userId) == True: # checks if user has applied to job already
            print("You have already applied for this Job\n")
            return None #returns back to prev screen if user has already applied
        else: #allows user to apply if they have havent already done so 
            print("Press 1 to apply for this job\nPress 2 to add job to your save later list\nPress 3 to go back to the list of jobs ")
            while True:    
                selection = int(input())
                if(selection == 1):
                    self.jobApplication(pickedJob)   #if the user selects 1, call the job application screen
                    self.getTitleList(jobList)
                    return None
                if(selection == 2):
                    self.addjobInterested(pickedJob)   #if the user selects 1, call the job interested screen
                    self.getTitleList(jobList)
                    return None
                elif(selection ==3):
                    return None      #if the user selects 2, go back to the job lists
              

    def printPickedJob(self, pickedJob):        #function to display job information and gives user an option to apply for the job
        system('clear')
        print("\nJob Title: "+ pickedJob[1]+"\nJob Description: "+ pickedJob[2]+ "\nJob Employer: " + pickedJob[3] + "\nJob Location: " + pickedJob[4] + "\nJob Salary: " + pickedJob[5] + "\n")

    def jobInterestedScreen(self, jobSavedList):        #function to display job information and gives user an option to apply for the job
        system('clear') 
        if len(jobSavedList) == 0:           #if no jobs are found in joblist return to job screen
            print("No Jobs Saved")
            input("\tPress any key to return to the Job Screen\n")
            return None
        
        job = Job()
        i = 1
        print("\nList of Interested Jobs:")
        for JOB in jobSavedList:         #for every job in joblist, print the job title
            print("\t"+ str(i) + "  job title:", JOB[1])
            i += 1
    
        print("\nSelect a job to remove from saved list")
        selection = int(input("Or press '0' to return to the Options Screen\n"))         #user selects a job they want to learn more about
        
        if selection == 0:             #0 to return to job screen
            return None
        else: # need to add a checker so the selection is not out of range 
            pickedJob = jobSavedList[selection - 1]          #if user selects a job from joblist, call printPickedJob function that displays job info
            job.removeInterestedJob(pickedJob[0])
            print("Job removed from saved list\n")
            return None

    def jobApplication(self, pickedJob):
        system('clear')
        if(pickedJob[6]==self.loggedInUser.getUserId()):            #checking if the user is the one who posted the job since they cannot apply for a job they posted
            print("You cannot apply for a job that you posted.")
            #return None          #if the user is the one who posted the job, bring them back to the job list
        
        else:
            con = sqlite3.connect("incollege.db")
            graduationDate=input("\nEnter graduation Date: ") #add format checker in py
            startDate=input("\nEnter the date you can start: ")
            aboutParagraph=input("\nEnter a paragraph explaining why you think you would be a good fit for this job: ")
            userId=self.loggedInUser.getUserId()
            jobId=pickedJob[0]
            newApplication=Job()
            newApplication.createApplication(graduationDate,startDate,aboutParagraph, userId, jobId)
            print("\nJob applied successfully\n")
            input("Press any key to return to the Job List Screen\n")
            #return None
    
    def addjobInterested(self, pickedJob):
        system('clear')
        job = Job()
        userId=self.loggedInUser.getUserId()
        jobId = pickedJob[0]
        if job.hasInterested(jobId,userId ) == True:
            print("You already have this job on your save list\n")
            input("Press any key to return to the Job List Screen\n")
            return None
        job.addInterestedJob(userId,jobId)
        print("job added to save list successfully")
        return None

        