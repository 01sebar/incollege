import pytest
from lib.User import User

class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user", "Pass123!", "John", "Doe")
        assert user.findOne(newUserId) != None
        assert user.findOne(0) == None # findOne(0) should always return None since database IDs start counting at 1
