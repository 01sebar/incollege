import sqlite3
class Job:

    def create(self, title, description, employer, location, salary, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO jobs (job_title, job_description, job_employer, job_location, job_salary, job_user_id) VALUES (?, ?, ?, ?, ?, ?)",
                    (title, description, employer, location, salary, userId))
        con.commit()
        return cur.lastrowid

    def findOne(self, jobId):
          con = sqlite3.connect("incollege.db")
          cur = con.cursor()
          res = cur.execute("SELECT job_title FROM jobs WHERE job_id = ? LIMIT 1",
                      (jobId,))
          job = res.fetchone()
          return job
    def findAll(self):
          con = sqlite3.connect("incollege.db")
          cur = con.cursor()
          res = cur.execute("SELECT job_id, job_title, job_description, job_employer, job_location, job_salary, job_user_id FROM jobs WHERE job_id IS NOT NULL ",
                      )
          jobList = res.fetchall()
          return jobList
    def createApplication(self,graduationDate,startDate,aboutParagraph,userId,jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        status =1
        cur.execute("INSERT INTO jobsApplied (user_id,job_id,graduation_date,starting_date,about_paragraph, status) VALUES (?, ?, ?, ?, ?,?)",
                    (userId,jobId,graduationDate,startDate,aboutParagraph,status))
        con.commit()
        return cur.lastrowid
    def removeJob(self, jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM jobs WHERE job_id = ?""", (jobId,))
        con.commit()
        return
    def addInterestedJob(self, userId, jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO jobsInterested (user_id, job_id) VALUES (?, ?)",
                    (userId, jobId))
        con.commit()
        return cur.lastrowid
    def hasApplied(self,jobId,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT user_id FROM jobsApplied WHERE job_id = ? AND user_id = ?",
            (jobId,userId))
        jobIdList = res.fetchone()
        if jobIdList: 
            return True
        else: 
            return False
    def hasInterested(self,jobId,userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT user_id FROM jobsInterested WHERE job_id = ? AND user_id = ?",
            (jobId,userId))
        jobIdList = res.fetchone()
        if jobIdList: 
            return True
        else: 
            return False
    def findAllInterested(self, userId):
          con = sqlite3.connect("incollege.db")
          cur = con.cursor()
          res = cur.execute("SELECT * FROM jobs INNER JOIN jobsInterested on jobs.job_id = jobsInterested.job_id WHERE user_id = ? ",
                      (userId,))
          jobList = res.fetchall()
          return jobList
    def removeInterestedJob(self, jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM jobsInterested WHERE job_id = ?""", (jobId,))
        con.commit()
        return
    def updateStatus(self, jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        newStatus = 0
        cur.execute(
            "UPDATE jobsApplied SET status = ? WHERE job_id = ?",
            (newStatus, jobId))
        con.commit()
    def checkStatus(self, user_id):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        status = 0
        res = cur.execute(
            "SELECT * FROM jobsApplied WHERE status = ? AND user_id = ?",
            (status, user_id))
        checkFalse = res.fetchall()
        for job in checkFalse:
            self.removeApplication(job[2],job[1])
        if checkFalse:
            return True
        else:
            return False

    def removeApplication(self, jobId, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        status = 0
        cur.execute("""DELETE FROM jobsApplied WHERE status = ? AND user_id = ?""", 
                      (status,userId))
        con.commit()
        return
