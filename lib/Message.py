import sqlite3
from lib.User import User

class Message:

    
        
    def __init__(self, userId):
        self.userId=userId

    def createMessage(self,toUserId,message):           #function to create a new message
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("INSERT INTO messages (from_user_id, to_user_id, message) VALUES (?, ?, ?)",
                    (self.userId,toUserId,message))
        con.commit()
        return cur.lastrowid

    def removeOne(self, messageID):                                 #function to remove a message from messages table
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM messages WHERE message_id = ?""", (messageID,))
        con.commit()
        return

    def deleteMessage(self, messageID):
        self.removeOne(messageID)
        return

    def getMessages(self):                                              #function that gets all the incoming messages of the user
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT message_id, from_user_id, to_user_id, message FROM messages
            INNER JOIN users ON  user_id = to_user_id
            WHERE to_user_id = ? """,
            (self.userId,))
        messages = res.fetchall()
        return messages

    def getSender(self, fromUserId):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT user_firstname, user_lastname FROM users
            INNER JOIN messages ON  from_user_id = user_id
            WHERE user_id = ? """,
            (fromUserId,))
        Sender = res.fetchone()
        return Sender
    