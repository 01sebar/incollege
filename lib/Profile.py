import sqlite3
from lib.User import User
from lib.utils.Format import Format

class Profile:

    def __init__(self, loggedInUser: User):
        self.profileId = None
        self.loggedInUser = loggedInUser

    def getProfileId(self):
        return self.profileId

    def create(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO profiles (profile_user_id) VALUES (?)",
                    (self.loggedInUser.getUserId(),))
        con.commit()
        self.profileId = cur.lastrowid
        return cur.lastrowid

    def exists(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT profile_id FROM profiles WHERE profile_user_id = ? LIMIT 1",
            (self.loggedInUser.getUserId(), ))
        profile = res.fetchone()
        # Return boolean value if profile exists for a given profile_user_id
        if profile:
            self.profileId = profile[0]
        return profile != None

    def setTitle(self, title: str):
        format = Format()
        title = format.titleCase(title)
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE profiles SET profile_title = ? WHERE profile_user_id = ?",
            (title, self.loggedInUser.getUserId()))
        con.commit()

    def setDescription(self, description: str):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE profiles SET profile_description = ? WHERE profile_user_id = ?",
            (description, self.loggedInUser.getUserId()))
        con.commit()
    
    def findOne(self, p_userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT profile_Id, profile_title, profile_description FROM profiles WHERE profile_user_id = ? LIMIT 1",
            (p_userId, ))
        profile = res.fetchone()
        #con.close()
        return profile

    
    def setMajor(self, major: str):
        self.loggedInUser.updateMajor(major)

    def setUniversity(self, university):
        self.loggedInUser.updateUniversity(university)