import pytest
from lib.User import User


class TestClass:

    def testUserType(self):
        # TO-DO check user type
        user = User(None)
        user2 = User(None)

        user.create(
            "user1", "Pass123!", "Joe", "Momma", 0)
        user.createDefaultSettings()
        assert user.getUsertype() == 0

        user2.create(
            "user1", "Pass123!", "Joe", "Momma", 1)
        user2.createDefaultSettings()
        assert user2.getUsertype() == 1

    def testSendMessage(self):
        # TO-DO create 2 users
        # One regular, one premium
        # Check count of regular inbox
        # Have Premium send message to regular
        # Verify count of regular inbox == 1
        print("")
