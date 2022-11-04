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
    def __init__(self, userId):
        self.userId=userId

    def sendMessage(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("""SELECT user_id, user_firstname, user_lastname FROM Users WHERE user_id not like 'userId' """)
        userList = res.fetchall()       #get a list of all users and exclude logged in user
        i=1
        for users in userList:
            if(users[1] == self.userId):
                continue
            print(str(i), ":", users[1], users[2])
            i += 1
        userToMessage = int(input("Select a user to send a message to or press 0 to return to the menu\n"))         #select a user to send a message to
        if userToMessage == 0:              
            return None
        friend = Friend(self.getUserId())
        friendsList = friend.getFriends()
        if (userToMessage not in friendsList):          #if the user is not in their friends list, then they cant send a message to them
            print("I'm sorry, you are not friends with that person.\n")
            selection= int(input(print("\nSelect 1 to see a list of your friends or 0 to return to the options screen\n")))         #user is given the option to see a list of only their friends
            if(selection==0):
                return None
            elif(selection==1):
                self.sendMessageFriends(friendsList)        #if the user wants to they can select the option to generate a list of friends to send a message to



    def sendMessageFriends(self,friendsList):       #function to show only a list of friends to send a message to
        i=1
        for myFriend in friendsList:
                    if(myFriend[1] == self.userId):
                        continue
                    print(str(i), ":", myFriend[1], myFriend[2])
                    i += 1
    # def sendMessageStandard(self):
    #     friend = Friend(self.getUserId())
    #     friendsList = friend.getFriends()
    #     if not friendsList: 
    #         print("There is no one in your network...\n")
    #         input("\tPress any key to return to options screen\n")
    #         optionsScreen(self)