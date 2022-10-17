import pytest
from lib.User import User
from lib.Friend import Friend

# Test Friend Invite
# Test whether friend invite was sent
# Test Accept/Rejecting Invite
# Show network screen


class TestClass:
    def testCreate(self):
        user1 = User(None)
        user2 = User(None)

        user1.create("User1", "Password123!", "John",
                     "Smith", "USF", "CompSci")

        user2.create("user2", "Pass234!", "Jane",
                     "Doe", "USF", "Computer Science")

        user1.createDefaultSettings()
        user2.createDefaultSettings()

        friend = Friend(user1.getUserId())
        friendInviteId = friend.sendInvite(user2.getUserId())
        friend2 = Friend(user2.getUserId())
        friend2.addFriend(friendInviteId)

        friendsListOut = friend.findMyFriends()
        friendsListIn = friend.getFriends()
        friendslist = friendsListOut + friendsListIn

        isFriends = False
        for i in friendslist:
            if(i[2] == "jane" and i[3] == "doe"):
                isFriends = True

        assert isFriends == True
