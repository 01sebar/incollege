import pytest
from lib.User import User
from lib.Message import Message


class TestClass:

    def testUserType(self):
        # TO-DO check user type
        user = User(None)
        newUserId = user.create(
            "user1", "Pass123!", "Joe", "Momma", 0)
        user.createDefaultSettings()

    def testSendMessage(self):
        # Create 2 users
        # One regular, one premium
        # Check count of regular inbox
        # Have Premium send message to regular
        # Verify count of regular inbox == 1
        userRegular = User(None)
        userRegularId = userRegular.create(
            "user1", "Pass123!", "Joe", "Momma", 0)
        userPremium = User(None)
        userPremiumId = userPremium.create(
            "user2", "Pass123!", "Joe", "Momma", 1)

        # Check if premium user can send message to regular
        messageFromRegularToPremium = Message(userRegularId)
        assert len(messageFromRegularToPremium.getMessages()) == 0
        messageFromPremiumToRegular = Message(userPremiumId)
        messageFromPremiumToRegular.createMessage(
            userRegularId, "message body")
        # Check if message received
        assert len(messageFromRegularToPremium.getMessages()) == 1
