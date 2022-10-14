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