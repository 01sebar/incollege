import pytest
from lib.User import User
from lib.Message import Message
from lib.Notification import Notification
from lib.Profile import Profile
from lib.Api import Api
from lib.Job import Job

class TestClass:

    def testApi(self):
        
        api=Api()
        api.readStudentAccountsFile()

        newUser=User(None)
        foundUser=newUser.findOneByUsername("antrei")
        assert(foundUser[1]=="antrei")
        assert(foundUser[2]=="Pass123!")
    

        api.readNewJobsFile()
        newJob=Job()
        foundJob=newJob.findOneByName("Job 1")
        assert (foundJob[0]=="Job 1")

        newUser2 = User(0)
        newUser2.create("Admin", "Password123!", "admin", "admin", 1)
        api.writeMyCollegeUsersFile()
        assert(newUser2.findOneByUsername("Admin")[1] == "Admin")
        