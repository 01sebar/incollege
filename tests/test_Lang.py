import pytest
from lib.User import User
from lib.Setting import Setting


class TestClass:

    def testCreate(self):
        user = User(None)
        newUserId = user.create("user", "Pass123!", "Joe", "Momma")
        user.createDefaultSettings()
        setting = Setting()
        assert setting.getValue("language", newUserId) == "english"
        setting.update("language", "spanish", user.userId)
        assert setting.getValue("language", newUserId) == "spanish"
