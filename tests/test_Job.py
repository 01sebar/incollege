import pytest
from lib.User import User
from lib.Job import Job


class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user", "Pass123!", "John", "Doe")
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        assert job.findOne(newJobId) != None
        # findOne(0) should always return None since database IDs start counting at 1
        assert job.findOne(0) == None

    def testCreateApplicationAndHasApplied(self):
        user = User(None)
        newUserId = user.create("user2", "Pass123!",
                                "John", "Doe")
        userToApply = User(None)
        newUserToApplyId = userToApply.create(
            "user3", "Pass123!", "John", "Doe")
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        assert job.hasApplied(newJobId, newUserToApplyId) == False
        applicationId = job.createApplication("2023", "2023-01-01",
                                              "lorem ipsum", newUserToApplyId, newJobId)
        assert job.hasApplied(newJobId, newUserToApplyId) == True
