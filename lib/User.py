import sqlite3
from lib.Setting import Setting


class User:

    def __init__(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def create(self, username, password, firstname, lastname):
        firstname = firstname.lower()
        lastname = lastname.lower()
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (user_username, user_password, user_firstname, user_lastname) VALUES (?, ?, ?, ?)",
            (username, password, firstname, lastname))
        con.commit()
        self.userId = cur.lastrowid
        return self.userId

    def findOneByUsername(self, username):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT user_id, user_username, user_password FROM users WHERE user_username = ? LIMIT 1",
            (username, ))
        user = res.fetchone()
        return user

    def findOne(self, userId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT user_id, user_username, user_firstname, user_lastname FROM users WHERE user_id = ? LIMIT 1",
            (userId, ))
        user = res.fetchone()
        return user


    def createDefaultSettings(self):
        setting = Setting()
        setting.create("email", "true", self.userId)
        setting.create("sms", "true", self.userId)
        setting.create("targetedAdvertising", "true", self.userId)
        setting.create("language", "english", self.userId)
