import instaloader
import pandas as pd
from instaloader import BadCredentialsException

class Instagram:
    def __init__(self):
        self.username = ""
        self.password = ""

    def extractFollowers(self):
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return [follower.username for follower in profile.get_followers()]
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return [followee.username for followee in profile.get_followees()]

    def checkLogin(self): 
        self.bot = instaloader.Instaloader()
        username = str(input("Enter your username: "))
        password = str(input("Enter your password: "))
        
        try:
            self.bot.login(username, password) 
        except BadCredentialsException:
            print("Either username or password is wrong!")
            return False # Return False so the user can try again.
        
        # Setting login credentials since they were checked for correctness
        self.username = username
        self.password = password
        return True
