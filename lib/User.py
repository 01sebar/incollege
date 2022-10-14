import sqlite3
from lib.Setting import Setting


class User:

    def __init__(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def isLoggedIn(self):
        return self.userId != None

    def create(self, username, password, firstname, lastname, university):
        firstname = firstname.lower()
        lastname = lastname.lower()
        university = university.lower()
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (user_username, user_password, user_firstname, user_lastname, user_university) VALUES (?, ?, ?, ?, ?)",
            (username, password, firstname, lastname, university))
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

    def findManyByLastname(self, lastname: str):
        lastname = "%" + lastname.lower() + "%"
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            # We use "LIKE" instead of "=" to potentially allow for better search results
            "SELECT user_id, user_firstname, user_lastname FROM users WHERE user_lastname LIKE ? LIMIT 1",
            (lastname, ))
        users = res.fetchmany()
        return users

    def findManyByUniversity(self, university: str):
        university = "%" + university.lower() + "%"
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            # We use "LIKE" instead of "=" to potentially allow for better search results
            "SELECT user_id, user_firstname, user_lastname FROM users WHERE user_university LIKE ? LIMIT 1",
            (university, ))
        users = res.fetchmany()
        return users

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
