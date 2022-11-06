import pytest
from lib.User import User


class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user", "Pass123!", "John", "Doe", 0)
        assert user.findOne(newUserId) != None
        # findOne(0) should always return None since database IDs start counting at 1
        assert user.findOne(0) == None
