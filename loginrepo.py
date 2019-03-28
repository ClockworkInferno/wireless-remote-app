from user import User
from user import NewUser
#from registerservice import RegisterUser
class LoginRepo:
    def find(self, username, password):
        return User(username,password)
class LoginAdd:
    def add(self, username, password, email, fname, lname):
        return RegUser(username, password, email, fname, lname)
class LoginSearch:
    def find(self, username, fname, lname):
        return RegUser(username, fname, lname)
