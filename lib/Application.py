import sqlite3

class Application:

    def findMany(self, jobId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT job_applied_key, user_username, about_paragraph FROM jobsApplied INNER JOIN users ON users.user_id = jobsApplied.user_id WHERE jobsApplied.job_id = ?", (jobId,))
        applicationsList = res.fetchall()
        return applicationsList

    