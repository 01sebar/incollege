import sqlite3

class Education:
    def __init__(self, profileId: int):
        self.profileId = profileId

    def create(self, schoolName, degree, startingYear, endingYear):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO educations (edu_schoolName, edu_degree, edu_startingYear, edu_endingYear, education_profile_Id) VALUES (?, ?, ?, ?, ?)",
                    (schoolName, degree, startingYear, endingYear, self.profileId))
        con.commit()
        return cur.lastrowid
    
    def getMany(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT education_Id, edu_schoolName, edu_degree, edu_startingYear, edu_endingYear, education_Id FROM educations WHERE education_profile_Id = ?", (self.profileId,))
        totEducation = res.fetchall()
        con.close()
        return totEducation
    
    def getCount(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("SELECT COUNT() FROM educations WHERE education_profile_Id = ?", (self.profileId,))
        count = res.fetchone()[0]
        con.close()
        return count
    
    def removeOne(self, educationId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM educations WHERE education_Id = ?""", (educationId,))
        con.commit()
        return