import pytest
from lib.User import User


class TestClass:

    def testUserType(self):
        # TO-DO check user type
        user = User(None)
        newUserId = user.create(
            "user1", "Pass123!", "Joe", "Momma", 0)
        user.createDefaultSettings()

    def testSendMessage(self):
        # TO-DO create 2 users
        # One regular, one premium
        # Check count of regular inbox
        # Have Premium send message to regular
        # Verify count of regular inbox == 1
        print("")
