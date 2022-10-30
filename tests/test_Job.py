import pytest
from lib.User import User
from lib.Job import Job


class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user1", "Pass123!", "John", "Doe")
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        assert job.findOne(newJobId) != None
        # findOne(0) should always return None since database IDs start counting at 1
        assert job.findOne(0) == None

    def testJobInterest(self):
        user = User(None)
        newUserId = user.create("user2", "Pass123!", "John", "Doe")
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        # Job is now added to job interests
        assert job.addInterestedJob(newUserId, newJobId) != None
        # hasInterested(newUserId, newJobId) should always return True after job is added to job interests
        assert job.hasInterested(newJobId, newUserId) == True
        # Job is now removed from job interests
        assert job.removeInterestedJob(newJobId) == None
        # hasInterested(newUserId, newJobId) should always return False after job is removed from job interests
        assert job.hasInterested(newJobId, newUserId) == False