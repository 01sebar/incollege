import pytest
from lib.User import User
from lib.Job import Job


class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user1", "Pass123!", "John", "Doe", 0)
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        assert job.findOne(newJobId) != None
        # findOne(0) should always return None since database IDs start counting at 1
        assert job.findOne(0) == None

    def testJobInterest(self):
        user = User(None)
        newUserId = user.create("user2", "Pass123!", "John", "Doe", 0)
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

    def testCreateApplicationAndHasApplied(self):
        user = User(None)
        newUserId = user.create("user2", "Pass123!",
                                "John", "Doe", 0)
        userToApply = User(None)
        newUserToApplyId = userToApply.create(
            "user3", "Pass123!", "John", "Doe", 0)
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", newUserId)
        assert job.hasApplied(newJobId, newUserToApplyId) == False
        applicationId = job.createApplication("2023", "2023-01-01",
                                              "lorem ipsum", newUserToApplyId, newJobId)
        assert job.hasApplied(newJobId, newUserToApplyId) == True

    def testCheckStatusAndUpdateStatus(self):
        user4 = User(None)
        user4Id = user4.create("user4", "Pass123!",
                               "John", "Doe", 0)
        user5 = User(None)
        user5Id = user5.create(
            "user3", "Pass123!", "John", "Doe", 0)
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", user4Id)
        applicationId = job.createApplication("2023", "2023-01-01",
                                              "lorem ipsum", user5Id, newJobId)
        assert job.checkStatus(newJobId) == True
        job.updateStatus(newJobId)
        assert job.checkStatus(newJobId) == False

    def testRemoveJob(self):
        user6 = User(None)
        user6Id = user6.create("user6", "Pass123!",
                               "John", "Doe", 0)
        user4 = User(None)
        user4Id = user4.create(
            "user4", "Pass123!", "John", "Doe", 0)
        job = Job()
        newJobId = job.create("Software Developer", "program stuff",
                              "Google", "San Francisco, CA", "500000", user4Id)
        # We make sure the job is in DB
        assert job.findOne(newJobId) != None
        # We remove the job from DB
        job.removeJob(newJobId)
        # We make sure the job is removed from DB
        assert job.findOne(newJobId) == None
