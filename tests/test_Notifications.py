import pytest
from lib.User import User
from lib.Message import Message
from lib.Notification import Notification
from lib.Profile import Profile

class TestClass:

    def testCreateProfile(self):
        
        user = User(None)   #create user object
        
        
        user.create("user1", "Pass123!", "Joe", "Momma", 0)         
        user.createDefaultSettings()
        notification=Notification(user)         #create notification object
    
        assert (notification.profileNotCreated()==False)        #assert profile is not created yet

        profile = Profile(user)         #create profile for user
        profile.create()

        assert(notification.profileNotCreated()==True)      #assert profile is created
       

    
