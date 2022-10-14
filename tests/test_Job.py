import pytest
from lib.User import User
from lib.Job import Job

class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user", "Pass123!", "John", "Doe")
        job = Job()
        newJobId = job.create("Software Developer", "program stuff", "Google", "San Francisco, CA", "500000", newUserId)
        assert job.findOne(newJobId) != None
        assert job.findOne(0) == None # findOne(0) should always return None since database IDs start counting at 1
