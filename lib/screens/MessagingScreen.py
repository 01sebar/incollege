from cmath import exp
import sqlite3
from os import system
from traceback import print_tb
from lib.User import User
from lib.Profile import Profile
from lib.Education import Education
from lib.Experience import Experience
from lib.screens.ExperienceScreen import ExperienceScreen
from lib.screens.EducationScreen import EducationScreen
from lib.Friend import Friend

class MessagingScreen:
    def __init__(self, loggedInUser: User):
        self.loggedInUser = loggedInUser

    def sendMessagePremium(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("SELECT user_id, user_firstname, user_lastname FROM Users WHERE user_id IS NOT NULL ",)
        userList = res.fetchall()
        
        
    
    def sendMessageStandard(self):
        friend = Friend(loggedInUser.getUserId())
        friendsList = friend.getFriends()