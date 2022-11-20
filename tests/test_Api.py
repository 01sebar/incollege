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
        foundUser=newUser.findOneByUsername("areiss")
        assert(foundUser[1]=="areiss")
        assert(foundUser[2]=="Pass123!")
    

        api.readNewJobsFile()
        newJob=Job()
        foundJob=newJob.findOneByName("Cashier")
        assert (foundJob[0]=="Cashier")