
import os
import pickle
from handler.login.user_profile import UserProfile
# Rukovalac, serijalizacija
# Ovo bi mi bla PirjavaNaSistem iz dijagrama


class LoginHandler(object):

    def __init__(self, user_file):
        self.user_file = user_file
        if not os.path.isfile(self.user_file):
            open(self.user_file, mode='w').close()

    # serijalizujumeo listu korisnika
    def createUser(self, username, password):
        try:
            userList = pickle.load(open(self.user_file, 'rb'))
        except:
            userList = {}

        if username in userList:
            return False
        userList[username] = UserProfile(username, password)
        pickle.dump(userList, open(self.user_file, 'wb'))
        return True

    def login_user(self, username, password):
        userList = {}
        try:
            userList = pickle.load(open(self.user_file, 'rb'))
        except:
            return None

        if username in userList:
            if userList[username].password == password:
                return userList[username]
        return None

    def save_profile(self, profile):
        userList = {}
        try:
            userList = pickle.load(open(self.user_file, 'rb'))
        except:
            pass

        userList[profile.username] = profile
        pickle.dump(userList, open(self.user_file, 'wb'))
