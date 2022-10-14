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
        friends = res.fetchmany()
        return friends

    def sendInvite(self, userToInviteID):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO friends (friend_from_user_id, friend_to_user_id, friend_is_invite) VALUES (?, ?, ?)",
            (self.userId, userToInviteID, 1))
        con.commit()
        self.userId = cur.lastrowid
        return self.userId
