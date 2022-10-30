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
        i = 1
        print("\nList of Jobs:")
        for job in jobList:         #for every job in joblist, print the job title
            if self.hasApplied(job[0],self.loggedInUser.getUserId()) == True:
                print("\t\u2611"+ str(i) + "-", job[1])
            else:
                print("\t\u2610"+ str(i) + "-", job[1])
            i += 1
        
        print("Select a job to learn more about it:")
        selection = int(input("Press '0' to return to the Options Screen\n"))         #user selects a job they want to learn more about
        
        if selection == 0:             #0 to return to job screen
            return None
        else: # need to add a checker so the selection is not out of range 
            pickedJob = jobList[selection - 1]          #if user selects a job from joblist, call printPickedJob function that displays job info
            self.printPickedJob(pickedJob,jobList)
        
        if self.hasApplied(job[0],self.loggedInUser.getUserId()) == True: # checks if user has applied to job already
            return None #returns back to prev screen if user has already applied
        else: #allows user to apply if they have havent already done so 
            print("Press 1 to apply for this job\nPress 2 to go back to the list of jobs ")
            while True:    
                selection = int(input())
                if(selection == 1):
                    self.jobApplication(pickedJob,jobList)   #if the user selects 1, call the job application screen
                    self.getTitleList(jobList)
                    return None
                
                elif(selection ==2):
                    return None      #if the user selects 2, go back to the job lists
              


    def printPickedJob(self, pickedJob,jobList):        #function to display job information and gives user an option to apply for the job
        system('clear')
        print("got to print picked job screeen owo ")
        print("Job Title: "+ pickedJob[1]+"\nJob Description: "+ pickedJob[2]+ "\nJob Employer: " + pickedJob[3] + "\nJob Location: " + pickedJob[4] + "\nJob Salary: " + pickedJob[5] + "\n")


    def jobApplication(self, pickedJob,jobList):
        system('clear')
        if(pickedJob[6]==self.loggedInUser.getUserId()):            #checking if the user is the one who posted the job since they cannot apply for a job they posted
            print("You cannot apply for a job that you posted.")
            return None          #if the user is the one who posted the job, bring them back to the job list
        else:
            con = sqlite3.connect("incollege.db")
            graduationDate=input("\nEnter graduation Date: ") #add format checker in py
            startDate=input("\nEnter the date you can start: ")
            aboutParagraph=input("\nEnter a paragraph explaining why you think you would be a good fit for this job: ")
            userId=self.loggedInUser.getUserId()
            jobId=pickedJob[0]
            newApplication=Job()
            newApplication.createApplication(graduationDate,startDate,aboutParagraph, userId, jobId)
        
        print("Job applied successfully\n")
        input("Press any key to return to the Job List Screen\n")
        return None



    def hasApplied(self,jobId,userID):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT job_id FROM jobsApplied WHERE user_id = ? LIMIT 1",
            (userID))
        jobIdList = res.fetchall()
        if jobId in jobIdList: return True
        else: return False
        