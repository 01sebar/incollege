import sqlite3


class Friend:

    def __init__(self, userId):
        self.userId = userId

    def findMyFriends(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT friend_id, user_id, user_firstname, user_lastname FROM friends
            INNER JOIN users ON user_id=friend_to_user_id
            WHERE friend_from_user_id = ? AND friend_is_invite = 0""",
            (self.userId, ))
        friends = res.fetchall()
        return friends

    def sendInvite(self, userToInviteID):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO friends (friend_from_user_id, friend_to_user_id, friend_is_invite) VALUES (?, ?, ?)",
            (self.userId, userToInviteID, 1))
        con.commit()
        # print("cur.lastrowid:", cur.lastrowid)
        return cur.lastrowid

    def getInvites(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT friend_id, user_id, user_firstname, user_lastname FROM friends
            INNER JOIN users ON user_id=friend_from_user_id
            WHERE friend_to_user_id = ? AND friend_is_invite = 1""",
            (self.userId, ))
        friends = res.fetchall()
        return friends

    def addFriend(self, friendKey):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""UPDATE friends SET friend_is_invite = ? WHERE friend_id = ?""",
            (0, friendKey)) # Need to remove user from invitations list on both ends
        con.commit()
        return
    
    def removeOne(self, friendId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM friends WHERE friend_id = ?""", (friendId,))
        con.commit()
        return

    def removeFriend(self, friendId):
        self.removeOne(friendId)
        return

    def rejectInvite(self, friendId):
        self.removeOne(friendId)
        return

    def getFriends(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT friend_id, user_id, user_firstname, user_lastname FROM friends
            INNER JOIN users ON user_id=friend_from_user_id
            WHERE friend_to_user_id = ? OR friend_from_user_id = ? AND friend_is_invite = 0""",
            (self.userId, self.userId))
        friends = res.fetchall()
        return friends
        
    def getFriendsUserID(self, friendId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT friend_to_user_id FROM friends WHERE friend_id = ? """,
            (friendId, ))
        friend = res.fetchone()
        return friend
