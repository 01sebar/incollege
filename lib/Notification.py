import sqlite3
from lib.Profile import Profile
from lib.User import User

class Notification:
    def __init__(self, loggedInUser: User):
        self.profileId = None
        self.loggedInUser = loggedInUser

    def NumOfAppliedJobs(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM jobsApplied WHERE user_id = ?",
            (userId))
        appliedJobList = res.fetchone()
        return len(appliedJobList)

    def newJobPosted(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute()
        return

    def appliedJobDeleted(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute()
        return

    def newMemberJoined(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute()
        return

    def weekSinceLastJobApply(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute()
        return
    
    def profileNotCreated(self):
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