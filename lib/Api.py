from lib.Job import Job
from lib.Profile import Profile
from lib.User import User
from lib.Experience import Experience
from lib.Education import Education

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
    
    def writeMyCollegeAppliedJobsFile():
        return None
    
    def writeMyCollegeSavedJobsFile():
        return None
    
    def update(self):
        self.writeMyCollegeJobsFile()
        self.writeMyCollegeProfilesFile()
        self.writeMyCollegeUsersFile()