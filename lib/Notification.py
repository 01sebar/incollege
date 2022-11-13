import sqlite3
from lib.Profile import Profile
from lib.User import User
from lib.Message import Message

class Notification:
    def __init__(self, loggedInUser: User):
        self.profileId = None
        self.loggedInUser = loggedInUser
        self.dayCount = 0

    def NumOfAppliedJobs(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT * FROM jobsApplied WHERE user_id = ?""",
            (userId))
        appliedJobList = res.fetchone()
        return len(appliedJobList)

    def newJobPosted(self, title, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM users WHERE user_id != ? """, (userId))
        usersToNotify = res.fetchall()
        if len(usersToNotify) > 0:
            for user in usersToNotify:
                newMessage = Message(str(user[0]))
                newMessage.createMessage(str(user[0]), "A new Job as been posted:" + str(title) + " Apply Now!")
        return usersToNotify

    def appliedJobDeleted(self,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("""SELECT job_id FROM jobsApplied WHERE user_id = ? AND status = ?""", (userId, 0))
        deletedJobIds = res.fetchall()
        deletedJobTitles = []
        for jobId in deletedJobIds:
            res = cur.execute("""SELECT job_title FROM jobs WHERE job_id = ?""", (jobId))
            deletedJobTitles.append(res.fetchone())

        return deletedJobTitles

    def newMemberJoined(self, username, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM users WHERE user_id != ? """, (userId))
        usersToNotify = res.fetchall()

        if len(usersToNotify) > 0:
            for user in usersToNotify:
                newMessage = Message(str(user[0]))
                newMessage.createMessage(str(user[0]), str(username) + " has joined InCollege! Say Hello!")
        return

    def weekSinceLastJobApply(self, userId):

        newMessage = Message(str(userId))
        newMessage.createMessage(str(userId), str("Its has been more than 7 days since you've applied for a job. Go forth and start applying!"))

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

