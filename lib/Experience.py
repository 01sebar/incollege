import sqlite3

class Experience:
    def __init__(self, profileId: int):
        self.profileId = profileId

    def create(self, title, employer, dateStarted, dateEnded, location, description):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO experiences (experience_title, experience_employer, experience_date_started, experience_dete_ended, experience_location, experience_description, experience_profile_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (title, employer, dateStarted, dateEnded, location, description, self.profileId))
        con.commit()
        return cur.lastrowid
    
    def getCount(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("SELECT COUNT() FROM experiences WHERE experience_profile_id = ?", (self.profileId,))
        count = res.fetchone()[0]
        return count