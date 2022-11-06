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
from lib.Message import Message


class MessagingScreen:
    def __init__(self, userId):
        self.userId=userId

    def messageList(self):
        newUser = User(self.userId)
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("""SELECT user_id, user_firstname, user_lastname FROM users WHERE NOT user_id = ? """,(self.userId,))
        userList = res.fetchall()       #get a list of all users and exclude logged in user
        i=1
        for users in userList:
            if(users[1] == self.userId):
                continue
            print(str(i), ":", users[1], users[2])
            i += 1
        selection = int(input("Select a user to send a message to or press 0 to return to the menu\n"))         #select a user to send a message to
        if selection == 0:              
            return None
        userToMessage = userList[selection - 1]
        userToMessageID= userToMessage[0]       #the user we want to send the message to ID
        friend = Friend(self.userId)            #creating friend object and getting list of loggedinuser's friends
        friendsList = friend.getFriends()
        print(friendsList)
        
        if ((len(friendsList) == 0 or userToMessageID not in friendsList[1]) and newUser.getUsertype() != 2):          #if the user is not in their friends list, then they cant send a message to them
            print("I'm sorry, you are not friends with that person.\n")
            selection= int(input(print("\nSelect 1 to see a list of your friends or 0 to return to the options screen\n")))         #user is given the option to see a list of only their friends
            if(selection==0):
                return None
            elif(selection==1):
                self.sendMessageFriends(friendsList)        #if the user wants to they can select the option to generate a list of friends to send a message to
                return None
        else:                                         
            self.sendMessage(userToMessageID)           #if the usertomessage is in their friends list then we can call the send message function
            return None


    def sendMessageFriends(self,friendsList):       #function to show only a list of friends to send a message to
        i=1
        for myFriend in friendsList:
            if(myFriend[1] == self.userId):
                continue
            print(str(i), ":", myFriend[1], myFriend[2])
            i += 1
        selection = int(input("Select a user to send a message to or press 0 to return to the menu\n"))         #select a user to send a message to
        if selection == 0:              
            return None
        userToMessage = friendsList[selection - 1]
        userToMessageID= userToMessage[0]
        self.sendMessage(userToMessageID)           #if the usertomessage is in their friends list then we can call the send message function
        return None


    def sendMessage(self, userToMessageID):
        messageToSend=""
        while(messageToSend==""):
            messageToSend=input("\nEnter the message you would like to send: \n")
        newMessage= Message(self.userId)
        newMessage.createMessage(userToMessageID,messageToSend)


    def viewIncomingMessages(self,messageList):                 #function that prints all the incoming messages
        newMessage= Message(self.userId)
        i=1
        for messages in messageList:
            Sender=newMessage.getSender(messages[1])
            print(str(i), ": from : "+ Sender[0]+" "+Sender[1])
            i += 1
        selection = int(input("Select a message to view or press 0 to return to the menu\n"))         
        if selection == 0:              
            return None
        messageToView = messageList[selection - 1]
        self.viewMessage(messageToView)                         #calling function to view a specific message
        
    def viewMessage(self, messageToView):                       #function to view a specific message and give options to delete/ reply
        print("\n"+ messageToView[3] + "\n")
        selection=""
        while(selection!='y' or selection!='n'):
            selection = input("Would you like to delete this message? y/n? \n")    #prompt the user to delete the message they just read
            if (selection=='y'):
                    message = Message(self.userId)
                    message.removeOne(messageToView[0])         #if the user wants to delete this message, call the removeone function that takes in message_id
                    print("\nMessage Removed\n")
                    return
            else:
                return