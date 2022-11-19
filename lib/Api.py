from lib.Job import Job

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
            jobFormatted = f'{j[1]} - {j[2]} - {j[3]} - {j[5]}\n'
            f.write(jobFormatted)
            f.write("=====\n")
        f.close()
        return None
    
    def writeMyCollegeProfilesFile():
        return None
    
    def writeMyCollegeUsersFile():
        return None
    
    def writeMyCollegeAppliedJobsFile():
        return None
    
    def writeMyCollegeSavedJobsFile():
        return None