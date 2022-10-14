import sqlite3


class Setting:

    def create(self, key, value, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO settings (setting_key, setting_value, setting_user_id) VALUES (?, ?, ?)",
            (key, value, userId))
        con.commit()
        #print("new setting key value created with id:", cur.lastrowid,
              #"and key:", key)
        return cur.lastrowid

    def update(self, key, newValue, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE settings SET setting_value = ? WHERE setting_key = ? AND setting_user_id = ?",
            (newValue, key, userId))
        con.commit()

    def getValue(self, key, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT setting_value FROM settings WHERE setting_key = ? AND setting_user_id = ? LIMIT 1",
            (key, userId))
        setting = res.fetchone()
        if not setting:
            return None
        return setting[0]
