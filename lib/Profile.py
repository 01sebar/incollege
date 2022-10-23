import sqlite3
from lib.User import User

class Profile:

    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser

    def exists(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT profile_id FROM profiles WHERE profile_user_id = ? LIMIT 1",
            (self.loggedInUser.getUserId(), ))
        profile = res.fetchone()
        # Return boolean value if profile exists for a given profile_user_id
        return profile != None
