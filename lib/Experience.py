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
    
    def getMany(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT experience_id, experience_title, experience_employer, experience_date_started, experience_dete_ended, experience_location, experience_description FROM experiences WHERE experience_profile_id = ?", (self.profileId,))
        experiences = res.fetchall()
        con.close()
        return experiences
    
    def getCount(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("SELECT COUNT() FROM experiences WHERE experience_profile_id = ?", (self.profileId,))
        count = res.fetchone()[0]
        con.close()
        return count
    
    def removeOne(self, experienceId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM experiences WHERE experience_id = ?""", (experienceId,))
        con.commit()
        return