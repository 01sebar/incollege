from lib.Job import Job
from lib.Profile import Profile
from lib.User import User
from lib.Experience import Experience
from lib.Education import Education
from lib.Application import Application

class Api:

    def readStudentAccountsFile():
        return None
    
    def readNewJobsFile():
        return None
    
    def writeMyCollegeJobsFile(self):
        job = Job()
        jobs = job.findAll()
        f = open("MyCollege_jobs.txt", "w")
        for j in jobs:
            jobFormatted = f'{j[1]} - {j[2]} - {j[3]} - {j[5]}'
            f.write(jobFormatted)
            f.write("\n=====\n")
        f.close()
        return None
    
    def writeMyCollegeProfilesFile(self):
        profile = Profile(None)
        # profile_Id, profile_title, profile_description, profile_user_id
        profiles = profile.findAll()
        # print(profiles)
        # input("debug")
        f = open("MyCollege_profiles.txt", "w")
        for p in profiles:
            profileTitle = p[1]
            profileFormatted = f'{profileTitle}\n'
            userId = p[3]
            user = User(userId)

            # user_id, user_username, user_firstname, user_lastname, user_university, user_major
            tempUser = user.findOne(userId)
            userUniversity = tempUser[4]
            userMajor = tempUser[5]
            profileDescription = p[1]
            profileFormatted += f'{userMajor}\n{userUniversity}\n{profileDescription}\n'

            profileId = p[0]
            experience = Experience(profileId)
            experienceList = experience.getMany()
            profileFormatted += f'{experienceList}\n'

            education = Education(profileId)
            educationList = education.getMany()
            profileFormatted += f'{educationList}'
            f.write(profileFormatted)
            f.write("\n=====\n")
        f.close()
        return None
    
    def writeMyCollegeUsersFile(self):
        user = User(0)
        # user_id, user_username, user_Type
        users = user.findMany()
        f = open("MyCollege_users.txt", "w")
        for u in users:
            userType = "plus"
            if u[2] == 1:
                userType = "standard"
            userUsername = u[1]
            userFormatted = f'{userUsername} {userType}'
            f.write(userFormatted)
            f.write("\n=====\n")
        f.close()
        return None
    
    def writeMyCollegeAppliedJobsFile(self):
        job = Job()
        # job_id, job_title, job_description, job_employer, job_location, job_salary, job_user_id
        jobs = job.findAll()
        f = open("MyCollege_appliedJobs.txt", "w")
        application = Application()
        for j in jobs:
            jobId = j[0]
            jobTitle = j[1]
            jobFormatted = f'{jobTitle}\n'
            # job_applied_key, user_username, about_paragraph
            applications = application.findMany(jobId)
            for a in applications:
                userName = a[1]
                aboutParagraph = a[2]
                jobFormatted += f'{userName}\n{aboutParagraph}'
            f.write(jobFormatted)
            f.write("\n=====\n")
        f.close()
        return None
    
    def writeMyCollegeSavedJobsFile(self):
        user = User(None)
        # user_id, user_username, ...
        users = user.findMany()
        job = Job()
        f = open("MyCollege_savedJobs.txt", "w")
        for u in users:
            # job_id, job_title, ...
            savedJobs = job.findAllInterested(u[0])
            if len(savedJobs) != 0:
                userUsername = u[1]
                savedJobsFormatted = f'{userUsername}'
                for sJ in savedJobs:
                    savedJobsFormatted += f'\n{sJ[1]}'
                f.write(savedJobsFormatted)
                f.write("\n=====\n")
        f.close()
        return None
    
    def update(self):
        self.writeMyCollegeJobsFile()
        self.writeMyCollegeProfilesFile()
        self.writeMyCollegeUsersFile()
        self.writeMyCollegeAppliedJobsFile()
        self.writeMyCollegeSavedJobsFile()