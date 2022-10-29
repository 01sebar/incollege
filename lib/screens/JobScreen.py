from os import system
from pickle import FALSE, TRUE
import sqlite3
import os
from lib.Job import Job
from lib.User import User

class jobScreen:
    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser

    def getTitleList(self, jobList):       #function to display list of jobs that user can pick from
        if len(jobList) == 0:           #if no jobs are found in joblist return to job screen
            print("No Jobs Found")
            input("\tPress any key to return to the Job Screen\n")
            jobScreen(self.loggedInUser)
        i = 1
        for job in jobList:         #for every job in joblist, print the job title
            print(str(i) + ": ", job[1])
            i += 1
        print("0: return to the Job Screen\n")
        selection = int(input("Select a job to learn more about it: "))         #user selects a job they want to learn more about
        if selection == 0:             #0 to return to job screen
            jobScreen(self.loggedInUser)

        else:
            pickedJob = jobList[selection - 1]          #if user selects a job from joblist, call printPickedJob function that displays job info
            self.printPickedJob(pickedJob,jobList)
              


    def printPickedJob(self, pickedJob,jobList):        #function to display job information and gives user an option to apply for the job
        system('clear')
        print("Job Title: "+ pickedJob[1]+"\nJob Description: "+ pickedJob[2]+ "\nJob Employer: " + pickedJob[3] + "\nJob Location: " + pickedJob[4] + "\nJob Salary: " + pickedJob[5] + "\n")
        print("hello test")
        selection=input("\nPress 1 to apply for this job\nPress 2 to go back to the list of jobs ")
        
        if(selection == 1):
            self.jobApplication(pickedJob,jobList)   #if the user selects 1, call the job application screen
        elif(selection ==2):
            self.getTitleList(jobList)      #if the user selects 2, go back to the job lists
        else:
            selection=("\n\nPress 1 to apply for this job\nPress 2 to go back to the list of jobs")


    def jobApplication(self, pickedJob,jobList):
        system('clear')
        print("hello test got to job application")
        if(pickedJob[6]==self.loggedInUser.getUserId()):            #checking if the user is the one who posted the job since they cannot apply for a job they posted
            print("You cannot apply for a job that you posted.")
            self.getTitleList(jobList)          #if the user is the one who posted the job, bring them back to the job list
        else:
            con = sqlite3.connect("incollege.db")
            graduationDate=input("\nEnter graduation Date: ")
            startDate=input("\nEnter the date you can start: ")
            aboutParagraph=input("\nEnter a paragraph explaining why you think you would be a good fit for this job: ")
            userId=self.loggedInUser.getUserId()
            jobId=pickedJob[0]

            newApplication=Job()
            newApplication.createApplication(self,graduationDate,startDate,aboutParagraph,userId,jobId)
            
            print("\nEnter graduation date: ")

    def hasApplied(self,jobId,userID):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT job_id FROM jobsApplied WHERE user_id = ? LIMIT 1",
            (userID))
        jobIdList = res.fetchall()
        if jobId in jobIdList: return TRUE
        else: return FALSE
        